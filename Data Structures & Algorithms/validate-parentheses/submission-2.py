class Solution:
    def isValid(self, s: str) -> bool:
        ans = []
        for i in range(len(s)):
            if s[i]=="(" or s[i] == "{" or s[i] == "[":
                ans.append(s[i])
            elif s[i]==")":
                if not ans:  # stack is empty but we need to close something
                    return False
                if ans[-1] == "{" or ans[-1]=="[":
                    return False
                elif ans[-1] == "(":
                    ans.pop()
                else:
                    return False
            elif s[i]=="}":
                if not ans:  # stack is empty but we need to close something
                    return False
                if ans[-1] == "(" or ans[-1]=="[":
                    return False
                elif ans[-1] == "{":
                    ans.pop()
                else:
                    return False
            elif s[i]=="]":
                if not ans:  # stack is empty but we need to close something
                    return False
                if ans[-1] == "{" or ans[-1]=="(":
                    return False
                elif ans[-1] == "[":
                    ans.pop()
                else:
                    return False
        if len(ans) == 0:
            return True
        return False

