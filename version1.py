# Katherine Bonsell / katbon
# 2015.2.16

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

while True:
	resp = requests.get(url)

	if resp.status_code != 404:
		message = client.messages.create(body=(url + " Index of /2015"),
			to="{{ recipient }}",
			from_="{{ sender }}")
		print message.sid
		break
		
	time.sleep(3600)