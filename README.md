# DICTDIFF

## Description

A python module that allows you to compare two dictionaries and notes which keys:

- Have values that changed
- Have values that are the same
- Have been added
- Have been removed

## Example

```python
from dictdiff import DictDiff

dict1 = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4
}

dict2 = {
    "a": 1,
    "b": 6,
    "d": 4,
    "e": 5
}

diff = DictDiff(dict1, dict2)

print("added: {}".format(diff.added))
print("removed: {}".format(diff.removed))
print("modified: {}".format(diff.modified))
print("same: {}".format(diff.same))
```

```console
$ python3 ./example.py
added: {'e': 5}
removed: ['c']
modified: {'b': 6}
same: ['a', 'd']
```
