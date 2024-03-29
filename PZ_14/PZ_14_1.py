def find_dostoevsky_surnames(file_path):
    with open(file_path, 'r') as f:
        text = f.read()
    dostoevsky_surnames = set()
    for word in text.split():
        if 'Достоевск' in word:
            dostoevsky_surnames.add(word)
    return dostoevsky_surnames

file_path = "../PZ_14/Dostoevsky.txt"
print(find_dostoevsky_surnames(file_path))

#Этот код открывает файл Dostoevsky.txt и читает его содержимое.
# Затем он разбивает текст на слова, используя split(), и перебирает каждое слово.
# Если слово содержит Достоевск, оно добавляется в множество dostoevsky_surnames.
# В конечном итоге, функция возвращает это множество, которое содержит уникальные варианты фамилий Достоевского.