# Eight Queens by Gordon Horsington
# Python 3 and Raspberry Pi Sense HAT
import sys, time, os
from sense_hat import SenseHat
sense = SenseHat()
def main():
    r       = [92, 0, 0]
    g       = [0, 92, 0]
    yellow  = [120, 120, 0]
    blue    = [0, 0, 120]
    white   = [120, 120, 120]
    empty_board = [
        g,r,g,r,g,r,g,r,
        r,g,r,g,r,g,r,g,
        g,r,g,r,g,r,g,r,
        r,g,r,g,r,g,r,g,
        g,r,g,r,g,r,g,r,
        r,g,r,g,r,g,r,g,
        g,r,g,r,g,r,g,r,
        r,g,r,g,r,g,r,g]
    results = [[0],[0],[0],[0],[0],[0],[0],[0],]
    for x in range(8):
        for y in range(91):
            results[x].append(0)
    find_all(results)
    game = [-1,-1,-1,-1,-1,-1,-1,-1]
    x, y, playing, display, midgame = 3, 4, True, False, False
    sense.set_pixels(empty_board)
    sense.set_pixel(x, y, blue)
    while playing:
        for event in sense.stick.get_events():
            if event.action == 'pressed':               
                if event.direction == 'up':
                    y, midgame = increase(y)
                if event.direction == 'down':
                    y, midgame = decrease(y)     
                if event.direction == 'right':
                    x, midgame = decrease(x)     
                if event.direction == 'left':
                    x, midgame = increase(x)
                if event.direction == 'middle':
                    if display:
                        playing = False
                    else:
                        if good_move(game, x, y):
                            midgame = True
                        else:
                            best = find_best(game, results)
                            display = show_answer(game, sense, white, blue, yellow, results, best)
                if midgame:
                    sense.set_pixels(empty_board)
                    sense.set_pixel(x, y, blue)
                    display, midgame = show_game(game, sense, white, blue)
    sense.clear()
    sys.exit()
def show_answer(game, sense, white, blue, yellow, results, best):
    for count in range(8):
        if game[count] >= 0:
            sense.set_pixel(count, game[count], blue)
    for count in range(8):
        if results[count][best] == game[count]:
            shade = white
        else:
            shade = yellow
        sense.set_pixel(count, results[count][best], shade)
        game[count] = -1
    return True
def show_game(game, sense, white, blue):
    count = 0
    for column in range(8):
        if game[column] != -1:
            sense.set_pixel(column, game[column], white)
            count += 1
    if count == 8:
        for count in range(3):
            time.sleep(0.25)
            for column in range(8):
                sense.set_pixel(column, game[column], blue)
            time.sleep(0.25)
            for column in range(8):
                sense.set_pixel(column, game[column], white)
        for column in range(8):
            game[column] = -1
        return True, False
    return False, False
def good_move(game, x, y):
    if game[x] == y:
        return False
    game[x] = y
    plus, minus = x + y, x - y
    for column in range(8):
        if column != x:
            row = game[column]
            if row == y or column + row == plus or column - row == minus:
                game[column] = -1
    return True
def find_best(game, results):
    better = 0
    best = 0
    for count in range(92):
        good = 0
        for column in range(8):
            if results[column][count] == game[column]:
                good +=1
        if good > better:
            better = good
            best = count
    return best  
def find_all(results):
    answer  = [0,0,0,0,0,0,0,0]
    number, row, count, flag= 0, 0, 8, True
    while number < 92:
        if flag:
            row += 1
        flag = True
        last = row - 1
        answer[last] += 1
        if row == 1:
            answer[last] = count
            count -= 1
        if not answer[last]:
            break
        if answer[last] > 8:
            answer[last] = 0
            row -= 1
            flag = False
        if flag and row != 1:
            flag = test(last, row, answer)
        if flag and row == 8:
            flag = False
            for column in range(8):
                results[column][number] = answer[column] - 1
            number += 1
    return
def test(last, row, answer):
    while (last):
        column = answer[last -1]
        trial = answer[row -1]
        if trial == column or trial == (column + row - last) or trial== (column - row + last):
            return False
        last -= 1
    return True
def increase(square):
    if square > 0:
        square -= 1
    else:
        square = 7
    return square, True
def decrease(square):
    if square < 7:
        square += 1
    else:
        square = 0
    return square, True
if __name__ == '__main__':
    main()
