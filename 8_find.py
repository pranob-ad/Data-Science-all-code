file = open("my_file.txt", "r")
text = file.read()
file.close()

paragraph = text.split("\n\n")
sentence = text.split(". ")
word = text.split(" ")
character = list(text)

print("Paragraphs:", len(paragraph))
print("Sentences:", len(sentence))
print("Words:", len(word))
print("Characters:", len(character))