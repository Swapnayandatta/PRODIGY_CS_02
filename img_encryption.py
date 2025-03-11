from PIL import Image
import os

def encrypt_image(input_path, output_path, key):
    if not os.path.exists(input_path):
        print("Error: Input file does not exist.")
        return
    
    img = Image.open(input_path)
    img = img.convert("RGB")  # Ensure image is in RGB mode
    pixels = img.load()
    normalized_key = key % 256

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = (r ^ normalized_key, g ^ normalized_key, b ^ normalized_key)
    
    img.save(output_path,format=img.format)
    print(f"Process done. File saved as {output_path}")

def decrypt_image(input_path, output_path, key):
    # XOR operation is symmetric, so we use encrypt_image function
    encrypt_image(input_path, output_path, key)

# Main Menu
choice = int(input("Press 1 for Encryption\nPress 2 for Decryption\n"))

if choice == 1:
    input_path = input("Enter the input image name: ")
    output_path = input("Enter the name of your encrypted file: ")
    key = int(input("Enter the key: "))
    encrypt_image(input_path, output_path, key)

elif choice == 2:
    input_path = input("Enter the input image name: ")
    output_path = input("Enter the name of your decrypted file: ")
    key = int(input("Enter the key: "))
    decrypt_image(input_path, output_path, key)

else:
    print("Invalid choice. Please enter 1 or 2.")
