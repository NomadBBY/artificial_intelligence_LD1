# Importējiet nepieciešamos moduļus: pip install pygame pip install Tkinter

import pygame          
import tkinter as tk   
from copy import deepcopy   

# Inicializējas pygame modulis
pygame.init()

# RGB krāsu vērtības
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREY = (128, 128, 128)
BLUE = (0, 0, 255)

<<<<<<< HEAD
# Nosaka katra laukuma izmēru 
SQUARE = 800 // 8  

# Ielādē un maina kroņa attēla izmēru
CROWN = pygame.transform.scale(pygame.image.load('AI_LD1\crown.png'), (50, 25))
=======
CROWN = pygame.transform.scale(pygame.image.load('crown.png'), (50, 25))
>>>>>>> 53cb3e40cbdcf8cfb5c26e41673448ea9676a0d6

# Definē funkciju, lai zīmētu dambretes kvadrātus
def draw_squares(game_screen):
    game_screen.fill(BLACK)
    for row in range(8):
        for col in range(row % 2, 8, 2):
            # Aprēķina zīmējamā kvadrāta augšējā kreisā stūra koordinātas
            x = col * SQUARE
            y = row * SQUARE
            # Izveidojiet kvadrātam taisnstūrveida objektu
            rect = pygame.Rect(x, y, SQUARE, SQUARE)
            pygame.draw.rect(game_screen, RED, rect)


# Definē funkciju, lai iegūtu kvadrāta rindu un kolonnu, pamatojoties uz spēlētāja peles pozīciju
def get_row_col_from_mouse(pos):
    # Peles pozīcijas x un y koordinātas
    x, y = pos
    row_index = y // SQUARE
    col_index = x // SQUARE
    return row_index, col_index

# Definē spēles lauka klasi
class Game_Board:

    def __init__(self):
<<<<<<< HEAD
        # Izveido gadījumu mainīgos, lai izsekotu spēles stāvoklim
        self.game_board = []   #Saraksts kas satur sevī spēles galdu 
        self.red_pieces_remaining = self.white_pieces_remaining = 12   # Esošo kauliņu skaits
        self.num_red_kings = self.num_white_kings = 0   # Esošo karaļu skaits
        self.create_board()   

    # Definē rezultāta aprēķināšanas metodi
    def calculate_score(self, king_weight=0.5):  
        #  Aprēķina rezultātu, pamatojoties uz atšķirību starp katras krāsas gabalu skaitu un karaļa figūru skaitu
        return self.white_pieces_remaining - self.red_pieces_remaining + (
                self.num_white_kings * king_weight - self.num_red_kings * king_weight)

    # Definē funkciju, lai iegūtu visus konkrētas krāsas gabalus, kas pašlaik atrodas uz galda
=======
        self.game_board = []
        self.red_pieces_remaining = self.white_pieces_remaining = 12
        self.num_red_kings = self.num_white_kings = 0
        self.create_board()

    def calculate_score(self, king_weight=0.5):  # def evaluate(self):
        return self.white_pieces_remaining - self.red_pieces_remaining + (
                self.num_white_kings * king_weight - self.num_red_kings * king_weight)

>>>>>>> 53cb3e40cbdcf8cfb5c26e41673448ea9676a0d6
    def get_pieces_on_board_by_color(self, color, empty=0):
        # Izveido tukšu sarakstu, lai saglabātu norādītās krāsas gabalus
        pieces_on_board = []
        for rows in self.game_board:
            for piece in rows:
                # Ja kauliņu saraksts nav tukšs un ir pareizā krāsā, pievienojiet to šīs krāsas gabalu sarakstam
                if piece != empty and piece.color == color:
                    pieces_on_board.append(piece)
        return pieces_on_board

