# Functional Programming using Immutable Data.

import collections

def print_scientists(scientists):
    for scientist in scientists:
        print(scientist)


# 1st attempt:
scientists = [
    {'name': 'Ada Lovelace', 'field': 'math', 'born': 1815, 'nobel': False},
    {'name': 'Emmy Noether', 'field': 'math', 'born': 1882, 'nobel': False},
    {'name': 'Marie Curie', 'field': 'phyics', 'born': 1867, 'nobel': True},
    {'name': 'Tu Youyou', 'field': 'chemistry', 'born': 1930, 'nobel': True},
    {'name': 'Ada Yonath', 'field': 'chemistry', 'born': 1939, 'nobel': True},
    {'name': 'Vera Rubin', 'field': 'astronomy', 'born': 1928, 'nobel': False},
    {'name': 'Sally Ride', 'field': 'physics', 'born': 1951, 'nobel': False},
]
print("1.")
print_scientists(scientists)

# Demonstrate data is mutable.

scientists[0]['name'] = "Linda Lovelace"
print("2.")
print_scientists(scientists)

# Use "collections" to create imutable structures:
Scientist = collections.namedtuple('Scientist', 
                                   ['name', 'field', 'born', 'nobel'])

ada = Scientist(name='Ada Lovelace', field='math', born=1815, nobel=False)
print(ada)
print(ada.field, ada.name)

# Can' assign:
# ada.name = "Marie Curie" # won't work!

scientists = [Scientist(name='Ada Lovelace', field='math', born=1815, nobel=False),
              Scientist(name='Emmy Noether', field='math', born=1882, nobel=False),
              Scientist(name='Marie Curie', field='phyics', born=1867, nobel=True),
              Scientist(name='Tu Youyou', field='chemistry', born=1930, nobel=True),
              Scientist(name='Ada Yonath', field='chemistry', born=1939, nobel=True),
              Scientist(name='Vera Rubin', field='astronomy', born=1928, nobel=False),
              Scientist(name='Sally Ride', field='physics', born=1951, nobel=False)]

print("3.")
print_scientists(scientists)
# But list is mutable.

# To ensure everything is immutable:
scientists = (Scientist(name='Ada Lovelace', field='math', born=1815, nobel=False),
              Scientist(name='Emmy Noether', field='math', born=1882, nobel=False),
              Scientist(name='Marie Curie', field='phyics', born=1867, nobel=True),
              Scientist(name='Tu Youyou', field='chemistry', born=1930, nobel=True),
              Scientist(name='Ada Yonath', field='chemistry', born=1939, nobel=True),
              Scientist(name='Vera Rubin', field='astronomy', born=1928, nobel=False),
              Scientist(name='Sally Ride', field='physics', born=1951, nobel=False))

print("4.")
print_scientists(scientists)
# But tuple is immutable.
