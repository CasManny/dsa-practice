from collections import defaultdict, deque

class Solution:
    def alienDictionary(words):
        adj = {char: set() for word in words for char in word}
        in_degrees = {char: 0 for char in adj}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""

            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        in_degrees[w2[j]] += 1
                    break 

            queue = deque([char for char in in_degrees if in_degrees[char] == 0])
            res = []

            while queue:
                char = queue.popleft()
                res.append(char)
                for neighbor in adj[char]:
                    in_degrees[neighbor] -= 1
                    if in_degrees[neighbor] == 0:
                        queue.append(neighbor)

        if len(res) != len(in_degrees):
            return ""

        return "".join(res)
        