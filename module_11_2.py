from inspect import getmodule


def introspection_info(obj):
    info = {
        'type': type(obj),
        'Атрибуты обьекта': dir(obj),
        'Методы обьекта': [attr for attr in dir(obj) if callable(getattr(obj, attr))],
        'Модуль, к которому объект принадлежит': getmodule(obj)
    }
    return info

number_info = introspection_info(42)
print(number_info)

