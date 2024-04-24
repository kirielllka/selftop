import json


def sol1():
    with open("file1.txt", "r") as file1, open("file2.txt", "r") as file2:
        lines1 = file1.readlines()
        lines2 = file2.readlines()

    for line1, line2 in zip(lines1, lines2):
        if line1 != line2:
            print(f"Несовпадающая строка из file1.txt: {line1}")
            print(f"Несовпадающая строка из file2.txt: {line2}")
def sol2():
    with open("input.txt", "r") as file:
        content = file.read()

    characters = len(content)
    lines = content.count('\n')
    vowels = sum(1 for char in content if char.lower() in 'aeiouаеёиоуыэюя')
    consonants = sum(1 for char in content if char.isalpha() and char.lower() not in 'aeiouаеёиоуыэюя')
    numbers = sum(1 for char in content if char.isdigit())

    with open("output.txt", "w") as output_file:
        output_file.write(f"Количество символов: {characters}\n")
        output_file.write(f"Количество строк: {lines}\n")
        output_file.write(f"Количество гласных букв: {vowels}\n")
        output_file.write(f"Количество согласных букв: {consonants}\n")
        output_file.write(f"Количество цифр: {numbers}\n")
def sol3():
    with open("input.txt", "r") as file:
        lines = file.readlines()

    with open("output.txt", "w") as output_file:
        output_file.writelines(lines[:-1])
def sol4():
    with open('file.txt', 'r') as file:
        max_length = 0
        for line in file:
            if len(line) > max_length:
                max_length = len(line)
        print("Самая длинная строка в файле имеет длину:", max_length)
def sol5():
    word = input("Введите слово для поиска: ")
    count = 0

    with open('file.txt', 'r') as file:
        for line in file:
            count += line.count(word)

    print("Слово", word, "встречается", count, "раз в файле.")
def sol6():
    word_to_find = input("Введите слово для замены: ")
    replacement_word = input("Введите слово, на которое заменить: ")

    with open('file.txt', 'r') as file:
        text = file.read()

    new_text = text.replace(word_to_find, replacement_word)

    with open('file.txt', 'w') as file:
        file.write(new_text)

    print("Слово", word_to_find, "было заменено на слово", replacement_word, "в файле.")
def open():
    global employees
    employees = []
    with open('employer.txt', 'r') as file1:
        employees = json.load(file1)
def add_emp():
    global employees
    name = input('Введите имя работника:')
    age = input('Введите возраст работника:')
    position = input('Профессия работника:')
    employer = {'Фамилия':name,'Возраст':age,'Профессия':position}
    employees.append(employer)
def edit_empl():
    name = input('Введите имя сотрудника:')
    global employees
    for employer in employees:
        if employer['Фамилия'] == name:
            employer['Возраст'] == int(input('введите возраст:'))
            employer['Профессия'] == input('Введите новую профессию:')
def find_by_name():
    name = input('Введите фамилию')
    global employees
    for employee in employees:
        if employee['Фамилия'] == name:
            print(employee)
def find_by_age():
    age = int(input('Введите возраст:'))
    global employees
    for employee in employees:
        if employee['Возраст'] == age:
            print(employee)
def print_all():
    global employees
    for employee in employees:
        print(employee)
def find_employees_by_initial():
    letter = input('Введите первую букву фамилии:')
    for employee in employees:
        if employee['Фамилия'][0].lower() == letter.lower():
            print(employee)
def save_employees():
    with open("employer.txt", 'w') as file1:
        json.dump(employees, file1)
def delete_employee(name):
    global employees
    employees = [employee for employee in employees if employee['Фамилия'] != name]
def main():
    open()

    while True:
        print("\n1. Добавить сотрудника")
        print("2. Изменить данные о сотруднике")
        print("3. Удалить сотрудника")
        print("4. Найти по фамилии")
        print("5. вывести сотрудников одного возраста")
        print("6. Вывести сотрудников по инициалам")
        print("7. Вывести всех сотрудников")
        print("8. Сохранить и выйти")

        choice = input("Напишите ваш выбор: ")

        if choice == '1':
            add_emp()
        elif choice == '2':
            edit_empl()
        elif choice == '3':
            delete_employee()
        elif choice == '4':
            find_by_name()
        elif choice == '5':
            find_by_age()
        elif choice == '6':
            find_employees_by_initial()
        elif choice == '7':
            print_all()
        elif choice == '8':
            save_employees()
            break
        else:
            print("Неправильный выбор.")
if __name__ == '__main__':
    main()

