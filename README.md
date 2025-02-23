# PDF to Text with Text-to-Speech

## Project Description
This project extracts text from a PDF file and converts it into speech using Python. It utilizes the **PyPDF2** library to read PDF documents and **pyttsx3** for text-to-speech conversion. The script reads a specific page from the PDF, extracts the text, and then uses a speech engine to read the extracted text aloud. This project is particularly useful for users who prefer an audio representation of textual content or need accessibility support.

## Features
- Extracts text from any PDF file.
- Reads text from a specific page (customizable).
- Converts extracted text into speech.
- Handles cases where PDFs have insufficient pages.
- Works offline without requiring an internet connection.
- Simple and lightweight with minimal dependencies.

## Tech Stack Used
- **Python** - Primary programming language.
- **PyPDF2** - For extracting text from PDFs.
- **pyttsx3** - For text-to-speech conversion.

## Setup Instructions
### Prerequisites
Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Installation
1. Clone this repository or create a new Python script.
2. Install the required dependencies using pip:
   ```bash
   pip install PyPDF2 pyttsx3
   ```
3. Place your PDF file in the same directory as the script.

### Usage
1. Modify the `pdf_path` variable to the name of your PDF file.
2. Adjust the `pages[index]` to specify the page number you want to extract text from.
3. Run the script using:
   ```bash
   python script.py
   ```
4. The extracted text will be read aloud using the text-to-speech engine.

## Future Enhancements
- Add support for extracting text from multiple pages.
- Implement a GUI for better user experience.
- Support for different voice and speech rate customization.
- Ability to save extracted text as a file.

## Conclusion
This project provides a simple and effective way to convert PDF text into speech. It can be extended for accessibility tools, audiobook generation, and document summarization.

