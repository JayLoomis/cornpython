import curses
import math
import random

DCHARS = {"horizontal": 9473,
          "vertical": 9475,
          "corner_snw": 9491,
          "corner_sne": 9487,
          "corner_nne": 9495,
          "corner_nnw": 9499,
          "low_half": 0x2584,
          "up_half": 0x2580,
          "left_half": 0x258C,
          "right_half": 0x2590,
          "up": 9650,
          "down": 9660,
          "left": 9668,
          "right": 9658,
          "fisheye": 9678}

VALID_DIRECTIONS = [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT]

def move_pos(pos, dir, bounds):
    """ Adjust's the character's position

    Doesn't draw anything, just adjusts the position.

    Params:
        pos - The starting position as a tuple of row and column. This is the
              coordinate order of curses, not the more common x, y.
        dir - The cardinal direction in which to move, as a single character
              string in lower case, i.e. "n", "s", "e", or "w".
        bounds - The maximum y and x positions of the playfield, assuming an
                 upper-left y, x origin of 0, 0. Stored in a tuple.
    """
    if dir == curses.KEY_UP:
        if pos[0] > 0:
            return (pos[0] - 1, pos[1])
        else:
            return pos
    elif dir == curses.KEY_DOWN:
        if pos[0] < bounds[0]:
            return (pos[0] + 1, pos[1])
        else:
            return pos
    elif dir == curses.KEY_LEFT:
        if pos[1] < bounds[1]:
            return (pos[0], pos[1] - 1)
        else:
            return pos
    elif dir == curses.KEY_RIGHT:
        if pos[1] > 0:
            return (pos[0], pos[1] + 1)
        else:
            return pos

stdscr = curses.initscr()

# Turning off key echoing. This means that input from the keyboard isn't
# automatically idsplayed in screen.
curses.noecho()

# Turning off buffered input mode, the default, which keeps input in a
# buffer until you hit return. With it off, we can process keystrokes as they
# are entered.
curses.cbreak()

# Use the keyboard constants provided by curses to avoid multi-char escape
# sequences.
stdscr.keypad(True)

# Make the cursor invisible.
curses.curs_set(0)


rows, cols = stdscr.getmaxyx()

# Note the maximum column and row values for bounds checking.
bounds = (rows -1, cols -1)

cur_pos = (rows // 2, cols // 2)
prev_pos = cur_pos
tail_pos = cur_pos

# Randomly determine a starting direction, and draw the appropriate arrow.
start_dir = random.randint(0, 3)
if start_dir == 0:
    stdscr.addch(cur_pos[0], cur_pos[1], DCHARS["up"])
elif start_dir == 1:
    stdscr.addch(cur_pos[0], cur_pos[1], DCHARS["down"])
elif start_dir == 2:
    stdscr.addch(cur_pos[0], cur_pos[1], DCHARS["left"])
elif start_dir == 3:
    stdscr.addch(cur_pos[0], cur_pos[1], DCHARS["right"])



# Main game loop!
while True:
    cmd = stdscr.getch()

    if cmd in VALID_DIRECTIONS:
        new_pos = move_pos(cur_pos, cmd, bounds)
        if new_pos != cur_pos:
            tail_pos = prev_pos
            prev_pos = cur_pos
            cur_pos = new_pos

            # Draw the head and redraw the neck
            if cmd == curses.KEY_UP:
                stdscr.addch(cur_pos[0], cur_pos[1], DCHARS["up"])
                if tail_pos[1] > cur_pos[1]:
                    prev_char = DCHARS["corner_nne"]
                elif tail_pos[1] < cur_pos[1]:
                    prev_char = DCHARS["corner_nnw"]
                else:
                    prev_char = DCHARS["vertical"]

            elif cmd == curses.KEY_DOWN:
                stdscr.addch(cur_pos[0], cur_pos[1], DCHARS["down"])
                if tail_pos[1] > cur_pos[1]:
                    prev_char = DCHARS["corner_sne"]
                elif tail_pos[1] < cur_pos[1]:
                    prev_char = DCHARS["corner_snw"]
                else:
                    prev_char = DCHARS["vertical"]

            elif cmd == curses.KEY_LEFT:
                stdscr.addch(cur_pos[0], cur_pos[1], DCHARS["left"])
                if tail_pos[0] > cur_pos[0]:
                    prev_char = DCHARS["corner_snw"]
                elif tail_pos[0] < cur_pos[0]:
                    prev_char = DCHARS["corner_nnw"]
                else:
                    prev_char = DCHARS["horizontal"]

            elif cmd == curses.KEY_RIGHT:
                stdscr.addch(cur_pos[0], cur_pos[1], DCHARS["right"])
                if tail_pos[0] > cur_pos[0]:
                    prev_char = DCHARS["corner_sne"]
                elif tail_pos[0] < cur_pos[0]:
                    prev_char = DCHARS["corner_nne"]
                else:
                    prev_char = DCHARS["horizontal"]

            stdscr.addch(prev_pos[0], prev_pos[1], prev_char)
        else:
            continue

    elif cmd == ord("q"):
        break

    stdscr.refresh()


#stdscr.addstr(0, 0, "Your window has {} columns and {} rows.".format(cols, rows))
#stdscr.addstr(1, 0, "It's so nice to meet you!")
#stdscr.addch(2, 0, 179)
#stdscr.addch(3, 0, 196)
#stdscr.addch(4, 0, 219)


# Standard stuff to shut down. Bascially do the opposite of setup!
stdscr.keypad(False)
curses.nocbreak()
curses.echo()

curses.endwin()
