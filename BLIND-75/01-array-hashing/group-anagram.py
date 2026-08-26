from collections import defaultdict

def group_anagram(words):
    group = defaultdict(list)

    for word in words:
        count = [0] * 26

        for ch in word:
            count[ord(ch) - ord("a")] += 1
        
        group[tuple(count)].append(word)


    return list(group.values())

words = ["word", "code", "deco", "rdwo"]
print(group_anagram(words))        


