# -*- coding: utf-8 -*-
"""
Formatting
"""


__author__ = 'Vadim Arsenev'
__version__ = '1.2.3'
__data__ = '08.03.2025'


def formatCardRarity(cardRarity):
    if cardRarity == 'common':
        rarity = 'com'
    elif cardRarity == 'legendary':
        rarity = 'leg'     
    else:
        rarity = cardRarity

    return rarity


def formatRealTeams(teamName):
    abbr = ''
    abbr = 'ARS' if teamName == 'Arsenal' else abbr
    abbr = 'AVL' if teamName == 'Aston Villa' else abbr
    abbr = 'BHA' if teamName == 'Brighton & Hove Albion' else abbr
    abbr = 'BOU' if teamName == 'AFC Bournemouth' else abbr
    abbr = 'BRE' if teamName == 'Brentford' else abbr
    abbr = 'CHE' if teamName == 'Chelsea' else abbr
    abbr = 'CRY' if teamName == 'Crystal Palace' else abbr
    abbr = 'EVE' if teamName == 'Everton' else abbr
    abbr = 'FUL' if teamName == 'Fulham' else abbr
    abbr = 'IPS' if teamName == 'Ipswich Town' else abbr
    abbr = 'LEI' if teamName == 'Leicester City' else abbr
    abbr = 'LIV' if teamName == 'Liverpool' else abbr
    abbr = 'MCI' if teamName == 'Manchester City' else abbr
    abbr = 'MUN' if teamName == 'Manchester United' else abbr
    abbr = 'NEW' if teamName == 'Newcastle United' else abbr
    abbr = 'NFO' if teamName == 'Nottingham Forest' else abbr
    abbr = 'SOU' if teamName == 'Southampton' else abbr
    abbr = 'TOT' if teamName == 'Tottenham Hotspur' else abbr
    abbr = 'WHU' if teamName == 'West Ham United' else abbr
    abbr = 'WOL' if teamName == 'Wolverhampton Wanderers' else abbr
    abbr = 'PSG' if teamName == 'Paris Saint Germain' else abbr
    abbr = 'BVB' if teamName == 'Borussia Dortmund' else abbr
    abbr = 'ATM' if teamName == 'Atlético Madrid' else abbr
    abbr = 'LEV' if teamName == 'Bayer 04 Leverkusen' else abbr
    abbr = 'LIL' if teamName == 'LOSC Lille' else abbr
    abbr = 'INT' if teamName == 'Inter' else abbr
    abbr = 'BAR' if teamName == 'FC Barcelona' else abbr
    abbr = 'BAY' if teamName == 'FC Bayern München' else abbr
    abbr = 'PSV' if teamName == 'PSV' else abbr
    abbr = 'FEY' if teamName == 'Feyenoord' else abbr
    abbr = 'RMA' if teamName == 'Real Madrid' else abbr
    abbr = 'BEN' if teamName == 'Benfica' else abbr
    abbr = 'BRU' if teamName == 'Club Brugge' else abbr
    abbr = 'ZEN' if teamName == 'Zenit' else abbr
    abbr = 'KRA' if teamName == 'Krasnodar' else abbr
    abbr = 'RUB' if teamName == 'Rubin Kazan' else abbr
    abbr = 'KRY' if teamName == 'Krylya Sovetov' else abbr
    abbr = 'AKR' if teamName == 'Akron' else abbr
    abbr = 'LOK' if teamName == 'Lokomotiv Moskva' else abbr
    abbr = 'CSK' if teamName == 'CSKA Moskva' else abbr
    abbr = 'DMO' if teamName == 'Dinamo Moskva' else abbr
    abbr = 'ROS' if teamName == 'Rostov' else abbr
    abbr = 'SPA' if teamName == 'Spartak Moskva' else abbr
    abbr = 'PNN' if teamName == 'FK Nizjni Novgorod' else abbr
    abbr = 'FAK' if teamName == 'Fakel' else abbr
    abbr = 'ORE' if teamName == 'Orenburg' else abbr
    abbr = 'AKH' if teamName == 'Akhmat Grozny' else abbr
    abbr = 'DMH' if teamName == 'Makhachkala' else abbr
    abbr = 'KHI' if teamName == 'Khimki' else abbr

    return abbr
