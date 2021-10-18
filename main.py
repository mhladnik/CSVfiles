with open("seznam.csv", "r") as seznam:
    seznam = seznam.read().splitlines()  #kaj dela [:3] ?

    for row in seznam:
        row_data = row.split(",")  # besedilo v vrstici ločimo z vejico: ['Tina', '23', 'female']
        if len(row_data) == 3:
            print(f"{row_data[0]} is {row_data[1]} years old and {row_data[2]}.")