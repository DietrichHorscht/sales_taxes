#!/usr/bin/env python3
from math import ceil

TAX_FREE = ['book', 'chocolate', 'pill']


def get_tax_rate_by_description(description: str):
    has_tax = True
    has_duty = False
    for word in description.split():
        if [free for free in TAX_FREE if word.upper().startswith(free.upper())]:
            has_tax = False
            continue
        if "imported" == word.lower():
            has_duty = True
    return round((0.1 if has_tax else 0.0) + (0.05 if has_duty else 0.0), 2)


def round_up_tax(tax: float):
    return ceil(tax * 20) / 20
