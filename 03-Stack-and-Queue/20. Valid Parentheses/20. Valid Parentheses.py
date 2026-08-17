1class Solution:
2    def isValid(self, s: str) -> bool:
3        st=list()
4        for ch in s:
5            if ch in ({[:
6                st.append(ch)
7            else:
8                if len(st)==0:
9                    return False
10                else:
11                    if (ch==')' and st.pop()!='(') or (ch==']' and st.pop()!='[') or (ch=='}' and st.pop()!='{'):
12                        return False
13    
14        return True if len(st)==0 else False
15        