numlist1 = [1,2,3,4,5]
numlist2 = [3,4,5,6,7,3]
newlist = []
nonum = []
def intersect(numlist1, numlist2, newlist, nonum):
    for i in range(len(numlist1)):
        for j in range(len(numlist2)):
            if numlist1[i] == numlist2[j]:
                    newlist.append(numlist1[i])
            else:
                nonum.append(numlist1[1])
    return newlist

print(intersect(numlist1, numlist2, newlist, nonum))

def elimrep(newlist):
    finlist = []
    for i in range(len(newlist)):
        for j in range(len(newlist)):
            if newlist[i] == newlist[j]:
                del newlist[j]
            else:
                finlist.append(newlist[j])
    return finlist
print(elimrep(newlist))