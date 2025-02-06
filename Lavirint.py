#Igraš kao avanturista koji mora da pronađe izlaz iz složenog labirinta dok izbegava razne prepreke i prikuplja predmete.

#U ovom primeru koristićemo tkinter za GUI i Pillow za rad sa slikama. Igra je detaljna i kompleksna 
#i koristiće osnovne funkcionalnosti tkinter-a kao što su Canvas, Label, Button, itd.

# Pillow biblioteka je za rad sa slikama

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GRID_SIZE = 20
CELL_SIZE = 30
NUM_CELLS_X = WINDOW_WIDTH // CELL_SIZE
NUM_CELLS_Y = WINDOW_HEIGHT // CELL_SIZE


COLOR_WALL = 'black'
COLOR_PATH = 'white'
COLOR_PLAYER = 'blue'
COLOR_ITEM = 'green'
COLOR_EXIT = 'red'

class MazeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Lavirint")
        self.canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg=COLOR_PATH)
        self.canvas.pack()

        self.player_pos = [1, 1]
        self.exit_pos = [NUM_CELLS_X - 2, NUM_CELLS_Y - 2]
        self.items = []
        self.walls = []
        self.create_maze()
        self.draw_maze()

       
        self.root.bind("<KeyPress>", self.move_player)

        self.score = 0
        self.score_label = tk.Label(root, text=f"Poeni: {self.score}", font=("Arial", 16))
        self.score_label.pack()

    def create_maze(self):
        for x in range(NUM_CELLS_X):
            for y in range(NUM_CELLS_Y):
                if random.random() < 0.2:  
                    if (x, y) != tuple(self.player_pos) and (x, y) != tuple(self.exit_pos):
                        self.walls.append((x, y))
                elif random.random() < 0.1: 
                    if (x, y) != tuple(self.player_pos) and (x, y) != tuple(self.exit_pos):
                        self.items.append((x, y))

    def draw_maze(self):
        self.canvas.delete("all")
        for (x, y) in self.walls:
            self.canvas.create_rectangle(x * CELL_SIZE, y * CELL_SIZE,
                                         (x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE,
                                         fill=COLOR_WALL)
       
        for (x, y) in self.items:
            self.canvas.create_rectangle(x * CELL_SIZE, y * CELL_SIZE,
                                         (x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE,
                                         fill=COLOR_ITEM)

        ex, ey = self.exit_pos
        self.canvas.create_rectangle(ex * CELL_SIZE, ey * CELL_SIZE,
                                     (ex + 1) * CELL_SIZE, (ey + 1) * CELL_SIZE,
                                     fill=COLOR_EXIT)

       
        px, py = self.player_pos
        self.canvas.create_rectangle(px * CELL_SIZE, py * CELL_SIZE,
                                     (px + 1) * CELL_SIZE, (py + 1) * CELL_SIZE,
                                     fill=COLOR_PLAYER)

    def move_player(self, event):
        key = event.keysym
        if key == "Up":
            new_pos = [self.player_pos[0], self.player_pos[1] - 1]
        elif key == "Down":
            new_pos = [self.player_pos[0], self.player_pos[1] + 1]
        elif key == "Left":
            new_pos = [self.player_pos[0] - 1, self.player_pos[1]]
        elif key == "Right":
            new_pos = [self.player_pos[0] + 1, self.player_pos[1]]
        else:
            return

     
        if (0 <= new_pos[0] < NUM_CELLS_X and
            0 <= new_pos[1] < NUM_CELLS_Y and
            tuple(new_pos) not in self.walls):
            self.player_pos = new_pos
                
            if tuple(new_pos) in self.items:
                self.items.remove(tuple(new_pos))
                self.score += 10
                self.score_label.config(text=f"Poeni: {self.score}")
                
            if tuple(new_pos) == tuple(self.exit_pos):
                messagebox.showinfo("Pobeda!", "Pobedio si!")
                self.root.quit()

            self.draw_maze()

def main():
    root = tk.Tk()
    game = MazeGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
    
#Inicijalizacija: Postavljamo osnovne dimenzije prozora i veličine ćelija labirinta. Definišemo boje za zidove, put, igrača, predmete i izlaz.

#MazeGame Klasa:

#__init__: Postavljamo GUI, pravimo labirint i crtamo ga na ekranu.
#create_maze: Randomizujemo zidove i predmete. Zidovi i predmeti ne mogu biti na početnoj ili krajnjoj poziciji.
#draw_maze: Crtamo zidove, predmete, izlaz i igrača na Canvas.
#move_player: Pomera igrača na osnovu pritisnutih tastera i proverava sudare sa zidovima i predmete. Ako igrač dođe do izlaza, prikazuje pobedničku poruku.
#Pokretanje igre: main funkcija pokreće GUI i igru.
