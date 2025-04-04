# 5 - faca a analise em seu pinguin favorito e escolha um valor e thereshold ( justiffique a escolha de thereshold)
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Carregar a imagem recortada do pinguim
imagem_recortada = Image.open('pinguim_vermelho_recortado.jpg')

# Converter a imagem para o espaço de cores RGB (Pillow usa RGB por padrão)
imagem_rgb = imagem_recortada.convert('RGB')

# Obter os dados dos pixels da imagem
pixels = np.array(imagem_rgb)

# Função para aplicar threshold na cor vermelha


def aplicar_threshold(pixels, threshold_r, threshold_g, threshold_b):
    """
    Aplica uma máscara para filtrar pixels vermelhos baseado nos thresholds de R, G e B.
    """
    # Criar a máscara para destacar os pixels vermelhos
    mascara = (pixels[:, :, 0] > threshold_r) & (
        pixels[:, :, 1] < threshold_g) & (pixels[:, :, 2] < threshold_b)
    return mascara


# Variar o valor do threshold para análise
# Valores para testar de threshold para o canal R (vermelho)
threshold_values = [50, 100, 150, 200]
threshold_g = 100  # Limite para G (verde), que deve ser baixo
threshold_b = 100  # Limite para B (azul), que deve ser baixo

# Exibir a imagem original para referência
plt.figure(figsize=(10, 5))
plt.imshow(imagem_rgb)
plt.axis('off')  # Desliga os eixos para uma visualização mais limpa
plt.title("Imagem Original")
plt.show()

# Testar diferentes valores de threshold
for threshold_r in threshold_values:
    mascara = aplicar_threshold(pixels, threshold_r, threshold_g, threshold_b)

    # Criar uma nova imagem com os pixels vermelhos isolados
    imagem_resultante = np.zeros_like(pixels)
    imagem_resultante[mascara] = pixels[mascara]

    # Converter a imagem resultante de volta para uma imagem Pillow
    imagem_resultante_pillow = Image.fromarray(imagem_resultante)

    # Exibir a imagem com o threshold aplicado
    plt.figure(figsize=(10, 5))
    plt.imshow(imagem_resultante_pillow)
    plt.axis('off')
    plt.title(f"Threshold aplicado (R > {threshold_r})")
    plt.show()

    # Calcular a quantidade de pixels vermelhos isolados
    quantidade_pixels = np.sum(mascara)
    print(
        f"Threshold R > {threshold_r}: {quantidade_pixels} pixels vermelhos isolados.")
