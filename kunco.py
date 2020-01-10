from telegram.error import NetworkError, Unauthorized
from time import sleep
import random
import logging
import telegram
import time


update_id = None


def main():
    global update_id
    bot = telegram.Bot('TOKEN')
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    while True:
        try:
            kuncobot(bot)
        except NetworkError:
            sleep(1)
        except Unauthorized:
            update_id += 1

def messages():
    random_messages = ['boğazım çok kötü',
               'akıntım var',
               'raporluyum ben çalışmıyorum bugün',
               'yemeğe kadar uzanayım',
               'uzanayım biraz',
               'çok yoruldum',
               'hastayım',
               'elektrikler gitti',
               'begüm orospusu',
               'yaprak orospusu',
               'calisiyom yarin :(',
               'sikiyim yarin is var',
               'erken kalkcam ben çok kalamam haberin olsun',
               'sikicem bu telegram desktop appini silecem yakında',
               'annem sebze yapmış',
               'gel sana kebap yedireyim',
               'gel sana döner yedireyim',
               'gel sana hamburger yedireyim',
               'edodayız gel',
               'çağdaş ne zaman geliyon',
               'çağdaş',
               'tuğçe',
               'çaço',
               'bi daha sticker atarsan engeli yersin',
               'dc gel orda konuşalım bu konuyu',
               'ben yemek yiyem bi',
               'hak mi bu kardesim',
               'benim bu yalanlara karnim tok',
               'iyice yalanci oldun',
               'o kadar yirtiyoz win icin yarrak basi veriyor',
               'kanka ea bu sana diyoruz paket boş iş diye dinlemiyosun',
               'modern tibbin olmadigi donemde dogsam 1 yasimi goremezmisim ben',
               'doktora gitcem yarin',
               'birazdan utanacaksin',
               'salaksin herhalde',
               'puahjaajja',
               'fatih terim mi sikti seni',
               'bilmiyosun sen bu yemek islerini konusma',
               'millet ronaldo dusurup durur bize gelene bak yazik',
               'roket atacaz cagdasla yemege kadar',
               'yapsaydin kardesim mallik varsa yapamiyon iste',
               'dc mi ?',
               'sus benim chatimi aglama duvarina cevirdin',
               'bi is de pürüzsüz geçsin aq',
               'sabah eleman mesaj attim sikicem belalarini artik',
               'kiralar belli yasam belli',
               'cok harcadim bu ay',
               'borcum var',
               'isten cikamam borcum var',
               'figur aldim',
               'doymadim ben',
               'bi tane daha olsa yerim',
               'eve geciyorum birazdan',
               'annemler yemeğe bekliyor',
               'babama maçı ayarlıcam',
               "7'de evde olmam lazim",
        ]
    return random.choice(random_messages)

def kuncobot(bot):
    global update_id
    for update in bot.get_updates(offset=update_id, timeout=10, limit=1):
        update_id = update.update_id + 1

        if update.message:
            secondstowait = random.randint(2,3)
            time.sleep(secondstowait)
            bot.send_message(update.message.chat_id,text = messages())



if __name__ == '__main__':
    main()