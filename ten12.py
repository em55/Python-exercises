def rev_pairs(wlist):
        return ((w,cw) for i,w in enumerate(wlist)  for cw in wlist[i+1:]  if w == cw[::-1])

if __name__ == "__main__":
        with open('words.txt') as fin:
                        wordlist =list(set( w for w in fin.read().split()  if w))
        print len(wordlist)
        print "Reverse pairs are: \n"
        for w,cw in rev_pairs(wordlist):
                 print w,cw
