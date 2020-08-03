#!/bin/python

# To run, you will need to install python3 as well as pandas. 
# you can install pandas with pip (or pip3) with the following
# command:  ` python -m pip install pandas `

import os
import numpy as np
import pandas as pd
import csv
import argparse

parser = argparse.ArgumentParser(description="Winterspring Ski Team Bonus EP Calculator!", formatter_class=argparse.RawTextHelpFormatter)

def dir_path(path):
    if os.path.isfile(path):
        return path
    else:
        raise argparse.ArgumentTypeError(f"readable_dir:{path} is not a valid path")

parser.add_argument("-path", type=dir_path, help="The path to the WoWCombatLog.txt file to be parsed. Careful, these files can be pretty big! If you don't know where this is, its probably near where you put your addons folder like C:\\\Program Files\\World Of Wacraft\\_classic_\\Logs\\WowCombatLogs.txt")

args = vars(parser.parse_args())

# The assumption here is that if you went to get
# the DMT buffs, you got the HP buff and that counts
# as one world buff slot
world_buffs = [
    "Rallying Cry of the Dragonslayer", 
    #"Fengus\' Ferocity", 
    "Spirit of Zandalar",
    "Mol\'dar\'s Moxie", 
    "Songflower Serenade", 
    #"Slip\'kik\'s Savvy",
    "Warchief\'s Blessing",
]


# If there are other consumables missing, add them to the list
# surrounded with double quotes. If there is an apostrophe, as 
# in "Mol'dar's Moxie" you will need to put a backslash before each
# occurance  as so: "Mol\'dar\'s Moxie", 
consumables = [
    "Spirit of Zanza", 
    "Greater Armor", 
    "Greater Stoneshield", 
    "Greater Arcane Elixir", 
    "Winterfall Firewater", 
    "Elixir of the Mongoose", 
    "Elixir of the Giants", 
    "Greater Agility", 
    "Flask of the Titans", 
    "Flask of Supreme Power", 
    "Flask of Distilled Wisdom"
    "Greater Nature Protection Potion",
    "Nature Protection Potion",
    "Greater Fire Protection Potion"
]

with open (args['path']) as infile:
    reader = csv.reader(infile)
    title = next(reader)
    headers = next(reader)

header_indices = [i for i, item in enumerate(headers) if item]

df = pd.read_csv(args['path'], usecols=[6, 10], skiprows=[0,1])

hero_consumables = {}
hero_world_buffs = {}

# iterate over the dataframes and check if the the buff is something
# of interest, if it is, mark who has the buff by adding it map of 
#       char_name -> { set of buffs }
# 
# For consumes we make a different map of 
#       char_name => { buff_name -> count }
#
# This produces information about how many of a certain type of consume
# were used and not just which ones were used

for index, row in df.iterrows():
    if(row[1] in consumables):

        if (row[0] not in hero_consumables):
            hero_consumables[row[0]] = {}
            
        if row[1] not in hero_consumables[row[0]]: 
            hero_consumables[row[0]][row[1]] = 0
        hero_consumables[row[0]][row[1]] += 1

    elif (row[1] in world_buffs):
        if (row[0] not in hero_world_buffs):
            hero_world_buffs[row[0]] = {}

        if row[1] not in hero_world_buffs[row[0]]: 
            hero_world_buffs[row[0]][row[1]] = True

    
#for name, buffs in hero_world_buffs.items():
#    if (len(buffs) >= 1):
#        print (name + " gets bonus ep for world buffs!")

world_buffs_out = pd.DataFrame(hero_world_buffs)
world_buffs_out.to_csv('wbuffs.csv')

consumes_out = pd.DataFrame(hero_consumables)
consumes_out.to_csv('consumes.csv')

#with open('world_buffs.csv', 'w') as csvfile:
#    writer = csv.DictWriter(csvfile, fieldnames = world_buffs)
#    writer.writeheader()
#    writer.writerows(hero_world_buffs.values())

