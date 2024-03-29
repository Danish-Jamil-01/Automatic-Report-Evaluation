import pytesseract
from PIL import Image

# Path to the Tesseract executable, update this according to your installation
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def image_to_text(image_path, output_file):
    try:
        # Open the image file
        with Image.open(image_path) as img:
            # Use Tesseract to do OCR on the image
            text = pytesseract.image_to_string(img)
            
            # Write the extracted text to a file
            with open(output_file, "w", encoding="utf-8") as file:
                file.write(text)
            print("Text extracted successfully and written to", output_file)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    # Path to the image file
    image_path = 'report.jpg'  # Update this with your image file path
    
    # Output file path
    output_file = "ExtractedText.txt"

    # Convert image to text and write to file
    image_to_text(image_path, output_file)
