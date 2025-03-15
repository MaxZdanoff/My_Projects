
import numpy as np
class RubiksCube:
    def __init__(self):
        self.topSide = np.array([
            ['b', 'r', 'r'],
            ['o', 'w', 'b'],
            ['b', 'o', 'w']
        ])
        self.leftSide = np.array([
            ['w', 'w', 'r'],
            ['r', 'o', 'y'],
            ['y', 'w', 'o']
       ])
        self.frontSide = np.array([
            ['y', 'g', 'o'],
            ['g', 'g', 'y'],
            ['g', 'w', 'r']
        ])
        self.rightSide = np.array([
            ['g', 'o', 'g'],
            ['r', 'r', 'y'],
            ['g', 'g', 'w']
       ])
        self.backSide = np.array([
            ['y', 'b', 'o'],
            ['b', 'b', 'w'],
            ['b', 'o', 'o']
        ])
        self.bottomSide = np.array([
            ['y', 'b', 'w'],
            ['g', 'y', 'r'],
            ['b', 'y', 'r']
        ])

        self.turn_history = []

# ---------------------------------CORNERS----------------------------------------------------------------
    # @property allows you to define something like a method and access it like an attribute. Useful for making complicated attributes
    # without @property, the attributes will not be updated automatically when the cube is turned
    @property
    def A_corner(self):
        return sorted(list(map(str, [self.topSide[0][0], self.leftSide[0][0], self.backSide[0][2]])))
    @property
    def B_corner(self):
        return sorted(list(map(str, [self.topSide[0][2], self.backSide[0][0], self.rightSide[0][2]])))
    @property
    def C_corner(self):
        return sorted(list(map(str, [self.topSide[2][2], self.frontSide[0][2], self.rightSide[0][0]])))
    @property
    def D_corner(self):
        return sorted(list(map(str, [self.topSide[2][0], self.frontSide[0][0], self.leftSide[0][2]])))
    @property
    def U_corner(self):
        return sorted(list(map(str, [self.bottomSide[0][0], self.frontSide[2][0], self.leftSide[2][2]])))
    @property
    def V_corner(self):
        return sorted(list(map(str, [self.bottomSide[0][2], self.frontSide[2][2], self.rightSide[2][0]])))
    @property
    def W_corner(self):
        return sorted(list(map(str, [self.bottomSide[2][2], self.backSide[2][0], self.rightSide[2][2]])))
    @property
    def X_corner(self): #Backside listed twice. Still works.
        return sorted(list(map(str, [self.backSide[2][0], self.backSide[2][2], self.leftSide[2][0]])))

#-------------------------------CROSS EDGES----------------------------------------------------------------
    @property
    def blue_slot_cross(self):
        return list(map(str, [self.backSide[2][1], self.bottomSide[2][1]]))
    @property
    def red_slot_cross(self):
        return list(map(str, [self.rightSide[2][1], self.bottomSide[1][2]]))
    @property
    def green_slot_cross(self):
        return list(map(str, [self.frontSide[2][1], self.bottomSide[0][1]]))
    @property
    def orange_slot_cross(self):
        return list(map(str, [self.leftSide[2][1], self.bottomSide[1][0]]))
    @property
    def top_blue_slot_cross(self):
        return list(map(str, [self.backSide[0][1], self.topSide[0][1]]))
    @property
    def top_red_slot_cross(self):
        return list(map(str, [self.rightSide[0][1], self.topSide[1][2]]))
    @property
    def top_green_slot_cross(self):
        return list(map(str, [self.frontSide[0][1], self.topSide[2][1]]))
    @property
    def top_orange_slot_cross(self):
        return list(map(str, [self.leftSide[0][1], self.topSide[1][0]]))

    @property
    def equator_green(self):
        left = list(map(str, [self.frontSide[1][0], self.leftSide[1][2]]))
        right = list(map(str, [self.frontSide[1][2], self.rightSide[1][0]]))
        return [left, right]

    @property
    def equator_red(self):
        left = list(map(str, [self.rightSide[1][0], self.frontSide[1][2]]))
        right = list(map(str, [self.rightSide[1][2], self.backSide[1][0]]))
        return [left, right]

    @property
    def equator_blue(self):
        left = list(map(str, [self.backSide[1][0], self.rightSide[1][2]]))
        right = list(map(str, [self.backSide[1][2], self.leftSide[1][0]]))
        return [left, right]

    @property
    def equator_orange(self):
        left = list(map(str, [self.leftSide[1][0], self.backSide[1][2]]))
        right = list(map(str, [self.leftSide[1][2], self.frontSide[1][0]]))
        return [left, right]

    blue_edge = ('b', 'y')
    red_edge = ('r', 'y')
    green_edge = ('g', 'y')
    orange_edge = ('o', 'y')
