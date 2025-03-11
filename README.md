# PRODIGY_CS_02
Image Encryption and Decryption
A Python-based tool to encrypt and decrypt images using a simple XOR cipher algorithm. This project allows users to secure their image files by encrypting the pixel data with a unique key.

Features
Encryption: Secures an image by modifying its pixel data with a user-defined key.

Decryption: Recovers the original image using the same key used for encryption.

Interactive CLI: Provides an easy-to-use command-line interface to perform encryption and decryption.

Requirements
Python 3.x

The Pillow library for image processing

Installation
Clone this repository:

bash
git clone https://github.com/your-username/image-encryption-tool.git
cd image-encryption-tool
Install dependencies:

bash
pip install Pillow
Usage
Run the script using Python and follow the prompts to encrypt or decrypt an image:

bash
python image_encryption_tool.py
Example
Encryption:

Choose option 1 for encryption.

Provide the input image file name (e.g., image.jpg).

Specify a name for the encrypted file (e.g., encrypted_image.jpg).

Enter an encryption key (an integer).

Decryption:

Choose option 2 for decryption.

Provide the encrypted image file name (e.g., encrypted_image.jpg).

Specify a name for the decrypted file (e.g., decrypted_image.jpg).

Enter the same encryption key used to encrypt the image.

Notes
Ensure the input image file exists in the same directory as the script or provide its full path.

Keep the encryption key safe—losing it means you cannot recover the original image.

License
This project is licensed under the MIT License. See the LICENSE file for details.
 
