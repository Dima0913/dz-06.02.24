with open('file.txt', 'w', encoding='utf-8') as file:
    file.write("gfkfkfkf fgkfg fg kfgkfg fg \n")
    file.write("Дduf888888hnm8fnh8undf8unh8dnf8nsshfs\n")
    file.write("621357251\n")
    file.write("!@#№$;%^:&?*()-_=+\n")

with open('file.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

max_length = max(len(line) for line in lines)

print(f"Довжина найдовшого рядка: {max_length}")