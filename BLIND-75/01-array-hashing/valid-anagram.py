def valid_anagram(s, t):
    if len(s) != len(t):
        return False
    countT, countS = {}, {}

    n = len(s)
    
    for i in range(n):
        countS[s[i].lower()] = 1 + countS.get(s[i], 0)
        countT[t[i].lower()] = 1 + countT.get(t[i], 0)

    for ch in countT:
        if countT[ch] != countS.get(ch, 0):
            return False
    return True

print(valid_anagram("Silent", "Listen"))

    