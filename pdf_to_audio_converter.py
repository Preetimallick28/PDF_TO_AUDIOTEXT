import PyPDF2
import pyttsx3
import os

# Open the PDF file in STRING mode
pdf_path = 'Django Rest Framework Interview Question.pdf'

os.startfile(pdf_path)
with open(pdf_path , 'rb') as path:
    pdf_Reader = PyPDF2.PdfReader(pdf_path)

# Get text from the third page (index starts from 0)
pages = pdf_Reader.pages

total_pages = len(pages)

if total_pages>1:
    from_page = pages[0]

    # Extract text
    text = from_page.extract_text() if from_page else "No text found."

    # Initialize text-to-speech engine
    speak = pyttsx3.init()
    speak.say(text)
    speak.runAndWait()
else:
    print("Error:The PDF has less than 2 pages")













