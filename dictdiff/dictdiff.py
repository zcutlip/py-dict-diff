class DictDiff:
    def __init__(self, d1, d2):
        added, removed, modified, same = self._dict_compare(d1, d2)
        self.added = added
        self.removed = removed
        self.modified = modified
        self.same = same

    def _dict_compare(self, d1, d2):
        d1 = {int(k): v for k, v in d1.items()}
        d2 = {int(k): v for k, v in d2.items()}
        d1_keys = set(d1.keys())
        d2_keys = set(d2.keys())

        intersect_keys = d1_keys.intersection(d2_keys)
        intersect_keys = list(intersect_keys)
        intersect_keys.sort()

        added_keys = d2_keys - d1_keys
        added_keys = list(added_keys)
        added_keys.sort()
        added = {o: d2[o] for o in added_keys}

        removed = d1_keys - d2_keys
        removed = list(removed)
        removed.sort()

        modified = {o: d2[o] for o in intersect_keys if d1[o] != d2[o]}

        same = set(o for o in intersect_keys if d1[o] == d2[o])
        same = list(same)
        same.sort()

        return added, list(removed), modified, list(same)
