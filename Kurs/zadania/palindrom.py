




def palindrom(s):
    s = [s.lower().replace() if x.isalnum()]
    return s == s[::-1]

s = "A man a plan a canal Panama"
ans = palindrom(s)

if ans:
    print("True")
else:
    print("False")