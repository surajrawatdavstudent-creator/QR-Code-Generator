import qrcode
url = input("Enter you url :").strip()
file_path = "C:\\Users\\suraj\\OneDrive\\Documents\\Python Prac\\qrcode.png"

img = qrcode.make(url)
img.save(file_path)
print("Your QR Code is Genrated Sucessfully!")