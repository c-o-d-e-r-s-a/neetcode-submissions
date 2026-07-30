class Solution:

    #The last submitted solution performed encryption isntead of encoding
    #We just need to seperate values so that the reader can read them
    # 5#Hello5#World
    #  199#"199letterstring"
 
    def encode(self, strs: List[str]) -> str:

        # Using a list and .join() is much faster than myStr += 
        encoded_list = []
        for s in strs:
            encoded_list.append(str(len(s)) + "#" + s)
        return "".join(encoded_list)

    def decode(self, s: str) -> List[str]:

        myList,i = [],0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            myList.append(s[j+1 : j+1+length])
            i = j + 1 + length
        
        return myList
        


        