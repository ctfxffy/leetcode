class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count

        if len(s) < total_len:
            return []

        need = {}
        for word in words:
            need[word] = need.get(word, 0) + 1

        ans = []

        for offset in range(word_len):
            left = offset
            count = 0
            window = {}

            for right in range(offset, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]

                if word not in need:
                    window = {}
                    count = 0
                    left = right + word_len
                    continue

                window[word] = window.get(word, 0) + 1
                count += 1

                while window[word] > need[word]:
                    left_word = s[left:left + word_len]
                    window[left_word] -= 1
                    count -= 1
                    left += word_len

                if count == word_count:
                    ans.append(left)
                    left_word = s[left:left + word_len]
                    window[left_word] -= 1
                    count -= 1
                    left += word_len

        return ans
