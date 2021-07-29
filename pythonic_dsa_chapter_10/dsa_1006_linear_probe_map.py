from pythonic_dsa_chapter_10.dsa_1004_hash_map_base import *


class ProbeHashMap(HashMapBase):
    """Hash map implemented with linear probing for collision resolution."""
    _AVAIL = object()   # sentinal marks locations of previous deletions

    def is_available(self, j):
        """Return True if index j is available in table."""
        return self.table[j] is None or self.table[j] is ProbeHashMap._AVAIL

    def find_slot(self, j, k):
        """Search for key k in bucket at index j.

        Return (success, index) tuple, described as follows:
        If match was found, success is True and index denotes its location.
        If no match found, success is False and index denotes first available slot.
        """
        first_avail = None
        while True:
            if self.is_available(j):
                if first_avail is None:
                    first_avail = j              # mark this as first avail
                if self.table[j] is None:
                    return False, first_avail    # search has failed
            elif k == self.table[j].key:
                return True, j                   # found a match
            j = (j + 1) % len(self.table)        # keep looking (cyclically)

    def bucket_getitem(self, j, k):
        found, s = self.find_slot(j, k)
        if not found:
            raise KeyError("Key Error: " + repr(k))     # no match found
        return self.table[s].value

    def bucket_setitem(self, j, k, v):
        found, s = self.find_slot(j, k)
        if not found:
            self.table[s] = self.Item(k, v)     # insert new item
            self.n += 1                         # size has increased
        else:
            self.table[s].value = v            # overwrite existing

    def bucket_delitem(self, j, k):
        found, s = self.find_slot(j, k)
        if not found:
            raise KeyError("Key Error: " + repr(k))         # no match found
        self.table[s] = ProbeHashMap._AVAIL                 # mark as vacated

    def __iter__(self):
        for j in range(len(self. table)):                   # scan entire table
            if not self.is_available(j):
                yield self.table[j].key


