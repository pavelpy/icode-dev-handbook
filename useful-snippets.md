# Useful snippets
По умолчанию в примерах кода использутеся python 3.x

```python
def to_str(bytes_or_str):
    '''func that takes a str or bytes 
    and always returns a str.
    '''
	if isinstance(bytes_or_str, bytes):
		value = bytes_or_str.decode('utf-8')
	else:
		value = bytes_or_str
	return value  # Instance of str


def to_bytes(bytes_or_str):
    ''' func that takes a str or bytes
    and always returns a bytes
    '''
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value  # Instance of bytes
```


```python
# Python 2
def to_unicode(unicode_or_str):
    '''func that takes a str or unicode
    and always returns a unicode
    '''
    if isinstance(unicode_or_str, str):
        value = unicode_or_str.decode('utf-8')
    else:
        value = unicode_or_str
    return value  # Instance of unicode

# Python 2
def to_str(unicode_or_str):
    ''' that takes str or unicode 
    and always returns a str
    '''
    if isinstance(unicode_or_str, unicode):
        value = unicode_or_str.encode('utf-8')
    else:
        value = unicode_or_str
    return value  # Instance of str
```
