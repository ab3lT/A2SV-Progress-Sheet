class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s[::-1].split() # Reversing the order of the words 
        words.sort() # sorting the words by the last numbers
        result = [ word[1:][::-1] for word in words ] # Strip the digit off and re-reverse the words.
        return ' '.join(result)