# keywords_from_pdf

m.py           : returns text from pdf file through the function pdf_to_text 

n.py           : This modeule can receive command line argument of text file ,
                 by default it uses the m.py module to extract text from pdf.
                 The stopwords and 'v*' are also removed. 
                 Finally,It stores the lists of text,textranks of keywords/small phrases in a pickle file

get_output.py  : loads the pickle file and takes command line arguments to display keywords and weights

The package pytextrank is extensively used which is a python wrapper for TextRank library.

Also , changes done to the pdf.py file of PyPDF2 package to support space after Tj/TJs 
