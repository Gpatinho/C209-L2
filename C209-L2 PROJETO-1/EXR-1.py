import os

import PIL.Image
from PIL import Image
import matplotlib.pyplot as plt #MUDEI ESSA LINHA AQUI

# Caminhos das imagens
img1_path = 'P1.jpg'
img2_path = 'P2.jpg'
img3_path = 'P3.jpg'
img4_path = 'P4.jpg'

img1 = Image.open(img1_path)
img2 = Image.open(img2_path)
img3 = Image.open(img3_path)
img4 = Image.open(img4_path)

# Tamanho máximo para ajustar todas as imagens
altura_maxima = max(img1.height, img2.height, img3.height, img4.height)
largura_total = img1.width + img2.width + img3.width + img4.width

# Função para redimensionar as imagens para a altura máxima


def redimensionar_imagem(imagem, altura_maxima):
    proporcao = altura_maxima / float(imagem.height)
    largura_nova = int(imagem.width * proporcao)
    return imagem.resize((largura_nova, altura_maxima), PIL.Image.Resampling.LANCZOS)


# Redimensionar todas as imagens para a altura máxima
img1 = redimensionar_imagem(img1, altura_maxima)
img2 = redimensionar_imagem(img2, altura_maxima)
img3 = redimensionar_imagem(img3, altura_maxima)
img4 = redimensionar_imagem(img4, altura_maxima)

# Criar uma nova imagem com largura total e altura máxima
imagem_combinada = Image.new('RGB', (largura_total, altura_maxima))

# Colocar as imagens na imagem combinada, ajustando a posição
x_offset = 0
for img in [img1, img2, img3, img4]:
    # Colar a imagem na posição certa
    imagem_combinada.paste(img, (x_offset, 0))
    x_offset += img.width  # Atualizar a posição x para a próxima imagem

# Exibir a imagem combinada usando matplotlib
# Tamanho ajustado para ver todas as imagens claramente
plt.figure(figsize=(10, 5))
plt.imshow(imagem_combinada)  # Exibe a imagem combinada
plt.axis('off')  # Desliga os eixos para uma visualização mais limpa
plt.show()  # Mostra a imagem
imagem_combinada.save('imagem_combinada.jpg')
type(imagem_combinada)

print("Diretório atual:", os.getcwd())