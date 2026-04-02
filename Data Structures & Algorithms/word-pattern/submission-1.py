class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        
        if len(pattern) != len(words):
            return False
        
        char_to_word = {}
        # We use a set to keep track of words already assigned to a character
        used_words = set() 
        
        for char, word in zip(pattern, words):
            if char in char_to_word:
                # If character exists, it must match the current word
                if char_to_word[char] != word:
                    return False
            else:
                # If character is new, the word must also be new
                if word in used_words:
                    return False
                char_to_word[char] = word
                used_words.add(word)
                
        return True
