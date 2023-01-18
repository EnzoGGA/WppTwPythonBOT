# MENSAGEM

def comando_atual(num_conv, desativado, lista_msgs, lista_num_adm, prefix, msg):
    tem_prefixo = conferir_prefixo(msg, prefix)
    is_img, legenda = conferir_img(num_conv)
    if not is_img:
        if tem_prefixo:
            msg_total = msg
            msg = msg.lower().split(" ")[0].replace(prefix, '')
            arg = coletar_arg(msg_total)
            print(f'{cor("info")}Comando "{msg}" detectado!')
            if msg == 'menu':
                if desativado: send_msg(lista_msgs[0]); sair(2); return
                menu_msg = arquivos.ler_escrever(prefix, 'menu')
                send_msg(menu_msg)
            elif msg == 'conv':
                send_msg('Número da conversa no chat: '+ str(num_conv))
            elif msg in ["desativar", "off"]:
                nome, numero = coletas()
                if not conferir_login(numero): send_msg(lista_msgs[2]); sair(2); return
                if desativado: send_msg("Já desativado"); return
                send_msg("Bot desativado!")
                mud_desc(f'Bot desligado, tente novamente mais tarde com "{prefix}menu"')
                desativar_ativar(desativado=True)
            elif msg in ["ativar", "on"]:
                nome, numero = coletas()
                if not conferir_login(numero): send_msg(lista_msgs[2]); sair(2); return
                if not desativado: send_msg("Já ativo"); return
                send_msg("Bot ativado!")
                mud_desc(lista_msgs[3])
                desativar_ativar(desativado=False)
            elif msg in ['oi', 'opa', 'ola']:
                if desativado: send_msg(lista_msgs[0]); sair(2); return
                send_msg('Opa, bot on, Envie "menu" para ver a lista de comandos :)')
            elif msg == 'nome':
                nome, numero = coletas()
                if desativado: send_msg(lista_msgs[0]); sair(2); return
                send_msg(f'Olá {nome}, {numero}')
            elif msg == 'pergunta':
                if desativado: send_msg(lista_msgs[0]); sair(2); return
                msg = resposta()
                send_msg(msg)
            elif msg in ['prefixo', 'prefix']:
                nome, numero = coletas()
                if conferir_login(numero):
                    if not arg is None:
                        send_msg(f"Alterando prefixo '{prefix}'")
                        arquivos.ler_escrever(prefix, 'prefix', False, arg[0])
                        prefix = arquivos.ler_escrever(prefix, 'prefix')
                        send_msg(f"Prefixo alterado com sucesso para '{prefix}'")
                        mud_desc(lista_msgs[3])
                    else:
                        send_msg(lista_msgs[1])
                else:
                    send_msg(f"O prefixo é {prefix}")
            elif msg == 'diga':
                if desativado: send_msg(lista_msgs[0]); sair(2); return
                if not arg is None:
                    send_msg(arg)
                else:
                    send_msg(lista_msgs[1])
            elif msg == 'adm':
                nome, numero = coletas()
                if conferir_login(numero):
                    if not arg is None:
                        send_msg(f"Adicionando número {arg} na lista de administradores...")
                        arg = arg.replace("-", " ").replace("+", " ").replace(" ", "")
                        try:
                            int(arg)
                            lista_login = arquivos.ler_escrever(prefix, 'login')
                            if not arg in lista_login:
                                lista_login.append(arg)
                                arquivos.ler_escrever(prefix, 'login', False, lista_login)
                                send_msg("Sucesso!")
                            else:
                                send_msg(f"{arg} já é adiministrador!")
                        except Exception:
                            send_msg("Erro, digite um número valido!")
                    else:
                        send_msg(lista_msgs[1])
                else:
                    send_msg(lista_msgs[2])
            elif msg in ['dado', 'dados']:
                if desativado: send_msg(lista_msgs[0]); sair(2); return
                send_msg(str(random.randint(1, 6)))
            elif msg in ['conversar', 'conversa']:
                nome, numero = coletas()
                if desativado: send_msg(lista_msgs[0]); sair(2); return
                if arg == 'on' or arg == 'ligar' or arg == "1":
                    lista_simi_log = arquivos.ler_escrever(prefix, 'simi_login')
                    if not numero in lista_simi_log:
                        lista_simi_log.append(numero)
                        send_msg("Modo conversa ligado!")
                    else:
                        send_msg("Já ligado!")
                    arquivos.ler_escrever(prefix, 'simi_login', False, lista_simi_log)
                elif arg == 'off' or arg == 'desligar' or arg == "0":
                    lista_simi_log = arquivos.ler_escrever(prefix, 'simi_login')
                    try:
                        lista_simi_log.remove(numero)
                        send_msg("Modo conversa desligado!")
                    except Exception:
                        send_msg("Já desligado!")
                    arquivos.ler_escrever(prefix, 'simi_login', False, lista_simi_log)
                else:
                    send_msg(f"Mal uso do comando!\nUso: {prefix}conversa [1 para ligar e 0 para desligar]")
            elif msg == 'ts':
                nome, numero = coletas()
                if not conferir_login(numero): send_msg(lista_msgs[2]); sair(2); return
                if arg is None: send_msg(lista_msgs[1]); sair(2); return
                send_msg(f'Enviando transmissão "{arg}"...')
                ts_send(arg)
            elif msg == "sair":
                nome, numero = coletas()
                if not conferir_login(numero): send_msg(lista_msgs[2]); sair(2); return
                mud_desc(f'Bot desligado, tente novamente mais tarde com "{prefix}menu"')
                sair(1)
                time.sleep(1)
                exit()
            elif msg in ['tradutorpt', 'traduzirpt', 'translatept']:
                if arg is None: send_msg(lista_msgs[1]); sair(2); return
                send_msg(f"Traduzindo {arg} para pt-br")
                traducao, idioma = translate(arg, 'auto', 'pt')
                send_msg(
                    f'*Tradutor*\n\n*Texto original:* {arg} ({idioma.split("-")[0].lower().replace(" ", "")})\n*Texto traduzido para português:* {traducao}')
            elif msg == 'tradutoren' or msg == 'traduziren' or msg == 'translateen':
                send_msg(f"Traduzindo {arg} para ingles")
                traducao, idioma = translate(arg, 'auto', 'en')
                send_msg(
                    f'*Tradutor*\n\n*Texto original:* {arg} ({idioma.split("-")[0].lower().replace(" ", "")})\n*Texto traduzido para ingles:* {traducao}')
            elif msg in ['fig', 'img']:
                send_msg(lista_msgs[4])
            elif msg in ['pub', 'tweet', 'tweet']:
                nome, numero = coletas()
                if not conferir_login(numero): send_msg(lista_msgs[2]); sair(2); return
                if desativado: send_msg(lista_msgs[0]); sair(2); return
                try:
                    tw_post(arg)
                    send_msg("Tweet enviado com sucesso!")
                except Exception as e:
                    print(e)
                    send_msg("Erro ao enviar tweet")
            elif msg == 'twitter':
                if arg is None: send_msg(lista_msgs[1]); sair(2); return
                try:
                    text = get_tw_info(arg)
                    if text == 'Error': send_msg("Erro interno ou usuário não encontrado"); return
                    send_msg(text)
                except Exception as e:
                    send_msg("Error")
                    print(e)
            elif msg in ['admmsg', 'recado', 'sendadm']:
                if arg is None: send_msg(lista_msgs[1]); sair(2); return
                nome, numero = coletas()
                send_msg(f"Enviando {arg} para o administrador!")
                send_adm(lista_num_adm, f'Recado de {nome}\n'
                                        f'Mensagem: {arg}\n\n'
                                        f'*Dados*:\n'
                                        f'Nome do contato: {nome}\n'
                                        f'Número: {numero}\n'
                                        f'Nº da conversa: {num_conv}')
            elif msg in ['registrar', 'reg', 'register']:
                if arg is None: send_msg(lista_msgs[1]); sair(2); return
                numero = coletas()[1]
                try:
                    valores = arg.split('/')
                    ig = valores[0].replace('[', '').replace(']', '').replace(' ', '')
                    try:
                        senha = valores[1].strip(' ')
                    except IndexError:
                        senha = ''
                except Exception:
                    send_msg(lista_msgs[1])
                    sair(2)
                    return
                ig_num = literal_eval(arquivos.ler_semfiltro('ig_num'))
                ig_pass = literal_eval(arquivos.ler_semfiltro('ig_pass'))
                try:
                    num = ig_num[ig]
                    send_msg(f"O usuario {ig} ja tem um número registrado na nossa base de dados!\nIG: *{ig}*\nNúmero: *{num}*")
                    send_msg(f'Para mudar o numero use o comando {prefix}log [seu usuario aqui]/[sua senha aqui] que o bot fará o novo registro (Caso esqueça a senha entre em contato com o administrador do bot:\nhttps://wa.me/5561981316353')
                except KeyError:
                    ig_pass[ig] = senha
                    ig_num[ig] = numero
                    arquivos.ler_semfiltro('ig_num', ig_num, True)
                    arquivos.ler_semfiltro('ig_pass', ig_pass, True)
                    num = ig_num[ig]
                    send_msg(f'Usuario adicionado com sucesso na base de dados!\n '
                             f'Para usar, mencione o bot na postagem com um video\n\nUsuário: *{ig}*\nSenha: *{senha}*\nNúmero: *{num}*')
            elif msg in ['login', 'log', 'mundarnum']:
                if arg is None: send_msg(lista_msgs[1]); sair(2); return
                nome, numero = coletas()
                dados = arg.split('/')
                ig_pass = literal_eval(arquivos.ler_semfiltro('ig_pass'))
                ig_num = literal_eval(arquivos.ler_semfiltro('ig_num'))
                try:
                    ig = dados[0]
                    senha = dados[1]
                    senha_reg = ig_pass[ig]
                    num = ig_num[ig]
                    if not numero == num:
                        if senha == senha_reg:
                            send_msg("Registrando novo número")
                            ig_num[ig] = numero
                            arquivos.ler_semfiltro('ig_num', ig_num, True)
                            send_msg('Sucesso!\n\n')
                        else:
                            send_msg(f"Senha incorreta, verifique os dados!\nUsuário: {ig}\nNúmero registrado: {num}")
                    else:
                        send_msg("Seu número atual já está registrado! Faça bom proveito😁")
                except IndexError:
                    send_msg(f"Não consegui achar seu registro aqui :(\nNão tem problema, use o codigo '{prefix}reg' para se registrar! confira o menu.")
            elif msg in ['%', 'cupido', 'cup']:
                if arg is None: send_msg(lista_msgs[1]); sair(2); return
                send_msg("Verificando compatibilidade!")
                nomes = arg.split('/')
                response = lover(nomes)
                send_msg(response)
            elif msg == 'covid':
                text = covid()
                send_msg(text)
            elif msg == 'conselho':
                send_msg(conselho())
            elif msg in ['rep', 'repetir']:
                if arg is None: send_msg(lista_msgs[1]); sair(2); return
                try:
                    dados = arg.split('/')
                    msg = dados[0]
                    qnt = int(dados[1])
                    valor = msg * qnt
                    if len(valor) > 50_000:
                        send_msg("Mensagem muito longa digite um valor que a soma de caracteres dê ate 50.000")
                    else:
                        send_msg(valor)
                except:
                    send_msg(lista_msgs[1])
            elif msg in ['calc', 'calculadora']:
                if arg is None: send_msg(lista_msgs[1]); sair(2); return
                try:
                    sinais = ['+','-','*','^','//', '/']
                    dados = ''
                    sinal = ''
                    for sinal in sinais:
                        dados = arg.split(sinal)
                        if not len(dados) <= 1:
                            sinal = sinal
                            break
                    if not len(dados) <= 1:
                        num = [float(dados[0].replace(" ", '')), float(dados[1].replace(' ', ''))]
                        res = calc(sinal, num)
                        send_msg(f"*Calculadora*\n\n{dados[0]} {sinal} {dados[1]} =\n*{res}*")
                    else:
                        raise ValueError
                except Exception as e:
                    print(e)
                    send_msg(lista_msgs[1])
            else:
                send_msg(
                    f'Desculpe, o comando "{prefix}{msg}" ainda não esta registrado! \nVerifique os comandos existentes com "{prefix}menu"')
        elif msg.split(' ')[0].lower() == 'menu':
            print(f'{cor("info")}Comando "{msg}" detectado!')
            if desativado: send_msg(lista_msgs[0]); sair(2); return
            menu_msg = arquivos.ler_escrever(prefix, 'menu')
            send_msg(menu_msg)
        elif conferir_simi(prefix):
            if desativado: mark_read(num_conv)
            simi_txt = simi_conv(prefix)
            send_msg(simi_txt)
            print(f'{cor("info")}Simi "{msg}" detectado, respondendo com "{simi_txt}"')
        else:
            print(f'{cor("info")}Mensagem "{msg}" detectado!')
            mark_read(num_conv)
    elif is_img:
        if tem_prefixo:
            legenda = legenda.lower().split(" ")[0].replace(prefix, '')
            print(f'{cor("info")}Imagem com comando "{legenda}" detectado!')
            if legenda in ['fig', 'f', 'sticker', 'st']:
                abrir_f_conv(num_conv)
                if desativado: send_msg(lista_msgs[0]); sair(2); return
                try:
                    download_img()
                    send_msg("Fazendo figurinha...")
                    send_fig()
                    download_img(True)
                    send_msg("Sucesso!")
                except Exception as e:
                    print(e)
                    send_msg("Erro ao fazer figurinha, tente novamente mais tarde")
            elif legenda == 'img':
                abrir_f_conv(num_conv)
                if desativado: send_msg(lista_msgs[0]); sair(2); return
                try:
                    download_img()
                    send_msg("Reenviando imagem...")
                    send_media()
                    download_img(True)
                    send_msg("Sucesso")
                except Exception as e:
                    print(e)
                    send_msg("Erro ao fazer figurinha, tente novamente mais tarde")

            else:
                send_msg(f'Desculpe, o comando "{prefix}{msg}" ainda não esta registrado! \nVerifique os comandos existentes com "{prefix}menu"')
        else:
            print(f'{cor("info")}Imagem detectada!')
            mark_read(num_conv)
    sair(5)


