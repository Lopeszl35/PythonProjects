def seq_fibonacci(num, quantidade):
    fibonacci_sequence = [num]

    if quantidade > 1:
        fibonacci_sequence.append(num + 1)

    while len(fibonacci_sequence) < quantidade:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    return fibonacci_sequence

def programa_pricipal():
    num = int(input("Informe o número que iniciara a sequência de fibonacci: "))
    quant = int(input("Informe o tamanho da sequência de fibonacci: "))

    print(seq_fibonacci(num, quant))


if __name__ == "__main__":
    programa_pricipal()