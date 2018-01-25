import tweepy
import swapi
from secrets import *
from random import randint

auth = tweepy.OAuthHandler(C_KEY, C_SECRET)  
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)  
api = tweepy.API(auth)
#Get planet from SWAPI
planet = swapi.get_planet(randint(1, 61))
tweet = "Planet\nName: " + planet.name+"\nRotation Period: "+planet.rotation_period+"\nOrbital Period: "+planet.orbital_period+"\nDiameter: "+planet.diameter+"\nClimate:"+planet.climate+"\nGravity: "+planet.gravity+"\nTerrain: "+planet.terrain+"\nSurface_water:" +planet.surface_water+"\nPopulation:" +planet.population+"\nby: SWAPI -> https://swapi.co/"
api.update_status(tweet)