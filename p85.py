#! python

import time
import euler

def main():

    solutions = []
    areas = []

    # find the square with just over 2 million rectangles
    square_width = 20
    num_rects_under = 0
    num_rects_over = 0
    while num_rects_over < 2000000:
        num_rects_over = 0
        for w in range(1, square_width + 1):
            for h in range(1, square_width + 1):
                num_rects_over += (square_width - w + 1) * (square_width - h + 1)
        if num_rects_over > 2000000:
            solutions.append(num_rects_under)
            solutions.append(num_rects_over)
            areas.append((square_width - 1) * (square_width - 1))
            areas.append(square_width * square_width)
        else:
            num_rects_under = num_rects_over
        square_width += 1

    # now we'll reduce the height by one each time and grow the width until we just pop over 2 million
    for height in range(square_width - 1, 0, -1):
        num_rects_under = 0
        num_rects_over = 0
        width = square_width
        while num_rects_over < 2000000:
            num_rects_over = 0
            for w in range(1, width + 1):
                for h in range(1, height + 1):
                    num_rects_over += (width - w + 1) * (height - h + 1)
            if num_rects_over > 2000000:
                solutions.append(num_rects_under)
                solutions.append(num_rects_over)
                areas.append((width - 1) * (height))
                areas.append(width * height)
            else:
                num_rects_under = num_rects_over
            width += 1

    # find closest solution
    solutions = [abs(2000000 - s) for s in solutions]
    min_index = solutions.index(min(solutions))
    min_area = areas[min_index]
    print(min(solutions))
    print(min_area)

if __name__ == "__main__":
    start = time.time()
    main()
    print('RUNTIME: ', time.time() - start, 's')
