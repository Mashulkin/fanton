# -*- coding: utf-8 -*-
"""
Getting team details
"""
from simple_settings import settings
from functions.tournament import get_teamDetails
from functions.format import formatCardRarity


__author__ = 'Vadim Arsenev'
__version__ = '1.0.0'
__data__ = '01.05.2023'


def teamDetails(fantasyTeamId):
    teamData = get_teamDetails(fantasyTeamId)

    card1PlayerName = teamData['data']['node']['cards'][0]['player']['name']
    card1PlayerId = teamData['data']['node']['cards'][0]['player']['id']
    card1Rarity= teamData['data']['node']['cards'][0]['rarity'].lower()

    card2PlayerName = teamData['data']['node']['cards'][1]['player']['name']
    card2PlayerId = teamData['data']['node']['cards'][1]['player']['id']
    card2Rarity= teamData['data']['node']['cards'][1]['rarity'].lower()

    card3PlayerName = teamData['data']['node']['cards'][2]['player']['name']
    card3PlayerId = teamData['data']['node']['cards'][2]['player']['id']
    card3Rarity= teamData['data']['node']['cards'][2]['rarity'].lower()

    card4PlayerName = teamData['data']['node']['cards'][3]['player']['name']
    card4PlayerId = teamData['data']['node']['cards'][3]['player']['id']
    card4Rarity= teamData['data']['node']['cards'][3]['rarity'].lower()

    try:
        card5PlayerName = teamData['data']['node']['cards'][4]['player']['name']
        card5PlayerId = teamData['data']['node']['cards'][4]['player']['id']
        card5Rarity= teamData['data']['node']['cards'][4]['rarity'].lower()
    except IndexError:
        card5PlayerName = ''
        card5PlayerId = ''
        card5Rarity = ''

    cardCaptain = teamData['data']['node']['captain']['id']

    card1Rarity = formatCardRarity(card1Rarity)
    card2Rarity = formatCardRarity(card2Rarity)
    card3Rarity = formatCardRarity(card3Rarity)
    card4Rarity = formatCardRarity(card4Rarity)
    card5Rarity = formatCardRarity(card5Rarity)

    return card1PlayerName, card1PlayerId, card1Rarity, \
        card2PlayerName, card2PlayerId, card2Rarity, \
        card3PlayerName, card3PlayerId, card3Rarity, \
        card4PlayerName, card4PlayerId, card4Rarity, \
        card5PlayerName, card5PlayerId, card5Rarity, cardCaptain
