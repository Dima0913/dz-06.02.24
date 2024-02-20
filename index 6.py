with open('file.txt', 'w', encoding='utf-8') as file:
    file.write("Hello world\n")
  
old_word = "Hello"
new_word = "Bye"

with open('file.txt', 'r', encoding='utf-8') as file:
    text = file.read()

text = text.replace(old_word, new_word)
print(text)