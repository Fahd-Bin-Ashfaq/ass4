from PIL import Image
import pytesseract

# Agar tesseract install hai to yeh line zaroori ho sakti hai:
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Correct path to your image
image_path = r"C:\Users\Fahad Ahmed\Desktop\mid\1.jpeg"

# Load the image
image = Image.open(image_path)

# OCR to extract text
text = pytesseract.image_to_string(image)

# Print extracted text
print("Extracted Text:\n")
print(text)
