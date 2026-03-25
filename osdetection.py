import platform
import sys

def get_os():
    """Return the operating system name: 'Windows', 'Linux', 'Darwin' (macOS)."""
    return platform.system()

def is_conda_available():
    """Check if conda is in PATH."""
    import shutil
    return shutil.which("conda") is not None

def get_python_executable():
    """Return the path to the current Python interpreter."""
    return sys.executable