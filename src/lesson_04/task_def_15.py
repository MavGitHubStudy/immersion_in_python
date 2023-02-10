def kwd_only_arg(*, arg):
    """Пример только ключевой функции"""
    print(arg)  # Печатаем для примера, а не для привычки !


# kwd_only_arg(42)
"""
TypeError: kwd_only_arg() takes 0 positional arguments but 1 was given
"""
kwd_only_arg(arg=42)
