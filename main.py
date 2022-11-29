from src.Kuznechik import Kuznechik

if __name__ == '__main__':
    mode = int(input('Выберите режим работы шифра "Кузнечик":\n'
                     '1) Зашифрование\n'
                     '2) Расшифрование\n'
                     '3) Перекодировка текста\n'))
    source_option = int(input('Исходный текст - это:\n'
                              '1) Hex-строка\n'
                              '2) Произвольный текст\n'
                              '3) Текст в base64\n'))
    new_option = int(input('Новый текст представить в виде:\n'
                           '1) Hex-строка\n'
                           '2) Произвольный текст\n'
                           '3) Текст в base64\n'))
    input_enc = ['', 'hex', 'text', 'base64'][source_option]
    output_enc = ['', 'hex', 'text', 'base64'][new_option]
    machine = Kuznechik(input_enc, output_enc)
    if mode == 1:
        machine.encrypt()
    elif mode == 2:
        machine.decrypt()
    elif mode == 3:
        with open('input.txt', 'r', encoding='utf-8') as f0:
            text0 = f0.read()
            with open('output.txt', 'w', encoding='utf-8') as f:
                f.write(Kuznechik.converter(text0, input_enc, output_enc))
