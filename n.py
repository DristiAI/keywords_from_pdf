import pytextrank
import json
import os
import re
from nltk.corpus import stopwords
import pickle
from m import pdf_to_text #the module created in directory

PATH='data/JavaBasics-notes.pdf'
FILE1='./_encap/text.json'


if os.path.exists(FILE1):
    print('using the existing file...')
else:
    with open(FILE1,'w') as f:
        text=pdf_to_text(PATH)
        text=re.sub(r'\W',' ',text).lower()
        print(text)
        dict_={'id':'000','text':text}
        r=json.dumps(dict_)
        f.write(r)
        
        

tmp_json="./_encap/tmp.json"
tmp2_json='./_encap/tmp2.json'

with open(tmp_json, 'w') as f:
    for graf in pytextrank.parse_doc(pytextrank.json_iter(FILE1)):
        f.write("%s\n" % pytextrank.pretty_print(graf._asdict()))
        # to view output 
        #print(pytextrank.pretty_print(graf))
graph, ranks = pytextrank.text_rank(tmp_json)
pytextrank.render_ranks(graph, ranks)

stopwords=stopwords.words('english')

with open(tmp2_json, 'w') as f:
    k=[]
    out=open('keywordsall.data','wb')
    output=open('./out/all_keywords.txt','w')
    for rl in pytextrank.normalize_key_phrases(tmp_json, ranks):
        f.write("%s\n" % pytextrank.pretty_print(rl._asdict()))
        # to view output in this notebook
        rl= list(rl)
        if(rl[0] in stopwords or rl[3].startswith('v')):  #removes stopwords and verbs
            pass
        else:
            print(rl[0:2])
            pickle.dump(rl[0:2],out)
            output.write(json.dumps(rl[0:2]))
            output.write('\n')
            
    out.close()
               
   


