from inspect import getmodule


def introspection_info(obj):
    info = {
        'type': type(obj),
        'Атрибуты обьекта': dir(obj),
        'Модуль, к которому объект принадлежит': getmodule(obj)
    }
    return info

number_info = introspection_info(42)
print(number_info)

