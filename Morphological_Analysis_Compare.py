#Morphological Analysis
#Janome:ver.0.3.9
#MeCab:ver.0.996
#Juman++:ver.2.0.0
#Nagisa:ver.0.2.3

import re
import sys
import MeCab
import time
from pprint import pprint
from janome.tokenizer import Tokenizer
from pyknp import Juman
import codecs
import nagisa

def Janome_Run(str):
    t = Tokenizer()
    tokens=t.tokenize(str)
    for token in tokens:
        print(token)
    
def MeCab_Run(str):
    mecab = MeCab.Tagger()
    print(mecab.parse(str))
    
    
def Jumanpp_Run(str):
    jumanpp=Juman()
    tokens=jumanpp.analysis(str)
    for mrph in tokens.mrph_list():
        print(mrph.midasi,mrph.genkei,mrph.hinsi)
   
def Nagisa_Run(str):
    tokens = nagisa.tagging(str)
    print(tokens)
    
if __name__ == '__main__':
    print("Please put a text file.\n")
    filename = input()
    with open(filename) as file:
        script = file.read()
    
    print("Please select a way to morphological analysis\n")
    print(" Janome:ja, MeCab:me, Juman++:jp, Nagisa:na, end:e\n")
    way_of_morpho = input()

    #start to measure
    start = time.time()

    if way_of_morpho == "ja":
        Janome_Run(script)
    elif way_of_morpho == "me":
        MeCab_Run(script)
    elif way_of_morpho == "jp":
        Jumanpp_Run(script)
    elif way_of_morpho == "na":
        Nagisa_Run(script)
    else:
        print("Bye!")
    
    #finish measuring
    total_time = time.time() - start

    if way_of_morpho != "e":
        print("Total time:{0}".format(total_time) + "[sec]")
    

    
    
