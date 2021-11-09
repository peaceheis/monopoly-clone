import json

from tkinter.ttk import Style
from constants import BACKGROUND
from tkinter import *

class Board(Frame):
    def __init__(self): 
        self.root = Tk()
        super().__init__()

        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.USABLE_LENGTH= self.SCREEN_WIDTH*.9
        self.PAD_X = self.SCREEN_WIDTH - self.USABLE_LENGTH
        self.PAD_Y = self.SCREEN_HEIGHT - self.USABLE_LENGTH
        

        self.createBoard()
        print(f"{self.PAD_X=}, {self.PAD_Y=}, {self.USABLE_LENGTH=}")

    def createBoard(self): 
        content = Frame(self.root, background="#123456", padx=self.PAD_X, pady=self.PAD_Y)
        style = Style()
        top_left_corner = Frame(content, borderwidth=2, relief="solid", background="#accec4")
        top_right_corner = Frame(content, borderwidth=2, relief="solid", background="#d4cca4")
        bottom_left_corner = Frame(content, borderwidth=2, relief="solid", background="#AAAAAA")
        bottom_right_corner = Frame(content, borderwidth=2, relief="solid", background="#FFFFFF")

        top_rectangles = [Frame(content, borderwidth=2, relief="solid", background=f"#d4cc{i*8+10}") for i in range(9)]
        left_rectangles = [Frame(content, borderwidth=2, relief="solid", background=f"#1dab{i*8+10}") for i in range(9)]
        bottom_rectangles = [Frame(content, borderwidth=2, relief="solid", background=f"#b3c6{i*8+30}") for i in range(9)]
        right_rectangles = [Frame(content, borderwidth=2, relief="solid", background=f"#BBF5{i*8+20}") for i in range(9)]
        
        content.grid(column=0, row=0, sticky=(N, S, E, W))
        top_left_corner.grid(column=0, row=0, sticky=(N, S, E, W))
        top_right_corner.grid(column=10, row=0, sticky=(N, S, W, E))
        bottom_right_corner.grid(column=10, row=10, sticky=(S, N, E, W))
        bottom_left_corner.grid(column=0, row=10, sticky=(S, N, W, E))

        for i, rect in enumerate(top_rectangles): 
            rect.grid(column=i+1, row=0, sticky=(N, S, E, W))


        for i, rect in enumerate(left_rectangles): 
            rect.grid(row=i+1, column=0, sticky=(W, E, N, S))
            minirect = Frame(rect, background="#000000")
            minirect2 = Frame(rect, background="#FFFFFF")
            minirect.grid(row=0, column=0, sticky=(N, E, W))
            minirect2.grid(row=1, column=2)
            rect.columnconfigure(0, weight=1, minsize=15)
            rect.rowconfigure(0, weight=1, minsize=15)

        for i, rect in enumerate(bottom_rectangles): 
            rect.grid(column=i+1, row=10, sticky=(S, N, E, W))

        for i, rect in enumerate(right_rectangles):
            rect.grid(row=i+1, column=10, sticky=(E, W, N, S))

        one_through_nine = [i+1 for i in range(9)]
        self.root.columnconfigure(0, weight=1, minsize=15) 
        content.columnconfigure((0, 10), weight=2, minsize=15)
        content.columnconfigure(one_through_nine, weight=1, minsize=15)
        self.root.rowconfigure(0, weight=1, minsize=15)
        content.rowconfigure((0, 10), weight=2, minsize=15)
        content.rowconfigure(one_through_nine, weight=1, minsize=15)
        
        




    def populate_board(self): 
        pass

def main() : 

    board = Board()
    board.root.geometry(f"{board.SCREEN_WIDTH}x{board.SCREEN_HEIGHT}")
    board.root.mainloop()

if __name__ == '__main__':
    main()
