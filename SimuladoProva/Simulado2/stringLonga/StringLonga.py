def encontrar_string_mais_longa(lista: list) -> str:
    maiorString_len = 0
    maiorString_str = ''
    for linha in lista:
        if len(linha) > maiorString_len:
            maiorString_len = len(linha)
            maiorString_str = linha

    return maiorString_str

def program():
    lista = ["Ola mundo", "Estou programando em python", "oi", "Eu amo programar e quero logo um emprego e ganhar dinheiro"]
    maiorString = encontrar_string_mais_longa(lista)
    print(maiorString)

program()

