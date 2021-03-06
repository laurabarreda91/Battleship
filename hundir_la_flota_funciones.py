import numpy as np
import random
import os
import pygame
from emoji import emojize
import pandas as pd
from time import sleep

# FUNCIONES DE SONIDO
def play_boat_sound():
    pygame.mixer.Sound.play(pygame.mixer.Sound("boat_sound.wav"))

def play_water_sound():
    pygame.mixer.Sound.play(pygame.mixer.Sound("water_sound.wav"))
    
def play_octopus_sound():
    pygame.mixer.Sound.play(pygame.mixer.Sound("octopus_sound.wav"))


# FUNCION INICIAR TABLERO
def board_starter():
    board = np.full((10,10), fill_value="\U000026AA")
    return board


# FUNCION COLOCAR PULPO
def place_octopus(board):
    octopus_positioned = False
    while octopus_positioned == False:
        column = random.randint(0, 9)
        row = random.randint(0, 9)
        octopus_position = (row, column)
        if board[octopus_position] != "\U000026F5":
            board[octopus_position] = "\U0001F419"
            octopus_positioned = True


# FUNCION ELEGIR QUE BARCO QUIERES COLOCAR

def choose_boat(available_boats):
    sleep(1)
    for index, boat in enumerate(available_boats):
        print(index, boat)
    sleep(1)
    index = int(input("\nEnter the number of the boat you want to place: "))
    while 0 > index or index > 10:
        index = int(input("\nWrong number, enter a valid number: "))
    chosen_boat = available_boats[index]
    available_boats.pop(index)
    sleep(1)
    print("\nYou chose the boat:" , chosen_boat, "\n")
    return chosen_boat



# FUNCION ELEGIR BARCO RANDOM 

def choose_random_boat(available_boats_random):
    if len(available_boats_random) == 1:
        chosen_boat = available_boats_random[0]
        available_boats_random.pop(0)
        return chosen_boat
    else:
        index = random.randint(0,(len(available_boats_random)-1))
        chosen_boat = available_boats_random[index]
        available_boats_random.pop(index)
    return chosen_boat
    

# FUNCION DEFINIR COORDENADAS BARCO INDIVIDUAL

def define_boat_position(board,chosen_boat):

    chosen_boat = len(str(chosen_boat))
    position_defined = False

    while position_defined == False:
        sleep(1)
        column = int(input("Enter the number of the starting position column: "))
        while 0 > column or column > 10:
            column = int(input("\nWrong number, enter a number from 0 to 9"))
        row = int(input("\nEnter the number of the starting position row: "))
        while 0 > row or row > 10:
            row = int(input("\nWrong number, enter a number from 0 to 9"))
        boat_position = (row, column)
        sleep(1)
        print("\nThe starting position is:" , boat_position, "\n")
        if board[boat_position] != "\U000026F5":
            position_defined = True
        else:
            print("There is already a boat in this cell, please pick a different one \n")
    return boat_position,column,row


# FUNCION DEFINIR COORDENADAS BARCO INDIVIDUAL RANDOM

def define_boat_position_random(board,chosen_boat):

    chosen_boat = len(str(chosen_boat))
    position_defined = False

    while position_defined == False:
        column = random.randint(0, 9)
        while 0 > column or column > 10:
            column = random.randint(0, 9)
        row = random.randint(0, 9)
        while 0 > row or row > 10:
            row = random.randint(0, 9)
        boat_position = (row, column)
        if board[boat_position] != "\U000026F5":
            position_defined = True
    return boat_position,column,row


# FUNCION PEDIR DIRECCI??N BARCO INDIVIDUAL AL USUARIO

