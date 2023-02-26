# Lambda
# Создать lambda функцию, которая принимает на вход имя и выводит его в формате “Hello, {name}”
my_name = ['Michael']
final_sentence = list(map(lambda name: f"Hello {name}", my_name))
print (final_sentence)



def function(name): return f'Hello {name}'


print(function('Michael'))


# Создать lambda функцию, которая принимает на вход
# список имен и выводит их в формате “Hello, {name}” в
# другой список

names = ['Michael', 'Danik']
formated_names = list(map(lambda name: f'Hello {name}', names))
print(formated_names)


# Напишите генератор который принимает список
# numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7] и
# возвращает новый список только с положительными
# числами с обработкой исключений


numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7, 'Text']


# def fun(list1):
#     list2 = []

#     for i in list1:
#         try:
#             if i >= 0:
#                 list2.append(i)
#         except:
#             print('Не удалось обработать значение: ', i)

#     return list2


# print(fun(numbers))


def my_generator(list1):
    for i in list1:
        try:
            if i >= 0:
                yield i
            else:
                raise Exception
        except:
            yield f'Не удалось обработать значение: {i}'


list_generator = my_generator(numbers)

print (list_generator)
for element in list_generator:
    print(element)



# Необходимо составить список чисел которые
# указывают на длину слов в строке: sentence = " thequick
# brown fox jumps over the lazy dog", но только если слово
# не "the" с обработкой исключений

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
print (words)








