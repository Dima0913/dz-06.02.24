with open('input.txt', 'w') as file:
    file.write("line\n")
    file.write("line 2\n")
    file.write("12345\n")
    file.write("@#%&*()\n")

with open('input.txt', 'r') as file:
    text = file.read()

bukva = len(text)
ryadok = text.count('\n')
litera = sum(text.count(lines) for lines in "fgjafjfgajefgeGeIDafgjfg")
Bukva = sum(text.count(BIGbukva) for BIGbukva in "hfefaffffffafefJeANM<GOUMUaAGeUMueishmAaunisnhDHUudifmhidfddddddddhbfgydbfgbdfbgdfgbdfgyd")
digit = sum(char.isdigit() for char in text)

with open('output.txt', 'w') as file:
    file.write(f"sumvoly: {bukva}\n")
    print(f"sumboly: {bukva}")

    file.write(f"radky: {ryadok}\n")
    print(f"radky: {ryadok}")

    file.write(f"golosny: {litera}\n")
    print(f"golosny: {litera}")

    file.write(f"prugolosny: {Bukva}\n")
    print(f"prugolosny: {Bukva}")

    file.write(f"count: {digit}\n")
    print(f"count: {digit}")