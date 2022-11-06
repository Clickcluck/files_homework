def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        content = f.readlines()
        lines_amount = len(content)
    return lines_amount, file_name, content


part_1 = read_file('1.txt')
part_2 = read_file('2.txt')
part_3 = read_file('3.txt')

info = [part_1, part_2, part_3]
info.sort()

with open('final_file.txt', 'w', encoding='utf-8') as f:
    for amount, name, text in info:
        f.write(f"{name}\n{amount}\n")
        for line in text:
            f.writelines(line.strip() + "\n")