#--------------------------------------------------------------------------------------------------------
    ''''@property
    def A_slot_edge(self):
        return sorted(list(map(str, [self.backSide[1][2], self.leftSide[1][0]])))

    @property
    def B_slot_edge(self):
        return sorted(list(map(str, [self.backSide[1][0], self.rightSide[1][2]])))

    @property
    def C_slot_edge(self):
        return sorted(list(map(str, [self.frontSide[1][2], self.rightSide[1][0]])))

    @property
    def D_slot_edge(self):
        return sorted(list(map(str, [self.frontSide[1][0], self.leftSide[1][2]])))'''

    def turn(self, side):
        self.turn_history.append(side)
        if side == 'R':
            self.rightSide = np.rot90(self.rightSide, 3)
            top_col = self.topSide[:, 2].copy()
            front_col = self.frontSide[:, 2].copy()
            back_col = self.backSide[:, 0].copy()
            bottom_col = self.bottomSide[:, 2].copy()

            self.frontSide[:, 2] = bottom_col
            self.topSide[:, 2] = front_col
            self.bottomSide[:, 2] = back_col[::-1]
            self.backSide[:, 0] = top_col[::-1]
        if side == '-R':
            self.rightSide = np.rot90(self.rightSide)
            top_col = self.topSide[:, 2].copy()
            front_col = self.frontSide[:, 2].copy()
            back_col = self.backSide[:, 0].copy()
            bottom_col = self.bottomSide[:, 2].copy()

            self.frontSide[:, 2] = top_col
            self.bottomSide[:, 2] = front_col
            self.backSide[:, 0] = bottom_col[::-1]
            self.topSide[:, 2] = back_col[::-1]
        if side == 'R2':
            self.rightSide = np.rot90(self.rightSide, 2)
            top_col = self.topSide[:, 2].copy()
            front_col = self.frontSide[:, 2].copy()
            back_col = self.backSide[:, 0].copy()
            bottom_col = self.bottomSide[:, 2].copy()

            self.frontSide[:, 2] = back_col[::-1]
            self.bottomSide[:, 2] = top_col
            self.backSide[:, 0] = front_col[::-1]
            self.topSide[:, 2] = bottom_col
        if side == 'L':
            self.leftSide = np.rot90(self.leftSide, 3)
            top_col = self.topSide[:, 0].copy()
            front_col = self.frontSide[:, 0].copy()
            back_col = self.backSide[:, 2].copy()
            bottom_col = self.bottomSide[:, 0].copy()

            self.frontSide[:, 0] = top_col
            self.bottomSide[:, 0] = front_col
            self.backSide[:, 2] = bottom_col[::-1]
            self.topSide[:, 0] = back_col[::-1]
        if side == '-L':
            self.leftSide = np.rot90(self.leftSide)
            top_col = self.topSide[:, 0].copy()
            front_col = self.frontSide[:, 0].copy()
            back_col = self.backSide[:, 2].copy()
            bottom_col = self.bottomSide[:, 0].copy()

            self.frontSide[:, 0] = bottom_col
            self.topSide[:, 0] = front_col
            self.backSide[:, 2] = top_col[::-1]
            self.bottomSide[:, 0] = back_col[::-1]
        if side == 'L2':
            self.leftSide = np.rot90(self.leftSide, 2)
            top_col = self.topSide[:, 0].copy()
            front_col = self.frontSide[:, 0].copy()
            back_col = self.backSide[:, 2].copy()
            bottom_col = self.bottomSide[:, 0].copy()


            self.frontSide[:, 0] = back_col[::-1]
            self.topSide[:, 0] = bottom_col
            self.backSide[:, 2] = front_col[::-1]
            self.bottomSide[:, 0] = top_col
        if side == 'U':
            self.topSide = np.rot90(self.topSide, 3)
            front_row = self.frontSide[0].copy()
            left_row = self.leftSide[0].copy()
            back_row = self.backSide[0].copy()
            right_row = self.rightSide[0].copy()

            self.leftSide[0] = front_row
            self.backSide[0] = left_row
            self.rightSide[0] = back_row
            self.frontSide[0] = right_row
        if side == '-U':
            self.topSide = np.rot90(self.topSide)
            front_row = self.frontSide[0].copy()
            left_row = self.leftSide[0].copy()
            back_row = self.backSide[0].copy()
            right_row = self.rightSide[0].copy()

            self.leftSide[0] = back_row
            self.frontSide[0] = left_row
            self.rightSide[0] = front_row
            self.backSide[0] = right_row
        if side == 'U2':
            self.topSide = np.rot90(self.topSide, 2)
            front_row = self.frontSide[0].copy()
            left_row = self.leftSide[0].copy()
            back_row = self.backSide[0].copy()
            right_row = self.rightSide[0].copy()

            self.leftSide[0] = right_row
            self.frontSide[0] = back_row
            self.rightSide[0] = left_row
            self.backSide[0] = front_row
        if side == 'D':
            self.bottomSide = np.rot90(self.bottomSide, 3)
            front_row = self.frontSide[2].copy()
            left_row = self.leftSide[2].copy()
            back_row = self.backSide[2].copy()
            right_row = self.rightSide[2].copy()

            self.leftSide[2] = back_row
            self.frontSide[2] = left_row
            self.rightSide[2] = front_row
            self.backSide[2] = right_row
        if side == '-D':
            self.bottomSide = np.rot90(self.bottomSide)
            front_row = self.frontSide[2].copy()
            left_row = self.leftSide[2].copy()
            back_row = self.backSide[2].copy()
            right_row = self.rightSide[2].copy()

            self.leftSide[2] = front_row
            self.backSide[2] = left_row
            self.rightSide[2] = back_row
            self.frontSide[2] = right_row
        if side == 'D2':
            self.bottomSide = np.rot90(self.bottomSide, 2)
            front_row = self.frontSide[2].copy()
            left_row = self.leftSide[2].copy()
            back_row = self.backSide[2].copy()
            right_row = self.rightSide[2].copy()

            self.leftSide[2] = right_row
            self.frontSide[2] = back_row
            self.rightSide[2] = left_row
            self.backSide[2] = front_row
        if side == 'F':
            self.frontSide = np.rot90(self.frontSide, 3)
            top_row = self.topSide[2].copy()
            right_col = self.rightSide[:, 0].copy()
            bottom_row = self.bottomSide[0].copy()
            left_col = self.leftSide[:, 2].copy()

            self.rightSide[:, 0] = top_row
            self.bottomSide[0] = right_col[::-1]
            self.leftSide[:, 2] = bottom_row
            self.topSide[2] = left_col[::-1]
        if side == '-F':
            self.frontSide = np.rot90(self.frontSide)
            top_row = self.topSide[2].copy()
            right_col = self.rightSide[:, 0].copy()
            bottom_row = self.bottomSide[0].copy()
            left_col = self.leftSide[:, 2].copy()

            self.rightSide[:, 0] = bottom_row[::-1]
            self.bottomSide[0] = left_col
            self.leftSide[:, 2] = top_row[::-1]
            self.topSide[2] = right_col
        if side == 'F2':
            self.frontSide = np.rot90(self.frontSide, 2)
            top_row = self.topSide[2].copy()
            right_col = self.rightSide[:, 0].copy()
            bottom_row = self.bottomSide[0].copy()
            left_col = self.leftSide[:, 2].copy()


            self.rightSide[:, 0] = left_col[::-1]
            self.bottomSide[0] = top_row[::-1]
            self.leftSide[:, 2] = right_col[::-1]
            self.topSide[2] = bottom_row[::-1]
        if side == 'B':
            self.backSide = np.rot90(self.backSide, 3)
            top_row = self.topSide[0].copy()
            right_col = self.rightSide[:, 2].copy()
            bottom_row = self.bottomSide[2].copy()
            left_col = self.leftSide[:, 0].copy()

            self.rightSide[:, 2] = bottom_row[::-1]
            self.topSide[0] = right_col
            self.leftSide[:, 0] = top_row[::-1]
            self.bottomSide[2] = left_col
        if side == '-B':
            self.backSide = np.rot90(self.backSide)
            top_row = self.topSide[0].copy()
            right_col = self.rightSide[:, 2].copy()
            bottom_row = self.bottomSide[2].copy()
            left_col = self.leftSide[:, 0].copy()

            self.rightSide[:, 2] = top_row
            self.bottomSide[2] = right_col[::-1]
            self.leftSide[:, 0] = bottom_row
            self.topSide[0] = left_col[::-1]
        if side == 'B2':
            self.backSide = np.rot90(self.backSide, 2)
            top_row = self.topSide[0].copy()
            right_col = self.rightSide[:, 2].copy()
            bottom_row = self.bottomSide[2].copy()
            left_col = self.leftSide[:, 0].copy()

            self.topSide[0] = bottom_row[::-1]
            self.rightSide[:, 2] = left_col [::-1]
            self.bottomSide[2] = top_row[::-1]
            self.leftSide[:, 0] = right_col[::-1]
        if side == 'M':
            top_col = self.topSide[:, 1].copy()
            back_col = self.backSide[:, 1].copy()
            bottom_col = self.bottomSide[:, 1].copy()
            front_col = self.frontSide[:, 1].copy()

            self.topSide[:, 1] = back_col[::-1]
            self.frontSide[:, 1] = top_col
            self.bottomSide[:, 1] = front_col
            self.backSide[:, 1] = bottom_col[::-1]
        if side == '-M':
            top_col = self.topSide[:, 1].copy()
            back_col = self.backSide[:, 1].copy()
            bottom_col = self.bottomSide[:, 1].copy()
            front_col = self.frontSide[:, 1].copy()

            self.topSide[:, 1] = front_col
            self.frontSide[:, 1] = bottom_col
            self.bottomSide[:, 1] = back_col[::-1]
            self.backSide[:, 1] = top_col[::-1]
        if side == 'M2':
            top_col = self.topSide[:, 1].copy()
            back_col = self.backSide[:, 1].copy()
            bottom_col = self.bottomSide[:, 1].copy()
            front_col = self.frontSide[:, 1].copy()

            self.topSide[:, 1] = bottom_col
            self.frontSide[:, 1] = back_col[::-1]
            self.bottomSide[:, 1] = top_col
            self.backSide[:, 1] = front_col[::-1]


    def create_scramble(self):
        import random
        move_set = list('R R2 -R U U2 -U L L2 -L D D2 -D F F2 -F B B2 -B'.split())
        i = 0
        scramble = []
        while i <= 20:
            random_move = move_set[random.randint(0, 17)]
            scramble.append(random_move)
            self.turn(random_move)
            i += 1
        return print(f'Scramble: {scramble}')


    @staticmethod
    def simplify_moves(moves):
        if len(moves) == 0:
            return
        if isinstance(moves, list):
            simplified_moves = ' '.join(moves)
            simplified_moves = list(simplified_moves.split())
        else:
            simplified_moves = list(moves.split())

        # Sexy move

        # print(list(moves.split()))
        i = 0

        while i < len(simplified_moves) - 1 and len(simplified_moves) != 1:
            x = simplified_moves[i]
            try:
                if x[1] == '2':
                    x_turn = x[0]
                else:
                    x_turn = x[1]
            except IndexError:
                x_turn = x[0]
            y = simplified_moves[i + 1]
            try:
                if y[1] == '2':
                    y_turn = y[0]
                else:
                    y_turn = y[1]
            except IndexError:
                y_turn = y[0]

            # Check if x & y turn the same side
            if x_turn == y_turn:
                try:
                    if x[1] == '2':
                        quantifier_x = 2
                    else:
                        quantifier_x = -1
                except IndexError:
                    quantifier_x = 1

                try:
                    if y[1] == '2':
                        quantifier_y = 2
                    else:
                        quantifier_y = -1
                except IndexError:
                    quantifier_y = 1

                turn_quantifier = quantifier_x + quantifier_y
                if turn_quantifier in {0, 4}:
                    simplified_moves[i:i + 2] = []
                elif turn_quantifier == 1:
                    simplified_moves[i:i + 2] = [x_turn]
                elif turn_quantifier in {-2, 2}:
                    simplified_moves[i:i + 2] = [x_turn + '2']
                elif turn_quantifier == 3:
                    simplified_moves[i:i + 2] = ['-' + x_turn]

            else:
                i += 1
            # print(simplified_moves)
            if i >= len(simplified_moves) - 1:
                break

        # Check if fully simplified
        for move in range(len(simplified_moves) - 1):
            if simplified_moves[move] == simplified_moves[move + 1] or simplified_moves[move] == simplified_moves[move + 1] + '2':
                return RubiksCube.simplify_moves(' '.join(simplified_moves))
            elif simplified_moves[move] == ('-' + simplified_moves[move + 1]):
                return RubiksCube.simplify_moves(' '.join(simplified_moves))
            elif '-' + simplified_moves[move] == simplified_moves[move + 1]:
                return RubiksCube.simplify_moves(' '.join(simplified_moves))
            elif simplified_moves[move] == simplified_moves[move + 1] + '2':
                return RubiksCube.simplify_moves(' '.join(simplified_moves))
            elif simplified_moves[move] + '2' == simplified_moves[move + 1]:
                return RubiksCube.simplify_moves(' '.join(simplified_moves))
        return simplified_moves

    @staticmethod
    def rotate_moves(moves, side):
        rotated_moves = []
        i = 0
        if side == 'right':
            while i < len(moves):
                if moves[i] == 'R':
                    rotated_moves.append('B')
                elif moves[i] == 'R2':
                    rotated_moves.append('B2')
                elif moves[i] == '-R':
                    rotated_moves.append('-B')
                elif moves[i] == 'L':
                    rotated_moves.append('F')
                elif moves[i] == 'L2':
                    rotated_moves.append('F2')
                elif moves[i] == '-L':
                    rotated_moves.append('-F')
                elif moves[i] == 'F':
                    rotated_moves.append('R')
                elif moves[i] == 'F2':
                    rotated_moves.append('R2')
                elif moves[i] == '-F':
                    rotated_moves.append('-R')
                elif moves[i] == 'B':
                    rotated_moves.append('L')
                elif moves[i] == 'B2':
                    rotated_moves.append('L2')
                elif moves[i] == '-B':
                    rotated_moves.append('-L')
                else:
                    rotated_moves.append(moves[i])
                i += 1
        elif side == 'left':
            while i < len(moves):
                if moves[i] == 'R':
                    rotated_moves.append('F')
                elif moves[i] == 'R2':
                    rotated_moves.append('F2')
                elif moves[i] == '-R':
                    rotated_moves.append('-F')
                elif moves[i] == 'L':
                    rotated_moves.append('B')
                elif moves[i] == 'L2':
                    rotated_moves.append('B2')
                elif moves[i] == '-L':
                    rotated_moves.append('-B')
                elif moves[i] == 'F':
                    rotated_moves.append('L')
                elif moves[i] == 'F2':
                    rotated_moves.append('L2')
                elif moves[i] == '-F':
                    rotated_moves.append('-L')
                elif moves[i] == 'B':
                    rotated_moves.append('R')
                elif moves[i] == 'B2':
                    rotated_moves.append('R2')
                elif moves[i] == '-B':
                    rotated_moves.append('-R')
                else:
                    rotated_moves.append(moves[i])
                i += 1
        elif side == 'back':
            while i < len(moves):
                if moves[i] == 'R':
                    rotated_moves.append('L')
                elif moves[i] == 'R2':
                    rotated_moves.append('L2')
                elif moves[i] == '-R':
                    rotated_moves.append('-L')
                elif moves[i] == 'L':
                    rotated_moves.append('R')
                elif moves[i] == 'L2':
                    rotated_moves.append('R2')
                elif moves[i] == '-L':
                    rotated_moves.append('-R')
                elif moves[i] == 'F':
                    rotated_moves.append('B')
                elif moves[i] == 'F2':
                    rotated_moves.append('B2')
                elif moves[i] == '-F':
                    rotated_moves.append('-B')
                elif moves[i] == 'B':
                    rotated_moves.append('F')
                elif moves[i] == 'B2':
                    rotated_moves.append('F2')
                elif moves[i] == '-B':
                    rotated_moves.append('-F')
                else:
                    rotated_moves.append(moves[i])
                i += 1

        return rotated_moves


    @staticmethod
    def undo_moves(moves):
        reversed_moves = []
        i = len(moves)-1
        while i >= 0:
            if moves[i] == 'R':
                reversed_moves.append('-R')
            elif moves[i] == '-R':
                reversed_moves.append('R')
            elif moves[i] == 'L':
                reversed_moves.append('-L')
            elif moves[i] == '-L':
                reversed_moves.append('L')
            elif moves[i] == 'U':
                reversed_moves.append('-U')
            elif moves[i] == '-U':
                reversed_moves.append('U')
            elif moves[i] == 'F':
                reversed_moves.append('-F')
            elif moves[i] == '-F':
                reversed_moves.append('F')
            elif moves[i] == 'B':
                reversed_moves.append('-B')
            elif moves[i] == '-B':
                reversed_moves.append('B')
            else:
                reversed_moves.append(moves[i])
            i -= 1

        return reversed_moves

    def corners_solve(self):
        X = 'b o y'.split()  # where the pieces should go
        W = 'b r y'.split()
        U = 'g o y'.split()
        V = 'g r y'.split()
        A = 'b o w'.split()
        B = 'b r w'.split()
        C = 'g r w'.split()
        D = 'g o w'.split()


        def is_corner_solved(check_corner):
            if check_corner == X:
                if 'y' == self.bottomSide[2][0] and 'b' == self.backSide[2][2] and 'o' == self.leftSide[2][0]:
                    return True

            if check_corner == W:
                if 'y' == self.bottomSide[2][2] and 'b' == self.backSide[2][0] and 'r' == self.rightSide[2][2]:
                    return True

            if check_corner == V:
                if 'y' == self.bottomSide[0][2] and 'g' == self.frontSide[2][2] and 'r' == self.rightSide[2][0]:
                    return True

            if check_corner == U:
                if 'y' == self.bottomSide[0][0] and 'g' == self.frontSide[2][0] and 'o' == self.leftSide[2][2]:
                    return True

            return False


        def remove_from_bottom(column):
            if column == 'V_corner':
                if self.frontSide[2][2] == 'y':
                    moves = 'R -U -R'
                    return moves
                moves = 'R U -R'
                return moves
            elif column == 'U_corner':
                if self.frontSide[2][0] == 'y':
                    moves = '-L U L'
                    return moves
                moves = '-L -U L'
                return moves
            elif column == 'X_corner':
                if self.backSide[2][2] == 'y':
                    moves = 'L -U -L'
                    return moves
                moves = 'L U -L'
                return moves
            elif column == 'W_corner':
                if self.backSide[2][0] == 'y':
                    moves = '-R U R'
                    return moves
                moves = '-R -U R'
                return moves

        def find_corner(corner_to_find):
            all_corners = {
                "A_corner": self.A_corner,
                "B_corner": self.B_corner,
                "C_corner": self.C_corner,
                "D_corner": self.D_corner,
                "U_corner": self.U_corner,
                "V_corner": self.V_corner,
                "W_corner": self.W_corner,
                "X_corner": self.X_corner,
            }

            # Find and return the corner name
            for name, corner in all_corners.items():
                if sorted(corner) == sorted(corner_to_find):
                    return name

            return 'X_corner'


        def X_corner_solve():
            corner_solve_alg = []

            case_1 = 'R U2 -R U2 -F U F'.split()
            case_2 = 'U R -U -R'.split()
            case_3 = '-U -F U F'.split()

            if is_corner_solved(X): #Check if the corner is solved
                return

            location = find_corner(X)
            if location in {'U_corner', 'V_corner', 'W_corner', 'X_corner'}: #Check if corner is at the bottom
                moves = remove_from_bottom(location)  # Remove from bottom if true
                for move in moves.split():
                    self.turn(move)
                corner_solve_alg.append(' '.join(moves.split()))

            turns = '' #Empty substring of U moves
            while find_corner(X) != 'A_corner':
                self.turn('U')
                turns += ' U' #Add to substring

            corner_solve_alg.append(' '.join(self.simplify_moves(turns.strip()))) #Simplify moves before adding to main move list

            cases = [case_1, case_2, case_3]
            for case in cases:
                    #Try all cases
                for move in self.rotate_moves(case, 'back'):
                    self.turn(move)
                if is_corner_solved(X):
                    corner_solve_alg.append(' '.join(self.rotate_moves(case, 'back'))) #If solved append moves to list
                    return print(f"X_corner: {self.simplify_moves(' '.join(corner_solve_alg))}") #Print for debugging
                    #return self.simplify_moves(' '.join(corner_solve_alg))
                else:
                    for move in self.undo_moves(self.rotate_moves(case, 'back')): #If not solved undo moves
                        self.turn(move)


        def U_corner_solve():
            corner_solve_alg = []
            case_1 = '-L U2 L U2 F -U -F'.split()
            case_2 = '-U -L U L'.split()
            case_3 = 'U F -U -F'.split()

            if is_corner_solved(U):  # Check if the corner is solved
                return

            location = find_corner(U)
            if location in {'U_corner', 'V_corner', 'W_corner', 'X_corner'}:  # Check if corner is at the bottom
                moves = remove_from_bottom(location)  # Remove from bottom if true
                for move in moves.split():
                    self.turn(move)
                corner_solve_alg.append(' '.join(moves.split()))

            turns = ''  # Empty substring of U moves
            while find_corner(U) != 'D_corner':
                self.turn('U')
                turns += ' U'  # Add to substring

            corner_solve_alg.append(' '.join(self.simplify_moves(turns.strip())))  # Simplify moves before adding to main move list

            cases = [case_1, case_2, case_3]
            for case in cases:
                # Try all cases
                for move in case:
                    self.turn(move)
                if is_corner_solved(U):
                    corner_solve_alg.append(' '.join(case))  # If solved append moves to list
                    return print(f"U_corner: {self.simplify_moves(' '.join(corner_solve_alg))}")  # Print for debugging
                    #return self.simplify_moves(' '.join(corner_solve_alg))
                else:
                    for move in self.undo_moves(case):  # If not solved undo moves
                        self.turn(move)

        def V_corner_solve():
            corner_solve_alg = []
            case_1 = 'R U2 -R U2 -F U F'.split()
            case_2 = 'U R -U -R'.split()
            case_3 = '-U -F U F'.split()

            if is_corner_solved(V):  # Check if the corner is solved
                return

            location = find_corner(V)
            if location in {'U_corner', 'V_corner', 'W_corner', 'X_corner'}:  # Check if corner is at the bottom
                moves = remove_from_bottom(location)  # Remove from bottom if true
                for move in moves.split():
                    self.turn(move)
                corner_solve_alg.append(' '.join(moves.split()))

            turns = ''  # Empty substring of U moves
            while find_corner(V) != 'C_corner':
                self.turn('U')
                turns += ' U'  # Add to substring

            corner_solve_alg.append(' '.join(self.simplify_moves(turns.strip())))  # Simplify moves before adding to main move list

            cases = [case_1, case_2, case_3]
            for case in cases:
                # Try all cases
                for move in case:
                    self.turn(move)
                if is_corner_solved(V):
                    corner_solve_alg.append(' '.join(case))  # If solved append moves to list
                    return print(f"V_corner: {self.simplify_moves(' '.join(corner_solve_alg))}")  # Print for debugging
                    #return self.simplify_moves(' '.join(corner_solve_alg))
                else:
                    for move in self.undo_moves(case):  # If not solved undo moves
                        self.turn(move)


        def W_corner_solve():
            corner_solve_alg = []
            case_1 = '-L U2 L U2 F -U -F'.split()
            case_2 = '-U -L U L'.split()
            case_3 = 'U F -U -F'.split()

            if is_corner_solved(W):  # Check if the corner is solved
                return

            location = find_corner(W)
            if location in {'U_corner', 'V_corner', 'W_corner', 'X_corner'}:  # Check if corner is at the bottom
                moves = remove_from_bottom(location)  # Remove from bottom if true
                for move in moves.split():
                    self.turn(move)
                corner_solve_alg.append(' '.join(moves.split()))

            turns = ''  # Empty substring of U moves
            while find_corner(W) != 'B_corner':
                self.turn('U')
                turns += ' U'  # Add to substring

            corner_solve_alg.append(' '.join(self.simplify_moves(turns.strip())))  # Simplify moves before adding to main move list

            cases = [case_1, case_2, case_3]
            for case in cases:
                # Try all cases
                for move in self.rotate_moves(case, 'back'):
                    self.turn(move)
                if is_corner_solved(W):
                    corner_solve_alg.append(' '.join(self.rotate_moves(case, 'back')))  # If solved append moves to list
                    return print(f"W_corner: {self.simplify_moves(' '.join(corner_solve_alg))}")  # Print for debugging
                    #return self.simplify_moves(' '.join(corner_solve_alg))
                else:
                    for move in self.undo_moves(self.rotate_moves(case, 'back')):  # If not solved undo moves
                        self.turn(move)


        X_corner_solve()
        U_corner_solve()
        V_corner_solve()
        W_corner_solve()


    def cross(self):
        print(self.blue_slot_cross)
        print(self.red_slot_cross)
        print(self.green_slot_cross)
        print(self.orange_slot_cross)


    def is_cross_edge_solved(self, edge):
        solved_state = {
            self.blue_edge: self.blue_slot_cross,
            self.red_edge: self.red_slot_cross,
            self.green_edge: self.green_slot_cross,
            self.orange_edge: self.orange_slot_cross,
        }
        if solved_state.get(edge) == list(edge):
            return True
        return False


    def count_cross_edges_solved(self):
        counter = 0
        for edge in [self.blue_edge, self.red_edge, self.green_edge, self.orange_edge]:
            if self.is_cross_edge_solved(edge):
                counter += 1
        return counter


    def are_cross_pieces_in_bottom(self):
        if 'y' in [self.bottomSide[0][1], self.bottomSide[1][2], self.bottomSide[2][1], self.bottomSide[1][0]]:
            return True
        return False


    def allign_cross_pieces(self):
        if not self.are_cross_pieces_in_bottom():
            return
        solved_pieces = []

        for i in range(4):
            self.turn('D')
            solved_pieces.append(self.count_cross_edges_solved())
        if solved_pieces.index(max(solved_pieces)) == 3:
            return
        elif solved_pieces.index(max(solved_pieces)) == 0:
            self.turn('D')
            move_set = ['D']
            return print(move_set)
        elif solved_pieces.index(max(solved_pieces)) == 1:
            self.turn('D2')
            move_set = ['D2']
            return print(move_set)
        elif solved_pieces.index(max(solved_pieces)) == 2:
            self.turn('-D')
            move_set = ['-D']
            return print(move_set)


    def solve_top_edges(self):
        move_set = []
        top_edges = {
            self.blue_edge: self.top_blue_slot_cross,
            self.red_edge: self.top_red_slot_cross,
            self.green_edge: self.top_green_slot_cross,
            self.orange_edge: self.top_orange_slot_cross,
        }
        edges_on_top = []
        for edge in [self.blue_edge, self.red_edge, self.green_edge, self.orange_edge]:
            if list(edge) in [self.top_blue_slot_cross, self.top_red_slot_cross, self.top_green_slot_cross, self.top_orange_slot_cross]:
                edges_on_top.append(edge)

        if len(edges_on_top) == 0:
            return
        else:
            for i in range(len(edges_on_top)):
                while list(edges_on_top[i]) != top_edges.get(edges_on_top[i]):
                    top_edges = {
                        self.blue_edge: self.top_blue_slot_cross,
                        self.red_edge: self.top_red_slot_cross,
                        self.green_edge: self.top_green_slot_cross,
                        self.orange_edge: self.top_orange_slot_cross,
                    }
                    if list(edges_on_top[i]) == top_edges.get(edges_on_top[i]):
                        break
                    self.turn('U')
                    move_set.append('U')
                if edges_on_top[i] == self.blue_edge:
                    self.turn('B2')
                    move_set.append('B2')
                elif edges_on_top[i] == self.red_edge:
                    self.turn('R2')
                    move_set.append('R2')
                elif edges_on_top[i] == self.green_edge:
                    self.turn('F2')
                    move_set.append('F2')
                elif edges_on_top[i] == self.orange_edge:
                    self.turn('L2')
                    move_set.append('L2')

        return print(f'(Cross Solve) Pieces on top: {self.simplify_moves(move_set)}')


    def count_flipped_edges_top(self): #Delete if not used
        counter = 0
        edges = [self.blue_edge, self.red_edge, self.green_edge, self.orange_edge]
        reversed_edges = list(edges[1])  # Create a copy of the list
        reversed_edges.reverse()  # Reverse it in place
        for i in range(4):
            reversed_list = list(edges[i])
            reversed_list.reverse()
            if reversed_list in [self.top_blue_slot_cross, self.top_red_slot_cross, self.top_green_slot_cross, self.top_orange_slot_cross]:
                counter += 1
        return counter


    def solve_flipped_edge_top(self):
        move_list = []
        if self.frontSide[0][1] != 'y':
            i = 0
            while self.frontSide[0][1] != 'y':
                self.turn('U')
                move_list.append('U')
                if len(move_list) == 4:
                    return

        if self.topSide[2][1] == 'g':
            insert_edge = ['-U', '-R', 'F', 'R']

            for move in insert_edge:
                self.turn(move)
                move_list.append(move)
                move_list = self.simplify_moves(move_list)
        elif self.topSide[2][1] == 'r':
            insert_edge = ['F', '-R', '-F']
            for move in insert_edge:
                self.turn(move)
                move_list.append(move)
                move_list = self.simplify_moves(move_list)
        elif self.topSide[2][1] == 'o':
            insert_edge = ['-F', 'L', 'F']
            for move in insert_edge:
                self.turn(move)
                move_list.append(move)
                move_list = self.simplify_moves(move_list)
        elif self.topSide[2][1] == 'b':
            insert_edge = ['-U', 'R', '-B', '-R']
            for move in insert_edge:
                self.turn(move)
                move_list.append(move)
                move_list = self.simplify_moves(move_list)

        return print(move_list)


    def one_move_solves_equator(self):
        one_move_edges = []
        list1 = [self.green_edge, self.red_edge, self.orange_edge, self.blue_edge]
        list2 = [self.equator_green, self.equator_red, self.equator_orange, self.equator_blue]
        for wanted, current in zip(list1, list2):
            if list(wanted) in current:
                one_move_edges.append(wanted[0])

        return one_move_edges



    def solve_side_edges_one_move(self):
        #count matches in [r, b, g, o] and [colors in equator layer on respective side excluding non-yellow edges and center pieces
        #(If equator matches is 4, still count 3)
        #If matches is zero, return
        #Pick a color and do one repeated move until solved
        #Check again for matches
        #If matches is less than original_matches-1, undo all moves and try different combination
        #Once all are solved, run move_list through simplified_moves()
        #Look for edges in top layer that can be solved in one move and then solve those
        #Do recursive call
        move_list = []

        one_move_solves = len(self.one_move_solves_equator())
        if one_move_solves > 3:
            one_move_solves = 3

        '''dictionary = {
            'g': [self.green_edge, 'F'],
            'r': [self.red_edge, 'R'],
            'o': [self.orange_edge, 'L'],
            'b': [self.blue_edge, 'B'],
        }'''
        edge_pieces = [self.green_edge, self.red_edge, self.orange_edge, self.blue_edge]
        turns = ['F', 'R', 'L', 'B']
        for edge in self.one_move_solves_equator():
            if edge == 'g':
                solve = []
                while not self.is_cross_edge_solved(self.green_edge):
                    self.turn('F')
                    solve.append('F')
                if len(self.one_move_solves_equator()) < one_move_solves - 1:
                    for move in self.undo_moves(solve):
                        self.turn(move)
                    break
                else:
                    move_list.append(solve)

        return print(move_list)

















