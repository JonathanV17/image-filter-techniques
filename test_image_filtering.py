# Importamos librerías estándar
import numpy as np      
import argparse         
import cv2              
import sys 

from Modules import cvlib as cvl

def parser_user_data():
    parser = argparse.ArgumentParser(description="Apply image filtering.")   # Objeto que analiza y define los argumentos de entrada
    parser.add_argument('--input_image', type=str, help='Path to the input image.')  # Argumento que indica la ruta de la imagen
    parser.add_argument('--filter_name', type=str, help='Filter name used as Kernel'
                        '[Median, Average, Gaussian]')  # Argumento que indica el tipo de filtro
    args = parser.parse_args()              # Función para obtener valores de los argumentos
    return args

def filter_median(img):
    median = cv2.medianBlur(img, 5)
    return median

def filter_average(img):
    average = cv2.blur(img, (5,5))
    return average 

def filter_gaussian(img):
    gaussian = cv2.GaussianBlur(img, (5,5), 10) # ksize, sigmaX
    return gaussian

def run_pipeline():
    args = parser_user_data()
    img = cvl.read_image(args.input_image)

    median = None
    average = None
    gaussian = None

    if args.filter_name == "Median":
        median = filter_median(img)
    elif args.filter_name == "Average":
        average = filter_average(img)
    elif args.filter_name == "Gaussian":
        gaussian = filter_gaussian(img)
    else:
        print("Invalid filter name. Try with [Median, Average, Gaussian]") 
        sys.exit(1)
    
    cvl.visualise_image ( img , title = ' Input image ')
    if median is not None:
        cvl.visualise_image ( median , title = ' Median image ')
    if average is not None:
        cvl.visualise_image ( average , title = ' Average image ')
    if gaussian is not None:
        cvl.visualise_image ( gaussian , title = ' Gaussian image ')
    cvl.close_windows()
    print('Program finished!\n')
    
if __name__ == "__main__":
    run_pipeline()