def choose_direction(board,chosen_boat):

    boat_position,column,row = define_boat_position(board,chosen_boat)

    column = int(column)
    row = int(row)
    chosen_boat = len(str(chosen_boat))

    sleep(1)
    if (9 - column) < chosen_boat:
        if (9 - row) < chosen_boat:
            print("Available positions: North or West \n")
            sleep(1)
            direction = input("Enter N for North or W for West: ")
        elif (row) < chosen_boat: 
            print("Available positions: South or West \n")
            sleep(1)
            direction = input("Enter S for South or W for West: ")
        else:
            print("Available positions: North, South or West \n")
            sleep(1)
            direction = input("Enter N for North, S for South or W for West: ")
    elif (column) < chosen_boat:
        if (row) < chosen_boat:
            print("Available positions: South or East \n")
            sleep(1)
            direction = input("Enter S for South or E for East: ")
        elif (9 - row) < chosen_boat:
            print("Available positions: North or West \n")
            sleep(1)
            direction = input("Enter N for North or W for West: ")
        else: 
            print("Available positions: North, South or East \n")
            sleep(1)
            direction = input("Enter N for North, S for South or E for East: ")
    elif (9 - row) < chosen_boat: 
        print("Available positions: North or West \n")
        sleep(1)
        direction = input("Enter N for North, E for East or W for West: ")
    elif (row) < chosen_boat: 
            print("Available positions: South, East or West \n")
            sleep(1)
            direction = input("Enter S for South, E for East or W for West: ")
    else:
        print("Available positions: North, South, East or West \n")
        sleep(1)
        direction = input("Enter N for North, S for South, E for East or W for West: ")
        

    return direction, boat_position, column, row


# FUNCI??N DEFINIR DIRECCI??N RANDOM

def choose_direction_random(board,chosen_boat):

    boat_position,column,row = define_boat_position_random(board,chosen_boat)

    column = int(column)
    row = int(row)
    chosen_boat = len(str(chosen_boat))

    direction_list = ["North", "South", "East", "West"]

    if (9 - column) < chosen_boat:
        if (9 - row) < chosen_boat:
            direction_list.remove("South")
            direction_list.remove("East")
            direction = random.choice(direction_list)
        elif (row) < chosen_boat: 
            direction_list.remove("North")
            direction_list.remove("East")
            direction = random.choice(direction_list)
        else:
            direction_list.remove("East")
            direction = random.choice(direction_list)
    elif (column) < chosen_boat:
        if (row) < chosen_boat:
            direction_list.remove("North")
            direction_list.remove("West")
            direction = random.choice(direction_list)
        elif (9 - row) < chosen_boat:
            direction_list.remove("South")
            direction_list.remove("East")
            direction = random.choice(direction_list)
        else: 
            direction_list.remove("West")
            direction = random.choice(direction_list)
    elif (9 - row) < chosen_boat: 
        direction_list.remove("South")
        direction = random.choice(direction_list)
    elif (row) < chosen_boat: 
        direction_list.remove("North")
        direction = random.choice(direction_list)
    else:
        direction = random.choice(direction_list)

    return direction, boat_position, column, row


# FUNCION COLOCAR BARCO INDIVIDUAL

def place_single_boat(board,chosen_boat,boat_position_list):

    direction, boat_position, column, row = choose_direction(board,chosen_boat)

    boat_position = [(boat_position)]
    column = int(column)
    row = int(row)
    chosen_boat = len(str(chosen_boat))
    sleep(1)
    print("\nPlacing boat in direction" , direction, "and position" , boat_position, "\n")

    while len(boat_position) < chosen_boat:
    
        if direction == "N":
            row = row - 1
        elif direction == "S":
            row = row + 1
        elif direction == "E":
            column = column + 1
        elif direction == "W":
            column = column - 1

        boat_position.append((row, column))

    for elem in boat_position:
        board[elem] = "\U000026F5"

    sleep(1)
    print(pd.DataFrame(board), "\n")
    sleep(1)
    print("Your boat has been placed \n")
    return board


# FUNCION COLOCAR BARCO M??QUINA

def place_single_boat_random(board,chosen_boat, boat_position_list):
    
    boat_has_been_placed = False

    while boat_has_been_placed == False:
        direction, boat_position, column, row = choose_direction_random(board,chosen_boat)
        boat_position = [(boat_position)]
        column = int(column)
        row = int(row)
        chosen_boat = len(str(chosen_boat))

        while len(boat_position) < chosen_boat:
        
            if direction == "North":
                row = row - 1
            elif direction == "South":
                row = row + 1
            elif direction == "East":
                column = column + 1
            elif direction == "West":
                column = column - 1

            boat_position.append((row, column))

        for elem in boat_position:
            if elem in boat_position_list:
                boat_position.pop[0]
        if len(boat_position) == chosen_boat:
            boat_position_list.append(boat_position)
            for elem in boat_position:
                board[elem] = "\U000026F5"
            boat_has_been_placed = True
    return board


