"""This program prints a list of all words that are anagrams"""
from collections import defaultdict
def anagrams(wlist):
    
    return ((w,cw) for i,w in enumerate(wlist)  for cw in wlist[i+1:]  if len(w)<=8 and sorted(w) == sorted(cw))
   
if __name__ == "__main__":
    with open('words.txt') as fin:
        wordlist =list(set( w for w in fin.read().split()  if w))
    print "Anagrams: \n"
    anags = defaultdict(list)

    fout = open("anagout.txt",'w')
    
    for w,cw in anagrams(wordlist):
        if w not in anags[w]:
            anags[w].append(w) 
        anags[w].append(cw)
        fout.write(str(anags))
        print anags

    fout.close()
       
                     
     
            
            
    
            
        
