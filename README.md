# Select and Send advanced Webex cards

This script allows you to select and send to a Webex room one example of an advanced webex cards located into the [**cards_attachements_examples**] subfolder

The file contained into this subfloder are only the **attachment** key of the Webex Card JSON data to be sent the the webex room. This key contains the body that is dispplayed into the message.

# Installation

## Step 0. Prerequisit

You must have created a webex bot first. If your bot is located into your laptop then use **ngork** to make it available on the INTERNET.

Have a look to the instructions here for that [Create a webex bot](https://github.com/pcardotatgit/Webex_Team_Chat_Bot_Python)

## Step 1. Create a working directory

Create a working directory into your laptop. Open a terminal CMD window into it. Name It XDR_BOT for example.

## Step 2. Copy the code into your laptop

The Download ZIP Method

The easiest way for anyone not familiar with git is to copy the ZIP package available for you in this page. Click on the Code button on the top right of this page. And then click on Download ZIP.

Unzip the zip file into your working directory.

The "git clone" method with git client

And here under for those of you who are familiar with Github.

You must have a git client installed into your laptop. Then you can type the following command from a terminal console opened into your working directory.

    git clone https://github.com/pcardotatgit/lab_simulator-001.git

## Step 3. Go to the code subfolder

Once the code unzipped into your laptop, then Go to the code subfolder.

## Step 4. Create a Python virtual environment

It is still a best practice to create a python virtual environment. Thank to this you will create a dedicated package with requested modules for this application.

### Create a virtual environment on Windows

    python -m venv venv 

### Create a virtual environment on Linux or Mac

    python3 -m venv venv

Depending on the python version you installed into your Mac you might have to type either 

- python -m venv venv

or maybe

- python3 -m venv venv    : python3 for python version 3.x  

or maybe 

- python3.9 -m venv venv  : if you use the 3.9 python version

And then move to the next step : Activate the virtual environment.

### Activate the virtual environment on Windows

    venv\Scripts\activate

### Activate the virtual environment on Linux or Mac

    source venv/bin/activate    

## Step 5. Install needed python modules

You can install them with the following 2 commands one after the other ( Windows / Mac / Linux ):

The following command might be required if your python version is old.

    python -m pip install --upgrade pip   

Then install required python modules ( Windows / Mac / Linux )

    pip install -r requirements.txt
    
## Configuration and prerequisit

1- You must have a valid **BOT_ACCESS_TOKEN**. That means that you must have created a Webex BOT first.
2- You must know the **room_id** of the destination webex room and the Webex Bot must be invited into it.

Then Edit the **config.py** file and set the correct values for the **DESTINATION_ROOM_ID** and **BOT_ACCESS_TOKEN**

## Run the script

Just run the script 

    python select_and_send_an_advanced_webex_card.py
    
The expected result is the selected card to be displayed into the Webex Room

## Where to go Next ? : Send an Alert Adaptative Card

Go to the next chapter in order to see an example of an advanced Alert Adaptative Card.

[webex_for_xdr_part-2_alert_cards_examples](https://github.com/pcardotatgit/webex_for_xdr_part-2_alert_cards_examples)

