from typing import List

def replace_files(filepath1, filepath2):
    with open(filepath1, 'rb+') as file1:
        data_file1 = file1.read()

        with open(filepath2, 'rb+') as file2:
            data_file2 = file2.read()
            file1.seek(0)
            file2.seek(0)
            file1.truncate(0)
            file2.truncate(0)

            file1.write(data_file2)
            file2.write(data_file1)


def get_int_numbers_from_file(filepath: str) -> List[int]:
    try:
        with open(filepath, 'r+') as file:
            numbers = []
            for line in file:
                numbers.append(int(line.replace('\n', '')))
            return numbers
    except Exception as ex:
        raise ValueError(str('Ошибка чтения файла: ' + str(ex)))


def get_float_numbers_from_file(filepath: str) -> List[float]:
    try:
        with open(filepath, 'r+') as file:
            numbers = []
            for line in file:
                numbers.append(float(line.replace('\n', '')))
            return numbers
    except Exception as ex:
        raise ValueError(str('Ошибка чтения файла: ' + str(ex)))

def write_numbers_to_file(filename: str, numbers: list) -> None:
    result = [str(i)+'\n' for i in numbers]

    with open(filename, 'w') as file:
        file.writelines(result)
