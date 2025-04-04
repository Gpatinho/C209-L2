# 5 - faca a analise em seu pinguin favorito e escolha um valor e thereshold ( justiffique a escolha de thereshold)
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregar a imagem recortada do pinguim
imagem_recortada = cv2.imread('pinguim_vermelho_recortado.jpg')

# Converter a imagem para o espaço de cores RGB (OpenCV usa BGR por padrão)
imagem_rgb = cv2.cvtColor(imagem_recortada, cv2.COLOR_BGR2RGB)

# Definir um valor de threshold para a cor vermelha
# Vamos filtrar os pixels que são aproximadamente vermelhos (R > 150, G < 100, B < 100)
threshold_r = 150
threshold_g = 100
threshold_b = 100

# Aplicar a máscara para destacar os pixels vermelhos
mascara = (imagem_rgb[:, :, 0] > threshold_r) & (
    imagem_rgb[:, :, 1] < threshold_g) & (imagem_rgb[:, :, 2] < threshold_b)

# Criar a imagem resultante com o pinguim isolado
imagem_resultante = np.zeros_like(imagem_rgb)
imagem_resultante[mascara] = imagem_rgb[mascara]

# Exibir a imagem resultante (pinguim isolado)
plt.imshow(imagem_resultante)
plt.axis('off')
plt.show()

# Salvar a imagem resultante com o pinguim vermelho isolado
cv2.imwrite('pinguim_vermelho_isolado_threshold.jpg',
            cv2.cvtColor(imagem_resultante, cv2.COLOR_RGB2BGR))
