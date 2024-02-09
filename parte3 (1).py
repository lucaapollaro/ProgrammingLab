def sum_csv(file):
    values = []
    for line in file:
        elements=line.split(',')
        if elements[0] != 'Date':
            value = elements[1]
            values.append(value)
    sum=0
    for i in values:
        sum += i
    return sum
    