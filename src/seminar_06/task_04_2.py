def guesser(puzzle: str, options: list[str], counts: int) -> int:
    counter = 0
    while counts > counter:
        counter += 1
        print(puzzle)
        user_input = input("Guess the answer:\n>>> ").lower()
        if user_input in options:
            return counter

    return 0


if __name__ == '__main__':
    print(guesser("Зимой и летом одним цветом", ["ёлка", "ель", "сосна"], 3))
