#!/usr/bin/env python3

import re


def filter_datum(fields, redaction, message, separator):
    """
    regex-ing
    """
    pattern = '|'.join([f'{field}=([^\\{separator}]+)' for field in fields])
