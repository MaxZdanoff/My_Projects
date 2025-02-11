import numpy as np
#Current scramble for cube with green as front and white as top: L' D2 L2 D2 U2 B D2 U2 B2 R2 B R U2 F' D2 R F' R2 D L2
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


    def corners_solve(self):
        X = 'b o y'.split()  # where the pieces should go
        W = 'b r y'.split()
        U = 'g o y'.split()
        V = 'g r y'.split()

        A_corner = sorted(list(map(str, [self.topSide[0][0], self.leftSide[0][0], self.backSide[0][2]])))
        B_corner = sorted(list(map(str, [self.topSide[0][2], self.backSide[0][0], self.rightSide[0][2]])))
        C_corner = sorted(list(map(str, [self.topSide[2][2], self.frontSide[0][2], self.rightSide[0][0]])))
        D_corner = sorted(list(map(str, [self.topSide[2][0], self.frontSide[0][0], self.leftSide[0][2]])))
        U_corner = sorted(list(map(str, [self.bottomSide[0][0], self.frontSide[2][0], self.leftSide[2][2]])))
        V_corner = sorted(list(map(str, [self.bottomSide[0][2], self.frontSide[2][2], self.rightSide[2][0]])))
        W_corner = sorted(list(map(str, [self.bottomSide[2][2], self.backSide[2][0], self.rightSide[2][2]])))
        X_corner = sorted(list(map(str, [self.backSide[2][0], self.backSide[2][2], self.leftSide[2][0]])))


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

        #solve V
        if self.bottomSide[0, 2]=='y' and self.frontSide[2, 2]=='g' and self.rightSide[2, 0]=='r':
            None
        elif X_corner == V:
            remove_from_bottom(1)
        elif W_corner == V:
            remove_from_bottom(2)
        elif U_corner == V:
            remove_from_bottom(4)
        elif V_corner == V:
            while self.bottomSide[0, 2] != 'y' or self.frontSide[2, 2] != 'g' or self.rightSide[2, 0] != 'r':
                self.turn('R')
                self.turn('U')
                self.turn('-R')
                V_corner = sorted(list(map(str, [self.bottomSide[0][2], self.frontSide[2][2], self.rightSide[2][0]])))
                if self.bottomSide[0, 2] != 'y' or self.frontSide[2, 2] != 'g' or self.rightSide[2, 0] != 'r':
                    self.turn('-U')

        k = 1
        C_corner = sorted(list(map(str, [self.topSide[2][2], self.frontSide[0][2], self.rightSide[0][0]])))
        while C_corner != V and k<=4 and (self.bottomSide[0, 2] != 'y' or self.frontSide[2, 2] != 'g' or self.rightSide[2, 0] != 'r'):
            self.turn('U')
            A_corner = sorted(list(map(str, [self.topSide[0][0], self.leftSide[0][0], self.backSide[0][2]])))
            B_corner = sorted(list(map(str, [self.topSide[0][2], self.backSide[0][0], self.rightSide[0][2]])))
            C_corner = sorted(list(map(str, [self.topSide[2][2], self.frontSide[0][2], self.rightSide[0][0]])))
            D_corner = sorted(list(map(str, [self.topSide[2][0], self.frontSide[0][0], self.leftSide[0][2]])))
            k = k + 1

            while self.bottomSide[0, 2]!='y' or self.frontSide[2, 2]!='g' or self.rightSide[2, 0]!='r':
                self.turn('R')
                self.turn('U')
                self.turn('-R')
                V_corner = sorted(list(map(str, [self.bottomSide[0][2], self.frontSide[2][2], self.rightSide[2][0]])))
                if self.bottomSide[0, 2]!='y' or self.frontSide[2, 2]!='g' or self.rightSide[2, 0]!='r':
                    self.turn('-U')
                A_corner = sorted(list(map(str, [self.topSide[0][0], self.leftSide[0][0], self.backSide[0][2]])))
                B_corner = sorted(list(map(str, [self.topSide[0][2], self.backSide[0][0], self.rightSide[0][2]])))
                C_corner = sorted(list(map(str, [self.topSide[2][2], self.frontSide[0][2], self.rightSide[0][0]])))
                D_corner = sorted(list(map(str, [self.topSide[2][0], self.frontSide[0][0], self.leftSide[0][2]])))
                U_corner = sorted(list(map(str, [self.bottomSide[0][0], self.frontSide[2][0], self.leftSide[2][2]])))
                V_corner = sorted(list(map(str, [self.bottomSide[0][2], self.frontSide[2][2], self.rightSide[2][0]])))
                W_corner = sorted(list(map(str, [self.bottomSide[2][2], self.backSide[2][0], self.rightSide[2][2]])))
                X_corner = sorted(list(map(str, [self.backSide[2][0], self.backSide[2][2], self.leftSide[2][0]])))
        A_corner = sorted(list(map(str, [self.topSide[0][0], self.leftSide[0][0], self.backSide[0][2]])))
        B_corner = sorted(list(map(str, [self.topSide[0][2], self.backSide[0][0], self.rightSide[0][2]])))
        C_corner = sorted(list(map(str, [self.topSide[2][2], self.frontSide[0][2], self.rightSide[0][0]])))
        D_corner = sorted(list(map(str, [self.topSide[2][0], self.frontSide[0][0], self.leftSide[0][2]])))
        U_corner = sorted(list(map(str, [self.bottomSide[0][0], self.frontSide[2][0], self.leftSide[2][2]])))
        V_corner = sorted(list(map(str, [self.bottomSide[0][2], self.frontSide[2][2], self.rightSide[2][0]])))
        W_corner = sorted(list(map(str, [self.bottomSide[2][2], self.backSide[2][0], self.rightSide[2][2]])))
        X_corner = sorted(list(map(str, [self.backSide[2][0], self.backSide[2][2], self.leftSide[2][0]])))

        #solve U
        '''if self.bottomSide[0, 0]=='y' and self.frontSide[2, 0]=='g' and self.leftSide[2, 2]=='o':
            return None
        else:
            if X_corner == U:
                remove_from_bottom(1)
            elif W_corner == U:
                remove_from_bottom(2)
            elif V_corner == U:
                remove_from_bottom(3)
            elif U_corner == U:
                while self.bottomSide[0, 0]!='y' or self.frontSide[2, 0]!='g' or self.leftSide[2, 2]!='o':
                    self.turn('-L')
                    self.turn('-U')
                    self.turn('L')
                    U_corner = sorted(list(map(str, [self.bottomSide[0][2], self.frontSide[2][2], self.rightSide[2][0]])))
                    if self.bottomSide[0, 0] != 'y' or self.frontSide[2, 0] != 'g' or self.leftSide[2, 2] != 'o':
                        self.turn('U')

            k = 1
            D_corner = sorted(list(map(str, [self.topSide[2][0], self.frontSide[0][0], self.leftSide[0][2]])))
            while D_corner != U and k <= 4 and (self.bottomSide[0, 0]!='y' or self.frontSide[2, 0]!='g' or self.leftSide[2, 2]!='o'):
                self.turn('U')
                A_corner = sorted(list(map(str, [self.topSide[0][0], self.leftSide[0][0], self.backSide[0][2]])))
                B_corner = sorted(list(map(str, [self.topSide[0][2], self.backSide[0][0], self.rightSide[0][2]])))
                C_corner = sorted(list(map(str, [self.topSide[2][2], self.frontSide[0][2], self.rightSide[0][0]])))
                D_corner = sorted(list(map(str, [self.topSide[2][0], self.frontSide[0][0], self.leftSide[0][2]])))
                k = k + 1

                while self.bottomSide[0, 0] != 'y' or self.frontSide[2, 0] != 'g' or self.leftSide[2, 2] != 'o':
                    self.turn('-L')
                    self.turn('-U')
                    self.turn('L')
                    U_corner = sorted(list(map(str, [self.bottomSide[0][0], self.frontSide[2][0], self.leftSide[2][2]])))
                    if self.bottomSide[0, 0] != 'y' or self.frontSide[2, 0] != 'g' or self.leftSide[2, 2] != 'o':
                        self.turn('U')
                    A_corner = sorted(list(map(str, [self.topSide[0][0], self.leftSide[0][0], self.backSide[0][2]])))
                    B_corner = sorted(list(map(str, [self.topSide[0][2], self.backSide[0][0], self.rightSide[0][2]])))
                    C_corner = sorted(list(map(str, [self.topSide[2][2], self.frontSide[0][2], self.rightSide[0][0]])))
                    D_corner = sorted(list(map(str, [self.topSide[2][0], self.frontSide[0][0], self.leftSide[0][2]])))
                    U_corner = sorted(list(map(str, [self.bottomSide[0][0], self.frontSide[2][0], self.leftSide[2][2]])))
                    V_corner = sorted(list(map(str, [self.bottomSide[0][2], self.frontSide[2][2], self.rightSide[2][0]])))
                    W_corner = sorted(list(map(str, [self.bottomSide[2][2], self.backSide[2][0], self.rightSide[2][2]])))
                    X_corner = sorted(list(map(str, [self.backSide[2][0], self.backSide[2][2], self.leftSide[2][0]])))
        A_corner = sorted(list(map(str, [self.topSide[0][0], self.leftSide[0][0], self.backSide[0][2]])))
        B_corner = sorted(list(map(str, [self.topSide[0][2], self.backSide[0][0], self.rightSide[0][2]])))
        C_corner = sorted(list(map(str, [self.topSide[2][2], self.frontSide[0][2], self.rightSide[0][0]])))
        D_corner = sorted(list(map(str, [self.topSide[2][0], self.frontSide[0][0], self.leftSide[0][2]])))
        U_corner = sorted(list(map(str, [self.bottomSide[0][0], self.frontSide[2][0], self.leftSide[2][2]])))
        V_corner = sorted(list(map(str, [self.bottomSide[0][2], self.frontSide[2][2], self.rightSide[2][0]])))
        W_corner = sorted(list(map(str, [self.bottomSide[2][2], self.backSide[2][0], self.rightSide[2][2]])))
        X_corner = sorted(list(map(str, [self.backSide[2][0], self.backSide[2][2], self.leftSide[2][0]])))'''






