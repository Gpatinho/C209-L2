# 2 - trocar todas as cores (mudar a cor dos pinguins para qualquer outra)
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Carregar a imagem combinada
imagem_combinada = Image.open("imagem_combinada.jpg")

# Converter a imagem para um array numpy para manipulação
imagem_array = np.array(imagem_combinada)

# Função para alterar a cor de áreas específicas (os pinguins)


def alterar_cor_pinguins(imagem_array, cor_original, cor_nova):
    """
    Substitui pixels de uma cor específica por uma nova cor.
    """
    # Converte a cor original e a cor nova para arrays numpy
    cor_original = np.array(cor_original)
    cor_nova = np.array(cor_nova)

    # Cria uma máscara onde a cor original é encontrada
    mask = np.all(imagem_array == cor_original, axis=-1)

    # Aplica a nova cor onde a máscara é verdadeira
    imagem_array[mask] = cor_nova
    return imagem_array


# Definir as cores dos pinguins (exemplo de cores, você deve ajustar conforme necessário)
# Essas cores podem ser ajustadas para as cores reais dos pinguins na sua imagem
cor_original_1 = [0, 0, 0]   # Preto (pinguim 1)
cor_original_2 = [0, 255, 255]  # Ciano (pinguim 2)
cor_original_3 = [0, 0, 255]  # Azul (pinguim 3)
cor_original_4 = [0, 255, 0]  # Verde (pinguim 4)

# Definir as novas cores para os pinguins
nova_cor_1 = [255, 255, 0]   # Amarelo (nova cor para o pinguim 1)
nova_cor_2 = [255, 0, 0]   # vermelho (nova cor para o pinguim 2)
nova_cor_3 = [255, 255, 255]   # Branco (nova cor para o pinguim 3)
nova_cor_4 = [0, 0, 0]   # Preto (nova cor para o pinguim 4)

# Alterar as cores dos pinguins na imagem
imagem_array = alterar_cor_pinguins(imagem_array, cor_original_1, nova_cor_1)
imagem_array = alterar_cor_pinguins(imagem_array, cor_original_2, nova_cor_2)
imagem_array = alterar_cor_pinguins(imagem_array, cor_original_3, nova_cor_3)
imagem_array = alterar_cor_pinguins(imagem_array, cor_original_4, nova_cor_4)

# Converter o array numpy de volta para uma imagem PIL
imagem_nova_cor = Image.fromarray(imagem_array)

# Exibir a imagem final
plt.figure(figsize=(10, 5))
plt.imshow(imagem_nova_cor)
plt.axis('off')  # Desliga os eixos para uma visualização mais limpa
plt.show()

# Salvar a nova imagem com as cores alteradas
imagem_nova_cor.save('imagem_pinguins_coloridos.jpg')
