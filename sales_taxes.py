#!/usr/bin/env python3
import re
import sys
from math import ceil

from typing import Tuple

TAX_FREE = ['book', 'chocolate', 'pill']
LINE_RGX = re.compile(r"^(\d+) (.*) at (\d+\.\d{2})$")


def main(argv):
    if len(argv) != 2:
        raise AttributeError("no basket file defined!")
    with open(argv[1], "r", encoding="utf8") as f:
        print(basket2receipt(f.readlines()))


def basket2receipt(lines):
    total = 0
    taxes = 0
    output = ""
    for line in lines:
        line = line.strip()
        if not line:
            continue  # empty line
        amount, text, price = read_line(line)
        if not price:
            raise ValueError(f"abort program, malformed line:\n{line}")
        tax_rate = get_tax_rate_by_description(text)
        tax = round_up_tax(tax_rate * price * amount) if tax_rate else 0
        total += price * amount + tax
        taxes += tax
        output += f"{amount} {text}: {(price * amount + tax):.2f}\n"
    output += f"Sales Taxes: {taxes:.2f}\n"
    output += f"Total: {total:.2f}"
    return output


def read_line(line: str) -> Tuple[int, str, float] or None:
    match = LINE_RGX.match(line)
    if match:
        return int(match[1]), str(match[2]), float(match[3])
    return None, None, None


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


if __name__ == '__main__':
    try:
        main(sys.argv)
    except (AttributeError, ValueError) as err:
        print(err)
        exit(1)
