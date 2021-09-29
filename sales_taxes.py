#!/usr/bin/env python3
from math import ceil

def round_up_tax(tax: float):
    return ceil(tax * 20) / 20
