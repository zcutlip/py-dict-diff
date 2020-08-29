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

