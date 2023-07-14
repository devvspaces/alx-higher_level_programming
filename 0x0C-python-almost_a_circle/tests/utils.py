#!/usr/bin/python3

"""
Test utilities
"""

from io import StringIO
from contextlib import redirect_stdout


def extract_stdout(function, *args, **kwargs):
    """Extract stdout
    """
    f = StringIO()
    with redirect_stdout(f):
        function(*args, **kwargs)
    return f.getvalue()
