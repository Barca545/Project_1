from tkinter import Frame, Label, Tk,Button

class Game:
    def __init__(self, root: Tk, rows_columns:int) -> None:
        # Columns and rows must be equal
        self.rows_columns = rows_columns
        self.cells = []
        self.turn = "X"
        self.moves = {}
        self.move = 0
        self.frame = Frame(root)
        self.over = False
        self.winner = ""
        
        #Configure frame
        self.frame.grid(row=0, column=0, sticky="news")

        # Pad the cell list 
        for index in range(0,(self.rows_columns**2)):
            self.cells.append("*")         

    def create_grid_buttons(self, event=None):
        """Create the 'cells' (buttons) for users to interact with."""
        # Configure the frame's grid
        self.frame.grid_rowconfigure(tuple(range(0,self.rows_columns)), weight=1)
        self.frame.grid_columnconfigure(tuple(range(0,self.rows_columns)), weight=1)
        
        # Fill out the grid with buttons
        for row in range(0,self.rows_columns):
            for col in range(0,self.rows_columns):
                btn = Button(self.frame, text=" ", **button_style, command=lambda row=row, col=col: self.place_piece(row,col))
                btn.grid(row=row, column=col, sticky="news")
        
        #Configure frame
        self.frame.grid(row=0, column=0, sticky="news")

    def place_piece(self, row, col):
        # Check the cell is within bounds and if the cell occupied
        # This check is actually unnecessary as the buttons' indices only go from 0-24
        # and the get_cell_index method can't produce a number > 24
        index = self.get_cell_index(row,col)
        if index <= ((self.rows_columns**2-1)) and self.cells[index]=="*":
            btn = Button(self.frame, text=f"{self.turn}", **button_style)
            btn.grid(row=row, column=col, sticky="nsew")
            
            # Update the move log
            self.cells[index] = self.turn
            self.moves[f"Move {self.move}, Player: {self.turn}"] = self.cells_to_string()
            self.move += 1

            # Check for a winner
            self.update_winner()
            print(self.over)
            if self.over:
                # Display a message saying who the winner is 
                # Save the game
                self.show_winner()

            # Change the current player
            if self.turn == "X":
                self.turn = "O"
                return
            if self.turn == "O":
                self.turn = "X"
                return             

    def update_winner(self):
        # Check the horizontal 
        winner = self.check_row()
        print(winner)
        if winner !=None:
            self.winner = winner
            self.over = True
        # Check vertical
        winner = self.check_col()
        if winner !=None:
            self.winner = winner
            self.over = True
        # Check diagonal
        winner = self.check_positive_diagonal()
        if winner !=None:
            self.winner = winner
            self.over = True
        winner = self.check_negative_diagonal()
        if winner !=None:
            self.winner = winner
            self.over = True
        # Check tie
        if self.is_tie():
            self.winner = "Tie"
            self.over = True

    def check_row(self, row=0) -> str:
        """Checks whether a player has formed a row of their pieces.
        If no connections have been made, returns `None`."""
        test = self.cells[self.get_cell_index(row, 0)]
        # Skip to the next row if text is a "*"
        if test == "*":
            # If the row is not the final row, recur the function
            if row != self.rows_columns-1:
                return self.check_row(row=row+1)
            else:
                return None

        # Loop through all of the cells in a column and compare them to the first cell 
        for col in range(0,self.rows_columns):
            # If a cell does not equal the first cell
            # and the row is not the final row, recur the function
            next = self.cells[self.get_cell_index(row, col)]
            if next != test:
                if row != self.rows_columns-1:
                   return self.check_row(row=row+1)
                else:
                    return None
        # If the check did not return/recur early, that means a winner has been found
        return test

    def check_col(self, col=0) -> str:
        """Checks whether a player has formed a row of their pieces.
        If no connections have been made, returns `None`."""
        test = self.cells[self.get_cell_index(0, col)]
        # Skip to the next row if text is a "*"
        if test == "*":
            # If the row is not the final row, recur the function
            if col != self.rows_columns-1:
                return self.check_col(col=col+1)
            else:
                return None

        # Loop through all of the cells in a column and compare them to the first cell 
        for row in range(0,self.rows_columns):
            # If a cell does not equal the first cell
            # and the row is not the final row, recur the function
            next = self.cells[self.get_cell_index(row, col)]
            if next != test:
                if col != self.rows_columns-1:
                   return self.check_col(col=col+1)
                else:
                    return None
        # If the check did not return/recur early, that means a winner has been found
        return test 
    
    def check_positive_diagonal(self):
        """Checks whether a player has formed a positive diagonal of their pieces.
        If no connections have been made, returns `None`."""
        test = self.cells[0]
        # Skip to the next row if text is a "*"
        if test == "*":
            return None

        # Loop through all of the cells in a column and compare them to the first cell 
        for row in range(0,self.rows_columns):
            # If a cell does not equal the first cell
            # and the row is not the final row, recur the function
            next = self.cells[self.get_cell_index(row, row)]
            if next != test:
                return None
                    
        # If the check did not return/recur early, that means a winner has been found
        return test
    

    def check_negative_diagonal(self):
        """Checks whether a player has formed a negative diagonal of their pieces.
        If no connections have been made, returns `None`."""
        test = self.cells[self.rows_columns-1]
        # Skip to the next row if text is a "*"
        if test == "*":
            return None

        # Loop through all of the cells in a column and compare them to the first cell 
        for row in range(0,self.rows_columns):
            # If a cell does not equal the first cell
            # and the row is not the final row, recur the function
            next = self.cells[self.get_cell_index(row, self.rows_columns-1-row)]
            if next != test:
                return None
                    
        # If the check did not return/recur early, that means a winner has been found
        return test

    def is_tie(self)->bool:
        """Returns `True` if a tie has occured."""
        # Checks if all cells in the Game are filled.
        # If a winner has not been found and all cells are filled, a tie has occured.
        for cell in self.cells:
            if cell =="*":
                return False
        return True 
    
    def get_cell_index(self, row:int, column:int):
        """Given a cell's row and column numbers, returns its index"""
        index = (row * self.rows_columns) + column
        return index

    def cells_to_string(self) -> str:
        """Create a string representation of the Game's cells."""
        board = ""
        for index in range(0,self.rows_columns**2):
            # If the cell is the last cell in the row concats it to the string with a linebreak
            if index % self.rows_columns == 0 and index != 0:
                board += "\n" + self.cells[index]
            # Otherwise just concat the strings
            else:
                board += self.cells[index]
        return board
    
    def show_winner(self):
        # Empty the frame of the cells
        for cell in self.frame.winfo_children():
            cell.destroy()
        # Display a label indicating the winner
        if self.winner != "Tie":
            label = Label(self.frame, text=f"{self.winner} Won!!")
        else:
            label = Label(self.frame, text=f"{self.winner}")
        # Style the label
        label.pack()
    
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