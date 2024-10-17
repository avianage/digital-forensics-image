# Image Forensics Tool

The **Image Forensics Tool** is a desktop application built with Python and Tkinter that provides various functionalities to analyze and assess image files. It can calculate the SHA-1 hash of images, check for steganography, validate the file extension against its actual format, perform Error Level Analysis (ELA), and extract EXIF metadata.

## Features

- **Upload Image:** Select an image file for analysis.
- **Calculate Hash (SHA-1):** Computes the SHA-1 hash of the uploaded image.
- **Check for Steganography:** Detects the presence of steganography in the image.
- **Check Signature:** Validates if the file extension matches the actual image type.
- **Perform ELA:** Analyzes the image to identify any modifications.
- **Get EXIF Data:** Extracts and displays EXIF metadata from the image.

## Requirements

Before running the application, ensure you have the following Python packages installed:

- `Pillow` - For image processing.
- `exifread` - For reading EXIF metadata.
- `opencv-python` - For image analysis.
- `numpy` - For numerical operations.

You can install the required packages using pip:

```bash
pip install Pillow exifread opencv-python numpy
```

## How to Use

1. **Clone the Repository:**

   Clone this repository to your local machine:

   ```bash
   git clone <repository-url>
   cd Image-Forensics-Tool
   ```

2. **Run the Application:**

   Open a terminal or command prompt, navigate to the directory where the script is located, and run:

   ```bash
   python image_forensics_tool.py
   ```

3. **Using the Application:**

   - Click on the **Upload Image** button to select an image file (supported formats: `.jpg`, `.jpeg`, `.png`).
   - Use the available buttons to perform various analyses on the uploaded image.
   - Results will be displayed in pop-up message boxes.

## File Structure

```
Image-Forensics-Tool/
│
├── image_forensics_tool.py   # Main application script
├── requirements.txt           # List of dependencies
└── README.md                  # Project documentation
```

## Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Pillow](https://pillow.readthedocs.io/en/stable/) for image processing.
- [OpenCV](https://opencv.org/) for image analysis.
- [ExifRead](https://pypi.org/project/exifread/) for extracting EXIF data.

```

### Instructions for Use

- **Replace `<repository-url>`** in the `Clone the Repository` section with the actual URL of your GitHub repository (if you plan to host the project on GitHub).
- You can add a `requirements.txt` file listing all the dependencies, which can be generated using the following command:

```bash
pip freeze > requirements.txt
```

This `README.md` provides users with all the necessary information to understand, install, and use the Image Forensics Tool effectively. Let me know if you need any further changes or additions!