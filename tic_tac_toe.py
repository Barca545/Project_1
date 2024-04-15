from tkinter import BOTH, Canvas, Event, Grid, Tk
from game_board import Game



root = Tk()
# root.attributes('-fullscreen', True)
height = 800
width = 800
root.geometry(f'{height}x{width}')
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)
    

def quit(event=None):
    root.destroy()

root.bind('<Escape>', quit)


#Create the gameboard
board = Game(root,width=width, height=height, rows_columns=5)
board.create_grid_buttons() 
root.mainloop()