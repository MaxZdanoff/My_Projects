from Cube_array import cube
from Cube_array import cube_state


def test_corners_solve():
    cube.create_scramble()
    cube.corners_info()

    expected = ['y', 'y', 'y', 'y']
    actual = [cube.bottomSide[0][0], cube.bottomSide[0][2], cube.bottomSide[2][0], cube.bottomSide[2][2]]

    expected_1 = ['g', 'g']
    actual_1 = [cube.frontSide[2][0], cube.frontSide[2][2]]

    expected_2 = ['r', 'r']
    actual_2 = [cube.rightSide[2][0], cube.rightSide[2][2]]

    expected_3 = ['o', 'o']
    actual_3 = [cube.leftSide[2][0], cube.leftSide[2][2]]

    expected_4 = ['b', 'b']
    actual_4 = [cube.backSide[2][0], cube.backSide[2][2]]

    print(cube_state())
    assert expected == actual
    assert expected_1 == actual_1
    assert expected_2 == actual_2
    assert expected_3 == actual_3
    assert expected_4 == actual_4


def main():
    num_tests = 100
    for _ in range(num_tests):
        test_corners_solve()


if __name__ == '__main__':
    main()