####################

# COLETAS

def colet(modo: str, caminho: str, IsPlural=False):
    if not IsPlural:
        Dados = driver.find_element(modo, caminho)
        return Dados
    if IsPlural:
        Dados = driver.find_elements(modo, caminho)
        return Dados


def conferir_img(num_conv):
    try:
        path_img = f'/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div/div[{num_conv}]/div/div/div/div[2]/div[2]/div[1]/span/div'
        path_leg = f'/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div/div[{num_conv}]/div/div/div/div[2]/div[2]/div[1]/span/span'
        colet('xpath', path_img)
        legenda = colet('xpath', path_leg).text
        if "Photo" in legenda: legenda = ''
        is_img = True
    except Exception:
        legenda = ''
        is_img = False
    return is_img, legenda


def coletar_ultima(num_conv):
    try:
        path_msg = f"/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div/div[{num_conv}]/div/div/div/div[2]/div[2]/div[1]/span/span"
        msg = colet('xpath', path_msg).text
        if not msg is None:
            return msg
        else:
            coletar_ultima(num_conv)
    except Exception as e:
        print("Error:\n", e)
        coletar_ultima(num_conv)


def conferir_prefixo(msg, prefix):
    if msg[0] == prefix:
        return True
    else:
        return False


def conferir_login(numero):
    lista_login = arquivos.ler_escrever(None, 'login')
    if numero in lista_login:
        return True
    else:
        return False