<<<<<<< HEAD
    # Define a class for the game board

    def __init__(self):
        # Initialize instance variables to keep track of the state of the game
        self.game_board = []   # list to store the game board
        self.red_pieces_remaining = self.white_pieces_remaining = 12   # number of pieces of each color remaining on the board
        self.num_red_kings = self.num_white_kings = 0   # number of king pieces of each color on the board
        self.create_board()   # create the initial game board

    # Define a function to calculate the score of the game board for the next move
    def evaluate_next_move(self, weight=0.5):
        # Calculate the score based on the difference between the number of pieces of each color and the number of king pieces
        return self.white_pieces_remaining - self.red_pieces_remaining + (self.num_white_kings * weight - self.num_red_kings * weight)

    # Define a function to get all the pieces of a certain color currently on the board
    def get_all_pieces(self, color):
        # Create an empty list to store the pieces of the specified color
        pieces = []
        # Loop over each row of the board
        for row in self.game_board:
            # Loop over each piece in the row
            for piece in row:
                # If the piece is not empty and is the correct color, add it to the list of pieces of that color
                if piece != 0 and piece.color == color:
                    pieces.append(piece)
        # Return the list of pieces of the specified color
        return pieces

    # Define a function to get all available moves for a specified piece on the board
    def available_moves(self, piece, row_index, col_index):
        # Update the game board with the specified move
=======
    def evaluate_next_move(self, weight = 0.5):
        return self.white_pieces_remaining - self.red_pieces_remaining + (self.num_white_kings * weight - self.num_red_kings * weight)

    def get_all_pieces(self, color):
        pieces = []
        for row in self.game_board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)
        return pieces

    def available_moves(self, piece, row_index, col_index):

>>>>>>> 53cb3e40cbdcf8cfb5c26e41673448ea9676a0d6
        self.game_board[piece.row_index][piece.col_index], self.game_board[row_index][col_index] = \
            self.game_board[row_index][col_index], self.game_board[piece.row_index][piece.col_index]
        # Move the piece to its new location
        piece.move(row_index, col_index)

        # If the piece has reached the opposite end of the board, make it a king
        if row_index == 8 - 1 or row_index == 0:
            piece.make_king()
            if piece.color == WHITE:
                self.num_white_kings += 1
            else:
                self.num_red_kings += 1

        # This function returns the game piece at a given row and column index in the game board.
    def get_piece(self, row, col):
        return self.game_board[row][col]
    
    # This function creates the game board by appending lists to the game_board list, 
    # and adding game pieces or None values to the sublists based on the row and column indices.
    def create_board(self, none=0):
        for rows in range(8):
            self.game_board.append([])
            for col in range(8):
                # If the column index is odd and the row index is even, or if the column index is even and the row index is odd,
                # add a game piece if the row index is less than 3 or greater than 4, or a None value otherwise.
                if col % 2 == ((rows + 1) % 2):
                    if rows < 3:
                        self.game_board[rows].append(Game_piece(rows, col, WHITE))
                    elif rows > 4:
                        self.game_board[rows].append(Game_piece(rows, col, RED))
                    else:
                        self.game_board[rows].append(none)
                else:
                    self.game_board[rows].append(none)
    
    # This function draws the game board by calling the draw_squares function and 
    # drawing game pieces on the screen based on their positions on the game board.
    def draw_game(self, game_screen, empty=0):
        draw_squares(game_screen)
        for rows in range(8):
            for cols in range(8):
                game_piece = self.game_board[rows][cols]
<<<<<<< HEAD
                # If the game piece is not None, draw it on the screen.
                if game_piece != empty:
                    game_piece.draw_piece(game_screen)
    
    # This function removes a game piece from the game board by setting its position to None,
    # and updates the number of remaining pieces of each color accordingly.
=======
                if game_piece != empty:
                    game_piece.draw_piece(game_screen)

>>>>>>> 53cb3e40cbdcf8cfb5c26e41673448ea9676a0d6
    def remove_piece(self, pieces, no_piece=0, one_piece=1):
        for piece in pieces:
            self.game_board[piece.row_index][piece.col_index] = no_piece
            if piece != no_piece:
                if piece.color == RED:
                    self.red_pieces_remaining -= one_piece
                else:
                    self.white_pieces_remaining -= one_piece
    
    # This function checks which player has won the game based on the number of remaining pieces of each color.
    # If red has no remaining pieces, white wins. If white has no remaining pieces, red wins.
    # Otherwise, the game is not over and None is returned.
    def get_winner(self, no_piece=0):
        if self.red_pieces_remaining <= no_piece:
            return WHITE
        elif self.white_pieces_remaining <= no_piece:
            return RED
        else:
            return None
