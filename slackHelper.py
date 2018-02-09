import requests


def sendTextToSlack(config, message):
	r = requests.post(config["SLACK_URL"], data='{"text": "' +message+ '"}')
	print(r.status_code, r.reason)
	print(r.text[:300])