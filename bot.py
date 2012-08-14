#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 23:57:17 2012

@author: jokame
"""

import time
import tweepy

consumer_key=""
consumer_secret=""
access_token=""
access_token_secret=""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

ids=[]

while True:
    busq = api.search(q=u'"¿Qué hora es?"', result_type='recent',
                      show_user=True, include_entities=False)

    if not len(busq) > 0:
        print "No hay menciones"
        
    for b in busq:
        mens=b.text.replace(u"¿Qué hora es?","")
        print b.text
        if mens == "":
            if b.id not in ids:
                hora = time.asctime()[11:20]
                tuit = 'Oye, @%s, aquí, en el D.F., la hora es: %s' %(b.from_user, hora)
                print tuit
#                api.update_status(tuit)
                ids.append(b.id)
                
    print api.rate_limit_status()['remaining_hits'], "***************\n\n"
    time.sleep(30)