def conferir_simi(prefix):
    nome, numero = coletas()
    lista_simi_log = arquivos.ler_escrever(prefix, 'simi_login')
    if numero in lista_simi_log:
        return True
    else:
        return False


def coletas():
    click_info()
    time.sleep(0.5)
    path_nome = '/html/body/div[1]/div/div/div[5]/span/div/span/div/div/section/div[1]/div[2]/h2/span'
    path_nome_group = '/html/body/div[1]/div/div/div[5]/span/div/span/div/div/section/div[1]/div/div[2]/div/div/div[1]/div/div[2]'
    path_num = '/html/body/div[1]/div/div/div[5]/span/div/span/div/div/section/div[1]/div[2]/div/span/span'
    try:
        numero = colet('xpath', path_num).text.replace("-", " ").replace("+", " ").replace(" ", "")
    except Exception:
        numero = "ERROR!!!!"
    try:
        nome = colet('xpath', path_nome).text
    except NoSuchElementException:
        nome = colet('xpath', path_nome_group).text
    except Exception:
        nome = 'ERROR!!!!'
    sair(1, True)
    if '~' in numero:
        numeroF = nome.replace("-", " ").replace("+", " ").replace(" ", "")
        nomeF = numero.replace('~', '')
    else:
        nomeF = nome
        numeroF = numero
    return nomeF, numeroF


