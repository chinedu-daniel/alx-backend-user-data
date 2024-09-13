#!/usr/bin/env python3
"""
regexing
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
        message: str, separator: str) -> str:
    """
    regex-ing
    """
    for f in fields:
        message = re.sub(f'{f}=.*?{separator}',
                f'{f}={redaction}{separator}', message)

    return message
