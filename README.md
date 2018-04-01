# ForIf.py

### A C-like condition assignment syntax in python

## Example

Why write cumbersome un-pythonic code like:

```python
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
```

When you can write this instead:

```python
from forif import if_exists

data = {'a': [1,2,3]} # Some random JSON you've received
for last in if_exists(data, lambda x: x['a'][-1]):
    print('last value is', last)
    break
else:
    print('could not find last value :(')
```

Now like C, you can assign, conditional and execute all at once.

Just don't forget to end the for: with break **if you want to use else:** if the conditional fails (_just like lambda, python can't have everything right_), it's not needed otherwise

## Another example

Let's say you've received a JSON response and you want to go over just the items which have both a name and an address:
```python
from forif import if_unpack, if_predicate_each

data = {
    'items': 2,
    'users': [
        {
            'name': 'pwn',
            'address': 'somewhere'
        },
        {
            'name': 'to',
            'address': None
        },
        {
            'name': 'own',
        }
    ]
}
for user in if_unpack(data, lambda x: x['users']):
    for name, address in if_predicate_each(user, lambda x: (x['name'], x['address'])):
        print('We found user %s with address %s' % (name, address))
```

will output just "We found user pwn with address somewhere"

# Install

Currently you can install this package via pip using (change tag 0.0.1 to whichever version you want):

```pip install -e git://github.com/tzickel/forif.git@0.0.1#egg=forif```

# Changelog

## 0.0.1 - 2018-04-01
* Initial release