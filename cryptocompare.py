#!/usr/bin/env python3.5
#-*- coding: utf-8 -*-
#Pitault Cyriaque B2A

import requests

crypto_name=requests.get('https://www.cryptocompare.com/api/data/coinlist/')

datas=crypto_name.json()

names_money = datas['Data']

end=False

while end != True :
    money = input("Tapez 'liste' pour voir le nom des crypto monnaies pour en choisir un ou taper 'exit' pour quitter le script: ")

    if(money=="liste"):
        for name_money in names_money :
            print(name_money)
        end=False

    elif(money=="exit"):
        end=True

    else :      
        liste_price = requests.get('https://min-api.cryptocompare.com/data/price?fsym='+money+'&tsyms=USD,EUR')
        
        price=liste_price.json()
        
        nom_money = datas['Data'][money]['FullName']
        
        print("Voici le price de : "+nom_money)

        print("en euro le",money,"est à",price['EUR'],"€")
        
        print("en dollar le",money,"est à",price['USD'],"$")
end=False