# Написать обычную функцию для факториала, генератор и
# рекурсию. Сравнить их время работы
import typing

def timer(func):
    import time
    def _wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        runtime = time.perf_counter() - start
        print(f"{func.__name__} took {runtime*100:.8f} ms")
        return result
    return _wrapper



def factorial_func(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact


def factorial_rec(n):
    if n == 0:
        return 1
    else:
        return n * factorial_rec(n - 1)


def factorials_up_to(x):
    a = 1
    for i in range(1, x+1):
        a *= i
        yield a


@timer
def get_fact_func(n):
    return factorial_func(n)


@timer
def get_fact_rec(n):
    return factorial_rec(n)


@timer
def get_fact_up_to(n):
    return list(factorials_up_to(n))[-1]


print (get_fact_func(68))
print (get_fact_rec(68))
print (get_fact_up_to(68))

# # Напишите декоратор, который проверял бы тип параметров
# # функции, конвертировал их если надо и складывал:

def typed(type: str):
    def my_decorator(func):
        def _wrapper(*args):
            if type == 'str':
                arguments = []
                for arg in args:
                    arguments.append(str(arg))
                result = func(*arguments)

            if type == 'int':
                arguments = []
                for arg in args:
                    arguments.append(int(arg))
                result = func(*arguments)

            if type == 'float':
                arguments = []
                for arg in args:
                    arguments.append(float(arg))
                result = func(*arguments)
          
            return result
        return _wrapper
    return my_decorator


@typed(type='str')
def add_two_symbols(a, b):
    return a + b


print (add_two_symbols("3", 5))
print(add_two_symbols(5, 5))
print(add_two_symbols('a', 'b'))


@typed(type='int')
def add_three_symbols(a, b, с):
        return a + b + с
print(add_three_symbols(5, 6, 7))
print(add_three_symbols("3", 5, 0))


@typed(type='float')
def add_three_symbols(a, b, с):
        return a + b + с
print(add_three_symbols(0.1, 0.2, 0.4))



# На вход подаётся некоторое количество (не больше сотни)
# разделённых пробелом целых чисел (каждое не меньше 0 и не
# больше 19). Выведите их через пробел в порядке
# лексикографического возрастания названий этих чисел в
# английском языке.Т.е., скажем числа 1, 2, 3 должны быть
# выведены в порядке 1, 3, 2, поскольку слово two в словаре
# встречается позже слова three, а слово three -- позже слова one
# (иначе говоря, поскольку выражение 'one' < 'three' < 'two'
# является истинным)






str_of_numbers = '5 10 12 19 1 3 5 8 2 4 6'


def sort_numbers (numbers: str):
    number_names = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
        6: "six", 7: "seven", 8: "eight", 9: "nine",
        10: "ten", 11: "eleven", 12: "twelve",
        13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",
        17: "seventeen", 18: "eighteen", 19: "nineteen"
    }

    init_data =[]
    for number in numbers.split(' '):
        init_data.append (
            ( int(number), number_names[int(number)]) 
            )

    print (init_data)
    sorted_data = sorted(init_data, key=lambda tup: tup[1])
    print (sorted_data)
    for element in sorted_data:
        print(element[0], end=' ')



sort_numbers (str_of_numbers)