def coletar_arg(msg):
    msg = msg.split(" ")
    del [msg[0]]
    arg = " ".join(msg)
    if arg == '': arg = None
    return arg


def len_conv():
    path_convs = "/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div/div"
    len_conversas = len(colet('xpath', path_convs, True))
    return len_conversas


def len_msg():
    path_div = '//div[@class="n5hs2j7m oq31bsqd gx1rr48f qh5tioqs"]/div'
    len_msgs = len(colet('xpath', path_div, True))
    return len_msgs


def conferir_desativado(prefix):
    if arquivos.ler_escrever(prefix, 'desativado') == '1':
        return True
    else:
        return False


def conf_qr():
    try:
        path_qr = '/html/body/div[1]/div/div/div[3]/div[1]/div/a'
        colet('xpath', path_qr)
        return False
    except Exception:
        return True


def conf_conv():
    tam_conv = len_conv()
    num_conv = 1
    while num_conv <= tam_conv:
        is_new = coletar_new(num_conv)
        if is_new:
            return num_conv
        else:
            pass
        num_conv += 1
    return None


def len_icon(num_conv):
    path_icon = f'/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div/div[{num_conv}]/div/div/div/div[2]/div[2]/div[2]/span[1]/div'
    len_ico = colet('xpath', path_icon, True)
    len_ico = len(len_ico)
    return len_ico


def conselho():
    frases = ['Aqui vai o conselho do dia!', 'E o conselho do dia é...', 'La vai conselho', 'Se liga nessa...', 'Lá vai']
    response = literal_eval(requests.request('GET', 'https://api.adviceslip.com/advice').text)['slip']['advice']
    responsept = translate(response, 'auto', 'pt-br')[0]
    text = f'{random.choice(frases)}\n\nPT: *{responsept}*\nEN: *{response}*'
    return text


def translate(texto, de, para, passou=False):
    if not passou: abas(f'https://translate.google.com/?sl={de}&tl={para}&text={texto}')
    path_translate = '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div/div[8]/div/div[1]/span[1]'
    path_lingua = '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[1]/c-wiz/div[2]/div/div[2]/div/div/span/button[1]/span[1]/span'
    autodetect = colet('xpath', path_lingua).text
    traducao = colet('xpath', path_translate).text.replace('\n', '')
    if autodetect == '': passou = True; translate(texto, de, para, passou)
    abas('', True)
    return traducao, autodetect


