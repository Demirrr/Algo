import bisect
import collections

class SortedList:
    def __init__(self, *elements, key_func=None):
        self._list = sorted(*elements, key=key_func)

    def index(self, item):
        i = bisect.bisect_left(self._list, item)
        if i < len(self._list) and self._list[i] == item:
            return i

    def delete(self, item):
        del self._list[self.index(item)]

    def add(self, item):
        bisect.insort(self._list, item)

    def __iter__(self):
        for item in self._list:
            yield item

    def __exists__(self, item):
        return self.index(item) is not None


l = SortedList(['apple', 'banana', 'orange', 'plum'])

print('apple' in l)
print('mapple' in l)
l.add('ab')
print(l.index('apple'))
l.delete('ab')
print(l.index('apple'))
