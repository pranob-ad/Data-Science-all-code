vowel = ['a', 'e', 'i', 'o', 'u']
word = input("Enter a word: ")
if not any(char in vowel for char in word.lower()):
    print("it is vowel free word")
else:
    print("it has vowel in word")


# Alternative solution
def solve(str,n):
    for i in range(n):
        if str[i] in vowel:
            return "it has vowel in word"
    return "it is vowel free word"
str = word #input("Enter a word: ")
n = len(str)
print(solve(str, n))


#another solution is
def is_vowel_free(s, n):
    vowel = ['a', 'e', 'i', 'o', 'u']
    if not any(char in vowel for char in s.lower()):
        print("it is vowel free word")
    else:
        print("it has vowel in word")

#word = input("Enter a word: ")
is_vowel_free(word, len(word))