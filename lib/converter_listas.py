arq_nome = input("Nome do arquivo: ")
modo = input("Modo 1/0 (1 = converter, 2 = reverter) ")
rev = None
if modo == "1": rev = False
elif modo == "2": rev = True


def converter():
    with open(arq_nome, 'r', encoding='utf-8') as file:
        txt = file.read()
        if not txt[0] == "[":
            with open(arq_nome, 'r', encoding='utf-8') as file_:
                txt = file_.readlines()
                for e in range(len(txt)):
                    txt[e] = txt[e].replace('\n', '')
                txt = str(txt).replace(', ', ',').replace("'", '')
                with open(arq_nome, 'w', encoding='utf-8') as file__:
                    file__.write(txt)


def reverter():
    with open(arq_nome, 'r', encoding='utf-8') as file:
        txt = file.read()
        if txt[0] == "[":
            txt = txt.strip("[]").replace(',', '\n')
            with open(arq_nome, 'w') as file_:
                file_.write(txt)


if rev:
    reverter()
else:
    converter()
