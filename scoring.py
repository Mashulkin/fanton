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

from functions.tournament import get_tournaments, get_teamDetails
from functions.players import scoringDetails


__author__ = 'Vadim Arsenev'
__version__ = '1.0.0'
__data__ = '15.08.2023'


ORDER = list(map(lambda x: x.split(':')[0].strip(), \
    read_txt(settings.COLUMNS_SCORING).split('\n')))


def tournInfo(tournament):
    """
    The main module for performing all operations of a request
       and writing to a file
    """
    print_headline(settings.RESULT_FILE_SCORING[0], settings.COLUMNS_SCORING, ORDER)
    data = tournament['data']['node']
    playersId = []
    # allScoring = []

    for item in data['teams']['edges']:
        # ***** Main query *****
        fantasyTeamId = item['node']['id']
        teamData = get_teamDetails(fantasyTeamId)
        position = ''

        for pos in range(4):
            cardPlayerName, cardId, minutes, \
                missedPasses, foulsDrawn, savesInBox, saves, \
                longBallsWon, accuratePasses, keyPasses, \
                tackles, accurateCrosses, blockedShots, \
                interceptions, cleanSheet, successfulDribbles, \
                bigChancesCreated, assists, goalsConceded, shotsOnTarget, \
                fouls, yellowCards, goals, clearances, scoring, \
                penaltiesCommitted, bigChancesMissed, hitWoodwork, penaltiesWon,\
                clearanceOffline, errorLeadToGoal = scoringDetails(teamData, pos)

            if minutes == '':
                continue
            
            # for i in scoring:
            #     if i not in allScoring:
            #         allScoring.append(i)

            position = 'GK' if pos == 0 else position
            position = 'D' if pos == 1 else position
            position = 'M' if pos == 2 else position
            position = 'F' if pos == 3 else position

            if cardId not in playersId:
                playersId.append(cardId)
                # Data generation and writing to file
                data_tournament = {
                    'cardPlayerName': cardPlayerName,
                    'cardId': cardId,
                    'position': position,
                    'minutes': minutes,
                    'missedPasses': missedPasses,
                    'foulsDrawn': foulsDrawn,
                    'savesInBox': savesInBox,
                    'saves': saves,
                    'longBallsWon': longBallsWon,
                    'accuratePasses': accuratePasses,
                    'keyPasses': keyPasses,
                    'tackles': tackles,
                    'accurateCrosses': accurateCrosses,
                    'blockedShots': blockedShots,
                    'interceptions': interceptions,
                    'cleanSheet': cleanSheet,
                    'successfulDribbles': successfulDribbles,
                    'bigChancesCreated': bigChancesCreated,
                    'assists': assists,
                    'goalsConceded': goalsConceded,
                    'shotsOnTarget': shotsOnTarget,
                    'fouls': fouls,
                    'yellowCards': yellowCards,
                    'goals': goals,
                    'clearances': clearances,
                    'penaltiesCommitted': penaltiesCommitted,
                    'bigChancesMissed': bigChancesMissed,
                    'hitWoodwork': hitWoodwork,
                    'penaltiesWon': penaltiesWon,
                    'clearanceOffline': clearanceOffline,
                    'errorLeadToGoal': errorLeadToGoal,
                }

                write_csv(settings.RESULT_FILE_SCORING[0], data_tournament, ORDER)
    # print(allScoring)

def main():
    """
    Request information about the fantasy tournament. General request
    """
    tournament = get_tournaments(sys.argv[1])
    tournInfo(tournament)


if __name__ == '__main__':
    for item in settings.RESULT_FILE_SCORING:
        remove_file(item)
    main()
