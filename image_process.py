from PIL import Image, ImageEnhance, ImageOps
import numpy as np
import io

def load_image(file_path, max_size=(800, 800)):
    """
    Load image from file path, convert to RGB, and optionally resize.
    Returns a PIL Image object.
    """
    try:
        img = Image.open(file_path)
        img = img.convert("RGB")
        # Resize if too large (maintain aspect ratio)
        img.thumbnail(max_size, Image.Resampling.LANCZOS)
        return img
    except Exception as e:
        raise RuntimeError(f"Failed to load image: {e}")

def preprocess_image(img, brightness=1.0, contrast=1.0):
    """
    Adjust brightness and contrast, then convert to grayscale.
    Returns a numpy array of grayscale values (0-255).
    """
    # Adjust brightness and contrast
    if brightness != 1.0:
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(brightness)
    if contrast != 1.0:
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(contrast)

    # Convert to grayscale
    gray = ImageOps.grayscale(img)
    return np.array(gray)

def resize_for_ascii(gray_array, width=None, height=None, aspect_ratio_correction=0.5):
    """
    Resize grayscale array for ASCII art, maintaining aspect ratio.
    aspect_ratio_correction: because characters are taller than wide.
    """
    h, w = gray_array.shape
    if width is None and height is None:
        # Default: width = 80 chars
        width = 80
    if width is not None:
        # Calculate height to preserve aspect ratio
        ratio = h / w
        height = int(width * ratio * aspect_ratio_correction)
        height = max(1, height)
    else:
        width = int(height / ratio / aspect_ratio_correction)
        width = max(1, width)

    # Resize using PIL
    img = Image.fromarray(gray_array)
    img = img.resize((width, height), Image.Resampling.LANCZOS)
    return np.array(img)