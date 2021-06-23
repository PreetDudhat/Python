import pytesseract
import os
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\preet\tesseract ocr.exe"


img = Image.open("asd.png")
text = pytesseract.image_to_string(img)
print(text)
