ALLOWED_CHARS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz "
value = "Привет!"
value = value.lower()
if not(set(value) <= set(ALLOWED_CHARS)):
    print("ошибка")
else:
    print("нет ошибок")