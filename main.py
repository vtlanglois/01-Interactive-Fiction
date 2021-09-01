#!/usr/bin/env python3
import sys
import json
import os
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"

#Get all json filenames within the json folder
path_to_json_files = "json/"
json_files = [pos_json for pos_json in os.listdir(path_to_json_files) if pos_json.endswith('.json')]

response = ""
#Allow player to select json file
while True:
  if response in json_files:
    break
  print("Select a Game File:")
  print(json_files)
  response = input()  
response = "json/"+response
file = open(response, )
world = json.load(file)

current = world["passages"][0]["name"]
response = ""
while True:
    # Find passage (update)
    current_location = {}
    # Go thru all passages, find neccessary passage
    for passage in world["passages"]:
      if passage["name"] == current:
        current_location = passage
        break
    # Display passage (render the world)
    print("\n" + current_location["name"] + " - " + current_location["cleanText"])
    # Print all passage links
    for link in current_location["links"]:
      print(link["linkText"] + " - " + link["passageName"])
    # Ask for response (get input)
    response = input("\nWhere do you want to go? ")
    if response == "quit":
        break
    # Check if passage link exists in current passage; else redo loop
    for link in current_location["links"]:
      if(response == link["linkText"] ):
        current = link["passageName"]
        break
    else:
      print("Option not found")

