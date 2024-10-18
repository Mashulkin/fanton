# -*- coding: utf-8 -*-
"""
Getting team details
"""
from simple_settings import settings
from functions.tournament import get_teamDetails
from functions.format import formatCardRarity, formatRealTeams


__author__ = 'Vadim Arsenev'
__version__ = '1.2.2'
__data__ = '18.10.2024'


def realTeamDetails(listOFTournRealTeams, listOfCards, realPlayerId):
    realTeamIds, realTeamName = [''] * 2
    for card in listOfCards:
        if card['node']['player']['id'] == realPlayerId:
            realTeamIds = card['node']['player']['teamIds']
            for team in listOFTournRealTeams:
                if team['team']['id'] in realTeamIds:
                    realTeamName = team['team']['name']
                    realTeamName = formatRealTeams(realTeamName)
                    break
    
    return realTeamIds, realTeamName


def teamDetails(fantasyTeamId, listOFTournRealTeams, listOfCards):
    teamData = get_teamDetails(fantasyTeamId)

    card1PlayerName = teamData['data']['node']['cards'][0]['player']['name']
    card1PlayerId = teamData['data']['node']['cards'][0]['player']['id']
    card1TeamId, card1TeamName = realTeamDetails(listOFTournRealTeams, listOfCards, card1PlayerId)
    card1Rarity= teamData['data']['node']['cards'][0]['rarity'].lower()

    card2PlayerName = teamData['data']['node']['cards'][1]['player']['name']
    card2PlayerId = teamData['data']['node']['cards'][1]['player']['id']
    card2TeamId, card2TeamName = realTeamDetails(listOFTournRealTeams, listOfCards, card2PlayerId)
    card2Rarity= teamData['data']['node']['cards'][1]['rarity'].lower()

    card3PlayerName = teamData['data']['node']['cards'][2]['player']['name']
    card3PlayerId = teamData['data']['node']['cards'][2]['player']['id']
    card3TeamId, card3TeamName = realTeamDetails(listOFTournRealTeams, listOfCards, card3PlayerId)
    card3Rarity= teamData['data']['node']['cards'][2]['rarity'].lower()

    card4PlayerName = teamData['data']['node']['cards'][3]['player']['name']
    card4PlayerId = teamData['data']['node']['cards'][3]['player']['id']
    card4TeamId, card4TeamName = realTeamDetails(listOFTournRealTeams, listOfCards, card4PlayerId)
    card4Rarity= teamData['data']['node']['cards'][3]['rarity'].lower()

    try:
        card5PlayerName = teamData['data']['node']['cards'][4]['player']['name']
        card5PlayerId = teamData['data']['node']['cards'][4]['player']['id']
        card5TeamId, card5TeamName = realTeamDetails(listOFTournRealTeams, listOfCards, card5PlayerId)
        card5Rarity= teamData['data']['node']['cards'][4]['rarity'].lower()
    except IndexError:
        card5PlayerName = ''
        card5PlayerId = ''
        card5TeamId = ''
        card5TeamName = ''
        card5Rarity = ''

    cardCaptain = teamData['data']['node']['captain']['id']

    card1Rarity = formatCardRarity(card1Rarity)
    card2Rarity = formatCardRarity(card2Rarity)
    card3Rarity = formatCardRarity(card3Rarity)
    card4Rarity = formatCardRarity(card4Rarity)
    card5Rarity = formatCardRarity(card5Rarity)

    return card1PlayerName, card1PlayerId, card1TeamId, card1TeamName, card1Rarity, \
        card2PlayerName, card2PlayerId, card2TeamId, card2TeamName, card2Rarity, \
        card3PlayerName, card3PlayerId, card3TeamId, card3TeamName, card3Rarity, \
        card4PlayerName, card4PlayerId, card4TeamId, card4TeamName, card4Rarity, \
        card5PlayerName, card5PlayerId, card5TeamId, card5TeamName, card5Rarity, cardCaptain


