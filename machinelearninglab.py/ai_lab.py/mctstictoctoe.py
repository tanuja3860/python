import math
import random
import sys
ITERATIONS = 1000   
C = 1.41             
WIN_LINES = [
   (0, 1, 2), (3, 4, 5), (6, 7, 8),   
   (0, 3, 6), (1, 4, 7), (2, 5, 8),   
   (0, 4, 8), (2, 4, 6),              
]
def winner(board):
   """Return 'X' or 'O' if someone has won, 'draw' if board is full, else None."""
   for a, b, c in WIN_LINES:
       if board[a] != ' ' and board[a] == board[b] == board[c]:
           return board[a]
   if ' ' not in board:
       return 'draw'
   return None
def legal_moves(board):
   return [i for i, cell in enumerate(board) if cell == ' ']
def other(player):
   return 'O' if player == 'X' else 'X'
def print_board(board, show_numbers=False):
   """Print the board; with show_numbers, empty squares show their number."""
   cells = [str(i) if (show_numbers and cell == ' ') else cell
            for i, cell in enumerate(board)]
   for r in range(3):
       print(' ' + ' | '.join(cells[3 * r:3 * r + 3]))
       if r < 2:
           print('---+---+---')
class Node:
   def __init__(self, board, player_to_move, parent=None, move=None):
       self.board = board                      
       self.player_to_move = player_to_move   
       self.parent = parent
       self.move = move                      
       self.children = []
       self.untried_moves = legal_moves(board) if winner(board) is None else []
       self.visits = 0
       self.wins = 0.0
   def is_fully_expanded(self):
       return len(self.untried_moves) == 0
   def is_terminal(self):
       return winner(self.board) is not None
   def ucb1(self, c):
       """UCB1 = exploitation + exploration."""
       exploit = self.wins / self.visits
       explore = c * math.sqrt(math.log(self.parent.visits) / self.visits)
       return exploit + explore
def select(node, c):
   """Phase 1: walk down the tree using UCB1 until a node that can be expanded."""
   while not node.is_terminal() and node.is_fully_expanded():
       node = max(node.children, key=lambda ch: ch.ucb1(c))
   return node
def expand(node):
   """Phase 2: add one new child for a move not yet tried."""
   if node.is_terminal():
       return node
   move = node.untried_moves.pop(random.randrange(len(node.untried_moves)))
   new_board = node.board[:]
   new_board[move] = node.player_to_move
   child = Node(new_board, other(node.player_to_move), parent=node, move=move)
   node.children.append(child)
   return child
def simulate(node):
   """Phase 3: play random moves to the end of the game. Return the result."""
   board = node.board[:]
   player = node.player_to_move
   result = winner(board)
   while result is None:
       move = random.choice(legal_moves(board))
       board[move] = player
       player = other(player)
       result = winner(board)
   return result
def backpropagate(node, result):
   """Phase 4: update visits and wins on the path back to the root."""
   while node is not None:
       node.visits += 1
       mover = other(node.player_to_move)
       if result == 'draw':
           node.wins += 0.5
       elif result == mover:
           node.wins += 1.0
       node = node.parent
def mcts(board, player, iterations=1000, c=1.41, verbose=False):
   """Run MCTS from the given position and return the best move."""
   root = Node(board[:], player)
   for _ in range(iterations):
       leaf = select(root, c)
       child = expand(leaf)
       result = simulate(child)
       backpropagate(child, result)
   if verbose:
       print(f"  MCTS statistics after {iterations} iterations "
             f"(player {player} to move):")
       print("   move | visits | wins  | win-rate")
       for ch in sorted(root.children, key=lambda n: -n.visits):
           rate = ch.wins / ch.visits
           print(f"    {ch.move}   | {ch.visits:6d} | {ch.wins:5.1f} | {rate:.2f}")
   best = max(root.children, key=lambda ch: ch.visits)
   return best.move
def ask_human(board, mark):
   """Ask the human for a move until a free square is entered."""
   moves = legal_moves(board)
   while True:
       text = input(f"Your move ({mark}) - choose one of {moves}: ").strip()
       if text.isdigit() and int(text) in moves:
           return int(text)
       print("  That is not a free square. Try again.")
def play(human='O', iterations=ITERATIONS, c=C):
   """MCTS plays one side, the human plays the other. X always moves first."""
   board = [' '] * 9
   player = 'X'
   print(f"You are {human}. MCTS is {other(human)} and uses "
         f"{iterations} iterations per move.")
   print("Empty squares show their number:\n")
   print_board(board, show_numbers=True)
   while winner(board) is None:
       print()
       if player == human:
           move = ask_human(board, player)
       else:
           print(f"MCTS ({player}) is thinking...")
           move = mcts(board, player, iterations, c, verbose=True)
           print(f"MCTS ({player}) plays square {move}")
       board[move] = player
       print()
       print_board(board, show_numbers=True)
       player = other(player)
   result = winner(board)
   print()
   if result == 'draw':
       print("The game is a draw.")
   elif result == human:
       print("You win!")
   else:
       print("MCTS wins!")
if __name__ == '__main__':
   if len(sys.argv) > 1 and sys.argv[1].isdigit():
       random.seed(int(sys.argv[1]))
   try:
       play(human='O')
   except (EOFError, KeyboardInterrupt):
       print("\nGame stopped.")