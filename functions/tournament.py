# -*- coding: utf-8 -*-
"""
Additional requests
"""
from simple_settings import settings
from common_modules.parser import ParserPost


__author__ = 'Vadim Arsenev'
__version__ = '1.0.0'
__data__ = '01.05.2023'


def get_tournaments(idTourn):
    payload = settings.BODY_TOURNAMENT
    variables = {'first': settings.FIRST, 'id': idTourn}
    requests_data = ParserPost(settings.API_URL, payload, variables)
    tournament = requests_data.parser_graphql_result_var()

    return tournament


def get_teamDetails(fantasyTeamId):
    payload = settings.BODY_TEAM_DETAILS
    variables = {'teamId': fantasyTeamId}
    requests_data = ParserPost(settings.API_URL, payload, variables)
    tournament = requests_data.parser_graphql_result_var()

    return tournament
