# -*- coding: utf-8 -*-
"""
Getting team details
"""
from simple_settings import settings
from functions.tournament import get_teamDetails
from functions.format import formatCardRarity


__author__ = 'Vadim Arsenev'
__version__ = '1.2.0'
__data__ = '18.10.2024'


def realTeamDetails(listOfCards, realPlayerId):
    realTeamId = ''
    for card in listOfCards:
        if card['node']['player']['id'] == realPlayerId:
            realTeamId = card['node']['player']['teamIds'][-1]
            break
    
    return realTeamId


def teamDetails(fantasyTeamId, listOfCards):
    teamData = get_teamDetails(fantasyTeamId)

    card1PlayerName = teamData['data']['node']['cards'][0]['player']['name']
    card1PlayerId = teamData['data']['node']['cards'][0]['player']['id']
    card1TeamId = realTeamDetails(listOfCards, card1PlayerId)
    card1Rarity= teamData['data']['node']['cards'][0]['rarity'].lower()

    card2PlayerName = teamData['data']['node']['cards'][1]['player']['name']
    card2PlayerId = teamData['data']['node']['cards'][1]['player']['id']
    card2TeamId = realTeamDetails(listOfCards, card2PlayerId)
    card2Rarity= teamData['data']['node']['cards'][1]['rarity'].lower()

    card3PlayerName = teamData['data']['node']['cards'][2]['player']['name']
    card3PlayerId = teamData['data']['node']['cards'][2]['player']['id']
    card3TeamId = realTeamDetails(listOfCards, card3PlayerId)
    card3Rarity= teamData['data']['node']['cards'][2]['rarity'].lower()

    card4PlayerName = teamData['data']['node']['cards'][3]['player']['name']
    card4PlayerId = teamData['data']['node']['cards'][3]['player']['id']
    card4TeamId = realTeamDetails(listOfCards, card4PlayerId)
    card4Rarity= teamData['data']['node']['cards'][3]['rarity'].lower()

    try:
        card5PlayerName = teamData['data']['node']['cards'][4]['player']['name']
        card5PlayerId = teamData['data']['node']['cards'][4]['player']['id']
        card5TeamId = realTeamDetails(listOfCards, card5PlayerId)
        card5Rarity= teamData['data']['node']['cards'][4]['rarity'].lower()
    except IndexError:
        card5PlayerName = ''
        card5PlayerId = ''
        card5TeamId = ''
        card5Rarity = ''

    cardCaptain = teamData['data']['node']['captain']['id']

    card1Rarity = formatCardRarity(card1Rarity)
    card2Rarity = formatCardRarity(card2Rarity)
    card3Rarity = formatCardRarity(card3Rarity)
    card4Rarity = formatCardRarity(card4Rarity)
    card5Rarity = formatCardRarity(card5Rarity)

    return card1PlayerName, card1PlayerId, card1TeamId, card1Rarity, \
        card2PlayerName, card2PlayerId, card2TeamId, card2Rarity, \
        card3PlayerName, card3PlayerId, card3TeamId, card3Rarity, \
        card4PlayerName, card4PlayerId, card4TeamId, card4Rarity, \
        card5PlayerName, card5PlayerId, card5TeamId, card5Rarity, cardCaptain


