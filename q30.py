class Solution(object):

    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        
        # trivial case
        if len(s) == 0 or len(words) == 0:
        	return []

        # put words in a set to speed up the lookup process O(1)
        words_set = set(words)
        word_length = len(words[0])
        word_counter = {}
        for word in words:
        	if word not in word_counter:
        		word_counter[word] = 1
        	else:
        		word_counter[word] += 1

        # set to store start index which is not a word
        not_word_indices = set()

        result = []
        
        for i in range(len(s) - len(words) * word_length+1):
        	seen_words = {}
        	for j in range(len(words)):
        		curr = i + j * word_length
        		if curr in not_word_indices:
        			break
	        	potential_word = s[curr, curr + word_length]
    	    	if potential_word not in words_set:
        			not_word_indices.add(curr)
        			break
        		else:
        			if potential_word in seen_words:
        				seen_words[potential_word] += 1
        			else:
        				seen_words[potential_word] = 1
        	else:
        		for word in word_counter:
        			if word not in seen_words or seen_words[word] != word_counter[word]:
        				break
        		else:
        			result.append(i)
        return result