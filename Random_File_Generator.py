import os
import sys
from random import choice
from keyboard import is_pressed
from time import sleep

def Image_Caller():   
    path_loc = f"{sys.path[0]}\Files"

    file_names = os.listdir(path_loc)
    file_chosen = choice(file_names)

    os.system(f"\"{path_loc}\\{file_chosen}\"")
    
    while True:
        if is_pressed("f"):
            file_chosen = choice(file_names)
            os.system(f"\"{path_loc}\\{file_chosen}\"")
        sleep(0.2)

if __name__ == "__main__":
    Image_Caller()
    
    
