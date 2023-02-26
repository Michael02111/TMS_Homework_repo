from file_module import replace_files, get_int_numbers_from_file, get_float_numbers_from_file, write_numbers_to_file
from typing import List

def get_even_numbers(some_of_numbers: List[int]) -> list:
    result = []
    for number in some_of_numbers:
        if number % 2 == 0:
            result.append(number)
    return (result)


def get_odd_numbers(some_of_numbers: List[int]) -> list:
    result = []
    for number in some_of_numbers:
        if number % 2 != 0:
            result.append(number)
    return (result)


def square(number: int | float):
    return number**2


def get_some_numbers_from_numbers(some_of_numbers: List[int]) -> tuple:
    if len(some_of_numbers) < 3:
        return 'Кол-во цифр меньше 3-х'
    else:
        return (some_of_numbers[0],
                some_of_numbers[1],
                some_of_numbers[-2],
                some_of_numbers[-1],)



def main():
    # Читаем файл с числами
    numbers = get_int_numbers_from_file('int_numbers.txt')


    if len(numbers) < 3:
        print("Вывести первый, второй, предпоследний и последний элементы данного файла: Ошибка выполнения, чисел меньше 3х ")
    else:
        print("Вывести первый, второй, предпоследний и последний элементы данного файла: ",
              get_some_numbers_from_numbers(numbers))


    write_numbers_to_file('odd_numbers.txt', get_odd_numbers(numbers))
    write_numbers_to_file('even_numbers.txt', get_even_numbers(numbers))

    float_numbers = get_float_numbers_from_file('float_numbers.txt')
    write_numbers_to_file('float_numbers.txt', map(square, float_numbers))

    replace_files('file_1.bin', 'file_2.bin')




if __name__ == '__main__':
    main()
