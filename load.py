def load_numbers(filename):
    numbers = []


    with open(filename, 'r')as file:
        for line in file:
            line = line.strip()
            if line:
                numbers.append(int(line))
    return numbers