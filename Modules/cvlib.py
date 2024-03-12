# Importamos librerías estándar
import numpy as np      # Libre para hacer operaciones matriciales y de álgebra lneal
import argparse         # Librería para definir y procesar líneas de comandos
import cv2              # Librería de visión computacional y procesamiento de imágenes
import sys              # Librería para manipular salidas, entradas y funciones del sistema

def close_windows () :
    key = cv2.waitKey(0) & 0xFF             # Variable que espera indefinidamente a que se presione una tecla y obtenemos su valor
    if key == ord('q'):                     # Comprovamos que la tecla presionada sea 'q'
        cv2.destroyAllWindows()             # Cerramos todas las ventanas
    else:
        None                                
    return None                             

def visualise_image ( img , title ) :
    cv2.imshow(title, img)                  # Mostramos la imagen con su respectivo título
    return None                             

def flip_image ( img ) : 
    img_reflected = cv2.flip(img,1)         # Aplicamos a la imagen una vuelta, de manera que quede invertida respecto al eje vertical
    return img_reflected                    # (1 indica vuelta en horizontal)

def translate_image ( img ) :
    img_translated = img
    M = np.float32([                        # Matrix de transformación de tipo flotante de 32 bits
        [1, 0, 50],                         # Traslación en X
        [0, 1, 0]                           # Traslación en Y
    ])

    img_translated = cv2.warpAffine(img_translated,M,(img.shape[1],img.shape[0])) # Función que aplica una transformada a una imagen
    return img_translated                   # 1:ancho, 0:alto. Nos regresa la imagen trasladada 

def rotate_image ( img ) :
    img_rotated = img   

    (height, width) = img_rotated.shape[:2] # Tomamos solo 2 elementos de la imagen (altura y ancho), el 3ero es el canal de color
    center = (width / 2, height / 2)        

    angle = 45                              # Grados de rotación
    scale = 1.0                             # Escala de 1 (no cambia)
    matrix = cv2.getRotationMatrix2D(center, angle, scale)  # Función para obtener matriz de rotación
    img_rotated = cv2.warpAffine(img_rotated, matrix, (width, height)) 
    
    return img_rotated

def read_image ( filename ) :
    img = cv2.imread(filename)              # Leemos el archivo de la imagen

    if img is None:
        print(f"Error, the image could not be read")
        sys.exit(1)
    else:
        return img

def parser_user_data() :
    parser = argparse.ArgumentParser(description="Parse user input.")   # Objeto que analiza y define los argumentos de entrada
    parser.add_argument('--input_image', type=str, help='Path to the input image.')  # Argumento que indica la ruta de la imagen
    args = parser.parse_args()              # Función para obtener valores de los argumentos

    return args

def run_pipeline():
    args = parser_user_data()
    img = read_image(args.input_image)
    img_rotated = rotate_image ( img )
    img_translated = translate_image ( img )
    img_reflected = flip_image ( img )
    visualise_image ( img , title = ' Input image ')
    visualise_image ( img_rotated , ' Rotated image ')
    visualise_image ( img_translated , ' Translated image ')
    visualise_image ( img_reflected , ' Reflected image ')
    close_windows ()
    print ( ' Program finished ! \ n ')

if __name__ == "__main__":
    run_pipeline()