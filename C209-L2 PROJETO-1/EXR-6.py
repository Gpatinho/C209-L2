from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Carregar a imagem recortada do pinguim
imagem_recortada = Image.open('pinguim_vermelho_recortado.jpg')

# Converter a imagem para o espaço de cores RGB (Pillow usa RGB por padrão)
imagem_rgb = imagem_recortada.convert('RGB')

# Obter os dados dos pixels da imagem
pixels = np.array(imagem_rgb)

# Função para aplicar threshold na cor vermelha e mudar para a cor roxa


def mudar_para_roxo(pixels, threshold_r, threshold_g, threshold_b):
    """
    Aplica uma máscara para filtrar pixels vermelhos baseado nos thresholds de R, G e B
    e muda a cor desses pixels para roxo (RGB: 128, 0, 128).
    """
    # Criar a máscara para destacar os pixels vermelhos
    mascara = (pixels[:, :, 0] > threshold_r) & (
        pixels[:, :, 1] < threshold_g) & (pixels[:, :, 2] < threshold_b)

    # Substituir os pixels vermelhos encontrados pela cor roxa
    pixels[mascara] = [128, 0, 128]  # Cor roxa (RGB)

    return pixels


# Definir os valores de threshold para o canal vermelho
threshold_r = 150
threshold_g = 100
threshold_b = 100

# Mudar os pixels vermelhos para roxo
pixels_mudados = mudar_para_roxo(pixels, threshold_r, threshold_g, threshold_b)

# Converter os dados dos pixels de volta para uma imagem Pillow
imagem_mudada_pillow = Image.fromarray(pixels_mudados)

# Exibir a imagem com a cor do pinguim alterada para roxo
plt.figure(figsize=(10, 5))
plt.imshow(imagem_mudada_pillow)
plt.axis('off')
plt.title(f"Pinguim Alterado para Roxo (Threshold R > {threshold_r})")
plt.show()

# Salvar a imagem resultante com o pinguim roxo
imagem_mudada_pillow.save('pinguim_roxo.jpg')
