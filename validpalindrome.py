def isPalindrome(self, s: str) -> bool:
        import string
        newstring=s.translate(str.maketrans('','',string.punctuation))
        newstring = ''.join([s for s in newstring if s!=' '])
        newstring = newstring.lower()

        print(newstring)
        left = 0
        right = len(newstring)-1
        print(newstring)
        while left<right:
            if newstring[left]==newstring[right]:
                left+=1
                right-=1
            else:
                return False
        return True
