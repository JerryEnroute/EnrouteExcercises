def isPalindrome(word):
    if len(word) <= 1:
        return True
    else:
        if word[0] == word[-1]:
            return isPalindrome(word[1:-1])
        else:
            return False

print(isPalindrome('racecar'))

print(isPalindrome('carmine'))