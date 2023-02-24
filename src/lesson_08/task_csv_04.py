import csv

with open('biostats_tab.tsv', 'r', newline='') as f:
    csv_file = csv.DictReader(f,
                              fieldnames=["name", "sex", "age", "height",
                                          "weight", "office"],
                              restkey="new",
                              restval="Main Office",
                              dialect='excel-tab',
                              quoting=csv.QUOTE_NONNUMERIC
                              )
    for line in csv_file:
        print(f'{line = }')
        print(f'{line["name"] =}\t{line["age"] = }')
"""
line = {'name': 'Name', 'sex': 'Sex', 'age': 'Age', 'height': 'Height (in)', 'weight': 'Weight (lbs)', 'office': 'Main Office'}
line["name"] ='Name'	line["age"] = 'Age'
line = {'name': 'Alex', 'sex': 'M', 'age': 41.0, 'height': 74.0, 'weight': 170.0, 'office': 'Main Office'}
line["name"] ='Alex'	line["age"] = 41.0
line = {'name': 'Bert', 'sex': 'M', 'age': 42.0, 'height': 68.0, 'weight': 166.0, 'office': 'Main Office'}
line["name"] ='Bert'	line["age"] = 42.0
line = {'name': 'Carl', 'sex': 'M', 'age': 32.0, 'height': 70.0, 'weight': 155.0, 'office': 'Main Office'}
line["name"] ='Carl'	line["age"] = 32.0
line = {'name': 'Dave', 'sex': 'M', 'age': 39.0, 'height': 72.0, 'weight': 167.0, 'office': 'Main Office'}
line["name"] ='Dave'	line["age"] = 39.0
line = {'name': 'Elly', 'sex': 'F', 'age': 30.0, 'height': 66.0, 'weight': 124.0, 'office': 'Main Office'}
line["name"] ='Elly'	line["age"] = 30.0
line = {'name': 'Fran', 'sex': 'F', 'age': 33.0, 'height': 66.0, 'weight': 115.0, 'office': 'Main Office'}
line["name"] ='Fran'	line["age"] = 33.0
line = {'name': 'Gwen', 'sex': 'F', 'age': 26.0, 'height': 64.0, 'weight': 121.0, 'office': 'Main Office'}
line["name"] ='Gwen'	line["age"] = 26.0
line = {'name': 'Hank', 'sex': 'M', 'age': 30.0, 'height': 71.0, 'weight': 158.0, 'office': 'Main Office'}
line["name"] ='Hank'	line["age"] = 30.0
line = {'name': 'Ivan', 'sex': 'M', 'age': 53.0, 'height': 72.0, 'weight': 175.0, 'office': 'Main Office'}
line["name"] ='Ivan'	line["age"] = 53.0
line = {'name': 'Jake', 'sex': 'M', 'age': 32.0, 'height': 69.0, 'weight': 143.0, 'office': 'Main Office'}
line["name"] ='Jake'	line["age"] = 32.0
line = {'name': 'Kate', 'sex': 'F', 'age': 47.0, 'height': 69.0, 'weight': 139.0, 'office': 'Main Office'}
line["name"] ='Kate'	line["age"] = 47.0
line = {'name': 'Luke', 'sex': 'M', 'age': 34.0, 'height': 72.0, 'weight': 163.0, 'office': 'Main Office'}
line["name"] ='Luke'	line["age"] = 34.0
line = {'name': 'Myra', 'sex': 'F', 'age': 23.0, 'height': 62.0, 'weight': 98.0, 'office': 'Main Office'}
line["name"] ='Myra'	line["age"] = 23.0
line = {'name': 'Neil', 'sex': 'M', 'age': 36.0, 'height': 75.0, 'weight': 160.0, 'office': 'Main Office'}
line["name"] ='Neil'	line["age"] = 36.0
line = {'name': 'Omar', 'sex': 'M', 'age': 38.0, 'height': 70.0, 'weight': 145.0, 'office': 'Main Office'}
line["name"] ='Omar'	line["age"] = 38.0
line = {'name': 'Page', 'sex': 'F', 'age': 31.0, 'height': 67.0, 'weight': 135.0, 'office': 'Main Office'}
line["name"] ='Page'	line["age"] = 31.0
line = {'name': 'Quin', 'sex': 'M', 'age': 29.0, 'height': 71.0, 'weight': 176.0, 'office': 'Main Office'}
line["name"] ='Quin'	line["age"] = 29.0
line = {'name': 'Ruth', 'sex': 'F', 'age': 28.0, 'height': 65.0, 'weight': 132.0, 'office': 'Main Office'}
line["name"] ='Ruth'	line["age"] = 28.0

Process finished with exit code 0
"""
