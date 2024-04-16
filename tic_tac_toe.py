from tkinter import Event, Grid, Tk
from game_board import Game

root = Tk()
height = 600
width = 600
root.geometry(f'{height}x{width}')
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)
    
def quit(event=None):
    # modify so it saves on close
    root.destroy()

#Create the gameboard
game = Game(root, rows_columns=3)
game.create_grid_buttons() 

root.bind('<Escape>', quit)
root.mainloop()