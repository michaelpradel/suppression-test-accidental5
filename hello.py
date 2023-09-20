"""
Toy example.
"""

def hello():
    """ A fantastic docstring. """
    # pylint: disable=missing-format-string-key
    print("\n")
    # some comment
    print("Hello %(first)s %(last)s" % {"First": "John", "last": "Doe"})
    # some other comment
    print("Hello %(first)s %(last)s" % {"first": "John", "ast": "Doe"})
