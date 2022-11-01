class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        sorted_words = [""] * len(words)
        for i in words:
            sorted_words[int(i[-1])-1] = i[:-1]
            
        return(' '.join(sorted_words))