def download_img(apagar=False):
    if not apagar:
        len_mensagens = len_msg()
        path_folder = f"/Users/{os.getlogin()}/Downloads"
        path_img = f'/html/body/div[1]/div/div/div[4]/div/div[2]/div/div[2]/div[3]/div[{len_mensagens}]/div/div/div[1]/div[1]/div/div[1]'
        path_down = f'/html/body/div[1]/div/span[3]/div/div/div[2]/div/div[1]/div[2]/div/div[5]/div'
        colet('xpath', path_img).click()
        colet('xpath', path_down).click()
        time.sleep(2)
        lista_arq = os.listdir(path_folder)
        len_lista = len(lista_arq)
        num = 0
        while num < len_lista - 1:
            nome_arq = lista_arq[num]
            if "WhatsApp" in nome_arq:
                extencao = nome_arq.split('.')[len(nome_arq.split('.')) - 1]
                path_downed = f"{path_folder}/{nome_arq}"
                path_replace = f"src/image.{extencao}"
                os.rename(path_downed, path_replace)
                print("Done")
                break
            num += 1
            if num > len_lista: num = 0
        sair(1)
    elif apagar:
        arquivo = os.listdir('src')[0]
        os.remove(f'src/{arquivo}')

##################################################################
# TWITTER:

def tw_post(texto: str):
    bot.create_tweet(text = texto)


def tw_ids(tw_id = None, get = False):
    if tw_id is None: get = True
    with open('lib/ids_tw', 'r') as f:
        old_ids = f.readlines()
        for index in range(len(old_ids)):
            old_ids[index] = old_ids[index].replace('\n', '')
        if not get:
            with open('lib/ids_tw', 'a') as file:
                if not tw_id in old_ids:
                    file.writelines(str(tw_id) + '\n')
        else:
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
               f'Twitter {"não" if user["protected"] == False else ""} protegido'
        return text
    except Exception:
        return 'Error'

def check_tw_new():
    try:
        mention = api.mentions_timeline()
        for mentions in mention:
            json = mentions._json
            old_ids = tw_ids()
            id_tw = json['id']
            if not str(id_tw) in old_ids:
                name_tw = json['user']['name']
                ig_tw = json['user']['screen_name']
                usr_loc = json['user']['location']
                id_tw_rpl = json['in_reply_to_status_id']
                name_tw_rpl = json['in_reply_to_screen_name']
                try: vd_leg = bot.get_tweet(id_tw_rpl)[0].text
                except Exception: vd_leg = ''
                print(cor('info') + f'Nova Menção de {name_tw} detectada!')
                ig_num = literal_eval(arquivos.ler_semfiltro('ig_num'))
                try:
                    num = ig_num[ig_tw]
                    try: bot.create_tweet(in_reply_to_tweet_id=id_tw, text=f'Salve {name_tw}\n\nIrei enviar o video no seu '
                                                                           f'Whatsapp ((**) *.****-{num[9:]})\nEsse não é'
                                                                           f' seu número? Envie uma mensagem a mim.')
                    except tw.errors.Forbidden:
                        tw_ids(id_tw)
                        pass
                    sair()
                    send_msg(f'https://wa.me/{num}')
                    click_msg()
                    time.sleep(2)
                    send_msg(f'Você pediu? aqui estou😊\n'
                             f'Enviando seu video...\n'
                             f'Tweetado por: *{name_tw_rpl}*\n'
                             f'Requisitado por: *{name_tw}*\n'
                             f'Localização: {usr_loc}')
                    tw_link = f'https://twitter.com/{name_tw_rpl}/status/{id_tw_rpl}'
                    video_name = f"{name_tw_rpl}´s_video_{ig_tw}´request_all_by_Ezn"
                    os.system(f'youtube-dl -o src/{video_name}.mp4 --retries 3 {tw_link}')
                    try: send_media(vd_leg)
                    except IndexError:
                        bot.create_tweet(in_reply_to_tweet_id=id_tw, text='Ocorreu um Erro :/\nCertifique-se que para'
                                                                              ' baixar midias a midia seja um video. Para baixar imagens'
                                                                              'você pdode entrar nas opções da imagens ao clicar nela (tres pontos) e após apertar em salvar, '
                                                                              'ou simplesmente tirar print.')
                        send_msg('Ocorreu um Erro :/\nCertifique-se que para baixar midias a midia seja um video. Para baixar imagens você pode entrar nas opções da imagens ao clicar nela (tres pontos) e após apertar em salvar ou simplesmente tirar print.')
                        tw_ids(id_tw)
                        break

                    arquivo = os.listdir('src')[0]
                    os.remove(f'src/{arquivo}')
                except KeyError:
                    bot.create_tweet(text=f'Olá {name_tw}\nInfelizmente não encontrei seu numero na minha base de dados,'
                                          f' mas não tem problema, use este comando no meu whatsapp para fazer seu registro!'
                                          f'\n\n{prefix}reg {ig_tw}/[seu número]/[crie uma senha]\nOu\nUse este link para registrar: '
                                          f'https://wa.me/556196884447?text={prefix}reg%20{ig_tw}%20%2F%20%5BCrie%20uma%20senha%5D', in_reply_to_tweet_id=id_tw)
                except Exception as e:
                    try:
                        print(f'Error no twitter! \n {e}')
                        send_msg('Erro, tente novamente mais tarde')
                        send_adm(lista_num_adm, str(e))
                        check_tw_new()
                    except Exception as e:
                        print(f'Error no twitter! \n {e}')
                        check_tw_new()
                tw_ids(id_tw)
                print(cor('check') + 'Tratado com sucesso!')
    except IndexError:
        pass
    except Exception as e:
        print(cor('erro')+f'Erro ao conferir novos tweets.\n{e}')
    time.sleep(1)
    sair()



