first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(i) - len(j) for i, j in zip(first, second) if len(i) != len(j))
print(list(first_result))

# Если списки имеют одинаковую длинну
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))
# Если списки разных длинн
second_result_2 = (len(first[i]) == len(second[i]) for i in range(min(len(first), len(second))))
print(list(second_result))
print(list(second_result_2))
