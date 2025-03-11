from PIL import Image

def encrypt_image(input_path,output_path,key):
    img = Image.open(input_path)
    pixels=img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i,j]

            pixels[i , j] =(r^key , g^key , b^key)
    img.save(output_path)
    print("Encryption done")

def decryption_image(input_path,output_patha,key):
    encrypt_image(input_path,output_patha,key) 


choice = int(input("Press 1 for Encryption\nPress 2 for decryption\n"))
if (choice == 1):
    input_path = input("Enter the input image name: ")
    output_path = input("Enter the name of your encrypted file: ")
    key = int(input("Enter the key: "))
    encrypt_image(input_path,output_path,key)

else :
    input_path = input("Enter the input image name: ")
    output_path = input("Enter the name of your decrypted file: ")
    key = int(input("Enter the key: "))
    decryption_image(input_path,output_path,key)
