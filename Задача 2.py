#Напишите функцию принимающую на вход только ключевые параметры(kwargs) и возвращающую словарь, где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление.
#reverse_kwargs(rev=True, acc="YES", stroka=4) -> {True: "rev", "YES": 'acc', 4: "stroka"}

def dictunary(a=2, b=3):
    dictun = {
        f'{a}': id(a),
        f'{b}': id(b)
    }

    return dictun
a = 2
b = 3
temp = dictunary(a, b)
print(temp)