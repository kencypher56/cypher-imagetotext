#!/usr/bin/env python3
"""
Environment setup script.
- Detects OS
- Asks user to choose between conda or venv
- For conda: installs Miniconda if missing, creates conda env 'cypher-imagetotext' with Python 3.10, installs requirements
- For venv: creates virtual environment in project directory, installs requirements
"""

import os
import sys
import subprocess
import platform
import shutil
from osdetection import get_os, is_conda_available

def run_command(cmd, env=None, capture=True):
    """Run a command and print output."""
    print(f"Running: {cmd}")
    if capture:
        result = subprocess.run(cmd, shell=True, env=env, text=True, capture_output=True)
        if result.returncode != 0:
            print(f"Command failed with exit code {result.returncode}")
            print("STDERR:", result.stderr)
            sys.exit(1)
        print(result.stdout)
        return result
    else:
        # For interactive commands (like conda activate in shell), we don't capture
        return subprocess.run(cmd, shell=True, env=env)

def install_miniconda():
    """Download and install Miniconda (depending on OS)."""
    os_name = get_os()
    if os_name == "Windows":
        # Download installer
        url = "https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe"
        installer = "miniconda.exe"
        run_command(f"curl -L {url} -o {installer}")
        # Install silently (JustMe, add to PATH)
        run_command(f"start /wait {installer} /InstallationType=JustMe /AddToPath=1 /RegisterPython=0 /S /D=%USERPROFILE%\\miniconda3")
        os.remove(installer)
        conda_path = os.path.expanduser("~\\miniconda3\\Scripts\\conda.exe")
    elif os_name == "Linux":
        url = "https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh"
        installer = "miniconda.sh"
        run_command(f"wget {url} -O {installer}")
        run_command(f"bash {installer} -b -p $HOME/miniconda3")
        os.remove(installer)
        conda_path = os.path.expanduser("~/miniconda3/bin/conda")
    elif os_name == "Darwin":  # macOS
        url = "https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh"
        installer = "miniconda.sh"
        run_command(f"curl -L {url} -o {installer}")
        run_command(f"bash {installer} -b -p $HOME/miniconda3")
        os.remove(installer)
        conda_path = os.path.expanduser("~/miniconda3/bin/conda")
    else:
        print(f"Unsupported OS: {os_name}")
        sys.exit(1)

    # Add conda to PATH for this script
    conda_dir = os.path.dirname(conda_path)
    os.environ["PATH"] = conda_dir + os.pathsep + os.environ.get("PATH", "")
    print("Miniconda installed successfully.")
    return conda_path

def setup_with_conda():
    """Setup environment using conda."""
    # Ensure conda is available
    if not is_conda_available():
        print("Conda not found. Installing Miniconda...")
        conda_path = install_miniconda()
    else:
        print("Conda already available.")

    env_name = "cypher-imagetotext"
    # Check if environment already exists
    result = subprocess.run(f"conda env list | grep {env_name}", shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"Conda environment '{env_name}' already exists. Updating...")
        run_command(f"conda env update -n {env_name} -f environment.yml")
    else:
        # Create environment with Python 3.10
        print("Creating conda environment...")
        run_command(f"conda create -n {env_name} python=3.10 -y")
        # Install requirements using pip in the environment
        run_command(f"conda run -n {env_name} pip install -r requirements.txt")

    print("\nConda setup complete. To activate the environment and run the app:")
    if platform.system() == "Windows":
        print(f"  conda activate {env_name}")
    else:
        print(f"  source activate {env_name}")
    print("  python run.py")

def setup_with_venv():
    """Setup environment using Python's venv."""
    venv_dir = "venv"
    # Check if venv already exists
    if os.path.exists(venv_dir):
        print(f"Virtual environment '{venv_dir}' already exists. Skipping creation.")
    else:
        print("Creating virtual environment...")
        run_command(f"{sys.executable} -m venv {venv_dir}")

    # Determine the pip path
    if platform.system() == "Windows":
        pip_path = os.path.join(venv_dir, "Scripts", "pip")
        activate_script = os.path.join(venv_dir, "Scripts", "activate")
    else:
        pip_path = os.path.join(venv_dir, "bin", "pip")
        activate_script = os.path.join(venv_dir, "bin", "activate")

    # Install requirements
    print("Installing requirements...")
    run_command(f"{pip_path} install -r requirements.txt")

    print("\nVirtual environment setup complete. To activate and run the app:")
    if platform.system() == "Windows":
        print(f"  {activate_script}")
    else:
        print(f"  source {activate_script}")
    print("  python run.py")

def main():
    print("Welcome to the Cypher Image to Text setup.")
    print("Choose how you want to set up the environment:")
    print("1) Use conda (creates environment 'cypher-imagetotext' with Python 3.10)")
    print("2) Use venv (creates local virtual environment)")
    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        setup_with_conda()
    elif choice == "2":
        setup_with_venv()
    else:
        print("Invalid choice. Exiting.")
        sys.exit(1)

if __name__ == "__main__":
    main()