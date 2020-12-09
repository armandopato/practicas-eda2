def parseCsv():
    with open("covid-19-mexico-01122020.csv", encoding='utf-8') as covidFile:
        lines = covidFile.read().splitlines()
        columnNames = lines[0].split(',')
        rows = []
        for i in range(1, len(lines)):
            entry = lines[i].split(',')
            rows.append((entry[0], entry[1], entry[2], int(entry[3]), entry[4], entry[5]))

    return columnNames, rows
