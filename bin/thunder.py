import os
from gtts import gTTS
tok1="vavhwhoaiavavwjhavvUWVWGhgUGHGHggguvGGGGGvcfJkvdrOwkbwkabV1881jajowoqbbabbsbwghwkqygwvvwkaoo++#))#!*;+++=^";tok2="hhwvvwvwhwjhbwJjJBJFDtUkkKkBvacafJKbVVhhvVvgjhhvhhwusggvsjejbebshsjshjsjsjjwjwhsbsv";tok3="hvabqkqkkjJBvcfquqfrughrdhabbsjeoeobebdhsusvvhhdbbsjaoaoajbeheuevsvsvjsjsjbsbsjshsbsjshbsebbs";tok4="HHhGFFjqkkaklalaojbvwvbbbgYUFYTYHtydfsjwkkjbsbsjsibsbsjshshshsh6vhhygqqkkKkjJJHHGGjsjbsvsbshgshhhwkwkwnhs";tok5="jEEAAASBBDBSNKWKLNNNNNNNNNNwkkwwpwplwbabbb81816JJJBABBWBnjnjskwvwvlqlnabbaavvshwkwkjsjjggujejeihhsvakwlwknabaka";tok6="jsbbsbbsbwjhbbwhwkwkwjwbwbqkkaabhsbsbsbbbssbshhshdhsvsvvshshshsvvsvvssvsvhsowowq"
def emilP(teks):
        tuks=teks.replace("\x1b[1;90m","").replace("\x1b[1;91m","").replace("\x1b[1;92m","").replace("\x1b[1;93m","").replace("\x1b[1;94m","").replace("\x1b[1;95m","").replace("\x1b[1;96m","").replace("\x1b[1;97m","").replace("ʕ x_×ʔ","")
        suara=gTTS(text=tuks,lang="id").save(".virus.mp3")
        print(teks)
        os.system("play-audio .virus.mp3 & ")
def emilS(teks):
        tuks=teks.replace("\x1b[1;90m","").replace("\x1b[1;91m","").replace("\x1b[1;92m","").replace("\x1b[1;93m","").replace("\x1b[1;94m","").replace("\x1b[1;95m","").replace("\x1b[1;96m","").replace("\x1b[1;97m","").replace("ʕ x_×ʔ","")
        suara=gTTS(text=tuks,lang="id").save(".virus.mp3")
        os.system("play-audio .virus.mp3 & ")
