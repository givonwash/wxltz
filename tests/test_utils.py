import sys
from typing import Union

sys.path.insert(0, "../src/wxltz")

from wxltz import utils
from wxltz.models import HSV, Proportion


def eps_checker(
    new: Union[int, float], old: Union[int, float], eps: Proportion = Proportion(0.1)
) -> bool:
    return abs((new - old) / old) <= eps


def hex_to_dec(hex_str: str) -> int:
    return int(hex_str[1:], 16)


def hex_to_hsv_to_hex(hex_str: str) -> None:
    hsv = utils.hex_to_hsv(hex_str)
    calc = utils.hsv_to_hex(HSV(*hsv))
    assert eps_checker(
        new=hex_to_dec(hex_str), old=hex_to_dec(calc), eps=Proportion(0.05)
    )


def test_hex_to_hsv_to_hex():
    hex_strs = ["#2E0F4D", "#000000", "#FFFFFF"]
    for hex_str in hex_strs:
        hex_to_hsv_to_hex(hex_str=hex_str)


def test_shade():
    assert True
