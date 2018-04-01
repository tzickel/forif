"""
A C-like condition assignment syntax in python.

Why write cumbersome un-pythonic code like:

data = {'a': [1,2,3]} # Some random JSON you've received
v = data.get('a', None) if data else None
found = False
if v:
    last = v[-1] if hasattr(v, '__getitem__') else None
    if last:
        found = True
        print('last value is', last)
if not found:
    print('could not find last value :(')

When you can write this instead:

from forif import if_exists

data = {'a': [1,2,3]} # Some random JSON you've received
for last in if_exists(data, lambda x: x['a'][-1]):
    print('last value is', last)
    break
else:
    print('could not find last value :(')

Now like C, you can assign, conditional and execute all at once.

Just don't forget to end the for: with break if you want to use else: if the conditional fails (just like lambda, python can't have everything right)
"""
def if_exists(obj, getter):
    try:
        ret = getter(obj)
    except:
        return
    yield ret


def if_predicate(obj, getter=None, predicate=lambda x: bool(x)):
    try:
        ret = getter(obj) if getter else obj
    except:
        return
    if predicate(ret):
        yield ret


def if_predicate_each(obj, getter=None, predicate=lambda x: bool(x)):
    try:
        ret = getter(obj) if getter else obj
    except:
        return
    _iter = getattr(ret, '__iter__', False)
    if _iter:
        for tmp in _iter():
            if not predicate(tmp):
                return
        yield ret
    else:
        if predicate(ret):
            yield ret


def if_unpack(obj, getter=None):
    try:
        ret = iter(getter(obj) if getter else obj)
    except:
        return
    for tmp in ret:
        yield tmp
