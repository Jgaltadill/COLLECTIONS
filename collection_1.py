#################################
#
#Author: Jordi Garcia Altadill
#Date: 07-02-2020
#
#Modified on 17-03-2020
#
#Script that obtain the GitHub Score for a single user
#
#################################
import requests
import json


#Function that returns an array with the points per event
def obtain_points(event):

	points = 0	

	#Obtain the event type from each element.
	event_type = event["type"];

	if (event_type == "PushEvent"):
		points = 5;				
	elif (event_type == "CreateEvent"):
		points =4
	elif (event_type == "IssuesEvent"):
		points =3
	elif (event_type == "CommitCommentEvent"):
		points = 2
	else:
		points = 1

	return points;

#Url to obtain the JSON from GitHub
url = 'https://api.github.com/users/badchoice/events'

user_activity = requests.get(url=url).json()


score = sum(map(obtain_points,user_activity))

print "The user GitHub score is: "+ str(score)







