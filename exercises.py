import re

class Game():
    def __init__(self):
        self.turn = 'X'
        self.tie = False
        self.winner = None
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }

    def play_game(self):
        print("Welcome to Tic-Tac_Toe")
        while self.winner == None or self.tie == False:
            self.render() 
            self.input()
            self.check_for_winner()
            self.check_for_tie()
            self.switch_turn()
            self.print_message()
            if self.winner != None or self.tie == True:
                break
        self.print_board()

    def print_board(self):
        b = self.board
        print(f"""
                A   B   C
            1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
                ----------
            2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
                ----------
            3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)

    def print_message(self):
        if self.tie == True:
            print("Tie Game!")
        elif self.winner:
            print(f"{self.winner} wins the game")
        else: 
            print(f"It's player {self.turn}'s turn!")
    
    def render(self):
        self.print_board()
        self.print_message() 

    def input(self):
        while True: 
            move = input(f"Enter a valid move (example A1): ").lower() 
            move_pattern = r'[abc][123]'
            match = re.match(move_pattern, move)

            if match:
                self.board[move] = self.turn
                break
       

    def check_for_winner(self):
        if self.board['a1'] and (self.board['a1'] == self.board['b1'] == self.board['c1']): self.winner = self.board['a1']
        if self.board['a2'] and (self.board['a2'] == self.board['b2'] == self.board['c2']): self.winner = self.board['a2']
        if self.board['a3'] and (self.board['a3'] == self.board['b3'] == self.board['c3']): self.winner = self.board['a3']
        if self.board['a1'] and (self.board['a1'] == self.board['a2'] == self.board['a3']): self.winner = self.board['a1']
        if self.board['b1'] and (self.board['b1'] == self.board['b2'] == self.board['b3']): self.winner = self.board['b1']
        if self.board['c1'] and (self.board['c1'] == self.board['c2'] == self.board['c3']): self.winner = self.board['c1']
        if self.board['a1'] and (self.board['a1'] == self.board['b2'] == self.board['c3']): self.winner = self.board['a1']
        if self.board['c1'] and (self.board['c1'] == self.board['b2'] == self.board['a3']): self.winner = self.board['c1']

    def check_for_tie(self):
        for cell, val in self.board.items():
            if val == None: return 
        if self.winner == None: self.tie = True

    def switch_turn(self):
        next_turn = {
            'O': 'X',
            'X': 'O',
        }
        self.turn = next_turn[self.turn]


game_instance = Game()
game_instance.play_game()