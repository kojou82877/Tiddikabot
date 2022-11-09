from fbchat import Client, log, _graphql
from fbchat.models import *
import json
import random
import wolframalpha
import requests
import time
import math
import sqlite3
from bs4 import BeautifulSoup
import os
import concurrent.futures
from difflib import SequenceMatcher, get_close_matches



class ChatBot(Client):

    def onMessage(self, mid=None, author_id=None, message_object=None, thread_id=None, thread_type=ThreadType.USER, **kwargs):
        try:
            msg = str(message_object).split(",")[15][14:-1]

            if ("//video.xx.fbcdn" in msg):
                msg = msg

            else:
                msg = str(message_object).split(",")[19][20:-1]
        except:
            try:
                msg = (message_object.text).lower()
                print(msg)
            except:
                pass
        def sendMsg():
            if (author_id != self.uid):
                self.send(Message(text=reply), thread_id=thread_id,
                          thread_type=thread_type)

        def sendQuery():
            self.send(Message(text=reply), thread_id=thread_id,
                      thread_type=thread_type)
        if(author_id == self.uid):
            pass
        else:
            try:
                conn = sqlite3.connect("messages.db")
                c = conn.cursor()
                c.execute("""
                CREATE TABLE IF NOT EXISTS "{}" (
                    mid text PRIMARY KEY,
                    message text NOT NULL
                );
                """.format(str(author_id).replace('"', '""')))

                c.execute("""
                INSERT INTO "{}" VALUES (?, ?)
                """.format(str(author_id).replace('"', '""')), (str(mid), msg))
                conn.commit()
                conn.close()
            except:
                pass
       
        try:
            if("search pdfiiixxd" in msg):
                searchFiles(self)
            elif "weakojouther okojouf" in msg:
                indx = msg.index("weathkojouer okojouf")
                query = msg[indx+11:]
                reply = weather(query)
                sendQuery()

            elif("mkojouute convekojoursation" in msg):
                try:
                    self.muteThread(mute_time=-1, thread_id=author_id)
                    reply = "xd 🔕"
                    sendQuery()
                except:
                    pass

            elif ("😶" in msg):
                time.sleep(60)
                reply = "[ Y0UR B!G D9D))Y K9IZ3N 09 FIIR3 <<(( (Y) ))>> 9LL KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                time.sleep(60)
                reply = "(Y) <3 ::((- Woh____(^^) (Y) -)) <3 Meri Sab :v Kuchh <3 Hai Par ;-) Muqaddar ^_^ Nahi,______(Y) :^) Kaash-Wo (Y) Meri >.< Kuchh__Na Hoti ^_^ Par-Muqaddar :) Hoti <3 (N)_____(*_*) :P ~~ (Y) :-D ((- 3:) #Kamlash 3:) -)) <3 ((- 0n -)) ^_^ = Fire (Y)"
                sendMsg()
                time.sleep(60)
                reply = "(Y) ((- 3:)  -)) (Y) :P <3 (^^^)_____((- <3 (^^) (Y)  - ^_^ (^^^) ((- K-4-M-L-3-S-H -)) (Y) :/ :P ((- H'-3'-R'-3 -)) (Y) ;/ :P (('- J'-U'-S'-T -')) <3 ~ N'-0'-N ~ 3:) (('- S'-T'-0'-P ')) "
                sendMsg()
                time.sleep(60)
                reply = "(((????????((((((((+)))))))))????????))^^^) (^^^) 3:) 3:) Y_0UR(^^^^^) (^^^^^) D_9D <3 :] <3 3:) 3:) 3:) (Y) O.o O.o :] :] =D =D (^^^) (^^^) (^^^^^) (^^^^^) (^|^|^|^|^|^|^|^|^|^|^|^|^) #UNB39T9BL3 =D :V :V (Y) (Y) #F9DD3B99ZZ (^^^) =D 3:) 3:) #K9ML35HH _H3R3 <()"
                sendMsg()
                time.sleep(60)
                reply = "Jab Milo Kisi Se <3 :) :) ________) To Jara Door Ka Rishta Rakhna :) <3 <3_______{{'Bahut Tadpaate Hain Aksar Seene Se Lagaane Waale-'}} (^^^) (^^^) (^^^) (^^^)]||!___) <33 ]> <3 (y) [[#Unstoppable_KamLesh_Here]] O_O"
                sendMsg()
                time.sleep(60)
                reply = "[[ :) ' #T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_K9ML35H 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( K9ML35H H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=K9ML35H'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH4NGI RUL3X K3 B4R3 M3 B44T K4RT3 HX 😃 1.GHANSYAM = Y3 APNII MA KI CHU7 BHII NIIL4M K4RD3G4 IDH K3 LIIY3 😃 2.ABHISHEK UF EKARAM = ISKI MA K0 J0 LUND D3G4 USKII SID3 S3 FIGHT K4R3G4 😃 PIC ABUS3 + GOD ABUS3 + AUTO REPLY K3 ALAWA KHUCH NHII J4NT4 😃 3.SHIVAY + SHERYANSH = INKI MA KI CHUT 😃 Y3 D0N0 APNII HII RUL3X G4LII D3 D3 G3 J4B UNKI M4 CHUDJ4TI H3 T4B 😃 KHUD B0LD3 IDH KII M4 K4 B0XD4 😃 INKI MA KO SHIF PIC OUR GOD ABUS3 OUR BHOKN4 AT4 H3 SHIF 😃 INKI MA BHII KH3T3 HOGII M3R3 P3T M3 S3 AY3 H3 Y3 KY4 H0SPITAL M3 KISII OUR R4NDII K3 B4CH3 M3R3 K0 D3DIY3 😃 4.PARVIIN = H4 Y3 T0 KHUD APNII M4 L4DKIY0 S3 CHUDW4T4 H3 😃 5.MANIISH = KHUD K0 L3GEND KII JH4TH S4MJT4 H3 L4KIIN ISK0 KHU9 K0 P4T4 H3 KII W0 M3RII JH4TH H3 😃 6.GABAR = H4 Y3 B4TT3L PIL4 H3 ISKI M4 CH0DN4 H3 T0 CH0D S4KT3 H0 1 YA 2 DIN T4K HII TIK3G4 😃 7 = DEEP = H4 Y3 BHII 3K R4NDII K4 B3T4 H3 😃 ISKI M4 KI CHU7 K3 H34RT H3 W0 BBHII D34TH H3 OUR BHII KHUCH PIL3 H3 USK4 N4M3 Y44D NHII H3 😃 H4 INKII M4 KITN4 BHII XH0DLO HAAR M4N3G3 HII NHII J4B T4K INKII M4 M4RK K3 N4RK NHII J4TII T4B T4K 😃"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGIIY0 KA GANG HERE ( IDH BHANGI GANG ON FIRE ) IDH BHANGISS GANG HERE ( IDH BHANGI KATORA LEKE BHIKH LENE WALE BHANGI GANG HERE ) BHANGISS  IDH KE SAARE BHANGI GANG K BHANGI HERE"
                sendMsg()
                



        except Exception as e:
            print(e)

        self.markAsDelivered(author_id, thread_id)

    def onMessageUnsent(self, mid=None, author_id=None, thread_id=None, thread_type=None, ts=None, msg=None):

        if(author_id == self.uid):
            pass
        else:
            try:
                conn = sqlite3.connect("messages.db")
                c = conn.cursor()
                c.execute("""
                SELECT * FROM "{}" WHERE mid = "{}"
                """.format(str(author_id).replace('"', '""'), mid.replace('"', '""')))

                fetched_msg = c.fetchall()
                conn.commit()
                conn.close()
                unsent_msg = fetched_msg[0][1]

                if("//video.xx.fbcdn" in unsent_msg):

                    if(thread_type == ThreadType.USER):
                        
                        self.send(Message(text=reply), thread_id=thread_id,
                                  thread_type=thread_type)
                        self.sendRemoteFiles(
                            file_urls=unsent_msg, message=None, thread_id=thread_id, thread_type=ThreadType.USER)
                    elif(thread_type == ThreadType.GROUP):
                        user = self.fetchUserInfo(f"{author_id}")[
                            f"{author_id}"]
                        username = user.name.split()[0]
                        #reply = f"{username} just unsent a video"
                        self.send(Message(text=reply), thread_id=thread_id,
                                  thread_type=thread_type)
                        self.sendRemoteFiles(
                            file_urls=unsent_msg, message=None, thread_id=thread_id, thread_type=ThreadType.GROUP)
                elif("//scontent.xx.fbc" in unsent_msg):

                    if(thread_type == ThreadType.USER):
                        
                        self.send(Message(text=reply), thread_id=thread_id,
                                  thread_type=thread_type)
                        self.sendRemoteFiles(
                            file_urls=unsent_msg, message=None, thread_id=thread_id, thread_type=ThreadType.USER)
                    elif(thread_type == ThreadType.GROUP):
                        user = self.fetchUserInfo(f"{author_id}")[
                            f"{author_id}"]
                        username = user.name.split()[0]
                        #reply = f"{username} just unsent an image"
                        self.send(Message(text=reply), thread_id=thread_id,
                                  thread_type=thread_type)
                        self.sendRemoteFiles(
                            file_urls=unsent_msg, message=None, thread_id=thread_id, thread_type=ThreadType.GROUP)

            except:
                pass


cookies = {
    "sb": "xasyYmAoy1tRpMGYvLxgkHBF",
    "fr": "0NxayJuewRHQ30OX3.AWVJwIYNh0Tt8AJv6kSwDamhkoM.BiMrVd.Iu.AAA.0.0.BiMtVZ.AWXMVaiHrpQ",
    "c_user": "100082541032800",
    "datr": "xasyYs51GC0Lq5H5lvXTl5zA",
    "xs": "31%3ABiM4za474tBPCQ%3A2%3A1668008118%3A-1%3A7715"
}


client = ChatBot("",
                 "", session_cookies=cookies)
print(client.isLoggedIn())

try:
    client.listen()
except:
    time.sleep(3)
    client.listen()
