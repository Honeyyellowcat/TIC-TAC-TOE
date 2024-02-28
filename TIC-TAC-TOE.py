import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic-Tac-Toe!")
        self.configure(bg='#fff9ef')  # Set background color  

        # Set window dimensions and center it
        window_width = 600
        window_height = 600
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_coordinate = (screen_width - window_width) // 2
        y_coordinate = (screen_height - window_height) // 2
        self.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

        self.current_player = 'X'
        self.game = TicTacToe()
        self.buttons = []
        self.create_board()
        self.create_quit_button()  # Create quit button

    def create_board(self):
        pad_x = 10
        pad_y = 10
        font_size = 20
        font = ("Comic Sans MS", font_size, "bold")  # Change font and style
        
        for i in range(3):
            row_buttons = []
            for j in range(3):
                button = tk.Button(self, text="", width=10, height=3, font=font, bg='#ffbee6', fg='white', relief=tk.FLAT,
                                    command=lambda row=i, col=j: self.on_button_click(row, col))
                button.grid(row=i, column=j, sticky="nsew", padx=pad_x, pady=pad_y)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

    def create_quit_button(self):
        quit_button = tk.Button(self, text="Quit", command=self.quit, bg='#ff9999', fg='white', relief=tk.FLAT,
                                 font=("Comic Sans MS", 16, "bold"), width=10, height=2)
        quit_button.grid(row=4, column=0, columnspan=3, padx=10, pady=(20, 10), sticky="nsew")  # Center the button

    def on_button_click(self, row, col):
        if self.game.make_move(row * 3 + col, self.current_player):
            self.buttons[row][col].config(text=self.current_player)
            if self.game.current_winner:
                messagebox.showinfo("Winner", f"Player {self.game.current_winner} wins!")
                self.reset_game()
            elif self.game.is_board_full():
                messagebox.showinfo("Tie", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def reset_game(self):
        self.current_player = 'X'
        self.game = TicTacToe()
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text='')

class TicTacToe():
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None

    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]

    def print_board(self):
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([s == letter for s in row]):
            return True

        col_ind = square % 3
        col = [self.board[col_ind+i*3] for i in range(3)]
        if all([s == letter for s in col]):
            return True

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([s == letter for s in diagonal2]):
                return True

        return False

    def is_board_full(self):
        return ' ' not in self.board

if __name__ == "__main__":
    app = TicTacToeGUI()
    app.mainloop()
