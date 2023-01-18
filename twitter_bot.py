import os
import time
from main import *
from colorama import *
import tweepy as tw
from dados import api_key, api_sec_key, main_token, main_token_sec, b_token, my_id
auth = tw.OAuthHandler(api_key, api_sec_key)
auth.set_access_token(main_token, main_token_sec)
bot = tw.Client(consumer_key=api_key, consumer_secret=api_sec_key, access_token=main_token, access_token_secret=main_token_sec, bearer_token=b_token)
api = tw.API(auth)
name = dict(api.get_settings()).get('screen_name')


def cor(var):
    if var == 'info':
        print(Fore.BLUE + f'[INFO]', end='')
    elif var == 'erro':
        print(Fore.RED + f'[ERROR]', end='')
    elif var == 'check':
        print(Fore.GREEN + f'[SUCESS]', end='')
    a = Style.RESET_ALL
    return a


def tw_post(texto: str):
    bot.create_tweet(text = texto)


def tw_ids(tw_id = None, get = False):
    if tw_id is None: get = True
    if not get:
        with open('lib/ids_tw', 'a') as f:
            f.writelines(str(tw_id) + '\n')
    else:
        with open('lib/ids_tw', 'r') as f:
            old_ids = f.readlines()
            for index in range(len(old_ids)):
                old_ids[index] = old_ids[index].replace('\n', '')
            return old_ids


def get_tw_info(usuario: str):
    try:
        user = api.get_user(screen_name=usuario.replace('@', ''))
        user = user._json
        text = f'Nome: {user["name"]}\n' \
               f'Usuário: {user["screen_name"]}\n' \
               f'ID do usuário: {user["id"]}\n' \
               f'Descrição: {user["description"]}\n' \
               f'Localização: {user["location"]}\n' \
               f'Seguidores: {user["followers_count"]}\n' \
               f'Seguindo: {user["friends_count"]}\n' \
               f'Criado em: {user["created_at"]}\n' \
               f'Número tweets curtidos: {user["favourites_count"]}\n' \
               f'Números de tweets: {user["statuses_count"]}\n' \
               f'Usuário {"não" if user["verified"] == False else ""} verificado\n' \
               f'Twitter {"não" if user["protected"] == False else ""} protegido\n'
        return text
    except Exception:
        return 'Error'

def check_tw_new():
    try:
        mentions = api.mentions_timeline()[0]
        old_ids = tw_ids()
        if not str(mentions._json['id']) in old_ids:
            id_tw = mentions._json['in_reply_to_status_id']
            name_tw = mentions._json['in_reply_to_screen_name']
            tw_link = f'https://twitter.com/{name_tw}/status/{id_tw}'
            os.system(f'youtube-dl -o src/video.mp4 --retries 3 {tw_link}')
            click_conv(1)
            send_media()
            sair(3)
            tw_ids(mentions._json['id'])
    except Exception as e:
        print(cor('erro')+f'Erro ao conferir novos tweets.\n{e}')