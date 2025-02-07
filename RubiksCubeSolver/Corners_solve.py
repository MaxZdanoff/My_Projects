import numpy as np
import Cube_array
class Corners:
    def __init__(self):
        from Cube_array import cube
        self.topCorners = np.array([
            [cube.backSide[0, 2].copy(), cube.topSide[0, 0].copy(), cube.leftSide[0, 0].copy()],
            [cube.backSide[0, 0].copy(), cube.topSide[0, 2].copy(), cube.rightSide[0, 2].copy()],
            [cube.frontSide[0, 0].copy(), cube.topSide[2, 0].copy(), cube.leftSide[0, 2].copy()],
            [cube.frontSide[0, 2].copy(), cube.topSide[2, 2].copy(), cube.rightSide[0, 0].copy()]
        ])
        self.bottomCorners = np.array([
            [cube.backSide[2, 2].copy(), cube.bottomSide[2, 0].copy(), cube.leftSide[2, 0].copy()],
            [cube.backSide[2, 0].copy(), cube.bottomSide[2, 2].copy(), cube.rightSide[2, 2].copy()],
            [cube.frontSide[2, 0].copy(), cube.bottomSide[0, 0].copy(), cube.leftSide[2, 2].copy()],
            [cube.frontSide[2, 2].copy(), cube.bottomSide[0, 2].copy(), cube.rightSide[2, 0].copy()]
        ])
    def corners_state(self):
        print(f'   [{self.topCorners[0, 0]}]     [{self.topCorners[1, 0]}]\n[{self.topCorners[0, 2]}][{self.topCorners[0, 1]}]     [{self.topCorners[1, 1]}][{self.topCorners[1, 2]}]')
        print(f'\n[{self.topCorners[2, 2]}][{self.topCorners[2, 1]}]     [{self.topCorners[3, 1]}][{self.topCorners[3, 2]}]\n   [{self.topCorners[2, 0]}]     [{self.topCorners[3, 0]}]')
        print(f'\n   [{self.bottomCorners[0, 0]}]     [{self.bottomCorners[1, 0]}]\n[{self.bottomCorners[0, 2]}][{self.bottomCorners[0, 1]}]     [{self.bottomCorners[1, 1]}][{self.bottomCorners[1, 2]}]')
        print(f'\n[{self.bottomCorners[2, 2]}][{self.bottomCorners[2, 1]}]     [{self.bottomCorners[3, 1]}][{self.bottomCorners[3, 2]}]\n   [{self.bottomCorners[2, 0]}]     [{self.bottomCorners[3, 0]}]')

    def solveCorners(self):
        X = np.array(['b', 'y', 'o']) #where the pieces should go
        W = np.array(['y', 'r', 'b'])
        U = np.array(['y', 'o', 'g'])
        V = np.array(['y', 'g', 'r'])

        A_corner = self.topCorners[0] #where they are currently
        B_corner = self.topCorners[1]
        C_corner = self.topCorners[2]
        D_corner = self.topCorners[3]
        X_corner = self.bottomCorners[0]
        W_corner = self.bottomCorners[1]
        U_corner = self.bottomCorners[2]
        V_corner = self.bottomCorners[3]
        if np.all(np.isin(A_corner, X_corner)):
            print("True")

Cube_array.cube.turn('')
corners = Corners()

corners.corners_state()
corners.solveCorners()
#to make turns work define Corners() as a new variable after coding the turns
#possibly consider removing all classes or figure out new way of making turns easier













