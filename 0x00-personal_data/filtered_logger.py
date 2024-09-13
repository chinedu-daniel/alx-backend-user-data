#!/usr/bin/env python3

import re


def filter_datum(fields, redaction, message, separator):
    """
    regex-ing
    """
    pattern = r'({})=([^{}]+)'.format('|'.join(fields), separator)
    return re.sub(pattern, r'\1=' + redaction, message
