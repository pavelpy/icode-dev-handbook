# Style guide

Желательно:

* Не превышать 3 отступов \(12 пробелов\).
* Максимальная длинна строки 79 символов \(Ref pep8\).
* Цикломатическая сложность\(количество линейно независимых маршрутов через программный код\) не больше 5.
* Избегать множественного наследования в классах.
* `@property` методы должны быть быстрыми; медленная и сложная работа должна быть вынесена в обычный метод.
* Docstring для каждого модуля, класса и функции.
* Использовать публичные атрибуты при создании класса.
* Что бы функция или метод вызывали ошибку вместо возврата None, если что то пошло не так.


Обязательно:

* git pull до git push
* Название переменных, классов, функций, модулей писать на английском в соответствии с принятыми обозначениями в данной предметной области \(не транслит\).
* Не включать бизнес-логику в JavaScript \(Front-end\).
* Использовать [unicode sandwich](#unicode-sandwich) при работе с текстом.
* Использовать `nonlocal` только в простых функциях.
* Использовать `super` для инициализации родительских классов.
* При создании своего декоратора использовать `wraps` декоратор из `functools` модуля
* Использовать `datetime` и `pytz` вместо `time`.

Нужно помнить:
* `__getattr__` вызывается только раз - когда идёт обращение к отсутствующему атрибуту, когда `__getattribute__` вызывается каждый раз при обращении к атрибуту.

Необходимо прочитать:
* Про заполнение комментариев [PEP 350 -- Codetags](https://www.python.org/dev/peps/pep-0350/). Кратко:
`# FIXME: insert in book comment style guide <Pavel 2018-04-18>`

## Примеры

Как определить цикломатическую сложность

```
$ pip install mccabe
$ python -m mccabe --min 5 mccabe.py
("185:1: 'PathGraphingAstVisitor.visitIf'", 5)
("71:1: 'PathGraph.to_dot'", 5)
("245:1: 'McCabeChecker.run'", 5)
("283:1: 'main'", 7)
("203:1: 'PathGraphingAstVisitor.visitTryExcept'", 5)
("257:1: 'get_code_complexity'", 5)
```

## Some tips
* для определения количества объектов в памяти `gc`
* \(Python 3.4+\) `tracemalloc` для более детального определения memory leak
* \(Python 2\) `heapy` аналог `tracemalloc` с меньшей функциональностью


## Python other links
- Code Style:
  - [Python: практики для написания эффективного кода](https://proglib.io/p/efficient-python-practices/)
  - [(Дзэн Питона) в примерах](http://www.russianlutheran.org/python/zen/zen.html)
  - [PEP 8](https://pep8.ru/doc/pep8/) - *полезно почитать общие рекомендации*
  - Советы от Google [часть 1](https://habrahabr.ru/post/179271/) [часть 2](https://habrahabr.ru/post/180509/)
- Note:
  - [27 шпаргалок по машинному обучению и Python в 2017](https://proglib.io/p/ds-cheatsheets/)
  - [Python Exercises](https://www.ynonperek.com/2017/09/21/python-exercises/)