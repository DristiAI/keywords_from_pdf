import argparse
import pickle
parser=argparse.ArgumentParser(description="pass the max number of keywords")
parser.add_argument('--n',help='number of keywords to output')
args=vars(parser.parse_args())

PATH='keywordsall.data'
f=open(PATH,'rb')
#data=pickle.load(f)

if(args['n']):
    n=int(args['n'])
else:
    n=20
def print_keywords(n):
    for i in range(n):
        l=pickle.load(f) 
        print('{} , {}'.format(l[0],l[1]))
        
print_keywords(n)