# FUNCION COLOCAR TODOS LOS BARCOS

def place_all_boats(board, available_boats,boat_position_list):
    sleep(1)
    print("Would you like to place your boats manually or random? \n")
    sleep(1)
    manual_or_random = input("Enter M for manually or R for random: ")
    if manual_or_random == "M":
        while len(available_boats) > 0:
            chosen_boat = choose_boat(available_boats)
            place_single_boat(board, chosen_boat, boat_position_list)
    elif manual_or_random == "R":
        place_all_boats_random(board,available_boats, boat_position_list)
        print("\nPlacing your boats \n")
        sleep(1)
        print(pd.DataFrame(board), "\n")

# FUNCION COLOCAR TODOS LOS BARCOS RANDOM

def place_all_boats_random(board, available_boats, boat_position_list):
    while len(available_boats) > 0:
        chosen_boat = choose_random_boat(available_boats)
        place_single_boat_random(board, chosen_boat, boat_position_list)


# FUNCI??N SELECCIONAR MODO DE DISPARO

def define_shooting_mode():
    print("Would you like to choose your shooting position or do you want to shoot randomly? \n")
    sleep(1)
    shooting_mode = input("Enter M for manual or R for random: ")
    sleep(1)
    return shooting_mode

# FUNCI??N SELECCIONAR POSICI??N DISPARO

def define_shooting_target(board):
    target_row = int(input("\nEnter the row where you want to shoot: "))
    target_column = int(input("\nEnter the column where you want to shoot: "))
    target = (target_row, target_column)
    target_octopus = [(target)]
    print(board[target], "\n")
    return target, target_octopus, target_row, target_column

# FUNCI??N SELECCIONAR POSICI??N DISPARO RANDOM

def define_shooting_target_random(board):
    target_row = random.randint(0, 9)
    target_column = random.randint(0, 9)
    target = (target_row, target_column)
    target_octopus = [(target)]
    return target, target_octopus, target_row, target_column


# FUNCI??N RESULTADO DISPARO TOUCHED
def result_shoot_touched(board,board_shooting,target):
    print("Touched \n")
    play_boat_sound()
    board_shooting[target] = "\U0000274C"
    board[target] = "\U0000274C"
    print(pd.DataFrame(board_shooting), "\n")
    return board, board_shooting


