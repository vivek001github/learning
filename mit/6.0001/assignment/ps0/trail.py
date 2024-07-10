# import math
# x = int(input("enter the value of x:"));
# y = int(input("enter the value of y:"));
# sum = x**y 
# print(sum ,math.log(x,y))


def lyrics_to_frequencies(lyrics):
   myDict = {}
   for word in lyrics: 
        if word in myDict:  
            myDict[word] += 1
        else:
            myDict[word] = 1
        return myDict