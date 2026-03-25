<div align="center">

# 🎨 Cypher Image to ASCII

### Convert Images to Beautiful ASCII Art with Advanced Controls

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)
![PySide6](https://img.shields.io/badge/PySide6-6.4%2B-green?style=flat-square&logo=qt)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

---

</div>

## ✨ Features

- 🖼️ **Advanced Image Processing** - Load and convert images to ASCII art with precision
- 🎨 **Multiple Themes** - Light, Dark, and Cyberpunk themes for every preference
- 📝 **Character Set Options** - Choose from various ASCII character sets
- 🎛️ **Real-time Controls**
  - Density slider for character density control
  - Width adjustment (40-200 characters)
  - Brightness and contrast adjustments
  - Live preview updates
- 💾 **Export Features** - Save ASCII art as `.txt` files
- 📋 **Clipboard Support** - Copy ASCII art directly to clipboard
- 🎭 **Sleek UI** - Modern, responsive interface with smooth animations
- 🚀 **Drag & Drop** - Simply drag image files onto the window
- ⚡ **High Performance** - Multi-threaded processing for smooth UI

---

## 🛠️ Technology Stack

### Core Framework
- **PySide6** (6.4.0+) - Qt framework for modern GUI
- **Python** (3.8+) - Core application logic
- **NumPy** (1.21.0+) - Image processing and array operations
- **Pillow** (9.0.0+) - Image loading and manipulation

### UI Components
- **QtAwesome** (1.2.0+) - FontAwesome 5 Solid Icons integration
- **Courier New** - Monospace font for ASCII preview
- **Custom QSS Styling** - Beautiful, responsive stylesheets

### Icons & Themes
- **FontAwesome 5 Solid** (fa5s)
  - 📁 `folder-open` - Load Images
  - 📥 `download` - Export ASCII
  - 📋 `copy` - Copy to Clipboard
  - 🎨 `palette` - Theme Selector

### Theme Colors

#### Light Mode
- Primary: `#007bff` (Blue)
- Background: `#f5f7fa` → `#e8ecf1` (Light Gray Gradient)

#### Dark Mode
- Primary: `#0d9aff` (Cyan)
- Background: `#1e1e1e` → `#0d0d0d` (Dark Gray Gradient)

#### Cyberpunk Mode
- Primary: `#00ffff` → `#ff00ff` (Cyan-Magenta)
- Background: `#0a0e27` → `#050813` (Deep Blue-Black Gradient)

---

## 📋 Requirements

```
PySide6>=6.4.0
Pillow>=9.0.0
numpy>=1.21.0
qtawesome>=1.2.0
```

---

## 🚀 Installation & Setup

### Automatic Setup (Recommended)

#### Step 1: Navigate to Project Directory
```bash
cd ~/Desktop/cypher-imagetotext
```

#### Step 2: Run the Setup Script
```bash
python3 setup.py
```

You'll be presented with a menu:
```
Welcome to the Cypher Image to Text setup.
Choose how you want to set up the environment:
1) Use conda (creates environment 'cypher-imagetotext' with Python 3.10)
2) Use venv (creates local virtual environment)
Enter 1 or 2:
```

##### Option 1: Conda (Recommended for system-wide installation)
- Automatically detects and installs **Miniconda** if not available
- Creates conda environment: `cypher-imagetotext` with Python 3.10
- Installs all dependencies via conda
- **Activation**:
  ```bash
  conda activate cypher-imagetotext
  python run.py
  ```

##### Option 2: Venv (Recommended for project-local isolation)
- Creates local virtual environment in `venv/` directory
- Installs all dependencies in isolated environment
- **Activation (Linux/macOS)**:
  ```bash
  source venv/bin/activate
  python run.py
  ```
- **Activation (Windows)**:
  ```cmd
  venv\Scripts\activate
  python run.py
  ```

### Manual Setup

If you prefer manual setup, follow these steps:

#### Step 1: Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# OR on Windows:
venv\Scripts\activate
```

#### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

Or install individually:
```bash
pip install PySide6>=6.4.0 Pillow>=9.0.0 numpy>=1.21.0 qtawesome>=1.2.0
```

---

## 🔧 Setup Script Features (setup.py)

The `setup.py` script automates environment setup with intelligent OS detection:

### Supported Operating Systems
- ✅ **Windows** (x86_64)
- ✅ **Linux** (x86_64)
- ✅ **macOS** (x86_64 & Apple Silicon)

### What setup.py Does

1. **OS Detection** - Identifies your operating system
2. **Environment Choice** - Interactive menu to select Conda or Venv
3. **Miniconda Auto-install** - Downloads and installs Miniconda if needed (Conda option)
4. **Conda Environment** - Creates `cypher-imagetotext` environment with Python 3.10 (Conda option)
5. **Dependency Installation** - Installs all requirements automatically
6. **Activation Instructions** - Provides OS-specific activation commands

### Script Workflow

```
setup.py
├── Detect OS
├── Create Menu (Conda vs Venv)
├── IF Conda Selected:
│   ├── Check if Miniconda installed
│   ├── If not: Download & Install Miniconda
│   ├── Create conda environment 'cypher-imagetotext'
│   ├── Install requirements.txt via pip in conda environment
│   └── Show activation instructions
└── IF Venv Selected:
    ├── Create local venv/ directory
    ├── Install requirements.txt via pip
    └── Show activation instructions
```

---

### Method 1: Direct Python Execution
```bash
python3 run.py
```

### Method 2: Module Execution
```bash
python3 -m gui
```

### Method 3: Interactive Testing
```bash
python3
>>> from gui import main
>>> main()
```

---

## 📖 Usage Guide

### 1. Load an Image
- **Click** the "Load Image" button (📁)
- Or **drag and drop** an image onto the preview area
- Supported formats: PNG, JPG, JPEG, WEBP

### 2. Adjust Settings
| Control | Range | Purpose |
|---------|-------|---------|
| **Charset** | Dropdown | Select ASCII character set |
| **Density** | 0.10 - 1.00 | Control character density |
| **Width** | 40 - 200 | ASCII art width in characters |
| **Brightness** | 0.00 - 2.00 | Adjust image brightness |
| **Contrast** | 0.00 - 2.00 | Adjust image contrast |

### 3. View Preview
- Left panel: Original image preview
- Right panel: Real-time ASCII art output

### 4. Export or Copy
- **Export TXT**: Save ASCII art as a text file (💾)
- **Copy**: Copy ASCII art to clipboard (📋)

### 5. Switch Theme
- Click the palette icon (🎨) and select:
  - **light** - Clean, bright interface
  - **dark** - Easy on the eyes
  - **cyberpunk** - Neon sci-fi aesthetic

---

## 📂 Project Structure

```
cypher-imagetotext/
├── run.py                 # Main entry point
├── gui.py                 # GUI initialization
├── ui.py                  # UI components & MainWindow class
├── image_process.py       # Image loading & preprocessing
├── ascii_process.py       # ASCII conversion logic
├── osdetection.py         # OS detection utilities
├── setup.py               # Automated environment setup
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── __pycache__/          # Python cache
```

### Key Files

**setup.py** - Automated environment setup script
```python
- OS Detection        # Detects Windows, Linux, macOS
- Conda Setup         # Auto-installs Miniconda if needed, creates environment
- Venv Setup          # Creates local Python virtual environment
- Dependency Install  # Automatically installs all requirements
- Interactive Menu    # User-friendly setup choice (Conda vs Venv)
```

**ui.py** - Main UI implementation
```python
- STYLES{}          # Theme definitions (Light/Dark/Cyberpunk)
- MainWindow       # Main application window
- WorkerThread     # Multi-threaded image processing
- animate_button() # Smooth button animations
```

**image_process.py** - Image utilities
```python
- load_image()           # Load and resize images
- preprocess_image()     # Adjust brightness/contrast
- resize_for_ascii()     # Resize for ASCII conversion
```

**ascii_process.py** - ASCII conversion
```python
- CHAR_SETS{}      # Character set definitions
- map_to_ascii()   # Convert image to ASCII art
- get_char_set()   # Retrieve character set
```

**osdetection.py** - OS detection utilities (used by setup.py)
```python
- get_os()               # Returns current OS (Windows/Linux/Darwin)
- is_conda_available()   # Checks if conda is installed
- Auto-detection         # Environmental variable inspection
```

---

## 🎨 Customization

### Adding Custom Character Sets
Edit `ascii_process.py`:
```python
CHAR_SETS = {
    "custom": "@%#*+=-:. ",
    # ... existing sets
}
```

### Modifying Themes
Edit `ui.py` STYLES dictionary:
```python
STYLES = {
    "custom": """
        QMainWindow {
            background: #your-color;
        }
        # ... more styles
    """
}
```

### Changing Default Theme
In `MainWindow.__init__()`:
```python
self.apply_theme("light")  # Change "light" to your theme
```

---

## 🐛 Troubleshooting

### Issue: Module Not Found
```
ModuleNotFoundError: No module named 'PySide6'
```
**Solution**: Install dependencies using `pip install -r requirements.txt`

### Issue: Unknown Property Warnings
```
Unknown property box-shadow
```
**Solution**: This is a non-critical QSS warning (already fixed in latest version)

### Issue: Application Won't Start
- Check Python version: `python3 --version` (requires 3.8+)
- Verify all dependencies are installed: `pip list | grep -E "PySide|Pillow|numpy|qtawesome"`
- Try in a virtual environment to avoid conflicts

### Issue: Image Processing Slow
- Reduce image resolution before loading
- Lower ASCII width for faster conversion
- Close other applications to free up resources

---

## 🎯 Performance Tips

1. **Smaller Images** - Load images < 2MB for best performance
2. **Optimal ASCII Width** - 80-120 characters provides good balance
3. **Charset Selection** - Simpler charsets process faster
4. **System Resources** - Ensure sufficient RAM (2GB+ recommended)

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 👤 Author

**Cypher** - Image to ASCII Art Converter

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

---

## 📞 Support

For issues or questions:
1. Check the troubleshooting section
2. Review the code comments
3. Test with different image formats
4. Verify all dependencies are correctly installed

---

<div align="center">

### Made with ❤️ using PySide6 and Python

⭐ **Star this repository if you find it useful!**

</div>
