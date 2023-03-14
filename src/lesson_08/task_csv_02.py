import csv

# dialect='excel' - запятая
# quoting (если в кавычки - это строка, иначе - число)
with open('biostats_tab.tsv', 'r', newline='') as f:
    csv_file = csv.reader(
        f, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
    for line in csv_file:
        print(line)
    print(type(line))
"""
'Name', 'Sex', 'Age', 'Height (in)', 'Weight (lbs)']
['Alex', 'M', 41.0, 74.0, 170.0]
['Bert', 'M', 42.0, 68.0, 166.0]
['Carl', 'M', 32.0, 70.0, 155.0]
['Dave', 'M', 39.0, 72.0, 167.0]
['Elly', 'F', 30.0, 66.0, 124.0]
['Fran', 'F', 33.0, 66.0, 115.0]
['Gwen', 'F', 26.0, 64.0, 121.0]
['Hank', 'M', 30.0, 71.0, 158.0]
['Ivan', 'M', 53.0, 72.0, 175.0]
['Jake', 'M', 32.0, 69.0, 143.0]
['Kate', 'F', 47.0, 69.0, 139.0]
['Luke', 'M', 34.0, 72.0, 163.0]
['Myra', 'F', 23.0, 62.0, 98.0]
['Neil', 'M', 36.0, 75.0, 160.0]
['Omar', 'M', 38.0, 70.0, 145.0]
['Page', 'F', 31.0, 67.0, 135.0]
['Quin', 'M', 29.0, 71.0, 176.0]
['Ruth', 'F', 28.0, 65.0, 132.0]
<class 'list'>

Process finished with exit code 0
"""