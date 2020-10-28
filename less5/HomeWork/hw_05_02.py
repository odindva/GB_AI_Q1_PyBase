# 2) Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.


file_name = 'file_2.txt'
lines = []
try:
    with open(file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
except IOError:
    print('Ошибка ввод-вывода')
print(f'количество строк в файле {file_name}: {len(lines)}')
for i in range(len(lines)):
    print(f'количество слов в строке {i}: {len(lines[i].split())}')
