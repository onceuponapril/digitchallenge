import re

class ExtractDigit:

    def __init__(self,input):
        self.input=str(input)


    def sumInput(self):
        sum=0
        digitList=re.findall(r"[+-]?\d+(?:\.\d+)?",str(self.input))

        for i in digitList:
            sum+=int(i)

        if sum==0:
            sum=""

        return sum
