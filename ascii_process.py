import numpy as np

# Default character sets
CHAR_SETS = {
    "basic": "@%#*+=-:. ",
    "extended": "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. ",
    "custom": " .:-=+*#%@",
}

def get_char_set(name):
    return CHAR_SETS.get(name, CHAR_SETS["basic"])

def map_to_ascii(gray_array, char_set, density=1.0, progress_callback=None):
    """
    Convert grayscale array to ASCII string with progress callback.
    progress_callback: function(row_index, total_rows) called after each row.
    """
    if gray_array.size == 0:
        return ""

    char_set_str = char_set
    if density < 1.0:
        subset_len = max(1, int(len(char_set_str) * density))
        char_set_str = char_set_str[:subset_len]

    max_idx = len(char_set_str) - 1
    if max_idx == 0:
        ascii_matrix = np.full(gray_array.shape, char_set_str[0], dtype=object)
    else:
        indices = (gray_array / 255.0) * max_idx
        indices = np.clip(indices, 0, max_idx).astype(int)
        ascii_matrix = np.array([char_set_str[i] for i in indices.flatten()]).reshape(gray_array.shape)

    lines = []
    total_rows = ascii_matrix.shape[0]
    for i, row in enumerate(ascii_matrix):
        lines.append(''.join(row))
        if progress_callback:
            progress_callback(i + 1, total_rows)
    return '\n'.join(lines)