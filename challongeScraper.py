import fileHelper, slackHelper, challongeHelper
import requests, schedule, time

def generateMatchAnnouncements():
	print("parsing...")
	config = fileHelper.loadJsonFile("config.json", "r")
	challongeHelper.init(config["CHALLONGE_USER"], config["CHALLONGE_API_KEY"])

	tournamentInfo = challongeHelper.getTournament(config["CHALLONGE_TOURNAMENT_ID"])
	participantDict = challongeHelper.buildParticipantDict(config["CHALLONGE_TOURNAMENT_ID"])
	matchDict = challongeHelper.buildMatchDict(config["CHALLONGE_TOURNAMENT_ID"])

	completedMatches = fileHelper.loadJsonFile("completedMatches.json", "r")
	matchIds = completedMatches["matchIds"]
	for m in matchDict:
		if m not in matchIds:
			match = matchDict[m]
			if match["state"] == "complete":
				winner, loser  = "", ""

				for p in participantDict:
					if p == match["winner-id"]:
						winner = participantDict[p]["name"]
					elif p == match["loser-id"]:
						loser = participantDict[p]["name"]

				slackHelper.sendTextToSlack(config, "MATCH ANNOUNCEMENT ({0}): {1} has beaten {2} by a score of {3}".format(tournamentInfo["name"], winner, loser, match["score"]))
				matchIds.append(m)
	completedMatches["matchIds"] = matchIds
	fileHelper.dumpJson("completedMatches.json", completedMatches)




schedule.every(10).seconds.do(generateMatchAnnouncements)

while True:
    schedule.run_pending()
    time.sleep(1)


