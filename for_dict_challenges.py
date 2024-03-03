# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]


def count_names(students: list) -> dict:
    count_names = {}
    for student in students:
        if student['first_name'] not in count_names:
            count_names[student['first_name']] = 1
        else:
            count_names[student['first_name']] += 1
    return count_names


count_names_dict = count_names(students)

for key, value in count_names_dict.items():
    print(f"{key}: {value}")

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]


def key_for_max_value(target_dict):
    target_key = ''
    max_value = 0
    for key, value in target_dict.items():
        if target_dict[key] > max_value:
            target_key = key
            max_value = target_dict[key]
    return target_key


count_names_dict = count_names(students)
frequent_name = key_for_max_value(count_names_dict)
print(f'Самое частое имя среди учеников: {frequent_name}')

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ], [  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]

for i in range(len(school_students)):
    count_names_dict = count_names(school_students[i])
    frequent_name = key_for_max_value(count_names_dict)
    print(f'Самое частое имя в классе {i + 1}: {frequent_name}')

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a',
     'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б',
     'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'},
                                 {'first_name': 'Маша'}]},
]

is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}


def count_gender(students: list, is_male: dict) -> dict:
    count_genders = {
        'девочки': 0,
        'мальчики': 0,
    }
    for name in students:
        if name['first_name'] in is_male:
            if is_male.get(name['first_name']):
                count_genders['мальчики'] += 1
            else:
                count_genders['девочки'] += 1
        else:
            print(f"Имя {name['first_name']} не найдено в словаре")
    return count_genders


for class_name in school:
    count_genders = count_gender(class_name['students'], is_male)
    print(
        f"Класс {class_name['class']}: девочки {count_genders['девочки']}, мальчики {count_genders['мальчики']}")

# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a',
     'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c',
     'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

girls = {}
boys = {}
for class_name in school:
    count_genders = count_gender(class_name['students'], is_male)
    girls[class_name['class']] = count_genders['девочки']
    boys[class_name['class']] = count_genders['мальчики']
print(f'Больше всего девочек в классе {key_for_max_value(girls)}')
print(f'Больше всего мальчиков в классе {key_for_max_value(boys)}')
