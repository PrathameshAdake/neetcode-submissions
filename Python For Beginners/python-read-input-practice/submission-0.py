def add_two_numbers() -> int:
    inputt = input()
    comma_sep_value = inputt.split(",")
    summ = 0
    for i in comma_sep_value:
        summ += int(i)
    return summ


# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
