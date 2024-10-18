
__author__ = 'Vadim Arsenev'
__version__ = '1.0.1'
__data__ = '18.10.2024'


API_URL = 'https://app.fan-ton.com/graphql'

# ID Tournaments (list of cards)
# EPL
RARITIES = 'COMMON'
LIST_CARDS = 'itFgHRn0z8Bf3bO9fZTbup2Z'

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

BODY_CARDS = \
"""
query getCards($myOwn: Boolean, $name: String, $tournaments: [ID!], $teams: [ID!], $positions: [PlayerPosition!], $citizenship: [String!], $rarities: [Rarity!], $tiers: [Int!], $games: [ID!], $userTeams: [ID!], $first: Int = 3, $after: Cursor, $excludedCards: [ID!], $isOnSale: Boolean, $isAtAuction: Boolean, $price: MoneyRangeInput, $orderBy: CardOrder, $goalsAvg: IntRangeInput, $goalsLast5: IntRangeInput, $assistsAvg: IntRangeInput, $assistsLast5: IntRangeInput, $minutesPlayedAvg: IntRangeInput, $minutesPlayedLast5: IntRangeInput, $cleanSheetsAvg: IntRangeInput, $cleanSheetsLast5: IntRangeInput, $isFree: Boolean) {
  cards(
    myOwn: $myOwn
    name: $name
    tournaments: $tournaments
    teams: $teams
    positions: $positions
    citizenship: $citizenship
    rarities: $rarities
    tiers: $tiers
    games: $games
    userTeams: $userTeams
    first: $first
    after: $after
    excludedCards: $excludedCards
    isOnSale: $isOnSale
    isAtAuction: $isAtAuction
    price: $price
    orderBy: $orderBy
    goalsAvg: $goalsAvg
    goalsLast5: $goalsLast5
    assistsAvg: $assistsAvg
    assistsLast5: $assistsLast5
    minutesPlayedAvg: $minutesPlayedAvg
    minutesPlayedLast5: $minutesPlayedLast5
    cleanSheetsAvg: $cleanSheetsAvg
    cleanSheetsLast5: $cleanSheetsLast5
    isFree: $isFree
  ) {
    edges {
      node {
        id
        rarity
        player {
          id
          name(locale: EN)
          teamIds
        }
      }
    }
  }
}
"""