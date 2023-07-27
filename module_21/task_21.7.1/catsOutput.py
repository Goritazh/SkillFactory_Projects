from cat import Cat

cat_1 = Cat("Барон", "мальчик", 2)
cat_2 = Cat("Сэм", "мальчик", 2)

print(f"""Имя: {cat_1.getName()}
Пол: {cat_1.getGender()}
Возраст: {cat_1.getAge()}
----------------""")
print(f"""Имя: {cat_2.getName()}
Пол: {cat_2.getGender()}
Возраст: {cat_2.getAge()}
----------------""")