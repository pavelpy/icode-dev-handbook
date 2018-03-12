# Text processing
## Unicode sandwich[^1]
![Unicode sandwich](assets/unicode_sandwich.png)
Суть: `bytes` на входе нужно как можно раньше преобразовать в `str`\(во время открытия текстового файла для чтения, к примеру\). "Мясо" - это бизнес логика программы, где вся работа происходит над `str` объектами. На выходе\(как можно позже\) отдаём `bytes`. В Django, к примеру, вьюхи должны отдавать Unicode `str` - Django сам определяет какую кодировку использовать при переводе в `bytes` \(Обычно это UTF-8\).

[^1]: термин “Unicode sandwich” был использован Ned Batchelder’ом в выступлении “Pragmatic Unicode” на US PyCon 2012






