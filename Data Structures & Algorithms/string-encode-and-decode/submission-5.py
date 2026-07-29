class Solution:

    #This function will encode a string
    #Lets use this method for encoding move every letter by 7 to the right
    #So if we have A then we make it -> G
    #If any numbers in the string we will increase them by 3
    #For special characters and whitespace we will leave them as they are
    #HeLlO24 My !23NaME -> (encode)OlSsV57 Tf !56UhTL -> (decode)HeLlO24 My !23NaME
    #We will use ASCII values
    #48-57(0-9), 65-90(A-Z), 97-122(a-z), 32 is blank space
    #For every seperated value in the list we will use a ,
 
    def encode(self, strs: List[str]) -> str:

        if len(strs) == 0:
            return "ZERO"

        myStr = ""

        for i in range (0,len(strs)):
            
            for j in range (0, len(strs[i])):

                char = ord(strs[i][j])

                if (char < 84 and char >= 65) or (char < 116 and char >= 97):
                    myStr += chr(char+7)

                elif (char >= 84 and char <= 90) or(char >= 116 and char <= 122):
                    myStr += chr(char-19)

                elif(char < 55 and char >= 48):
                    myStr += chr(char + 3)

                elif(char <= 57 and char >=55):
                    myStr += chr(char - 7)
                
                else:
                    myStr += strs[i][j]

            if not(i == len(strs) - 1):   
                myStr += "🙂"

        return myStr

    def decode(self, s: str) -> List[str]:

        if(len(s) == 0):
            myList = [""]
        elif(s == "ZERO"):
            myList = []
        else:
            myList = s.split("🙂")

        for i in range (0, len(myList)):

            myStr = ""

            for j in range (0, len(myList[i])):

                char = ord(myList[i][j])

                if (char <= 90 and char >= 72) or (char <= 122 and char >= 104):
                    myStr += chr(char-7)

                elif (char >= 65 and char < 72) or(char >= 97 and char < 104):
                    myStr += chr(char+19)

                elif(char <= 57 and char >= 51):
                    myStr += chr(char - 3)
                
                elif(char < 51 and char >=48):
                    myStr += chr(char + 7)

                else:
                    myStr += chr(char)
            
            myList[i] = myStr

        return myList
                
                

                



        
