data = []
for unit in open("liczby.txt"):
    data.append(unit.strip())

data = list(map(int, data))


def prime_numbers(number):
    results = []
    k = 2
    while number != 1:
        while number % k == 0:
            results.append(k)
            number //= k
        k += 1

    return results


current_max_factors = 0
current_max_factors_number = 0
current_different_factors = 0
current_different_factors_number = 0

for thing in data:

    factors = prime_numbers(thing)
    unique_factors = set(factors)

    if len(factors) > current_max_factors:
        current_max_factors_number = thing
        current_max_factors = len(factors)

    if len(unique_factors) > current_different_factors:
        current_different_factors = len(unique_factors)
        current_different_factors_number = thing

print(
    current_max_factors_number,
    current_max_factors,
    current_different_factors_number,
    current_different_factors
)
