class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split(" ")
        temp = ['0']*len(s)
        for i in s:
            temp[int(i[len(i)-1])-1] = i[:len(i)-1]
        return " ".join(temp)
