from PIL import Image
import pytesseract
import json

def load_translations_from_json():
    with open("translations.json", "r") as json_file:
        translations = json.load(json_file)
    return translations

def translate_to_telugu(word, translations):
    return translations.get(word, word)

# Correct path to tesseract executable
path_to_tesseract = "/Users/prasanna/opt/anaconda3/opt/homebrew/bin/tesseract"  # Replace with the actual path

# image_path = "/Users/prasanna/Downloads/generated-random-text.jpg"
image_path = "/Users/prasanna/Downloads/stand.jpeg"

# Load translations from JSON file
translations = load_translations_from_json()

# Opening the image & storing it in an image object
img = Image.open(image_path)

# Providing the tesseract executable location to pytesseract library
pytesseract.tesseract_cmd = path_to_tesseract

# Declare text variable outside the try block
text = ""

try:
    # Passing the image object to image_to_string() function
    # This function will extract the text from the image
    text = pytesseract.image_to_string(img)
    # Displaying the extracted text
    # print(text[:-1])

except Exception as e:
    # Print any exceptions that occur
    print("Error:", e)

myconfig = r"--psm 6 --oem 3"

text_from_config = pytesseract.image_to_string(Image.open("/Users/prasanna/Downloads/stand.jpeg"), config=myconfig)  # Fix the import here as well
print(text_from_config)

# Writing the extracted text to a file, appending to existing content with newline
with open("output.txt", "a") as file:
    file.write("\n" + text_from_config)

# Displaying the entire content of the file
with open("output.txt", "r") as file:
    file_content = file.read()
    # print("\nFile Content:\n", file_content)

# Translate each word to Telugu using the translate_to_telugu function
telugu_words = [translate_to_telugu(word, translations) for word in file_content.split()]

# Reconstruct the text with newlines
telugu_text = ' '.join(telugu_words)

# Print the translated text
print("\nTranslated Content:\n", telugu_text)

# Write the translated text into a Telugu file with newline
with open("teluguFile.txt", "w", encoding="utf-8") as telugu_file:
    telugu_file.write(telugu_text)

print("Translated content written to teluguFile.txt")