from game import Game

if __name__ == '__main__':
    width = 7
    height = 5
    if 1 <=width <= 15 and 1 <= height <= 8:
        game = Game(2 * width + 1, 2 * height + 1)
        game.run()
    else:
        print('错误的长宽')