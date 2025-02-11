import pytest
import Cube_array
import random
def test_V_corner():
    moves = 'R D -L'.split()
    for move in moves:
        Cube_array.cube.turn(move)
    Cube_array.cube.corners_solve()
    assert (Cube_array.cube.bottomSide[0, 2]=='y' and Cube_array.cube.frontSide[2, 2]=='g' and Cube_array.cube.rightSide[2, 0]=='r')

def main():
    test_V_corner()
if __name__ == '__main__':
    main()