cube = RubiksCube()
#moves = 'B L2 U2 F L2 B R U R2 -L B2 M2 R2 -D F2 -U F2 R2 -B D2 F2 L2 U F L U2'.split()
moves = 'L2 U2'.split()
for move in moves:
    cube.turn(move)

cube.corners_solve()


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
if __name__ == '__main__':
    main()


'''A_corner = self.topSide[0, 0], self.leftSide[0, 0], self.backSide[0, 2]
        A_corner = sorted(list(map(str, A_corner)))
        B_corner = self.topSide[0, 2], self.backSide[0, 0], self.rightSide[0, 2]
        B_corner = sorted(list(map(str, B_corner)))
        C_corner = self.topSide[2, 2], self.frontSide[0, 2], self.rightSide[0, 0]
        C_corner = sorted(list(map(str, C_corner)))
        D_corner = self.topSide[2, 0], self.frontSide[0, 0], self.leftSide[0, 2]
        D_corner = sorted(list(map(str, D_corner)))
        U_corner = self.bottomSide[0, 0], self.frontSide[2, 0], self.leftSide[2, 2]
        U_corner = sorted(list(map(str, U_corner)))
        V_corner = self.bottomSide[0, 2], self.frontSide[2, 2], self.rightSide[2, 0]
        V_corner = sorted(list(map(str, V_corner)))
        W_corner = self.bottomSide[2, 2], self.backSide[2, 0], self.rightSide[2, 2]
        W_corner = sorted(list(map(str, W_corner)))
        X_corner = self.backSide[2, 0], self.backSide[2, 2], self.leftSide[2, 0]'''



