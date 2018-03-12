# Style guide

Желательно:

* Не превышать 3 отступов \(12 пробелов\).
* Максимальная длинна строки 79 символов \(Ref pep8\).
* Цикломатическая сложность\(количество линейно независимых маршрутов через программный код\) не больше 5.

Обязательно:

* git pull до git push
* Название переменных, классов, функций, модулей писать на английском в соответствии с принятыми обозначениями в данной предметной области \(не транслит\).
* Не включать бизнес-логику в JavaScript \(Front-end\).
* Использовать [unicode sandwich](text-processing.md#unicode-sandwich) при работе с текстом.
* Использовать `nonlocal` только в простых функциях

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



