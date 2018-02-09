# ChallongeToSlack

ChallongeToSlack is a super-minimal slack app, which announces Tournament Bracket match results (hosted at challonge.com) and posts them to a slack channel.

Setup is as easy as filling in the four values in the `config.json` file:
```
{
	"CHALLONGE_USER" : "",
	"CHALLONGE_API_KEY" : "",

	"CHALLONGE_TOURNAMENT_ID" : "",

	"SLACK_URL" : ""
}
```
All you need to do to kick off the bot is to run the python file `challongeScraper.py`. 

*NOTE:* make sure that the matchId array in `completedMatches.json` is emptied before running the file for a new tournament.
