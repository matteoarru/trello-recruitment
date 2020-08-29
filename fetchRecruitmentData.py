#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Wed May  6 08:55:55 2020

@author: matteoarru
"""
from trello import TrelloClient
from trello import Board

import json

def getRecruitmentBoard(configurationFileName='api.json'):
    api={}

    # In[1]:
    with open(configurationFileName) as json_file:
        api = json.load(json_file)
    # In[2]:

    client = TrelloClient(
        api_key=api["api_key"],
        api_secret=api["api_secret"],
        token=api["token"]
    )
    all_boards = client.list_boards()
    last_board = all_boards[-1]
    recruitment =  Board()
    for  board in all_boards:
        if board.name==api["recruitment_board_name"]:
            recruitment=board
    print(recruitment.name)
    return recruitment
recruitment=getRecruitmentBoard()
all_lists = recruitment.all_lists()

def showLabel():
    for label in card.labels:
        print ("label: "+label.name)

for list_id in all_lists:
    print("Swimlane: "+list_id.name)
    for card in list_id.list_cards():
        print("card: "+card.name)
        showLabel()
