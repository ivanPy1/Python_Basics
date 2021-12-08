# 2. Создать текстовый файл (не программно),
# сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.


with open('lesson-5-hw-2_text.txt', 'r') as f:
    result = [len(line.split()) for line in f]
    print(f'В данном файле {len(result)} строк (строки).')
    [print(f'В строке {strg + 1} - {el} слов(а).') for strg, el in enumerate(result)] 