def scoringDetails(teamData, pos, listOFTournRealTeams, listOfCards):
    minutes, missedPasses, foulsDrawn, savesInBox, saves, \
        longBallsWon, accuratePasses, keyPasses, \
        tackles, accurateCrosses, blockedShots, \
        interceptions, cleanSheet, successfulDribbles, \
        bigChancesCreated, assists, goalsConceded, shotsOnTarget, \
        fouls, yellowCards, goals, clearances, penaltiesCommitted, \
        bigChancesMissed, hitWoodwork, penaltiesWon, clearanceOffline, \
        errorLeadToGoal, penaltiesSaved= [''] * 29

    try:
        cardPlayerName = teamData['data']['node']['cards'][pos]['player']['name']
        cardId = teamData['data']['node']['cards'][pos]['id']
        realPlayerId = teamData['data']['node']['cards'][pos]['player']['id']
        realTeamId, abbr = realTeamDetails(listOFTournRealTeams, listOfCards, realPlayerId)
    except IndexError:
        cardPlayerName = ''
        cardId = ''
        realPlayerId = ''

    scoring = []
    for item in teamData['data']['scores']['edges']:
        # if item['node']['ruleId'] not in scoring:
        #     scoring.append(item['node']['ruleId'])
        if item['node']['card']['id'] == cardId:
            if item['node']['ruleId'] == 'v4_missed_passes':
                missedPasses = item['node']['points']
                continue

            if item['node']['ruleId'] == 'v4_minutes_played':
                minutes = item['node']['points']
                continue

            if item['node']['ruleId'] == 'v4_fouls_drawn':
                foulsDrawn = item['node']['points']
                continue

            if item['node']['ruleId'] == 'v4_saves_inside_box':
                savesInBox = item['node']['points']
                continue

            if item['node']['ruleId'] == 'v4_saves':
                saves = item['node']['points']
                continue

            if item['node']['ruleId'] == 'v4_long_balls_won':
                longBallsWon = item['node']['points']
                continue

            if item['node']['ruleId'] == 'v4_accurate_passes':
                accuratePasses = item['node']['points']
                continue

            if item['node']['ruleId'] == 'v4_key_passes':
                keyPasses = item['node']['points']
                continue

            if item['node']['ruleId'] == 'v4_tackles':
                tackles = item['node']['points']
                continue

            if item['node']['ruleId'] == 'v4_accurate_crosses':
                accurateCrosses = item['node']['points']
                continue

            if item['node']['ruleId'] == 'v4_blocked_shots':
                blockedShots = item['node']['points']
                continue

            if item['node']['ruleId'] == 'v4_interceptions':
                interceptions = item['node']['points']
                continue

            if item['node']['ruleId'] == 'v4_clean_sheet':
                cleanSheet = item['node']['points']
                continue

            if item['node']['ruleId'] == 'v4_successful_dribbles':
                successfulDribbles = item['node']['points']
                continue

            if item['node']['ruleId'] == 'v4_big_chances_created':
                bigChancesCreated = item['node']['points']
                continue

            if item['node']['ruleId'] == 'v4_assists':
                assists = item['node']['points']
                continue

            if item['node']['ruleId'] == 'v4_goals_conceded':
                goalsConceded = item['node']['points']
                continue

            if item['node']['ruleId'] == 'v4_shots_on_target':
                shotsOnTarget = item['node']['points']
                continue

            if item['node']['ruleId'] == 'v4_fouls':
                fouls = item['node']['points']
                continue

            if item['node']['ruleId'] == 'v4_yellow_cards':
                yellowCards = item['node']['points']
                continue

            if item['node']['ruleId'] == 'v4_goals':
                goals = item['node']['points']
                continue

            if item['node']['ruleId'] == 'v4_clearances':
                clearances = item['node']['points']
                continue

            if item['node']['ruleId'] == 'v4_penalties_committed':
                penaltiesCommitted = item['node']['points']
                continue

            if item['node']['ruleId'] == 'v4_big_chances_missed':
                bigChancesMissed = item['node']['points']
                continue

            if item['node']['ruleId'] == 'v4_hit_woodwork':
                hitWoodwork = item['node']['points']
                continue

            if item['node']['ruleId'] == 'v4_penalties_won':
                penaltiesWon = item['node']['points']
                continue

            if item['node']['ruleId'] == 'v4_clearance_offline':
                clearanceOffline = item['node']['points']
                continue

            if item['node']['ruleId'] == 'v4_error_lead_to_goal':
                errorLeadToGoal = item['node']['points']
                continue

            if item['node']['ruleId'] == 'v4_penalties_saved':
                penaltiesSaved = item['node']['points']
                continue

    return cardPlayerName, realPlayerId, abbr, minutes, missedPasses, foulsDrawn, \
        savesInBox, saves, longBallsWon, accuratePasses, keyPasses, \
        tackles, accurateCrosses, blockedShots, interceptions, \
        cleanSheet, successfulDribbles, bigChancesCreated, assists, \
        goalsConceded, shotsOnTarget, fouls, yellowCards, goals, \
        clearances, scoring, penaltiesCommitted, bigChancesMissed, \
        hitWoodwork, penaltiesWon, clearanceOffline, errorLeadToGoal, \
        penaltiesSaved
