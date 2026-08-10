from typing import List

def read_integers() -> List[int]:
    values = input()
    listt = values.split(",")
    int_list = []

    for i in listt:
        int_list.append(int(i))
    return int_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