cube = RubiksCube()
def cube_state():
    print("         [" + " ".join(cube.topSide[0, :]) + "]")
    print("         [" + " ".join(cube.topSide[1, :]) + "]")
    print("         [" + " ".join(cube.topSide[2, :]) + "]")
    print()
    for i in range(3):
        print("[" + " ".join(cube.leftSide[i, :]) + "]" + "   " +
                "[" + " ".join(cube.frontSide[i, :]) + "]" + "   " +
                "[" + " ".join(cube.rightSide[i, :]) + "]" + "   " +
                "[" + " ".join(cube.backSide[i, :]) + "]")
    print()
    print("         [" + " ".join(cube.bottomSide[0, :]) + "]")
    print("         [" + " ".join(cube.bottomSide[1, :]) + "]")
    print("         [" + " ".join(cube.bottomSide[2, :]) + "]")

def main():
    '''moves = 'L2 -D R2 F -R D2 R2 D2 R B D2'.split() #Solve cross
    for move in moves:
        cube.turn(move)'''

    #cube.create_scramble()
    #cube.corners_solve()
    #cube.is_cross_edge_solved(cube.orange_edge)
    turns = ''.split()
    for turn in turns:
        cube.turn(turn)
    #cube.count_cross_edges_solved()
    #cube.allign_cross_pieces()
    #cube.solve_top_edges()
    #cube.count_flipped_edges_top()
    #cube.solve_flipped_edge_top() #Solves one flipped edge
    cube.one_move_solves_equator()
    cube.solve_side_edges_one_move()



    #Go through easy cases first. If no more pieces can be solved with easy methods, use flipped edge methods.

    #To do: Make solve_flipped_edges_top() method use less moves for opposite edges, make more cross methods





    '''moves = ''.split()
    for move in moves:
        cube.turn(move)'''

    print(cube_state())
    print("L' D2 L2 D2 U2 B D2 U2 B2 R2 B R U2 F' D2 R F' R2 D L2") # Cross solved
    print(cube.turn_history)


    #L' D2 L2 D2 U2 B D2 U2 B2 R2 B R U2 F' R2 D2 R B D2 (cross solved)
    # L' D2 L2 D2 U2 B D2 U2 B2 R2 B R U2 F' D2 R F' R2 D L2 (Original)
if __name__ == '__main__':
    main()
