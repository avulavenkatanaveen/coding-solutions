class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        l = []
        w = ""
        for i in paragraph:
            if i.isalpha():
                w += i.lower()
            else:
                if w != "":
                    l.append(w)
                    w = ""
        if w != "":
            l.append(w)
            
        max_count = 0
        res = ""
        for word in l:
            if word in banned:
                continue
                
            c = 0
            for item in l:
                if item == word:
                    c += 1
                    
            if c > max_count:
                max_count = c
                res = word
                
        return res