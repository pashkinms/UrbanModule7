def custom_write(file_name: str, strings: list[str]):
    string_number = 1
    string_position = {tuple: str}
    for string in strings:
        file = open(file_name, "a", encoding='utf-8')
        kui = (string_number, file.tell())
        string_position[string_number, file.tell()] = string
        file.write(string+'\n')
        file.close()
        string_number +=1

    return string_position

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)