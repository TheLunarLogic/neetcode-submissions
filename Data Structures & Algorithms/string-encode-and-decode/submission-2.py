class Solution:

    def encode(self, strs: List[str]) -> str:
        en_string = ""
        for c in strs :
            en_string += str(len(c))+"#"+c 
        print(en_string)
        return en_string


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            res.append(s[j+1 : j+1+length])
            i = j+1+length
        return res
