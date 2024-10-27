def custom_write(file_name, strings):
    f = open(file_name, 'w', encoding="utf8")
    strings_positions = {}
    for i in range(len(strings)):
        strings_positions.update({(i + 1, f.tell()): strings[i]})
        f.write(strings[i] + '\n')
    f.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
