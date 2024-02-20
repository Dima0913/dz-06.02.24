with open('file.txt', 'w', encoding='utf-8') as file:
    file.write("fgjfgfgjgfjfgjfg 1\n")
    file.write("fgjfgjfgjfg 2\n")
    file.write("7383422\n")
    file.write("ghkghkghkghhkgkghkgds\n")

word_to_count = "Рядок"

with open('file.txt', 'r', encoding='utf-8') as file:
    text = file.read()

word_count = text.count(word_to_count)

print(f"Кількість слів '{word_to_count}' у файлі: {word_count}")