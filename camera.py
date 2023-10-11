import cv2

# Carregar o classificador em cascata para faces frontais do OpenCV
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Iniciar a captura de vídeo
cap = cv2.VideoCapture(0)
 
while True:
    # Capturar quadro a quadro
    ret, frame = cap.read()

    # Converter o quadro para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar faces no quadro em escala de cinza
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Para cada face detectada
    for (x, y, w, h) in faces:
        # Desenhar um retângulo ao redor da face detectada
        cv2.rectangle(frame, (x, y), (x + w, y + h), (183, 196, 39), 2)

    # Exibir o quadro resultante
    cv2.imshow('Camera, clique Q para sair', frame)

    # Aguardar a tecla 'q' ser pressionada para sair do loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar a captura de vídeo e destruir todas as janelas abertas
cap.release()
cv2.destroyAllWindows()
