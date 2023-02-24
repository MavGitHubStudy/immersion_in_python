import json

my_dict = {
    "first_name": "Джон",
    "last_name": "Смит",
    "hobbies": ["кузнечное дело", "программирование", "путешествия"],
    "age": 35,
    "children": [
        {
            "first_name": "Алиса",
            "age": 5
        },
        {
            "first_name": "Маруся",
            "age": 3
        }
    ]
}

dict_to_json_text = json.dumps(my_dict)
print(f'{type(dict_to_json_text) = }\n{dict_to_json_text =}')

dict_to_json_text = json.dumps(my_dict, ensure_ascii=False)
print(f'{type(dict_to_json_text) = }\n{dict_to_json_text = }')
# строку можно преобразовать через метод encode в набор байт,
# переслать эти байты по каналам связи, а на другой стороне байты
# преобразуются в текст,
# текст через loads преобразуется к объекту Python
# и таким образом вы можете пересылать информацию по каналам связи
# от одного компьютера к другому
