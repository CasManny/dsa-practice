def valid_palindrone(s):
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and s[left].isalnum():
            left +=1 
        while left < right and s[right].isalnum():
            right -= 1
        
        if s[left].lower() != s[right].lower():
            return False
    return True
