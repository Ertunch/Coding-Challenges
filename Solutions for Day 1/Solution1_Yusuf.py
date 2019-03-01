#All credit goes to Eyup
#This solution expands Eyup's solution
from random import shuffle
a = [i for i in range(18)]
shuffle(a)  #randomly ordering the list

#code
k=17
b = [(i,j) for i in sorted(a) for j in sorted(a) if (i+j)==k] #used sorted to make the code cleaner
b[0:int((len(b)/2))] #taking the first half of the results
