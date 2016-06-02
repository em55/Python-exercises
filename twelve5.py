import ast
import regex

def diff(w1, w2):
    count = 0
    for c1, c2 in zip(w1, w2):
        if c1 != c2:
            count += 1
    return count

        
if __name__=="__main__":
    anags = ''
    with open('anagrams.txt') as fin:
        for word in fin.read().split():
            anags+=word
    anags = ast.literal_eval(anags)
    #print anags
    print "Metathesis pairs: "
    for k,v in anags.iteritems():
        for w in v:
           if diff(k,w) == 2:
               print k,w
        
