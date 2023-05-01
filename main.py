# -*- coding: utf-8 -*-
"""
Getting information about the NFT cards
"""
import addpath
import sys
from simple_settings import settings

from common_modules.csv_w import write_csv
from common_modules.txt_r import read_txt
from common_modules.headline import print_headline
from common_modules.my_remove import remove_file

from functions.tournament import get_tournaments
from functions.players import teamDetails


__author__ = 'Vadim Arsenev'
__version__ = '1.0.0'
__data__ = '01.05.2023'


ORDER = list(map(lambda x: x.split(':')[0].strip(), \
    read_txt(settings.COLUMNS).split('\n')))


def tournInfo(tournament):
    """
    The main module for performing all operations of a request
       and writing to a file
    """
    print_headline(settings.RESULT_FILE[0], settings.COLUMNS, ORDER)
    data = tournament['data']['node']
    numberOfTeams = data['numberOfTeams']
    nameTourn = data['enName']

    for item in data['teams']['edges']:
        # ***** Main query *****
        fantasyTeamId = item['node']['id']
        fantasyTeamPlace = item['node']['place']
        fantasyTeamScore = item['node']['score']
        accountId = item['node']['account']['id']
        accountName = item['node']['account']['name']
        idCard1 = item['node']['cards'][0]['id']
        idCard2 = item['node']['cards'][1]['id']
        idCard3 = item['node']['cards'][2]['id']
        idCard4 = item['node']['cards'][3]['id']
        try: 
            idCard5 = item['node']['cards'][4]['id']
        except IndexError:
            idCard5 = ''
        
        card1PlayerName, card1PlayerId, card1Rarity, \
        card2PlayerName, card2PlayerId, card2Rarity, \
        card3PlayerName, card3PlayerId, card3Rarity, \
        card4PlayerName, card4PlayerId, card4Rarity, \
        card5PlayerName, card5PlayerId, card5Rarity, \
        cardCaptain = teamDetails(fantasyTeamId)

        # Data generation and writing to file
        data_tournament = {
            'fantasyTeamPlace': fantasyTeamPlace,
            'fantasyTeamScore': fantasyTeamScore,
            'accountName': accountName,
            'idCard1': idCard1,
            'idCard2': idCard2,
            'idCard3': idCard3,
            'idCard4': idCard4,
            'idCard5': idCard5,
            'card1PlayerName': card1PlayerName,
            'card1PlayerId': card1PlayerId,
            'card1Rarity': card1Rarity,
            'card2PlayerName': card2PlayerName,
            'card2PlayerId': card2PlayerId,
            'card2Rarity': card2Rarity,
            'card3PlayerName': card3PlayerName,
            'card3PlayerId': card3PlayerId,
            'card3Rarity': card3Rarity,
            'card4PlayerName': card4PlayerName,
            'card4PlayerId': card4PlayerId,
            'card4Rarity': card4Rarity,
            'card5PlayerName': card5PlayerName,
            'card5PlayerId': card5PlayerId,
            'card5Rarity': card5Rarity,
            'cardCaptain': cardCaptain,
        }

        write_csv(settings.RESULT_FILE[0], data_tournament, ORDER)


def main():
    """
    Request information about the fantasy tournament. General request
    """
    tournament = get_tournaments(sys.argv[1])
    tournInfo(tournament)


if __name__ == '__main__':
    for item in settings.RESULT_FILE:
        remove_file(item)
    main()
