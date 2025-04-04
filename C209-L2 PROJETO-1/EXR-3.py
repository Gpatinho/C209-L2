# 3 - aplicar o espelhamento
from PIL import Image
import matplotlib.pyplot as plt

# Carregar a imagem salva com as cores alteradas
imagem_nova_cor = Image.open('imagem_pinguins_coloridos.jpg')

# Aplicar o espelhamento horizontal
imagem_espelhada = imagem_nova_cor.transpose(Image.FLIP_LEFT_RIGHT)

# Exibir a imagem espelhada
plt.figure(figsize=(10, 5))
plt.imshow(imagem_espelhada)
plt.axis('off')  # Desliga os eixos para uma visualização mais limpa
plt.show()

# Salvar a imagem espelhada
imagem_espelhada.save('imagem_pinguins_espelhada.jpg')
