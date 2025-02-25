from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import pad, unpad
import base64
import os
from PIL import Image

def derive_key(password: str, salt: bytes, key_size: int):
    """Derives a key from the password using PBKDF2."""
    return PBKDF2(password, salt, dkLen=key_size, count=100000)

def encrypt_message(message: str, password: str, aes_mode: str = "AES-128"):
    """Encrypts the message using AES encryption (128-bit or 256-bit)."""
    key_size = 16 if aes_mode == "AES-128" else 32
    salt = get_random_bytes(16)  # Generate a new salt
    key = derive_key(password, salt, key_size)
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
    return base64.b64encode(salt + cipher.iv + ciphertext)  # Return as bytes

def decrypt_message(encrypted_data: bytes, password: str, aes_mode: str = "AES-128"):
    """Decrypts the message using AES encryption (128-bit or 256-bit)."""
    key_size = 16 if aes_mode == "AES-128" else 32
    encrypted_data = base64.b64decode(encrypted_data)
    salt, iv, ciphertext = encrypted_data[:16], encrypted_data[16:32], encrypted_data[32:]
    key = derive_key(password, salt, key_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_padded_data = cipher.decrypt(ciphertext)
    return unpad(decrypted_padded_data, AES.block_size).decode("utf-8")

def embed_data_in_image(image_path, output_path, encrypted_bytes):
    """Embeds encrypted data inside an image using LSB steganography."""
    img = Image.open(image_path)
    pixels = img.load()
    text_length_bin = f"{len(encrypted_bytes):032b}"
    for i in range(32):
        x, y = i % img.width, i // img.width
        r, g, b = pixels[x, y]
        r = (r & ~1) | int(text_length_bin[i])
        pixels[x, y] = (r, g, b)
    binary_text = ''.join(f"{byte:08b}" for byte in encrypted_bytes)
    for i in range(len(binary_text)):
        x, y = (i + 32) % img.width, (i + 32) // img.width
        r, g, b = pixels[x, y]
        r = (r & ~1) | int(binary_text[i])
        pixels[x, y] = (r, g, b)
    img.save(output_path)

def extract_text_from_image(image_path):
    """Extracts encrypted text from an image by reading LSB-encoded data."""
    img = Image.open(image_path)
    pixels = img.load()
    length_bin = "".join(str((pixels[i, 0][0] & 1)) for i in range(32))
    text_length = int(length_bin, 2)
    binary_text = []
    for i in range(text_length * 8):
        x, y = (i + 32) % img.width, (i + 32) // img.width
        binary_text.append(str(pixels[x, y][0] & 1))
    extracted_bytes = bytearray(int("".join(binary_text[i:i+8]), 2) for i in range(0, len(binary_text), 8))
    return extracted_bytes

def hide_data(message_file, cover_file, output_folder, algorithm, password, confirm_password):
    if password != confirm_password:
        raise ValueError("Passwords do not match!")
    with open(message_file, "r") as f:
        message = f.read()
    encrypted_data = encrypt_message(message, password, algorithm)
    stego_filename = f"{os.path.splitext(os.path.basename(cover_file))[0]}_stego.png"
    output_path = os.path.join(output_folder, stego_filename)
    embed_data_in_image(cover_file, output_path, encrypted_data)
    return output_path

def extract_data(stego_file, output_folder, password, aes_mode="AES-128"):
    """Extracts and decrypts text from an image."""
    extracted_bytes = extract_text_from_image(stego_file)
    decrypted_text = decrypt_message(extracted_bytes, password, aes_mode)
    extracted_filename = f"{os.path.splitext(os.path.basename(stego_file))[0]}_extracted.txt"
    output_path = os.path.join(output_folder, extracted_filename)
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(decrypted_text)
    return output_path
