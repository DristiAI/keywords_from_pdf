import PyPDF2
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

filename='data/JavaBasics-notes.pdf'
def pdf_to_text(filename):
    with open(filename,'rb') as f:
        Reader=PyPDF2.PdfFileReader(f)
        text='' 
        for i in range(Reader.numPages):
            page=Reader.getPage(i)
            text+=page.extractText()
        return text
if __name__=='__main__':
     text=pdf_to_text(filename)
     print(text)
    
