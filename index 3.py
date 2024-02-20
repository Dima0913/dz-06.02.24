with open('input.txt', 'w', encoding='utf-8') as file:
    file.write("Рядок2\n")
    file.write("Рядок1\n")
    file.write("123dfhdf45\n")
    file.write("@#ssdhhsdhsd&*()\n")

with open('input.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

print("Файл до видалення рядка: \n")
print(''.join(lines))

lines = lines[:-1]


print("\nФайл після видалення рядка: \n")
print(''.join(lines))