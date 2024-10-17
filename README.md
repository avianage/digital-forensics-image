# Digital Forensic Tool for Images

This is a command-line tool designed for digital forensics of images. It performs various analyses, including metadata extraction, error level analysis (ELA), hash verification, file signature verification, and steganography detection.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Test Images](#test-images)
- [Examples](#examples)
- [License](#license)

## Features
- **Metadata Extraction**: Extracts and displays EXIF metadata from images.
- **Error Level Analysis (ELA)**: Detects tampering by highlighting edited areas in an image.
- **Hash Calculation**: Calculates MD5 and SHA-256 hashes for image integrity verification.
- **File Signature Verification**: Checks if the file extension matches its actual format.
- **Steganography Detection**: Identifies hidden data within images.

## Requirements
- Python 3.x
- Required Python packages:
  - `Pillow`
  - `numpy`
  - `scikit-image`
  - `hashlib`

You can install the required packages using pip:

```bash
pip install Pillow numpy scikit-image
```

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/digital-forensic-tool.git
   ```
2. Navigate to the project directory:
   ```bash
   cd digital-forensic-tool
   ```

## Usage
Run the tool from the command line with the following syntax:

```bash
python forensic_tool.py <image_path> [options]
```

### Options:
- `--metadata`: Extract metadata (EXIF).
- `--ela`: Perform Error Level Analysis.
- `--hash`: Calculate MD5 and SHA-256 hashes.
- `--signature`: Verify file signature.
- `--stego`: Detect hidden data (steganography).

## Test Images
You can test the tool with the following types of images located in the `sample_images` directory:
- Original, untampered images
- Edited or photoshopped images
- Images with hidden data (steganography)
- Corrupted or manipulated file signatures
- Compressed images
- Multiple image formats (e.g., `.jpg`, `.png`, `.bmp`)

## Examples
1. **Extract Metadata**:
   ```bash
   python forensic_tool.py sample_images/original_photo.jpg --metadata
   ```

2. **Perform Error Level Analysis**:
   ```bash
   python forensic_tool.py sample_images/photoshopped_photo.jpg --ela
   ```

3. **Calculate Hashes**:
   ```bash
   python forensic_tool.py sample_images/original_photo.jpg --hash
   ```

4. **Verify File Signature**:
   ```bash
   python forensic_tool.py sample_images/renamed_image.png --signature
   ```

5. **Detect Hidden Data**:
   ```bash
   python forensic_tool.py sample_images/stego_image.jpg --stego
   ```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

### Instructions for Use
- Replace `https://github.com/yourusername/digital-forensic-image-tool.git` with the actual URL of your GitHub repository.
- If you have any additional installation steps or configurations required for your tool, you can add them under the **Installation** section.
- If you decide to include a LICENSE file, ensure to add it to your repository as referenced in the **License** section.

Feel free to modify this `README.md` according to your project's specifics or any additional features you may want to include!