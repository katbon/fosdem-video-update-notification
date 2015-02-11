# Katherine Bonsell / katbon
# 2015.2.11

"""
fosdem-video-update-notification Version 1

This script scrapes the given URL once every hour until it no longer returns a 
status code of 404. It then sends a text message containing the URL and a 
description to a specified recipient using Twilio.
"""
import requests
import time
from twilio.rest import TwilioRestClient

url = 'http://video.fosdem.org/2015/'

account_sid = "{{ account_sid }}"
auth_token = "{{ auth_token }}"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body=(url, "Index of /2015"),
	to="{{ recipient }}",
	from_="{{ sender }}")

while True:
	req = requests.get(url)

	if req.status_code != 404:
		print message.sid
		break
		
	time.sleep(3600)