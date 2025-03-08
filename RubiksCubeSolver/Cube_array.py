import numpy as np
#Current scramble for cube with green as front and white as top: L' D2 L2 D2 U2 B D2 U2 B2 R2 B R U2 F' D2 R F' R2 D L2
class RubiksCube:
    def __init__(self):
        self.topSide = np.array([
            ['w', 'w', 'g'],
            ['w', 'w', 'g'],
            ['b', 'b', 'w']
        ])
        self.leftSide = np.array([
            ['b', 'o', 'o'],
            ['o', 'o', 'o'],
            ['o', 'o', 'o']
       ])
        self.frontSide = np.array([
            ['w', 'w', 'g'],
            ['g', 'g', 'g'],
            ['g', 'g', 'g']
        ])
        self.rightSide = np.array([
            ['r', 'w', 'w'],
            ['r', 'r', 'r'],
            ['r', 'r', 'r']
       ])
        self.backSide = np.array([
            ['o', 'r', 'r'],
            ['b', 'b', 'b'],
            ['b', 'b', 'b']
        ])
        self.bottomSide = np.array([
            ['y', 'y', 'y'],
            ['y', 'y', 'y'],
            ['y', 'y', 'y']
        ])

        self.turn_history = []

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
    def X_corner(self):
        return sorted(list(map(str, [self.backSide[2][0], self.backSide[2][2], self.leftSide[2][0]])))

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



    @staticmethod #Fix this
    def simplify_moves(moves):
        simplified_moves = list(moves.split())
        print(list(moves.split()))
        i = 0

        while i < len(simplified_moves)-1 and len(simplified_moves) != 1:
            x = simplified_moves[i]
            try:
                if x[1] == '2':
                    x_turn = x[0]
                else:
                    x_turn = x[1]
            except IndexError:
                x_turn = x[0]
            y = simplified_moves[i+1]
            try:
                if y[1] == '2':
                    y_turn = y[0]
                else:
                    y_turn = y[1]
            except IndexError:
                y_turn = y[0]

            #Check if x & y turn the same side
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
                    simplified_moves[i:i+2] = []
                elif turn_quantifier == 1:
                    simplified_moves[i:i+2] = [x_turn]
                elif turn_quantifier in {-2, 2}:
                    simplified_moves[i:i+2] = [x_turn + '2']
                elif turn_quantifier == 3:
                    simplified_moves[i:i+2] = [x_turn + "'"]

            else:
                i += 1
            print(simplified_moves)
            try:
                test = simplified_moves[i+1]
            except IndexError:
                break


















    def corners_solve(self):
        X = 'b o y'.split()  # where the pieces should go
        W = 'b r y'.split()
        U = 'g o y'.split()
        V = 'g r y'.split()
        A = 'b o w'.split()
        B = 'b r w'.split()
        C = 'g r w'.split()
        D = 'g o w'.split()

        def remove_from_bottom(column):
            if column == 3:
                moves = 'R U -R'.split()
                for move in moves:
                    self.turn(move)
            elif column == 4:
                moves = '-L -U L'.split()
                for move in moves:
                    self.turn(move)
            elif column == 1:
                moves = 'L U -L'.split()
                for move in moves:
                    self.turn(move)
            elif column == 2:
                moves = '-R -U R'.split()
                for move in moves:
                    self.turn(move)

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

            for name, corner in all_corners.items():
                if sorted(corner) == sorted(corner_to_find):
                    return print(name)

            return print('X_corner')
        find_corner(W)







cube = RubiksCube()
cube.turn('')
#moves = 'B L2 U2 F L2 B R U R2 -L B2 M2 R2 -D F2 -U F2 R2 -B D2 F2 L2 U F L U2'.split()


cube.corners_solve()
cube.simplify_moves('R R R R R R R R R R R R')

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
    moves = ''.split()
    for move in moves:
        cube.turn(move)

    # L' D2 L2 D2 U2 B D2 U2 B2 R2 B R U2 F' D2 R F' R2 D L2
    # L' D2 L2 D2 U2 B D2 U2 B2 R2 B R U2 F' D2 R F' R2 D L2
    print(cube_state())
    print("L' D2 L2 D2 U2 B D2 U2 B2 R2 B R U2 F' D2 R F' R2 D L2")
    print(cube.turn_history)

    #Simplify moves


if __name__ == '__main__':
    main()


