def ler_escrever(prefix, nome_arq, ler=True, escrita=None):
    if ler:
        try:
            with open(f"lib/{nome_arq}", 'r', encoding='UTF8') as valor_arq:
                valor_arq = valor_arq.read()
                try:
                    valor_arq = valor_arq.replace('{prefix}', prefix)
                except:
                    pass
                if valor_arq[0] == "[":
                    valor_arq = valor_arq.strip("[]").split(",")
                return valor_arq
        except Exception as e:
            print(f'Erro {e} ao tentar ler o arquivo {nome_arq}')
    else:
        try:
            with open(f"lib/{nome_arq}", 'w', encoding='UTF8') as valor_arq:
                if type(escrita) == list:
                    escrita = str(escrita).replace("'", '').replace(' ', '')
                valor_arq.write(escrita)
                return valor_arq
        except Exception as e:
            print(f'Erro {e} ao tentar ler o arquivo {nome_arq}')

def ler_semfiltro(nome_arq: str, dados=None, write = False):
    if dados is None:
        dados = {}
    if write is False:
        with open(f'lib/{nome_arq}', 'r') as f:
            valor = f.read()
        return valor
    else:
        with open(f'lib/{nome_arq}', 'w', newline='') as f:
            f.write(str(dados))