###################################################################
# CLICKS


def mark_read(num_conv):
    click_conv(num_conv)
    colet('xpath', '/html/body').send_keys(Keys.ESCAPE)
    time.sleep(0.25)


def abrir_f_conv(num_conv):
    sair(5)
    time.sleep(0.25)
    click_conv(num_conv)


def click_msg():
    len_msgs = len_msg()
    colet('xpath', f'/html/body/div[1]/div/div/div[4]/div/div[2]/div/div[2]/div[3]/div[{len_msgs}]/div/div/div[1]/div[1]/div[1]/div[1]').click()


def click_unread(num_conv):
    path_conv = f'/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div/div[{num_conv}]'
    tecla = colet('xpath', path_conv)
    ActionChains(driver).context_click(tecla).perform()
    path_unread = '/html/body/div[1]/div/span[4]/div/ul/div/li[5]/div'
    colet('xpath', path_unread).click()


def click_conv(num_conv):
    path_click = f'/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div/div[{num_conv}]'
    colet('xpath', path_click).click()


def click_info():
    path_info = '/html/body/div[1]/div/div/div[4]/div/header'
    colet('xpath', path_info).click()
    time.sleep(0.25)


def abas(url, is_close=False):
    if not is_close:
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(url)
        time.sleep(2)
    else:
        driver.close()
        driver.switch_to.window(driver.window_handles[0])


# MAIN

def sair(qnt_esc = 0, esc = False):
    try:
        if esc is True:
            raise Exception
        else:
            click_conv(lista_main_group[0])
    except Exception:
        for e in range(qnt_esc):
            time.sleep(0.1)
            colet('xpath', '/html/body').send_keys(Keys.ESCAPE)


def mud_desc(txt):
    tecla = ActionChains(driver)
    colet('xpath', '/html/body/div[1]/div/div/div[3]/header/div[1]/div/div').click()
    time.sleep(0.25)
    colet('xpath', '/html/body/div[1]/div/div/div[2]/div[1]/span/div/span/div/div/div[4]/div[2]/div/span[2]/button').click()
    tecla.key_down(Keys.CONTROL).key_down('a').send_keys(Keys.BACKSPACE).key_up(Keys.CONTROL).key_up('a').perform()
    colet('xpath', '/html/body/div[1]/div/div/div[2]/div[1]/span/div/span/div/div/div[4]/div[2]/div[1]/div[1]/div/div[2]').send_keys(txt)
    tecla.send_keys(Keys.ENTER).perform()
    time.sleep(1)
    sair(2)


def desativar_ativar(desativado):
    if desativado:
        arquivos.ler_escrever(prefix, 'desativado', False, '1')
    else:
        arquivos.ler_escrever(prefix, 'desativado', False, '0')


def ts_send(msg):
    len_conversas = len_conv()
    for e in range(1, len_conversas + 1):
        click_conv(e)
        send_msg(msg + '\nNúmero da conversa: ' + str(e))
    sair(1)


def calc(sinal, num):
    try:
        if not (num[0] + num[1]) > 999999999999:
            if sinal == '+':
                resposta = num[0] + num[1]
            elif sinal == '*':
                resposta = num[0] * num[1]
            elif sinal == '^':
                resposta = num[0] ** num[1]
            elif sinal == '-':
                resposta = num[0] - num[1]
            elif sinal == '/':
                resposta = num[0] / num[1]
            elif sinal == '//':
                resposta = num[0] // num[1]
            else:
                resposta = 'Error'
        else:
            resposta = "∞"
    except ZeroDivisionError:
        resposta = "Não é possivel dividir por 0"
    except OverflowError:
        resposta = '∞'
    return resposta



