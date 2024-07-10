# importing the modules
import PyPDF2
import pyttsx3

path = open('./res/pdfs/twopage.pdf', 'rb')
pdf = PyPDF2.PdfReader(path)
from_page = pdf.pages[0]
text = from_page.extract_text()

speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()
