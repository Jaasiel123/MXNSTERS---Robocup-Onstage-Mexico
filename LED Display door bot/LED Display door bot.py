# This code was made for the Robocup 2022 - Onstage.
# Team MXNSTERS - Mexico. Made by Joel Alberto Garza Muñoz 
# LED Display door

import serial
import argparse
from pathlib import Path           
import time                   
                                                      
from PIL import Image, ImageSequence
from rgbmatrix import RGBMatrix, RGBMatrixOptions

def get_frames(path):
    """Returns an iterable of gif frames."""
    frames = []
    with Image.open(path) as gif:
        for frame in ImageSequence.Iterator(gif):                 
            frame = frame.convert('RGB').resize((96, 128))  #Frame of the display
            frames.append(frame)
        return frames

def setup_matrix():
    options = RGBMatrixOptions()
    options.rows = 32
    options.cols = 32
    options.gpio_slowdown = 4                    #configuration of the matrix
    options.chain_length = 3                      
    options.parallel = 3                            
    #options.pixel_mapper_config = 'u-mapper'
    options.hardware_mapping = 'regular'
    
    return RGBMatrix(options=options)
    
    

def display_gif(screen, path):
    #"""Displays gif frames on matrix."""
    for frame in get_frames(path):
        screen.SetImage(frame)
        time.sleep(frame.info['duration']/1000)
        

    
if _name_ == '_main_':
    ser = serial.Serial('/dev/ttyACM0',9600, timeout=1)     #Serial comunication with arduino 
    ser.flush()                                                          
                                                                          
    
    path_to_gif = "/home/pi/Downloads/puerta-azul-recortadagif.gif"
    line = 0
    matrix = setup_matrix()                           #first gif to pop-up
        
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()             #The condition starts 
            print(line)                                                     
        
#Joel´s fingerprints       
        if int(line) == 1:
            #print("RECIBIDO 1")
            path_to_gif = "/home/pi/Downloads/sustosully.gif"                #todos los gifs
                                                                             #conforme
        elif int(line) == 2:                                                 #la persona
            #print("RECIBIDO 2")
            path_to_gif = "/home/pi/Downloads/puerta-boo"
            
        elif int(line) == 4:
            #print("RECIBIDO 4")
            path_to_gif = "/home/pi/Downloads/figuras-azules-minc"
            
        elif int(line) == 5:
            #print("RECIBIDO 5")
            path_to_gif = "/home/pi/Downloads/randal"
            
#Sussy´s fingerprints
            
        elif int(line) == 10:
            #print("RECIBIDO 10")
            path_to_gif = "/home/pi/Downloads/figuras-azules-minc"
        
        elif int(line) == 9:
            #print("RECIBIDO 9")
            path_to_gif = "/home/pi/Downloads/puerta-boo"
        
#Alejandro´s fingerprints
            
        elif int(line) == 3:
            #print("RECIBIDO 3")
            path_to_gif = "/home/pi/Downloads/sustosully.gif"
            
        elif int(line) == 6:
            #print("RECIBIDO 6")
            path_to_gif = "/home/pi/Downloads/randal"
            
        elif int(line) == 8:
            #print("RECIBIDO 8")
            path_to_gif = "/home/pi/Downloads/boo"
        display_gif(matrix, path_to_gif)
            
            
        display_gif(matrix, path_to_gif)