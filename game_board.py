from tkinter import BOTH, CENTER, Canvas, Frame, Grid, Tk,Button


class Game:
    def __init__(self, root: Tk, width, height, rows_columns:int) -> None:
        # Columns and rows must be equal
        self.rows_columns = rows_columns
        self.cells = []
        self.turn = "X"
        self.frame = Frame(root,width=width/2, height=height/2,  bg="red")
        self.cell_width = width//(2*rows_columns)
        self.moves = {}
        
        #Configure frame
        self.frame.grid(row=0, column=0, sticky="news")

        # Pad the cells based on the number of rows/columns
        while range(0,(self.rows_columns**2)):
            self.cells.append("0")
            print(0)

    def create_grid_buttons(self, event=None):
        # Configure the frame's grid
        self.frame.grid_rowconfigure(tuple(range(0,self.rows_columns)), weight=1)
        self.frame.grid_columnconfigure(tuple(range(0,self.rows_columns)), weight=1)
        
        # Fill out the grid with buttons
        for row in range(0,self.rows_columns):
            for col in range(0,self.rows_columns):
                index = self.get_cell_index(row,col)     
                print(index)   
                btn = Button(self.frame, **button_style, command=lambda row=row, col=col: self.place_piece(row,col))
                btn.grid(row=row, column=col, sticky="nsew")

    def place_piece(self, row, col):
        # Check the cell is within bounds and if the cell occupied
        # This check is actually unnecessary as the buttons' indices only go from 0-24
        # and the get_cell_index method can't produce a number > 24
        index = self.get_cell_index(row,col)
        if index <= ((self.rows_columns**2-1)) and int(self.cells[index])==0:
            btn = Button(self.frame, text=f"{self.turn}", **button_style, command=lambda row=row, col=col: self.place_piece(row,col))
            btn.grid(row=row, column=col, sticky="nsew")
            self.complete_move(index=index)
        # else:
        #     return False
        
                
    def get_cell_index(self, row:int, column:int):
        """Given a cell's row and column numbers, returns its index"""
        index = (row * self.rows_columns) + column
        return index

    def complete_move(self,index:int):
        self.cells[index] = self.turn
        if self.turn == "X":
            self.turn = "O"
            return
        if self.turn == "O":
            self.turn = "X"
        return   

button_style = {
    "bg": "lightgray",      
    "fg": "black",          
    "activebackground": "gray",  
    "borderwidth": 6,       
    "highlightthickness": 6,  
    "highlightbackground": "black",  
    "highlightcolor": "black"  ,
    "relief":'raised',    
}