import cv2

xI, yI, xF, yF = 0, 0, 0, 0
drawing = False
interruptor = False
recorte = None  # Para almacenar el recorte de la imagen

def dibujar(event, x, y, flags, param):
    global xI, yI, xF, yF, drawing, interruptor, recorte

    if event == cv2.EVENT_LBUTTONDOWN:
        xI, yI = x, y
        xF, yF = x, y
        drawing = True
        interruptor = False

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            xF, yF = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        xF, yF = x, y
        drawing = False
        interruptor = True
        recorte = img[yI:yF, xI:xF, :]

img = cv2.imread('D:\python\PYTHON\calculadora_SF_p1\img\img.jpg')  # Cambia esto a la ruta de tu imagen
cv2.namedWindow('Recortador de Imagen')
cv2.setMouseCallback('Recortador de Imagen', dibujar)

while True:
    display_img = img.copy()

    if drawing:
        cv2.rectangle(display_img, (xI, yI), (xF, yF), (0, 255, 0), 2)

    cv2.imshow('Recortador de Imagen', display_img)
    
    if interruptor and recorte is not None and recorte.shape[0] > 0 and recorte.shape[1] > 0:
        cv2.imshow('Recorte', recorte)  # Muestra el recorte
        
    k = cv2.waitKey(1) & 0xff
    if k == 27:  # Presionar 'q' para salir
        break

cv2.destroyAllWindows()
