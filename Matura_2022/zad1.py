def same_numbers(file):
    data = []
    for unit in open(file):
        data.append(unit.strip())

    results = []
    for number in data:
        if number[0] == number[-1]:
            results.append(number)
    print(len(results), results[0])


same_numbers("liczby.txt")
