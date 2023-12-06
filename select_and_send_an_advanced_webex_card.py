'''
    Read an Webex Card Attachment JSON file located into the [ cards_attachements_examples } subfolder and send it into 
    a webex room
'''
import requests
import sys, os
import config  as conf
from crayons import *
import json

ROOM_ID=conf.DESTINATION_ROOM_ID
ACCESS_TOKEN=conf.BOT_ACCESS_TOKEN
version=conf.version
URL = 'https://webexapis.com/v1/messages'


def read_webex_card(json_file): 
    data_list=[]
    data_dict={}  
    index=0
    file='./cards_attachements_examples/'+json_file
    with open(file,'r') as file:
        text_data=file.read()
        json_data=json.loads(text_data)    
    print(yellow(json_data,bold=True))
    return(json_data)

def load_card_and_send_it(json_file):
    headers = {'Authorization': 'Bearer ' + ACCESS_TOKEN,
               'Content-type': 'application/json;charset=utf-8'}
    cards_content=read_webex_card(json_file)
    print(red(cards_content))
    attachment={
    "roomId": ROOM_ID,
    "markdown": "Infection Alert !",
    "attachments": cards_content
    }
    response = requests.post(URL, json=attachment,headers=headers)
    if response.status_code == 200:
        # Great your message was posted!
        #message_id = response.json['id']
        #message_text = response.json['text']
        print("New message created")
        #print(message_text)
        print("====================")
        print(response)
    else:
        # Oops something went wrong...  Better do something about it.
        print(response.status_code, response.text)
    
if __name__=="__main__":
    files =[file for file in os.listdir('./cards_attachements_examples')]
    index=0
    print()
    print("Select a card here under by it s index :")
    print()
    for file in files:
        if '.json' in file:
            print(cyan(f'{index}- ',bold=True),yellow(file,bold=True))
            index+=1
    print()
    card_index=input(green('which card do you want to send ? : ',bold=True))
    print(red(files[int(card_index)]))
    load_card_and_send_it(files[int(card_index)])