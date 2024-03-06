# Преобразование ключей и значений словаря

# Напишите функцию key_params, принимающую на вход только ключевые параметры и возвращающую словарь, где ключ -
# значение переданного аргумента, а значение - имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

# def key_params(**kwargs):
#     res = {}
#     for key, value in kwargs.items():
#         if isinstance(value, (int, str, float, tuple)):
#             res[value] = key
#         else:
#             res[str(value)] = key
#     return  res


def key_params(**kwargs):
    res = {}
    for key, value in kwargs.items():
        try:
            hash(value)
            res[value] = key
        except TypeError:
            res[str(value)] = key
    return res


params = key_params(a=1, b='hello', c=[1, 2, 3], d={}, e=None)
print(params)

'''
def key_params(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if value is None:
            result[value] = key
        elif isinstance(value, (int, str, float, bool, tuple)):
            result[value] = key
        else:
            result[str(value)] = key
    return result
'''