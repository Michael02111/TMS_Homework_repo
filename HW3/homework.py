# Номер 1
def ex1():
    return (int(1.6), int(2.99))


# Номер 2
def ex2():
    string = 'www.my_site.com#about'
    new_string = string.replace('#', "/")
    return new_string


# НОМЕР 3
def ex3(c):
    return c + 'ing'

# НОМЕР 4


def ex4(string):
    new_string = string.split(' ')[::-1]
    print(new_string)
    return " ".join(new_string)

# НОМЕР 5


def ex5():
    a = ' Hello dear Michael! '
    b = a.strip()
    return b

# НОМЕР 6


def ex6():
    school = {
        "1а": 30, "1б": 28, "2а": 25, "2б": 21, "3а": 18,
        "3б": 19, "4а": 20, "4б": 23, "5а": 23, "5б": 18,
    }
    return school

# НОМЕР 7


def ex7():
    list = [
        'Max', 'Michael',
        'Jake', 'Finn', 'Olov'
        ]
    return (list[1])


# НОМЕР 8
def ex8():
    return True if 'employ' in 'employment' else False


# НОМЕР 9
def ex9():
    name_string = "My name is Agent Smith"
    print(len(name_string))
    print(name_string[1])
    print(name_string[3:18:3])


# НОМЕР 10
def ex10():
    list = [1, 5, 2, 9, 2, 9, 1]
    for number in list:
        if list.count(number) < 2:
            return number


def main():
    print('Задание 1')
    print(ex1())
    print(f"{'_':_^20}")
    print('Задание 2')
    print(ex2())
    print(f"{'_':_^20}")
    print('Задание 3')
    print(ex3('stroka'))
    print(f"{'_':_^20}")
    print('Задание 4')
    print(ex4('Ivanou Ivan'))
    print(f"{'_':_^20}")
    print('Задание 5')
    print(ex5())
    print(f"{'_':_^20}")
    print('Задание 6')
    print(ex6())
    print(f"{'_':_^20}")
    print('Задание 7')
    print(ex7())
    print(f"{'_':_^20}")
    print('Задание 8')
    print(ex8())
    print(f"{'_':_^20}")
    print('Задание 9')
    ex9()
    print(f"{'_':_^20}")
    print('Задание 10')
    print(ex10())
    print(f"{'_':_^20}")


if __name__ == '__main__':
    main()
