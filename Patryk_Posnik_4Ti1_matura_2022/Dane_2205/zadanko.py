def same_numbers():
    
    data = []
    
    for unit in open("Dane_2205/przyklad.txt"):
        data.append(unit.strip())
        
    results = []
        
    for number in data:
        if number[0] == number[-1]:
            results.append(number)
                
    print(f'ave {len(results)} {results[0]}')