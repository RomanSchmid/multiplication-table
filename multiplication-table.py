def create_list(size):
    main_list = []
    for i in range(size):
        sub_list = []
        for j in range(size):
            sub_list.append(i * j)
        main_list.append(sub_list)
    return main_list

multiplication_table = create_list(int(input("Size of multiplication table? ")))

print(multiplication_table)
print(multiplication_table[3][4]) # Fifth element of fourth list

for list in multiplication_table:
    for number in list:
        print(number, end=' ')
    print()
