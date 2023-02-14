link = 'https://docs.python/org/3/faq/programming.html#how-can-i-pass' \
       '-optional-or-keyword-parameters-from-one-function'
prefix, *_, suffix = link.split('/')
# (*_ - нам нужно куда-то упаковать значения, которые потом не нужны)
