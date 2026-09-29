def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    less = []
    greater = []
    pivot = numbers[-1]
    equals = []

    for number in numbers:

        if number < pivot:
            less.append(number)
        elif number > pivot:
            greater.append(number)
        else:
            equals.append(number)
        
    return quick_sort(less) + equals + quick_sort(greater)

