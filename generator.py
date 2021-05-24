user_input = int(input("Введите конечное число: "))

def generator_numbers(user_input):

    generator_number = (num for num in range(1, user_input+1, 2))
    generator_number = (*generator_number,)
    return generator_number

print(generator_numbers(user_input))
