#!/usr/bin/env python3
import sys
import json
import os
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"


# ----------------------------------------------------------------

def select_game():
  #Get all json filenames within the json folder
  path_to_json_files = "json/"
  json_files = [pos_json for pos_json in os.listdir(path_to_json_files) if pos_json.endswith('.json')]
  json_files = [json_file.replace(".json", "") for json_file in json_files]
  response = ""
  #Allow player to select json file
  while True:
    if response in json_files:
      break
    print("You have the following Game Paks:")
    print(json_files)
    print("Select a Game Pak:")
    response = input()  
  #get the file, create a world, return the world
  response = "json/"+response+".json"
  file = open(response, )
  world = json.load(file)
  return world


# ----------------------------------------------------------------

def find_current_location(location_label):
	if "passages" in world:
		for passage in world["passages"]:
			if location_label == passage["name"]:
				return passage
	return {}

# ----------------------------------------------------------------

def render(current_location, score, moves):
  if "name" in current_location and "cleanText" in current_location:
	 # Display passage (render the world)
    print("Moves: " + str(moves) + " | Score: " + str(score))
    print("\n" + current_location["name"] + " - " + current_location["cleanText"])
    # Print all passage links
    for link in current_location["links"]:
      print(" ->" + link["linkText"] + " - " + link["passageName"])
    

def get_input():
	response = input("Enter option: ")
	return response.upper().strip()

def update(current_location, location_label, response):
  #if there is no response, return location_label argument
	if response == "":
		return location_label
  # see if there are links in the current_location
	if "links" in current_location:
    #for each link, see if response matches a link
	  for link in current_location["links"]:
		  if(response == link["linkText"]):
			  return link["passageName"]
	else:
		print("Option not found.")
		return location_label


# ----------------------------------------------------------------

world = select_game()
location_label = world["passages"][0]["name"]
current_location = {}
response = ""
score = 0
moves = 0

while True:
  if response == "QUIT":
    break
  if "score" in current_location:
    score+=current_location["score"]
  location_label = update(current_location, location_label, response)
  current_location = find_current_location(location_label)
  render(current_location, score, moves)
  response = get_input()
  moves+=1

print("Thank you for playing!")
   

