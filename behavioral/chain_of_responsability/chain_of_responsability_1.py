# Implementando com funções
def handler_ABC(letter: str) -> str:
    letters = ['A', 'B', 'C']

    if letter in letters:
        return f'handler_ABC: conseguiu tratar o valor {letter}'

    return handler_DEF(letter)

def handler_DEF(letter: str) -> str:
    letters = ['D', 'E', 'F']

    if letter in letters:
        return f'handler_DEF: conseguiu tratar o valor {letter}'

    return handler_unsolver(letter)


def handler_unsolver(letter: str) -> str:
    return f'handler_unsolver: não sei tratar {letter}' 


if __name__ == "__main__":
    print(handler_ABC('A'))
    print(handler_ABC('B'))
    print(handler_ABC('C'))
    print()
    print(handler_ABC('D'))
    print(handler_ABC('E'))
    print(handler_ABC('F'))
    print()
    print(handler_ABC('G'))
    print(handler_ABC('H'))
    print(handler_ABC('I'))