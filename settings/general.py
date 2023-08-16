
__author__ = 'Vadim Arsenev'
__version__ = '1.0.0'
__data__ = '01.05.2023'


API_URL = 'https://app.fan-ton.com/graphql'

# for NFT cards only
COLUMNS = './settings/tournament.txt'
RESULT_FILE = ['./data/tournament.csv']

# for scoring only
COLUMNS_SCORING = './settings/scoring.txt'
RESULT_FILE_SCORING = ['./data/scoring.csv']

FIRST = 20000

BODY_TOURNAMENT = \
"""
query getTournament($id: ID!, $first: Int) {
    node(id: $id) {
        ... on Game {
            id
            enName: name(locale: EN)
            period {
                from
                to
            }
            tournaments {
                id
                name
            }
            isPaid
            isNft
            tournamentTeams {
                id
                team {
                    id
                    name
                }
            }
            numberOfTeams
            teams(first: $first) {
                edges {
                    cursor
                    node {
                        id
                        place
                        score
                        account {
                            id
                            name
                        }
                        cards {
                            id
                        }
                    }
                }
            }
            ticketPrice {
                amount
            }
        }
    }
}
"""

BODY_TEAM_DETAILS = \
"""
query getTeamDetails($teamId: ID!) {
    scores(teams: [$teamId], first: 99) {
        edges {
            node {
                id
                points
                card {
                    id
                }
                ruleId
            }
        }
    }
    node(id: $teamId) {
        ... on UserTeam {
            cards {
                id
                image
                rarity
                player {
                    id
                    name
                }
            }
            captain {
                id
            }
            score
            account {
                name
            }
        }
    }
}
"""
