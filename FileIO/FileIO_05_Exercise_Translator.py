from translate import Translator

translator = Translator(to_lang = 'ja')

newText = []

try:
    with open('test.txt', mode = 'r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        print(translation)
        # with open('test-japanese.txt', mode = 'w') as my_file2:
        #     my_file2.write(translation)

except FileNotFoundError as e:
    print("File not found, check your file path.")
    print(e)