<<<<<<< HEAD
    
    # This function returns a dictionary of valid moves for a given game piece.
    # The valid moves are determined by calling the traverse_left and traverse_right functions
    # with the appropriate arguments based on the color and position of the game piece.
=======

>>>>>>> 53cb3e40cbdcf8cfb5c26e41673448ea9676a0d6
    def get_valid_moves(self, piece):
        valid_moves = {}
        left_col = piece.col_index - 1
        right_col = piece.col_index + 1
        current_row = piece.row_index
    
        # If the game piece is red or a king, update valid_moves with valid moves to the left and right diagonally upwards.
        if piece.color == RED or piece.is_king:
            valid_moves.update(
                self.traverse_left(current_row - 1, max(current_row - 3, -1), -1, piece.color, left_col))
            valid_moves.update(
                self.traverse_right(current_row - 1, max(current_row - 3, -1), -1, piece.color, right_col))
        
        # If the game piece is white or a king, update valid_moves with valid moves to the left and right diagonally downwards.
        if piece.color == WHITE or piece.is_king:
            valid_moves.update(self.traverse_left(current_row + 1, min(current_row + 3, 8), 1, piece.color, left_col))
            valid_moves.update(
                self.traverse_right(current_row + 1, min(current_row + 3, 8), 1, piece.color, right_col))
    
        return valid_moves


    def traverse_left(self, start_row, stop_row, row_step, color, start_col, skipped=None):
        if skipped is None:
            skipped = []
        moves = {}
        last_piece = []
        for r in range(start_row, stop_row, row_step):
            if start_col < 0:
                break

            current_piece = self.game_board[r][start_col]
            if current_piece == 0:
                if skipped and not last_piece:
                    break
                elif skipped:
                    moves[(r, start_col)] = last_piece + skipped
                else:
                    moves[(r, start_col)] = last_piece

                if last_piece:
                    if row_step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, 8)
                    moves.update(
                        self.traverse_left(r + row_step, row, row_step, color, start_col - 1, skipped=last_piece))
                    moves.update(
                        self.traverse_right(r + row_step, row, row_step, color, start_col + 1, skipped=last_piece))
                break
            elif current_piece.color == color:
                break
            else:
                last_piece = [current_piece]

            start_col -= 1

        return moves

    def traverse_right(self, start_row, stop_row, row_step, color, start_col, skipped=None):
        if skipped is None:
            skipped = []
        moves = {}
        last_piece = []
        for r in range(start_row, stop_row, row_step):
            if start_col >= 8:
                break

            current_piece = self.game_board[r][start_col]
            if current_piece == 0:
                if skipped and not last_piece:
                    break
                elif skipped:
                    moves[(r, start_col)] = last_piece + skipped
                else:
                    moves[(r, start_col)] = last_piece

                if last_piece:
                    if row_step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, 8)
                    moves.update(
                        self.traverse_left(r + row_step, row, row_step, color, start_col - 1, skipped=last_piece))
                    moves.update(
                        self.traverse_right(r + row_step, row, row_step, color, start_col + 1, skipped=last_piece))
                break
            elif current_piece.color == color:
                break
            else:
                last_piece = [current_piece]

            start_col += 1

        return moves


