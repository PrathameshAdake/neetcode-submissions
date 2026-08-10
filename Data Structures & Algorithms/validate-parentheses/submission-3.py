class Solution:
    def isValid(self, s: str) -> bool:
        temp = []
        hashcheck = {")": "(", "]" : "[", "}" : "{"}

        for c in s:
            if c in hashcheck:
                if temp and temp[-1] == hashcheck[c]:
                    temp.pop()
                else:
                    return False
            else:
                temp.append(c)
        return True if not temp else False