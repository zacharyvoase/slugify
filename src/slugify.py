# -*- coding: utf-8 -*-

"""A generic slugifier utility (currently only for Latin-based scripts)."""

import re
import sys
import unicodedata

__version__ = '0.0.1'

# Micro stealing from the six module
if sys.version_info[0] == 3:
    text_type = str
else:
    text_type = unicode

def slugify(string):

    """
    Slugify a unicode string.

    Example:

        >>> slugify(u"Héllø Wörld")
        u"hello-world"

    """

    value = text_type(string)
    value = unicodedata.normalize('NFKD', value).encode(
        'ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value).strip().lower()
    return re.sub(r'[-\s]+', '-', value)