def covid():
    headers = {
        "X-RapidAPI-Key": "19318e22c3msh19d2d66c759bad6p14faf4jsn1f3f58714d21",
        "X-RapidAPI-Host": "covid-19-coronavirus-statistics.p.rapidapi.com"
    }
    responseBR = literal_eval(
        requests.request("GET", "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/total", headers=headers,
                         params={"country": f"Brazil"}).text.replace('null', 'None').replace('false', 'False'))
    response = literal_eval(
        requests.request("GET", "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/total", headers=headers,
                         params={"country": ""}).text.replace('null', 'None').replace('false', 'False'))
    text = f'*Dados do COVID-19 no Brasil🇧🇷🇧🇷*\n' \
           f'Mortes: *{int(responseBR["data"]["deaths"]):_.3f}*\n' \
           f'Casos: *{int(responseBR["data"]["confirmed"]):_.3f}*\n\n' \
           f'*Dados do COVID-19 mundial🗺️🌍*\n' \
           f'Mortes: *{int(response["data"]["deaths"]):_.3f}*\n' \
           f'Casos: *{int(response["data"]["confirmed"]):_.3f}*'
    return text


def lover(nomes: list):
    dados = {"sname": nomes[0], "fname": nomes[1]}
    headers = {"X-RapidAPI-Key": "19318e22c3msh19d2d66c759bad6p14faf4jsn1f3f58714d21", "X-RapidAPI-Host": "love-calculator.p.rapidapi.com"}
    response = literal_eval(requests.request("GET", "https://love-calculator.p.rapidapi.com/getPercentage", headers=headers, params=dados).text)
    return f"Bem vindo ao cupido!\nA compatibilidade de {nomes[0]} com {nomes[1]} é {response['percentage']}%"


def simi_conv(prefix):
    simi_txt = arquivos.ler_escrever(prefix, 'simi')
    resposta = random.choice(simi_txt)
    return resposta


def resposta():
    lista_resposta = ['Sim', 'Não', 'Talvez', 'Não sei', 'Talvez Sim', 'Talvez Não']
    resposta = random.choice(lista_resposta)
    return resposta


def send_fig():
    path_clip = '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/span'
    path_fig = '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[2]/button/input'
    path_env = '/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div'
    midia = os.listdir('src')[0]
    dir_atual = os.getcwd()
    try:
        colet('xpath', path_clip).click()
        colet('xpath', path_fig).send_keys(f"{dir_atual}/src/{midia}")
        time.sleep(0.5)
        colet('xpath', path_env).click()
    except Exception as e:
        print(e)
        send_media()
    time.sleep(1)


def send_media(legenda = ''):
    path_clip = '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/span'
    path_img = '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[1]/button/input'
    path_env = '/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div'
    path_leg = '/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[1]/div[1]/p'
    midia = os.listdir('src')[0]
    dir_atual = os.getcwd()
    try:
        colet('xpath', path_clip).click()
        time.sleep(0.5)
        colet('xpath', path_img).send_keys(f"{dir_atual}/src/{midia}")
        time.sleep(2)
        txtbox_leg = colet('xpath', path_leg)
        txtbox_leg.click()
        txtbox_leg.send_keys(legenda)
        colet('xpath', path_env).click()
    except IndexError:
        return IndexError
    except Exception as e:
        print(e)
        sair(1, esc=True)
        send_media(legenda)
    time.sleep(1)


def send_adm(lista_num_adm, msg):
    for e in lista_num_adm:
        click_conv(e)
        send_msg(msg)
        time.sleep(0.25)


def send_msg(msg):
    text_box = '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
    txt = colet('xpath', text_box)
    txt.click()
    tecla = ActionChains(driver)
    tecla.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).perform()
    pyperclip.copy(msg)
    tecla.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
    if len(msg) > 5000:
        time.sleep(5)
    elif len(msg) >= 1000:
        time.sleep(2.5)
    elif len(msg) >= 100:
        time.sleep(1)
    else:
        pass
    tecla.send_keys(Keys.ENTER).perform()
    tecla.send_keys(Keys.ENTER).perform()


def cor(var):
    if var == 'info':
        print(Fore.BLUE + f'[INFO]', end='')
    elif var == 'erro':
        print(Fore.RED + f'[ERROR]', end='')
    elif var == 'check':
        print(Fore.GREEN + f'[SUCESS]', end='')
    a = Style.RESET_ALL
    return a


def coletar_new(num_conv):
    len_ico = len_icon(num_conv)
    path_conv = f'//*[@id="pane-side"]/div[1]/div/div/div[{num_conv}]/div/div/div/div[2]/div[2]/div[2]/span[1]/div[{len_ico}]/span[@class="l7jjieqr cfzgl7ar ei5e7seu h0viaqh7 tpmajp1w c0uhu3dl riy2oczp dsh4tgtl sy6s5v3r gz7w46tb lyutrhe2 qfejxiq4 fewfhwl7 ovhn1urg ap18qm3b ikwl5qvt j90th5db aumms1qt"]'
    try:
        colet('xpath', path_conv)
        return True
    except Exception:
        return False


