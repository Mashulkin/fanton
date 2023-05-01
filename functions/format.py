# -*- coding: utf-8 -*-
"""
Formatting
"""


__author__ = 'Vadim Arsenev'
__version__ = '1.0.0'
__data__ = '01.05.2023'


def formatCardRarity(cardRarity):
    if cardRarity == 'common':
        rarity = 'com'
    elif cardRarity == 'legendary':
        rarity = 'leg'     
    else:
        rarity = cardRarity

    return rarity
