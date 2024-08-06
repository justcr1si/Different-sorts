def decode_instruction(command: str) -> str:
    # Стек для хранения строк и чисел перед скобками.
    # 116677301 - ID посылки.
    stack = []
    current_number = 0
    current_string = ''

    for symbol in command:
        if symbol.isdigit():
            # Обработка больших значений.
            # 299 -> 0 -> 2 -> 20 + 9 -> 290 + 9.
            current_number = current_number * 10 + int(symbol)
        elif symbol == '[':
            # Храним в стеке кортеж со строкой и номером, после чего обнуляем.
            stack.append((current_string, current_number))
            current_string, current_number = '', 0
        elif symbol == ']':
            # Распаковываем из стека кортеж со строкой и номером.
            # К текущей строке добавляем в начало строку до [.
            # После чего домножаем на number.
            last_string, number = stack.pop()
            current_string = last_string + current_string * number
        else:
            current_string += symbol

    return current_string


def main(command: str) -> None:
    print(decode_instruction(command))


if __name__ == '__main__':
    command_input = input()
    main(command_input)
