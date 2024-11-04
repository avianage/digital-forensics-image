import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import exifread
import hashlib
import numpy as np
import cv2
import mimetypes
import os

class ImageForensicsTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Forensics Tool")
        self.root.geometry("700x700")  # Adjusted window size
        self.root.configure(bg="#e0f7fa")  # Light blue background

        self.image_path = None

        # Create the UI elements
        self.title_label = tk.Label(self.root, text="Image Forensics Tool", font=("Arial", 24), bg="#e0f7fa", fg="#00796b")
        self.title_label.pack(pady=20)

        self.image_label = tk.Label(self.root, bg="#e0f7fa")
        self.image_label.pack(pady=10)

        # Frame to hold buttons side by side
        self.button_frame = tk.Frame(self.root, bg="#e0f7fa")
        self.button_frame.pack(pady=10)

        # Create buttons and add them to the button frame in a grid layout
        self.upload_button = tk.Button(self.button_frame, text="Upload Image", command=self.upload_image, bg="#4CAF50", fg="white", font=("Arial", 12), padx=10, pady=5)
        self.upload_button.grid(row=0, column=0, padx=5, pady=5)

        self.hash_button = tk.Button(self.button_frame, text="Calculate Hash (SHA-1)", command=self.calculate_hash, bg="#2196F3", fg="white", font=("Arial", 12), padx=10, pady=5)
        self.hash_button.grid(row=0, column=1, padx=5, pady=5)

        self.signature_button = tk.Button(self.button_frame, text="Check Signature", command=self.check_signature, bg="#9C27B0", fg="white", font=("Arial", 12), padx=10, pady=5)
        self.signature_button.grid(row=0, column=2, padx=5, pady=5)

        self.ela_button = tk.Button(self.button_frame, text="Perform ELA", command=self.perform_ela, bg="#673AB7", fg="white", font=("Arial", 12), padx=10, pady=5)
        self.ela_button.grid(row=0, column=3, padx=5, pady=5)

        self.metadata_button = tk.Button(self.button_frame, text="Extract EXIF Metadata", command=self.display_exif_metadata, bg="#795548", fg="white", font=("Arial", 12), padx=10, pady=5)
        self.metadata_button.grid(row=0, column=4, padx=5, pady=5)

        # Common text area to display metadata and other information
        self.metadata_text = tk.Text(root, wrap=tk.WORD, font=("Arial", 10), padx=10, pady=5)
        self.metadata_text.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    def upload_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif;*.bmp;*.tiff;*.tif")])
        if self.image_path:
            self.display_image()

    def display_image(self):
        img = Image.open(self.image_path)
        img.thumbnail((200, 200))  # Resize for display
        self.img_tk = ImageTk.PhotoImage(img)
        self.image_label.config(image=self.img_tk)

    def calculate_hash(self):
        if self.image_path:
            hash_value = self.hash_image(self.image_path)
            self.metadata_text.delete("1.0", tk.END)  # Clear the text area
            self.metadata_text.insert(tk.END, f"SHA-1 Hash: {hash_value}\n")
        else:
            messagebox.showwarning("Warning", "Please upload an image first.")

    def hash_image(self, image_path):
        hash_sha1 = hashlib.sha1()
        with open(image_path, "rb") as f:
            while chunk := f.read(8192):
                hash_sha1.update(chunk)
        return hash_sha1.hexdigest()

    def check_signature(self):
        if self.image_path:
            file_extension = self.image_path.split('.')[-1].lower()
            actual_format = self.detect_file_signature(self.image_path)
            self.metadata_text.delete("1.0", tk.END)  # Clear the text area

            if actual_format:
                if actual_format == file_extension:
                    self.metadata_text.insert(tk.END, "Signature is valid.\n")
                else:
                    self.metadata_text.insert(tk.END, f"Signature is invalid: expected .{actual_format} but found .{file_extension}\n")
            else:
                self.metadata_text.insert(tk.END, "Unknown file format or unsupported image type.\n")
        else:
            messagebox.showwarning("Warning", "Please upload an image first.")

    def detect_file_signature(self, file_path):
        """Detect the actual file signature based on its magic number."""
        with open(file_path, 'rb') as file:
            header = file.read(10)

            # Check for JPEG
            if header[:3] == b'\xff\xd8\xff':
                return 'jpg'
            # Check for PNG
            elif header[:8] == b'\x89PNG\r\n\x1a\n':
                return 'png'
            # Check for GIF
            elif header[:6] in [b'GIF87a', b'GIF89a']:
                return 'gif'
            # Check for BMP
            elif header[:2] == b'BM':
                return 'bmp'
            # Check for TIFF
            elif header[:4] in [b'II*\x00', b'MM\x00*']:
                return 'tiff'
            else:
                return None

    def perform_ela(self):
        if self.image_path:
            result = self.ela_analysis(self.image_path)
            self.metadata_text.delete("1.0", tk.END)  # Clear the text area
            self.metadata_text.insert(tk.END, result + "\n")
        else:
            messagebox.showwarning("Warning", "Please upload an image first.")

    def ela_analysis(self, image_path):
        try:
            original = Image.open(image_path).convert("RGB")
            original.save("temp_recompressed.jpg", "JPEG", quality=90)
            recompressed = Image.open("temp_recompressed.jpg").convert("RGB")

            original_np = np.array(original)
            recompressed_np = np.array(recompressed)

            ela = cv2.absdiff(original_np, recompressed_np)
            ela_gray = cv2.cvtColor(ela, cv2.COLOR_RGB2GRAY)
            ela_normalized = cv2.normalize(ela_gray, None, 0, 255, cv2.NORM_MINMAX)
            _, ela_thresholded = cv2.threshold(ela_normalized, 30, 255, cv2.THRESH_BINARY)

            ELA_result_path = "ela_result.png"
            cv2.imwrite(ELA_result_path, ela_thresholded)

            return f"ELA result saved as {ELA_result_path}"
        except Exception as e:
            return f"Error performing ELA: {str(e)}"

    def extract_exif_metadata(self, image_path):
        try:
            with open(image_path, 'rb') as f:
                tags = exifread.process_file(f)
                metadata = {tag: tags[tag] for tag in tags}
            return metadata
        except Exception as e:
            messagebox.showerror("Error", f"Failed to extract metadata: {e}")
            return None

    def display_exif_metadata(self):
        if self.image_path:
            metadata = self.extract_exif_metadata(self.image_path)
            self.metadata_text.delete("1.0", tk.END)  # Clear the text area

            if metadata:
                for tag, value in metadata.items():
                    self.metadata_text.insert(tk.END, f"{tag}: {value}\n")
            else:
                self.metadata_text.insert(tk.END, "No metadata found in this image.\n")
        else:
            messagebox.showwarning("No Image", "Please upload an image first.")


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageForensicsTool(root)
    root.mainloop()
