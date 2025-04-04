# 4 - recortar meu pinguin favorito
from PIL import Image
import numpy as np

# Carregar a imagem com o pinguim espelhado
imagem_espelhada = Image.open('imagem_pinguins_espelhada.jpg')

# Converter a imagem para um array numpy
imagem_array = np.array(imagem_espelhada)

# Definir a cor do pinguim vermelho (em formato RGB)
cor_vermelho = [255, 0, 0]

# Criar uma máscara onde a cor do pinguim vermelho está presente
mask_vermelho = np.all(imagem_array == cor_vermelho, axis=-1)

# Obter as coordenadas da região que contém a cor vermelha
# Encontrar o retângulo que envolve todos os pixels vermelhos
y_indices, x_indices = np.where(mask_vermelho)

# Garantir que há pelo menos um pixel vermelho
if y_indices.size > 0 and x_indices.size > 0:
    # Encontrar os limites da área do pinguim vermelho
    y_min, y_max = y_indices.min(), y_indices.max()
    x_min, x_max = x_indices.min(), x_indices.max()

    # Recortar a imagem na região do pinguim vermelho
    imagem_recortada = imagem_espelhada.crop((x_min, y_min, x_max, y_max))

    # Exibir a imagem recortada
    imagem_recortada.show()

    # Salvar a imagem recortada
    imagem_recortada.save('pinguim_vermelho_recortado.jpg')
else:
    print("Nenhum pinguim vermelho encontrado na imagem.")
