import pyttsx3
import PyPDF2
from tkinter import *
import customtkinter as ctk
from tkinter.filedialog import askopenfilename
import threading


filename = ''
t1 = ''

def readBook():
    global filename

    page_no = int(pageNo.get()) - 1

    book = open(filename, 'rb')
    pdfReader = PyPDF2.PdfReader(book)
    pages = len(pdfReader.pages)
    print(pages)
    speaker = pyttsx3.init()
    page = pdfReader.pages[page_no]
    text = page.extract_text()
    speaker.say(text)
    speaker.runAndWait()


def startReading():
    global filename, t1

    if filename == '' or pageNo.get() == '':
        return
 if (t1):
        # t1.kill()
        return print('Already Running!')

    t1 = threading.Thread(target=readBook, args=())
    t1.start()


def selectFile():
    global filename
    filename = askopenfilename(title="Choose a pdf file!", filetypes=[('Pdf File', ('.pdf'))])

    bookTitle['text'] = filename


root = ctk.CTk()

root.geometry("300x150")
root.title("Audio Book")


openBtn = ctk.CTkButton(root, text="Open", command=selectFile)
openBtn.pack(pady=(10, 10))


bookTitle = Label(root, text="")
bookTitle.pack(pady=(5))

pageNo = ctk.CTkEntry(root, text_color="white")
pageNo.pack()

startButton = ctk.CTkButton(root, text="Start", command=startReading)
startButton.pack()
# book = open('python_book.pdf.pdf', 'rb')
# pdfReader = PyPDF2.PdfReader(book)
# pages = len(pdfReader.pages)
# print(pages)
# speaker = pyttsx3.init()
# page = pdfReader.pages[7]
# text = page.extract_text()
# speaker.say(text)
# speaker.runAndWait()

root.mainloop()