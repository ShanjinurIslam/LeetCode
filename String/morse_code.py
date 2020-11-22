class Solution(object):
    def to_morse(self,word):
        arr = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."] 
        
        morse = ""
        
        for each in word:
            morse += arr[ord(each) - 97]
        
        return morse
    
    def uniqueMorseRepresentations(self, words):
        hash_map = {}
        
        for word in words:
            morse_code = self.to_morse(word)
            
            if morse_code in hash_map:
                continue
            else:
                hash_map[morse_code] = 1
                
        return len(hash_map.keys())