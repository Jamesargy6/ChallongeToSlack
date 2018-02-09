import challonge


def init(username, apiKey):
	challonge.set_credentials(username, apiKey)




def buildParticipantDict(tournamentId):
	rawParticipants = challonge.participants.index(tournamentId)
	participants = {}

	for rawP in rawParticipants:
		newP = 	{
					"name" : rawP["name"]
				}
		participants[rawP["id"]] = newP

	return participants


def buildMatchDict(tournamentId):
	rawMatches = challonge.matches.index(tournamentId)
	matches = {}

	for rawM in rawMatches:
		newM = 	{
					"winner-id" : rawM["winner-id"],
					"loser-id" : rawM["loser-id"],
					"state" : rawM["state"],
					"score" : rawM["scores-csv"]
				}
		matches[rawM["id"]] = newM

	return matches



def getTournament(tournamentId):
	# Retrieve a tournament by its id (or its url).
	return challonge.tournaments.show(tournamentId)
