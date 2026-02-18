class Solution:
    def reverseVowels_2(self, s: str) -> str:
        # create a Set of Vowels
        vowels = set("aeiouAEIOU")
        # Convert vowels to a list
        s = list(s)
        # define two pointers to move from both ends of the list moving inward
        pointer_init = 0
        pointer_end = len(s) - 1
        # while pointer_init is not reached pointer_end
        while pointer_init < pointer_end:
            # while pointer_init is not reached pointer_end and letter in pointer_init is not a vowel
            while pointer_init < pointer_end and s[pointer_init] not in vowels:
                # Move pointer to the next letter
                pointer_init += 1
            # while pointer_init is not reached pointer_end and letter in pointer_end is not a vowel
            while pointer_init < pointer_end and s[pointer_end] not in vowels: 
                # Move pointer to the previous letter
                pointer_end -= 1
            # At this point both are vowels so lets swap them
            s[pointer_init], s[pointer_end] = s[pointer_end], s[pointer_init]
            # move pointer_init and pointter_end
            pointer_init += 1
            pointer_end -= 1
        # Return reversed vowels word
        return "".join(s)


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