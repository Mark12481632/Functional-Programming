# Functional Programming using Map, Reduce and Filter.
# To "get an idea" about it.

from typing import NamedTuple

# Use "collections" to create imutable structures:
class Scientist(NamedTuple):
    name: str
    field: str
    born: int
    nobel: bool

# To ensure everything is immutable:
scientists = (Scientist(name='Ada Lovelace', field='math', born=1815, nobel=False),
              Scientist(name='Emmy Noether', field='math', born=1882, nobel=False),
              Scientist(name='Marie Curie', field='phyics', born=1867, nobel=True),
              Scientist(name='Tu Youyou', field='chemistry', born=1930, nobel=True),
              Scientist(name='Ada Yonath', field='chemistry', born=1939, nobel=True),
              Scientist(name='Vera Rubin', field='astronomy', born=1928, nobel=False),
              Scientist(name='Sally Ride', field='physics', born=1951, nobel=False))

# Filtering ...............

# Extract nobel winners - and make result immutable:
winners = tuple(filter(lambda x: x.nobel is True, scientists))
for winner in winners:
    print(winner)

print("---------------------------------")

def nobel_filter(x):
    return x.nobel is True

# Extract nobel winners - and make result immutable:
winners = tuple(filter(nobel_filter, scientists))
for winner in winners:
    print(winner)

print("---------------------------------")

# Python debelopers (non-functional) solution:
winners = tuple([x for x in scientists if x.nobel])
for winner in winners:
    print(winner)

# ====================================================

# Mapping .....
