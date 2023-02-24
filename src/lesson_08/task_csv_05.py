import csv

with open('biostats_tab.tsv', 'r', newline='') as f:
    csv_file = csv.DictReader(f,
                              fieldnames=["name", "sex", "age", ],
                              restkey="new",
                              restval="Main Office",
                              dialect='excel-tab',
                              quoting=csv.QUOTE_NONNUMERIC
                              )
    for line in csv_file:
        print(f'{line = }')
        print(f'{line["name"] =}\t{line["age"] = }')
"""
line = {'name': 'Name', 'sex': 'Sex', 'age': 'Age', 'new': ['Height (in)', 'Weight (lbs)']}
line["name"] ='Name'	line["age"] = 'Age'
line = {'name': 'Alex', 'sex': 'M', 'age': 41.0, 'new': [74.0, 170.0]}
line["name"] ='Alex'	line["age"] = 41.0
line = {'name': 'Bert', 'sex': 'M', 'age': 42.0, 'new': [68.0, 166.0]}
line["name"] ='Bert'	line["age"] = 42.0
line = {'name': 'Carl', 'sex': 'M', 'age': 32.0, 'new': [70.0, 155.0]}
line["name"] ='Carl'	line["age"] = 32.0
line = {'name': 'Dave', 'sex': 'M', 'age': 39.0, 'new': [72.0, 167.0]}
line["name"] ='Dave'	line["age"] = 39.0
line = {'name': 'Elly', 'sex': 'F', 'age': 30.0, 'new': [66.0, 124.0]}
line["name"] ='Elly'	line["age"] = 30.0
line = {'name': 'Fran', 'sex': 'F', 'age': 33.0, 'new': [66.0, 115.0]}
line["name"] ='Fran'	line["age"] = 33.0
line = {'name': 'Gwen', 'sex': 'F', 'age': 26.0, 'new': [64.0, 121.0]}
line["name"] ='Gwen'	line["age"] = 26.0
line = {'name': 'Hank', 'sex': 'M', 'age': 30.0, 'new': [71.0, 158.0]}
line["name"] ='Hank'	line["age"] = 30.0
line = {'name': 'Ivan', 'sex': 'M', 'age': 53.0, 'new': [72.0, 175.0]}
line["name"] ='Ivan'	line["age"] = 53.0
line = {'name': 'Jake', 'sex': 'M', 'age': 32.0, 'new': [69.0, 143.0]}
line["name"] ='Jake'	line["age"] = 32.0
line = {'name': 'Kate', 'sex': 'F', 'age': 47.0, 'new': [69.0, 139.0]}
line["name"] ='Kate'	line["age"] = 47.0
line = {'name': 'Luke', 'sex': 'M', 'age': 34.0, 'new': [72.0, 163.0]}
line["name"] ='Luke'	line["age"] = 34.0
line = {'name': 'Myra', 'sex': 'F', 'age': 23.0, 'new': [62.0, 98.0]}
line["name"] ='Myra'	line["age"] = 23.0
line = {'name': 'Neil', 'sex': 'M', 'age': 36.0, 'new': [75.0, 160.0]}
line["name"] ='Neil'	line["age"] = 36.0
line = {'name': 'Omar', 'sex': 'M', 'age': 38.0, 'new': [70.0, 145.0]}
line["name"] ='Omar'	line["age"] = 38.0
line = {'name': 'Page', 'sex': 'F', 'age': 31.0, 'new': [67.0, 135.0]}
line["name"] ='Page'	line["age"] = 31.0
line = {'name': 'Quin', 'sex': 'M', 'age': 29.0, 'new': [71.0, 176.0]}
line["name"] ='Quin'	line["age"] = 29.0
line = {'name': 'Ruth', 'sex': 'F', 'age': 28.0, 'new': [65.0, 132.0]}
line["name"] ='Ruth'	line["age"] = 28.0

Process finished with exit code 0
"""
