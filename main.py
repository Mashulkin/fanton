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

from functions.tournament import get_tournaments, get_cards
from functions.players import teamDetails


__author__ = 'Vadim Arsenev'
__version__ = '1.1.3'
__data__ = '06.03.2025'


ORDER = list(map(lambda x: x.split(':')[0].strip(), \
    read_txt(settings.COLUMNS).split('\n')))


def tournInfo(tournament):
    """
    The main module for performing all operations of a request
       and writing to a file
    """
    print_headline(settings.RESULT_FILE[0], settings.COLUMNS, ORDER)
    data = tournament['data']['node']
    realTournamentId = data['tournaments'][0]['id']
    cards = get_cards(realTournamentId)
    listOFTournRealTeams = data['tournamentTeams']
    listOfCards = cards['data']['cards']['edges']
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
        
        card1PlayerName, card1PlayerId, card1TeamId, card1TeamName, card1Rarity, \
        card2PlayerName, card2PlayerId, card2TeamId, card2TeamName, card2Rarity, \
        card3PlayerName, card3PlayerId, card3TeamId, card3TeamName, card3Rarity, \
        card4PlayerName, card4PlayerId, card4TeamId, card4TeamName, card4Rarity, \
        card5PlayerName, card5PlayerId, card5TeamId, card5TeamName, card5Rarity, \
        cardCaptain = teamDetails(fantasyTeamId, listOFTournRealTeams, listOfCards)

        card1Point, card2Point, card3Point, card4Point, card5Point = [''] * 5
        pointPerPlayer, remainingPlayers = [''] * 2

        # Data generation and writing to file
        data_tournament = {
            'fantasyTeamPlace': fantasyTeamPlace,
            'fantasyTeamScore': fantasyTeamScore,
            'accountName': accountName,
            'accountId': accountId,
            'idCard1': idCard1,
            'idCard2': idCard2,
            'idCard3': idCard3,
            'idCard4': idCard4,
            'idCard5': idCard5,
            'card1PlayerName': card1PlayerName,
            'card1PlayerId': card1PlayerId,
            'card1TeamId': card1TeamId,
            'card1TeamName': card1TeamName,
            'card1Rarity': card1Rarity,
            'card2PlayerName': card2PlayerName,
            'card2PlayerId': card2PlayerId,
            'card2TeamId': card2TeamId,
            'card2TeamName': card2TeamName,
            'card2Rarity': card2Rarity,
            'card3PlayerName': card3PlayerName,
            'card3PlayerId': card3PlayerId,
            'card3TeamId': card3TeamId,
            'card3TeamName': card3TeamName,
            'card3Rarity': card3Rarity,
            'card4PlayerName': card4PlayerName,
            'card4PlayerId': card4PlayerId,
            'card4TeamId': card4TeamId,
            'card4TeamName': card4TeamName,
            'card4Rarity': card4Rarity,
            'card5PlayerName': card5PlayerName,
            'card5PlayerId': card5PlayerId,
            'card5TeamId': card5TeamId,
            'card5TeamName': card5TeamName,
            'card5Rarity': card5Rarity,
            'cardCaptain': cardCaptain,
            'card1Point': card1Point,
            'card2Point': card2Point,
            'card3Point': card3Point,
            'card4Point': card4Point,
            'card5Point': card5Point,
            'pointPerPlayer': pointPerPlayer,
            'remainingPlayers': remainingPlayers,

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
