# -*- coding: utf-8 -*-
from icalendar.parser_tools import to_unicode
from icalendar.parser_tools import data_encode

try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict


def canonsort_keys(keys, canonical_order=None):
    """Sorts leading keys according to canonical_order.  Keys not specified in
    canonical_order will appear alphabetically at the end.
    """
    canonical_map = dict((k, i) for i, k in enumerate(canonical_order or []))
    head = [k for k in keys if k in canonical_map]
    tail = [k for k in keys if k not in canonical_map]
    return sorted(head, key=lambda k: canonical_map[k]) + sorted(tail)


def canonsort_items(dict1, canonical_order=None):
    """Returns a list of items from dict1, sorted by canonical_order.
    """
    return [(k, dict1[k]) for \
            k in canonsort_keys(dict1.keys(), canonical_order)]


class CaselessDict(dict):
    """A dictionary that isn't case sensitive, and only uses strings as keys.
    Values retain their case.
    """

    def __init__(self, *args, **kwargs):
        """Set keys to upper for initial dict.
        """
        super(CaselessDict, self).__init__(*args, **kwargs)
        for key, value in self.items():
            key_upper = to_unicode(key).upper()
            if key != key_upper:
                super(CaselessDict, self).__delitem__(key)
                self[key_upper] = value

    def __getitem__(self, key):
        key = to_unicode(key)
        return super(CaselessDict, self).__getitem__(key.upper())

    def __setitem__(self, key, value):
        key = to_unicode(key)
        super(CaselessDict, self).__setitem__(key.upper(), value)

    def __delitem__(self, key):
        key = to_unicode(key)
        super(CaselessDict, self).__delitem__(key.upper())

    def __contains__(self, key):
        key = to_unicode(key)
        return super(CaselessDict, self).__contains__(key.upper())

    def get(self, key, default=None):
        key = to_unicode(key)
        return super(CaselessDict, self).get(key.upper(), default)

    def setdefault(self, key, value=None):
        key = to_unicode(key)
        return super(CaselessDict, self).setdefault(key.upper(), value)

    def pop(self, key, default=None):
        key = to_unicode(key)
        return super(CaselessDict, self).pop(key.upper(), default)

    def popitem(self):
        return super(CaselessDict, self).popitem()

    def has_key(self, key):
        key = to_unicode(key)
        return super(CaselessDict, self).__contains__(key.upper())

    def update(self, indict):
        # Multiple keys where key1.upper() == key2.upper() will be lost.
        for key, value in indict.items():  # TODO optimize in python 2
            self[key] = value

    def copy(self):
        return type(self)(super(CaselessDict, self).copy())

    def __repr__(self):
        return 'CaselessDict(%s)' % data_encode(self)

    # A list of keys that must appear first in sorted_keys and sorted_items;
    # must be uppercase.
    canonical_order = None

    def sorted_keys(self):
        """Sorts keys according to the canonical_order for the derived class.
        Keys not specified in canonical_order will appear at the end.
        """
        return canonsort_keys(self.keys(), self.canonical_order)

    def sorted_items(self):
        """Sorts items according to the canonical_order for the derived class.
        Items not specified in canonical_order will appear at the end.
        """
        return canonsort_items(self, self.canonical_order)
