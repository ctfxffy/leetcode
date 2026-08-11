class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []
        i = 0
        n = len(words)

        while i < n:
            line_len = len(words[i])
            j = i + 1

            while j < n and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1

            line_words = words[i:j]
            words_len = sum(len(word) for word in line_words)
            gaps = j - i - 1

            if j == n or gaps == 0:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
            else:
                total_spaces = maxWidth - words_len
                base_spaces = total_spaces // gaps
                extra_spaces = total_spaces % gaps

                parts = []
                for k in range(gaps):
                    parts.append(line_words[k])
                    spaces = base_spaces + (1 if k < extra_spaces else 0)
                    parts.append(" " * spaces)
                parts.append(line_words[-1])
                line = "".join(parts)

            res.append(line)
            i = j

        return res
