"""
This a test code for our SUDOKU game

@author: Souad Yakubu(sny2)
@author: Edom Maru (eam43)
@date: Fall, 2022 
"""
#correct solved puzzle
from SUDOKU import Sudoku
game=Sudoku()
game.get_data('correctsudoku1.txt')
assert game.check()
assert game.check_answer(4)
assert game.column_answer(4)
assert game.box_answer(3)

# correct solved puzzle 2
game.get_data('correctsudoku2.txt')
assert game.check()
assert game.check_answer(1)
assert game.column_answer(2)
assert game.box_answer(5)

#wrong solved puzzle
game=Sudoku()
game.get_data('wrongsudoku.txt')
assert game.check() is False
assert game.check_answer(1) is False
assert game.column_answer(2) is False
assert game.box_answer(0) is False

print ('All test were passed!')