# FUNCI??N RESULTADO DISPARO PULPO
def result_shoot_octopus(board,board_shooting,target_row,target_column,target_octopus):
    print("Octopus \n")
    play_octopus_sound()
    if target_row == 0 and target_column == 0:
        target_row = target_row + 1
        target_octopus.append((target_row,target_column))
        target_column = target_column + 1
        target_octopus.append((target_row,target_column))
        target_row = target_row - 1
        target_octopus.append((target_row,target_column))

    elif target_row == 9 and target_column == 0:
        target_row = target_row - 1
        target_octopus.append((target_row,target_column))
        target_column = target_column + 1
        target_octopus.append((target_row,target_column))
        target_row = target_row + 1
        target_octopus.append((target_row,target_column))

    elif target_row == 9 and target_column == 9:
        target_row = target_row - 1
        target_octopus.append((target_row,target_column))
        target_column = target_column - 1
        target_octopus.append((target_row,target_column))
        target_row = target_row + 1
        target_octopus.append((target_row,target_column))

    elif target_row == 0 and target_column == 9:
        target_row = target_row + 1
        target_octopus.append((target_row,target_column))
        target_column = target_column - 1
        target_octopus.append((target_row,target_column))
        target_row = target_row - 1
        target_octopus.append((target_row,target_column))
    elif target_row == 0:
        target_column = target_column - 1
        target_octopus.append((target_row,target_column))
        target_row = target_row + 1
        target_octopus.append((target_row,target_column))
        target_column = target_column + 1
        target_octopus.append((target_row,target_column))
        target_column = target_column + 1
        target_octopus.append((target_row,target_column))
        target_row = target_row - 1
        target_octopus.append((target_row,target_column))
    elif target_row == 9:
        target_column = target_column - 1
        target_octopus.append((target_row,target_column))
        target_row = target_row - 1
        target_octopus.append((target_row,target_column))
        target_column = target_column + 1
        target_octopus.append((target_row,target_column))
        target_column = target_column + 1
        target_octopus.append((target_row,target_column))
        target_row = target_row + 1
        target_octopus.append((target_row,target_column))
    elif target_column == 0:
        target_row = target_row - 1
        target_octopus.append((target_row,target_column))
        target_column = target_column + 1
        target_octopus.append((target_row,target_column))
        target_row = target_row + 1
        target_octopus.append((target_row,target_column))
        target_row = target_row + 1
        target_octopus.append((target_row,target_column))
        target_column = target_column - 1
        target_octopus.append((target_row,target_column))
    elif target_column == 9:
        target_row = target_row - 1
        target_octopus.append((target_row,target_column))
        target_column = target_column - 1
        target_octopus.append((target_row,target_column))
        target_row = target_row + 1
        target_octopus.append((target_row,target_column))
        target_row = target_row + 1
        target_octopus.append((target_row,target_column))
        target_column = target_column + 1
        target_octopus.append((target_row,target_column))
    else:
        target_row = target_row - 1
        target_octopus.append((target_row,target_column))
        target_column = target_column - 1
        target_octopus.append((target_row,target_column))
        target_row = target_row + 1
        target_octopus.append((target_row,target_column))
        target_row = target_row + 1
        target_octopus.append((target_row,target_column))
        target_column = target_column + 1
        target_octopus.append((target_row,target_column))
        target_column = target_column + 1
        target_octopus.append((target_row,target_column))
        target_row = target_row - 1
        target_octopus.append((target_row,target_column))
        target_row = target_row - 1
        target_octopus.append((target_row,target_column))
    for elem in target_octopus:
        board_shooting[elem] = "\U0000274C"
        board[elem] = "\U0000274C"
    print(pd.DataFrame(board_shooting), "\n")
    return board, board_shooting


# FUNCI??N RESULTADO DISPARO AGUA
def result_shoot_water(board, board_shooting, target):
    print("Water \n")
    play_water_sound()
    board_shooting[target] = "\U0001F300"
    board[target] = "\U0001F300"
    print(pd.DataFrame(board_shooting), "\n")
    water = True
    return board, board_shooting, water

# FUNCION DISPAROS USUARIO

def shooting_user(board, board_shooting):

    shooting_mode = define_shooting_mode()
    if shooting_mode == "M":
        water = False

        while water == False:
            if "\U000026F5" in board:
                sleep(1)
                target, target_octopus, target_row, target_column = define_shooting_target(board)

                if board[target] != "\U0000274C" and board[target] != "\U0001F300":

                    if board[target] == "\U000026F5":
                        board, board_shooting = result_shoot_touched(board,board_shooting,target)

                    elif board[target] == "\U0001F419":
                        board, board_shooting = result_shoot_octopus(board,board_shooting,target_row,target_column,target_octopus)
                    else:
                        board, board_shooting, water = result_shoot_water(board, board_shooting, target)
                else:
                    print("You have already shoot to this position, please choose your cell again, \n")
            else:
                water = True
    if shooting_mode == "R":
            shooting_random(board, board_shooting)
    
    return board, board_shooting


# FUNCION DISPAROS MAQUINA

def shooting_random(board,board_shooting):

    water = False

    while water == False:
        if "\U000026F5" in board:
            sleep(1)
            target, target_octopus, target_row, target_column = define_shooting_target_random(board)

            if board[target] != "\U0000274C" and board[target] != "\U0001F300":
                if board[target] == "\U000026F5":
                    board, board_shooting = result_shoot_touched(board,board_shooting,target)

                elif board[target] == "\U0001F419":
                    board, board_shooting = result_shoot_octopus(board,board_shooting,target_row,target_column,target_octopus)

                else:
                    board, board_shooting, water = result_shoot_water(board, board_shooting, target)
        else:
            water = True

        return board, board_shooting