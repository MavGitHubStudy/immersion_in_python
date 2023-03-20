import logging

logging.basicConfig(
    filename="log/log.log",
    encoding='utf-8',
    format='{asctime} {lelelname} {funcName}->{lineno}: {msg}',
    style='{',
    level=logging.WARNING
)
# 26:54 - 27:35 - 28:45 информация будет дописываться в файл
