from func import load_operations
from func import exec_operations
from func import sorted_list
from func import conclusion

# имя файла с данными по операциям и количество последних операций для вывода <n>
file_name = 'operations.json'
n = 5

# получаем отсортированный список с <n> последними операциями для вывода
all_operations = load_operations(file_name)
list_of_operations = exec_operations(all_operations)
sorted_list_of_operations = sorted_list(list_of_operations)[0:n]

# выводим информацию
for operation in sorted_list_of_operations:
    print(conclusion(operation))
    print()