def scoringDetails(teamData, pos):
    minutes, missedPasses, foulsDrawn, savesInBox, saves, \
        longBallsWon, accuratePasses, keyPasses, \
        tackles, accurateCrosses, blockedShots, \
        interceptions, cleanSheet, successfulDribbles, \
        bigChancesCreated, assists, goalsConceded, shotsOnTarget, \
        fouls, yellowCards, goals, clearances, penaltiesCommitted, \
        bigChancesMissed, hitWoodwork, penaltiesWon, clearanceOffline, \
        errorLeadToGoal= [''] * 28

    try:
        cardPlayerName = teamData['data']['node']['cards'][pos]['player']['name']
        cardId = teamData['data']['node']['cards'][pos]['id']
    except IndexError:
        cardPlayerName = ''
        cardId = ''

    scoring = []
    for item in teamData['data']['scores']['edges']:
        # if item['node']['ruleId'] not in scoring:
        #     scoring.append(item['node']['ruleId'])
        if item['node']['card']['id'] == cardId:
            if item['node']['ruleId'] == 'v3_missed_passes':
                missedPasses = item['node']['points']
                continue

            if item['node']['ruleId'] == 'v3_minutes_played':
                minutes = item['node']['points']
                continue

            if item['node']['ruleId'] == 'v3_fouls_drawn':
                foulsDrawn = item['node']['points']
                continue

            if item['node']['ruleId'] == 'v3_saves_inside_box':
                savesInBox = item['node']['points']
                continue

            if item['node']['ruleId'] == 'v3_saves':
                saves = item['node']['points']
                continue

            if item['node']['ruleId'] == 'v3_long_balls_won':
                longBallsWon = item['node']['points']
                continue

            if item['node']['ruleId'] == 'v3_accurate_passes':
                accuratePasses = item['node']['points']
                continue

            if item['node']['ruleId'] == 'v3_key_passes':
                keyPasses = item['node']['points']
                continue

            if item['node']['ruleId'] == 'v3_tackles':
                tackles = item['node']['points']
                continue

            if item['node']['ruleId'] == 'v3_accurate_crosses':
                accurateCrosses = item['node']['points']
                continue

            if item['node']['ruleId'] == 'v3_blocked_shots':
                blockedShots = item['node']['points']
                continue

            if item['node']['ruleId'] == 'v3_interceptions':
                interceptions = item['node']['points']
                continue

            if item['node']['ruleId'] == 'v3_clean_sheet':
                cleanSheet = item['node']['points']
                continue

            if item['node']['ruleId'] == 'v3_successful_dribbles':
                successfulDribbles = item['node']['points']
                continue

            if item['node']['ruleId'] == 'v3_big_chances_created':
                bigChancesCreated = item['node']['points']
                continue

            if item['node']['ruleId'] == 'v3_assists':
                assists = item['node']['points']
                continue

            if item['node']['ruleId'] == 'v3_goals_conceded':
                goalsConceded = item['node']['points']
                continue

            if item['node']['ruleId'] == 'v3_shots_on_target':
                shotsOnTarget = item['node']['points']
                continue

            if item['node']['ruleId'] == 'v3_fouls':
                fouls = item['node']['points']
                continue

            if item['node']['ruleId'] == 'v3_yellow_cards':
                yellowCards = item['node']['points']
                continue

            if item['node']['ruleId'] == 'v3_goals':
                goals = item['node']['points']
                continue

            if item['node']['ruleId'] == 'v3_clearances':
                clearances = item['node']['points']
                continue

            if item['node']['ruleId'] == 'v3_penalties_committed':
                penaltiesCommitted = item['node']['points']
                continue

            if item['node']['ruleId'] == 'v3_big_chances_missed':
                bigChancesMissed = item['node']['points']
                continue

            if item['node']['ruleId'] == 'v3_hit_woodwork':
                hitWoodwork = item['node']['points']
                continue

            if item['node']['ruleId'] == 'v3_penalties_won':
                penaltiesWon = item['node']['points']
                continue

            if item['node']['ruleId'] == 'v3_clearance_offline':
                clearanceOffline = item['node']['points']
                continue

            if item['node']['ruleId'] == 'v3_error_lead_to_goal':
                errorLeadToGoal = item['node']['points']
                continue

    return cardPlayerName, cardId, minutes, missedPasses, foulsDrawn, \
        savesInBox, saves, longBallsWon, accuratePasses, keyPasses, \
        tackles, accurateCrosses, blockedShots, interceptions, \
        cleanSheet, successfulDribbles, bigChancesCreated, assists, \
        goalsConceded, shotsOnTarget, fouls, yellowCards, goals, \
        clearances, scoring, penaltiesCommitted, bigChancesMissed, \
        hitWoodwork, penaltiesWon, clearanceOffline, errorLeadToGoal