# Definē metodi kas atbild par kauliņu un tā kustībām
class Game_piece:
    # Konstantes
    PIECE_PADDING = 15
    OUTLINE_COLOR = (128, 128, 128)
    PIECE_OUTLINE = 2

    # Klases inicializācijas metode
    def __init__(self, row_index, col_index, color):
        self.row_index = row_index
        self.col_index = col_index
        self.color = color
        self.is_king = False
        self.x_pos = 0
        self.y_pos = 0
        self.calculate_position() #Atrod kauliņa atrašanas vietu uz spēles galda

    # Metode, kā aprēķināt figūras pozīciju uz spēles galda
    def calculate_position(self):
        self.x_pos = SQUARE * self.col_index + SQUARE // 2
        self.y_pos = SQUARE * self.row_index + SQUARE // 2

    # Metode kas atbild par karaļu kauliņiem
    def make_king(self):
        if not self.is_king:
            self.is_king = True

    # Metode kas atbild par kauliņa zimēšanu uz spēles galda
    def draw_piece(self, window):
        radius = SQUARE // 2 - self.PIECE_PADDING
        pygame.draw.circle(window, self.OUTLINE_COLOR, (self.x_pos, self.y_pos), radius + self.PIECE_OUTLINE)
        pygame.draw.circle(window, self.color, (self.x_pos, self.y_pos), radius)
        # Ja kauliņš ir karalis:
        if self.is_king:
            crown_x = self.x_pos - CROWN.get_width() // 2
            crown_y = self.y_pos - CROWN.get_height() // 2
            window.blit(CROWN, (crown_x, crown_y))

    # Kustību metode kauliņien
    def move(self, row, col):
        self.row_index = row
        self.col_index = col
        # Pārēķina atribūtus x_pos un y_pos, pamatojoties uz jaunajām rindu un kolonnu pozīcijām
        self.calculate_position()

    # Definē __repr__ metodi Game_piece klasei
    def __repr__(self):
        return str(self.color)


