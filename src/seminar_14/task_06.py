import json
from pathlib import Path


class ProjectException(Exception):
    pass


class LevelError(ProjectException):
    pass


class AccessError(ProjectException):
    pass


class User:
    def __init__(self, lvl, idx, name):
        self.lvl = lvl
        self.idx = idx
        self.name = name

    def __eq__(self, other):
        return self.idx == other.idx and self.name == other.name
        # if self.idx == other.idx and self.name == other.name:
        #     return True
        # else:
        #     return False

    def __hash__(self):
        return hash((self.idx, self.name))

    def __repr__(self):
        return f'User(lvl={self.lvl}, idx={self.idx}, name={self.name})'


def read_json(file: Path) -> set[User]:  # 1:01:56
    users = set()

    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for key, value in data.items():
        for idx, name in value.items():
            users.add(User(lvl=key, idx=idx, name=name))
    return users  # 1:01:56


# if __name__ == '__main__':
#     res = read_json(Path('names.json'))
#     print(f'{res = }')

class Project:
    _users = set()

    def read_json(self, file: Path):

        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for lvl, value in data.items():
            for idx, name in value.items():
                self._users.add(User(lvl, idx, name))

        return self._users


if __name__ == '__main__':
    project = Project()
    res = project.read_json(Path('names.json'))
    print(f'{res = }')
