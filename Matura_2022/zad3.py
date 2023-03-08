data = []
for unit in open("liczby.txt"):
    data.append(unit.strip())
data = list(map(int, data))


def third_numbers(file):
    thirds = []

    for number in range(0, len(file)):
        first_number = file[number]
        for search in range(0, len(file)):
            if number == search:
                continue

            second_number = file[search]
            if second_number % first_number == 0:
                for second_search in range(0, len(file)):
                    if number == second_search or search == second_search:
                        continue

                    third_number = file[second_search]
                    if third_number % second_number == 0:
                        thirds.append([first_number, second_number, third_number])

    return thirds


good_thirds = third_numbers(data)

print(len(good_thirds))
for element in good_thirds:
    print(element)


def fifth_numbers(file):
    fifth = []

    for number in range(0, len(file)):
        first_number = file[number]
        for search in range(0, len(file)):
            if number == search:
                continue

            second_number = file[search]
            if second_number % first_number == 0:
                for second_search in range(0, len(file)):
                    if number == second_search or search == second_search:
                        continue

                    third_number = file[second_search]
                    if third_number % second_number == 0:
                        for third_search in range(0, len(file)):
                            if number == third_search or search == third_search or second_search == third_search:
                                continue

                            fourth_number = file[third_search]
                            if fourth_number % third_number == 0:
                                for fourth_search in range(0, len(file)):
                                    if number == fourth_search or search == fourth_search or second_search == fourth_search or third_search == fourth_search:
                                        continue

                                    fifth_number = file[fourth_search]
                                    if fifth_number % fourth_number == 0:
                                        fifth.append([first_number, second_number, third_number, fourth_number, fifth_number])

    return fifth


good_fifth = fifth_numbers(data)

print(len(good_fifth))
