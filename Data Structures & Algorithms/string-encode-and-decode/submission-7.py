class Solution:

    #The last submitted solution performed encryption isntead of encoding
    #We just need to seperate values so that the reader can read them
    # 5#Hello5#World
    #  199#"199letterstring"
 
    def encode(self, strs: List[str]) -> str:

        myStr = ""

        for i in range(0, len(strs)):
            myStr += str(len(strs[i])) + "#" + strs[i]

        return myStr

    def decode(self, s: str) -> List[str]:

        myList = []
        i=0

        while i in range(0, len(s)):

             if s[i].isdigit():

              if s[i+1] == "#":
                myList.append(s[i+2 : i+2+int(s[i])])
                i = i+2+int(s[i])

              elif s[i+1].isdigit() and s[i+2] == "#":
                myList.append(s[i+3 : i+3+int(s[i] + s[i+1])])
                i = i+3+int(s[i] + s[i+1])

              elif s[i+1].isdigit() and s[i+2].isdigit() and s[i+3]=="#":
                myList.append(s[i+4 : i+4+int(s[i] + s[i+1] + s[i+2])])
                i = i+4+int(s[i] + s[i+1] + s[i+2])

             else:
                i += 1
            
        
        return myList

        
                

                



        
