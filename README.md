Image Steganography with AES Encryption
This project provides a Python-based application that combines image steganography and AES encryption to securely hide messages within image files. The application allows users to encrypt text messages and embed them into images, as well as extract and decrypt hidden messages from steganographic images.

DOWNLOAD OUR FIRST RELEASE FROM 

Features
AES Encryption: Utilizes the PyCryptodome library to encrypt messages with AES-128 or AES-256 encryption standards.
Image Steganography: Employs the Pillow library to embed encrypted messages into images using Least Significant Bit (LSB) steganography.
User-Friendly Interface: Provides a straightforward interface for users to hide and extract messages.
System Requirements
Operating System: Windows, macOS, or Linux
Python Version: Python 3.6 or newer
Dependencies:
PyCryptodome
Pillow
Ensure that the required Python libraries are installed. Refer to the System Requirements section for detailed instructions.

Usage
Hiding a Message:

Prepare the text message you wish to hide.
Select a cover image (e.g., cover_image.png).
Run the application and choose the "Hide Message" option.
Input the message, select the cover image, and provide a password for encryption.
The application will generate a new image file (e.g., stego_image.png) containing the hidden message.
Extracting a Message:

Run the application and choose the "Extract Message" option.
Select the steganographic image (e.g., stego_image.png).
Provide the password used during the hiding process.
The application will extract and decrypt the hidden message, displaying it to you.
Contributing
Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

License
This project is licensed under the MIT License.

Acknowledgments
PyCryptodome: For providing robust cryptographic functionalities.
Pillow: For offering comprehensive image processing capabilities.
This project was inspired by various open-source steganography and encryption tools.
