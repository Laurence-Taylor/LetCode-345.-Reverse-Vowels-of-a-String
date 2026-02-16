class Solution:
    def reverseVowels(self, s: str) -> str:
        # create a Set of Vowels
        vowels = set("aeiouAEIOU")
        # Find vowels
        vowels_found = [char for char in s if char in vowels]
        # Init reversed word
        reversed_vowels_word = ''
        # Create reversed vowels word
        for j in range(0,len(s)):
            if s[j] in vowels:
                reversed_vowels_word += vowels_found.pop() 
            else:
                reversed_vowels_word += s[j]
        return reversed_vowels_word
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.reverseVowels("IceCreAm"))