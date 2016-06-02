
def ages():
        for i in range(10,100):
                for j in range(i+9,100):
                        count = 0
                        age = []
                        mom = []
                        for k in range(100-j):
                                if str(i+k) == str(j+k)[::-1]:
                                        count += 1
                                        age.append(i+k)
                                        mom.append(j+k)
                                        if count == 8:
                                                print age
                                                print mom
                                                print "His current age is ", age[5]
                                                return 

ages()