def Twitter():
    while True:
        check_tw_new()
        time.sleep(10)


def Whatsapp(desativado, prefix, one_once: bool, lista_msgs):
    if one_once:
        driver.get("https://web.whatsapp.com")
        time.sleep(5)
        print(f'{cor("info")}Aguardando Leitura do codigo qr...')
        main(desativado, prefix, lista_msgs)
    else:
        check_wpp_new(lista_msgs)



def coletar_num_convs_main():
    len_conversas = len_conv()
    for num_conv in range(1, len_conversas + 1):
        try:
            is_new = coletar_new(num_conv)
            click_conv(num_conv)
            if is_new:
                click_unread(num_conv)
            time.sleep(0.25)
            nome, numero = coletas()
            if conferir_login(numero):
                lista_num_adm.append(num_conv)
            if nome == '__main__':
                lista_main_group.append(num_conv)
        except Exception:
            sair(1)
            pass
        sair(1)
    sair(5)


def check_wpp_new(lista_msgs):
    time.sleep(3)
    num_conv = conf_conv()
    if not lista_num_adm: coletar_num_convs_main()
    prefix = arquivos.ler_escrever(None, 'prefix')
    if not conf_qr(): login()
    if not num_conv is None:
        click_conv(num_conv)
        desativado = conferir_desativado(prefix)
        msg = coletar_ultima(num_conv)
        try:
            comando_atual(num_conv, desativado, lista_msgs, lista_num_adm, prefix, msg)
            sair(1)
            print(f'`{cor("check")}Mensagem tratada com sucesso!')
        except NoSuchElementException:
            sair(5)
            time.sleep(1)
            main(desativado, prefix, lista_msgs)
        except Exception as e:
            nome, numero = coletas()
            print(cor('Erro') + str(e))
            send_adm(lista_num_adm, f'*Error!!*\n'
                                    f'Dados:\n'
                                    f'Conversa Nº {num_conv}\n'
                                    f'Nome do contato: {nome}\n'
                                    f'Número: {numero}\n'
                                    f'Mensagem: {msg}\n'
                                    f'Erro:\n\n*{e}*')
            sair(5)
            main(desativado, prefix, lista_msgs)


def login(logged = False):
    while not logged:
        logged = conf_qr()


def main(desativado, prefix, lista_msgs):
    try:
        login()
        print(f'{cor("check")}Conectado!')
        if not desativado:
            mud_desc(lista_msgs[3])
        else:
            mud_desc(lista_msgs[0])
        coletar_num_convs_main()
        check_wpp_new(lista_msgs)
    except Exception as e:
        try:
            send_msg("Error! enviando log para o administrador, perdão por isso.")
        except Exception: pass
        finally:
            print(cor('Erro geral!\n') + str(e))
            time.sleep(1)
            main(desativado, prefix, lista_msgs)

import threading
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import pyperclip
from colorama import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import tweepy as tw
import os
import random
import time
import arquivos
import requests
from dados import api_key, api_sec_key, main_token, main_token_sec, b_token
from ast import literal_eval
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
lista_num_adm = []
lista_main_group = []
if __name__ == "__main__":
    auth = tw.OAuthHandler(api_key, api_sec_key)
    auth.set_access_token(main_token, main_token_sec)
    bot = tw.Client(consumer_key=api_key, consumer_secret=api_sec_key, access_token=main_token,
                    access_token_secret=main_token_sec, bearer_token=b_token)
    api = tw.API(auth, wait_on_rate_limit=True)
    name = dict(api.get_settings()).get('screen_name')
    os.system('cls' if os.name == 'nt' else 'clear')
    prefix = arquivos.ler_escrever(None, 'prefix')
    desativado = conferir_desativado(prefix)
    lista_msgs = [f'Bot desligado, tente novamente mais tarde com "{prefix}menu"',
    f"Erro!\nVerifique o uso do comando com {prefix}menu",
    "Apenas administradores podem usar esse comando, como descobriu hein?",
    f'Olá, Bot on, envie "menu" para ver a lista de comandos. prefixo: {prefix}\n',
    "Esse comando só pode ser usado na legenda de uma foto."]
    one_once = True
    try:
        Whatsapp(desativado, prefix, one_once, lista_msgs)
        one_once = False
        threads = []
        tweet = threading.Thread(target=Twitter, args=(), daemon=True)
        threads.append(tweet)
        tweet.start()
        while True:
            Whatsapp(desativado, prefix, one_once, lista_msgs)
    except NoSuchElementException:
        pass
    except Exception as e:
        driver.switch_to.window(driver.window_handles[0])
        try:
            send_msg('Error, tente novamente')
        except Exception:
            pass
        sair(3)
        main(desativado, prefix, lista_msgs)

driver.quit()
exit()