# Spēles loģikas klase
class Main_game:

    def __init__(self, game_window, player_color):
        # Inicializējiē valid_moves, turn, board un atlasītos atribūtus uz None
        self.valid_moves = None
        self.turn = None
        self.board = Game_Board
        self.selected = None
        # Iestata atribūtu game_window uz Pygame displeja virsmu, kas nodota kā arguments
        self.game_window = game_window
        # Iestata atribūtu player_color uz krāsu, kas nodota kā arguments
        self.player_color = player_color
        # Izsauc initialize_game metodi, lai inicializētu spēli
        self.initialize_game()

    # Metode kas seko līdzi pieejamajām kustībām
    def update(self):
        self.board.draw_game(self.game_window)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    # Definē initialize_game metodi
    def initialize_game(self):
        self.selected = None
        self.board = Game_Board()
        self.turn = RED if self.player_color == "red" else WHITE
        self.valid_moves = {}

    # Metode kas nosaka uzvarētāju
    def who_won(self):
        # Return the winner of the game by calling the get_winner method of the game board
        return self.board.get_winner()

    # Restarta metode
    def reset_game(self):
        self.initialize_game()

    # Kauliņa izvēles metode
    def select(self, row, col):
        if self.selected:
            result = self.get_move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
        return False
    
    # Metode kas nosaka nakošo kustību
    def get_move(self, row, col):
        piece = self.board.get_piece(row, col)

        # Pārbauda, vai ir atlasīts kauliņš, galamērķis ir tukšs un gājiens ir derīgs
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            # Kauliņš tiek parvietots uz atlasīto gabalu uz norādīto rindu un kolonnu
            self.board.available_moves(self.selected, row, col)

            # Pārbauda, vai gājiena laikā kāds kauliņš netika izlaists, un, ja nepieciešams, noņem to no galda
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove_piece(skipped)

            # Nomaina spēlētāja kārtu
            self.change_turn()

            # True ja viss izdevas, un gājiens der
            return True
        else:
            # False ja gājiens neder
            return False

    def draw_valid_moves(self, moves):
        # Parāda ceļu ko spelētājs var izvēlēties
        for move in moves:
            row, col = move
            # Aprēķina apļa centra koordinātas, pamatojoties uz rindu un kolonnu
            # no derīgā gājiena un katra laukuma lielums uz galda
            pygame.draw.circle(self.game_window, BLUE, (col * SQUARE + SQUARE // 2, row * SQUARE + SQUARE // 2), 15)

    def change_turn(self):
        # Atiestata derīgo gājienu vārdnīcu un maina gājienu uz nākamo spēlētāju
        self.valid_moves = {}
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED

    def get_board(self):
        return self.board

    # Pretinieka gājiens
    def oponent_move(self, board):
        self.board = board
        self.change_turn()

# Sākuma izvēles klase
class PlayerChooser:

    def __init__(self):
        self.color = None  
        self.window = None  

    # Metode kas atbild par spelētāja izvēli
    def choose_player(self):
        def select_player(color):
            self.color = color  
            self.window.destroy() 

        # Izveido izvēles logu
        self.window = tk.Tk()
<<<<<<< HEAD
        self.window.title("Izvēle")
        self.window.geometry("400x200")  

        # Vieta kur saglabāt tekstu
        title_label = tk.Label(self.window, text="Kurš sāk? (Dators/Cilvēks):", font=("Arial", 16))
        title_label.pack(pady=10)  
=======
        self.window.title("Choice")
        self.window.geometry("400x200")

        title_label = tk.Label(self.window, text="Who starts? (Computer/Human):", font=("Arial", 16))
        title_label.pack(pady=10)
>>>>>>> 53cb3e40cbdcf8cfb5c26e41673448ea9676a0d6

        # Izveido vietu kur turēt pogas
        button_frame = tk.Frame(self.window)
        button_frame.pack(pady=10)  

<<<<<<< HEAD
        # Izveido cilvēka pogas izvēli
        red_button = tk.Button(button_frame, text="Cilvēks", bg="red", fg="white", font=("Arial", 14), width=10, height=3,
                               command=lambda: select_player("red"))
        red_button.pack(side=tk.LEFT, padx=10)  

        # Izveido Datora pogas izvēli
        white_button = tk.Button(button_frame, text="Dators", bg="white", fg="black", font=("Arial", 14), width=10,
                                 height=3, command=lambda: select_player("white"))
        white_button.pack(side=tk.LEFT, padx=10)  
=======
        red_button = tk.Button(button_frame, text="Human", bg="red", fg="white", font=("Arial", 14), width=10, height=3,
                               command=lambda: select_color("red"))
        red_button.pack(side=tk.LEFT, padx=10)

        white_button = tk.Button(button_frame, text="Computer", bg="white", fg="black", font=("Arial", 14), width=10,
                                 height=3, command=lambda: select_color("white"))
        white_button.pack(side=tk.LEFT, padx=10)
>>>>>>> 53cb3e40cbdcf8cfb5c26e41673448ea9676a0d6

        self.window.mainloop()  

    # Definē spēlētāja izvēles klasi
    def get_color(self):
        self.choose_player()  
        return self.color  

# Definē MiniMax klasi
class MinMaxSolver:

    def __init__(self, depth_limit, player_color):
        self.max_depth = depth_limit  # Algoritma dziļums
        self.color = player_color  

    # Metode pašam algoritmam
    def algorithm(self, board_state, depth, is_maximizing, game_state):
        # Pārbauda vai dziļums ir atrasts vai dziļuma vertība ir 0
        if depth == 0 or board_state.get_winner() is not None:
            return board_state.evaluate_next_move(), board_state

        # Pārbauda, vai maksimizējam vai minimizējam
        if is_maximizing:
            maxEvaluation = float('-inf')  # Noklusētā maksimālā novērtējuma vērtība ir negatīva bezgalība
            best_path = None
            # Iterē pār visiem iespējamajiem gājieniem pašreizējam spēlētājam
            for move in self.get_all_moves(board_state, self.color, game_state):
                move_evaluation  = self.algorithm(move, depth - 1, False, game_state)[0]  # Rekursīvi novērtē gājienu
                maxEvaluation = max(maxEvaluation, move_evaluation)  # Atjauno maksimālo novērtējumu
                if maxEvaluation == move_evaluation:
                    best_path = move  # Atjauno labāko ceļu, ja pašreizējais gājiens ir ar augstāko novērtējumu

            return maxEvaluation, best_path  # Atgriež maksimālo novērtējumu un labāko ceļu
        else:
            min_evaluation  = float('inf')  # Noklusētā minimālā novērtējuma vērtība ir pozitīva bezgalība
            best_path = None
            # Iterē pār visiem iespējamajiem gājieniem pretiniekam
            for move in self.get_all_moves(board_state, self.get_enemy_color(), game_state):
                move_evaluation  = self.algorithm(move, depth - 1, True, game_state)[0]  # Rekursīvi novērtē gājienu
                min_evaluation  = min(min_evaluation , move_evaluation )  # Atjauno minimālo novērtējumu
                if min_evaluation  == move_evaluation :
                    best_path = move  # Atjauno labāko ceļu, ja pašreizējais gājiens ir ar zemāko novērtējumu

            return min_evaluation , best_path  # Atgriež minimālo novērtējumu un labāko ceļu


<<<<<<< HEAD
    def move(self, selected_piece, move_options, board, game, skip_move):
        # Šī metode saņem atlasītās figūras objektu, move_options tuple ar jauno rindu un kolonnas indeksu,
        # board objektu, kas atspoguļo spēles laukumu, game objektu, kas atspoguļo spēles logu,
        # un skip_move objektu, kas atspoguļo figūras, kas var tikt

        board.available_moves(selected_piece, move_options[0], move_options[1])     

        if skip_move:
            board.remove_piece(skip_move)  # Noņem visus izlaistos kauliņus

        return board  

    def get_all_moves(self, board, color, game):
        
        possible_states = []  

        for piece in board.get_all_pieces(color): 
            valid_moves = board.get_valid_moves(piece)  
            for move, skip in valid_moves.items(): 
                self.draw_moves(game, board, piece)  
                temp_state = deepcopy(board)  
                selected_piece_copy = temp_state.get_piece(piece.row_index, piece.col_index) 
                next_state = self.move(selected_piece_copy, move, temp_state, game, skip)  
                possible_states.append(next_state)  

        return possible_states  # Atgriež visus iespējamos stāvokļus 

    def draw_moves(self, game, board, piece):
        # Šī metode saņem spēles, dēļa un figūras objektus un uz spēles loga zīmē derīgos gājienus figūrai
        # Vispirms tā iegūst figūras derīgos gājienus no dēla, tad atjauno spēles logu, lai rādītu šos gājienus,
        # uzzīmējot apli ap figūru un zīmējot derīgo gājiena indikatorus. Pēc tam atjaunina displeju.

            valid_moves = board.get_valid_moves(piece)  # Iegūst visus derīgos gājienus figūrai no dēla
            board.draw_game(game.game_window)  # Zīmē spēles dēlu uz spēles loga
            pygame.draw.circle(game.game_window, (0,255,0), (piece.x_pos, piece.y_pos), 50, 5)  # Uzzīmē apli ap izvēlēto figūru
            game.draw_valid_moves(valid_moves.keys())  # Zīmē derīgo gājiena indikatorus uz spēles loga
            pygame.display.update()  # Atjaunina displeju

    def get_enemy_color(self):
        # Šī metode atgriež spēlētāja krāsas pretējo krāsu.
        # Ja spēlētāja krāsa ir SARKANA, tā atgriež BALTU, bet ja spēlētāja krāsa ir BALTA, tā atgriež SARKANU.

        if self.color == RED:
            return WHITE
        else:
            return RED
=======
class MinMaxSolver:
    def __init__(self, depth_limit, player_color):
        self.max_depth = depth_limit
        self.color = player_color

    def algorithm(self, board_state, depth, is_maximizing, game_state):
        if depth == 0 or board_state.get_winner() is not None:
            return board_state.evaluate_next_move(), board_state

        if is_maximizing:
            maxEvaluation = float('-inf')
            best_path = None
            for move in self.get_all_moves(board_state, self.color, game_state):
                move_evaluation  = self.algorithm(move, depth - 1, False, game_state)[0]
                maxEvaluation = max(maxEvaluation, move_evaluation)
                if maxEvaluation == move_evaluation:
                    best_path = move

            return maxEvaluation, best_path
        else:
            min_evaluation  = float('inf')
            best_path = None
            for move in self.get_all_moves(board_state, self.get_enemy_color(), game_state):
                move_evaluation  = self.algorithm(move, depth - 1, True, game_state)[0]
                min_evaluation  = min(min_evaluation , move_evaluation )
                if min_evaluation  == move_evaluation :
                    best_path = move
>>>>>>> 53cb3e40cbdcf8cfb5c26e41673448ea9676a0d6

            return min_evaluation , best_path

<<<<<<< HEAD
class main:
    def __init__(self):
        # Iestata spēles logu
        self.WINDOW = pygame.display.set_mode((800, 800))
        pygame.display.set_caption('Artis Čevers 211RDB183')

        # Logs kas ļauj spēlētājam izvēlēties kurš sāk
        valid_colors = ["red", "white"]
        color_chooser = PlayerChooser()
        color = None
        while color not in valid_colors:
            color = color_chooser.get_color()

        if color in valid_colors:
            self.run = True
            self.clock = pygame.time.Clock()
            self.game = Main_game(self.WINDOW, color)

            #  MinimaxSolver ar maksimālo dziļumu un spēlētāja krāsu
            self.solver = MinMaxSolver(3, WHITE)

    def run_game(self):
    # Palaist spēles ciklu līdz spēle ir beigusies
        while self.run:
            self.clock.tick(60)

            # Izmanto MinimaxSolver, lai veiktu AI gājienu, ja tā ir AI kārta
            if self.game.turn == WHITE:
                value, new_board = self.solver.algorithm(self.game.get_board(), self.solver.max_depth, True, self.game)
                self.game.oponent_move(new_board)

            # Pārbaudīt uzvarētāju pēc katras gājiena
            if self.game.who_won() is not None:
                print(self.game.who_won())
                self.run = False

            # Apstrādāt lietotāja notikumus
=======
    def move(self, selected_piece, move_options, board, game, skip_move):
        board.available_moves(selected_piece, move_options[0], move_options[1])
        if skip_move:
            board.remove_piece(skip_move)

        return board

    def get_all_moves(self, board, color, game):
        possible_states  = []

        for piece in board.get_all_pieces(color):
            valid_moves = board.get_valid_moves(piece)
            for move, skip in valid_moves.items():
                self.draw_moves(game, board, piece)
                temp_state  = deepcopy(board)
                selected_piece_copy  = temp_state .get_piece(piece.row_index, piece.col_index)
                next_state  = self.move(selected_piece_copy , move, temp_state , game, skip)
                possible_states .append(next_state )

        return possible_states

    def draw_moves(self, game, board, piece):
        valid_moves = board.get_valid_moves(piece)
        board.draw_game(game.game_window)
        pygame.draw.circle(game.game_window, (0,255,0), (piece.x_pos, piece.y_pos), 50, 5)
        game.draw_valid_moves(valid_moves.keys())
        pygame.display.update()
        #pygame.time.delay(100)

    def get_enemy_color(self):
        if self.color == RED:
            return WHITE
        else:
            return RED

class main:
    def __init__(self):
        self.WINDOW = pygame.display.set_mode((800, 800))
        pygame.display.set_caption('Artis Čevers 211RDB183')

        # Ask the player for their color
        valid_colors = ["red", "white"]
        color_chooser = ColorChooser()
        color = None
        while color not in valid_colors:
            color = color_chooser.get_color()

        if color in valid_colors:
            # Initialize game window here

            self.run = True
            self.clock = pygame.time.Clock()
            self.game = Main_game(self.WINDOW, color)

            # Initialize MinimaxSolver with max depth and player color
            self.solver = MinMaxSolver(3, WHITE)

    def run_game(self):
        while self.run:
            self.clock.tick(60)

            # Use MinimaxSolver to make an AI move
            if self.game.turn == WHITE:
                value, new_board = self.solver.algorithm(self.game.get_board(), self.solver.max_depth, True, self.game)
                self.game.ai_move(new_board)

            # Check for winner after each move
            if self.game.winner() is not None:
                print(self.game.winner())
                self.run = False

>>>>>>> 53cb3e40cbdcf8cfb5c26e41673448ea9676a0d6
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    row, col = get_row_col_from_mouse(pos)
                    self.game.select(row, col)

<<<<<<< HEAD
            # Atjaunināt spēles logu
            self.game.update()
    # Iziet no Pygame
    pygame.quit()

=======
            self.game.update()

        pygame.quit()

>>>>>>> 53cb3e40cbdcf8cfb5c26e41673448ea9676a0d6
if __name__ == '__main__':
    game = main()
    game.run_game()
