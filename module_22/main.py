array = list(map(int, input('Введите числа через пробел > ').split()))
number = int(input('Введите любое число > '))


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def binary_search(arr, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if arr[middle] == element:
        return middle
    elif element < arr[middle]:
        return binary_search(arr, element, left, middle - 1)
    else:
        return binary_search(arr, element, middle + 1, right)


ar = bubble_sort(array)
print(ar)

if ar[0] <= number <= ar[-1]:
    print(binary_search(ar, number, 0, len(ar)) - 1)
else:
    print('Число вне диапазона')
