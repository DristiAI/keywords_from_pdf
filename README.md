# keywords_from_pdf

OUTPUT KEYWORDS: [out/20keywords.csv](https://github.com/DristiAI/keywords_from_pdf/blob/master/out/20keywords.csv)

**m.py**           : <pre>returns text from pdf file through the function pdf_to_text</pre> 

**n.py**           : <pre> This modeule can receive command line argument of text file ,
                     by default it uses the m.py module to extract text from pdf.
                     The stopwords and 'v*' are also removed. 
                     Finally,It stores the lists of text,textranks of keywords/small phrases in a pickle file</pre>

**get_output.py**  : <pre>loads the pickle file and takes command line arguments to display keywords and weights</pre>

<br/>
The package pytextrank is extensively used which is a python wrapper for TextRank library.
<br/>
**Note** Some changes need to be done to the pdf.py file of PyPDF2 package to support space after Tj/TJ in this pdf 
