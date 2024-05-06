from functools import reduce
#1 score of the string
s="hello"
asci_val = list(map(lambda x: ord(x), "hello"))
pairs_ascii=zip(asci_val,asci_val[1:])
pairs_diff=map(lambda x: abs(x[0] - x[1]),pairs_ascii)
score=reduce(lambda a,b: a+b,pairs_diff)
print(score)
