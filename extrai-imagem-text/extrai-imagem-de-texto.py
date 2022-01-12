import easyocr

reader = easyocr.Reader(['pt'])

results = reader.readtext('./extrai-imagem-text/placa.png', paragraph=False, workers=1)

for result in results:
    print(f'Texto: {result[1]}\n'
        f'Posição: {result[0]}\n')