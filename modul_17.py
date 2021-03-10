def sorting(numbers):
    if len(numbers) <= 1:
        return numbers
    elements = numbers[0]
    left = list(filter(lambda x: x < elements, numbers))
    center = [i for i in numbers if i == elements]
    right = list(filter(lambda x: x > elements, numbers))
    return sorting(left) + center + sorting(right)

def search_(list_, entered_number):
    left = 0
    right = len(list_)-1
    while right > left:
        middle = (right + left) // 2
        if numbers[middle] == entered_number:
            return f"{middle-1} - номер позиции элемента, который меньше введенного Вами числа \n"\
                   f"{middle+1} - номер позиции элемента, который больше, либо равен введенному Вами числу"
        elif list_[left] == entered_number:
            if list_[left] == list_[0]:
                return f"Введенное число является наименьшим числом в последовательности, номер его позиции - {left}\n"\
                       f"{left+1} - номер позиции элемента, который больше или равен введенному Вами числу"
        elif list_[right] == entered_number:
            if list_[right] == list_[-1]:
                return f"Введенное число является наибольшим числом в последовательности, номер его позиции - {right}\n"\
                       f"{right-1} - номер позиции элемента, который меньше введенного Вами числа"
        elif list_[middle] > entered_number:
            if right == middle:
                return f"Введенное Вами число находится между индексами {left} и {right}"
            right = middle
        else:
            if left == middle:
                return f"{left} - номер позиции элемента, который меньше введенного Вами числа \n" \
                       f"{right} - номер позиции элемента, который больше или равен введенному Вами числу"
            left = middle

while True:
    try:
        numbers = list(set(map(int, input("Введите последовательность чисел через пробел:").split())))
        if len(numbers) <= 1:
            print('Вы не ввели последовательность, пожалуйста повторите ввод.\n')
            continue
        else:
            break
    except ValueError:
        print("Вы ошиблись при вводе, пожалуйста повторите ввод.\n")
        continue

list_ = sorting(numbers)
print()

while True:
    try:
        entered_number = int(input(f"Введите произвольное число в диапазоне от '{list_[0]} до {list_[-1]}': "))
        if entered_number < list_[0] or entered_number > list_[-1]:
            print('Введенное число находится вне указанного диапазона, пожалуйста повторите ввод.\n')
            continue
        else:
            break
    except ValueError:
        print("Вы ошиблись при вводе произвольного числа, пожалуйста повторите ввод.\n")
        continue

print(search_(list_, entered_number))
