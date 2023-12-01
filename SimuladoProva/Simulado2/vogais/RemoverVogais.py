def remover_vogais(palavra: str) -> str:
    resultado = ''
    for letra in palavra:
        if letra.lower() not in 'aeiouáéíóúãõâêîôûàèìòùäëïöü':
            resultado += letra

    return resultado

def program():
    stringOriginal = 'Estou programando python'

    stringModificada = remover_vogais(stringOriginal)
    print(stringModificada)

program()