#!/usr/bin/python3.4

import requests
from mtgsdk import Card
import PySimpleGUI as sg
#bailey
sg.theme('DarkTeal2')

layout = [  [sg.Text('Filename as .txt')],
            [sg.Input(key = '-FILE-'), sg.FileBrowse()],            
            [sg.Button('Submit'), sg.Button('Exit')]]

window = sg.Window('Deck Price', layout, grab_anywhere = True)

def cardNameAndPrices():
    
#willson
    total=0

    decklist = open(deck_txt,'r') #changed variable to read selected .txt file
    pricelist = open('deck_prices.txt','w')

    card_names = decklist.readlines()

    for card_name in card_names:
        card_name = str(card_name.strip())
        cards = Card.where(name=card_name).all()

        mids = [None] * (len(cards))
        prices = [None] * (len(cards))

        for i in range(len(cards)):
            mids[i] = cards[i].__dict__["multiverse_id"]

        filtered_mids = list(filter(None,mids))
        mids = filtered_mids

        for i in range(len(mids)):
            r = requests.get('https://api.scryfall.com/cards/multiverse/{}'.format(mids[i]))
            while r.status_code != 200:
                r = requests.get('https://api.scryfall.com/cards/multiverse/{}'.format(mids[i]))
            rjson = r.json()
            all_prices = rjson["prices"]
            usd = all_prices["usd"]
            prices[i] = usd

        filtered_prices = list(filter(None,prices))
        if len(filtered_prices) == 0:
            lowest = "not found"
        else:
            lowest = min(map(float, filtered_prices))
            total += lowest
        price_info = "{},{}".format(card_name.strip(), lowest)
        pricelist.write(price_info)
        #print(price_info)
#bailey
    pricelist.close()
    price = open('deck_prices.txt', 'r')
    final_price = price.read()
    sg.PopupNonBlocking(final_price, total) 

    pricelist.close()
    decklist.close()

while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    if event in 'Submit':
        deck_txt = (values['-FILE-'])
        cardNameAndPrices()
        
        
        
        
        #print(total)

window.close()
