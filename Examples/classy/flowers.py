""" A game about growing flowers.

This is the start of a little game about growing flowers in your garden.
At present, it only lets you passively wait for a set number of flowers to
bloom, but the infrastructure here could be easily refactored to create a game
where you could us a limited number of actions to care for the flowers to try
to get the best blooms, or concurrent sets of blooms, or whatever.

The module is actually intended as a demonstration of some object-oriented
programming techniques, and the mechanics of those techniques as implemented in
Python. For example, this is a module-level docstring. I've added full
docstrings to everything in the module to model how you should use them.
"""
import random as rnd
import curses

class Flower:
    """ Represents a single flower in the game.

    Each flower is its own object. The game object registers its bloom callback
    with each flower, so they can report back when they bloom.

    Attributes:
        name - The name of the flower.
        time_to_bloom - The number of days required to bloom.
                        Ranges from 4 to 12.
        color - The color of the flower's eventual bloom.
        size - The size of the flower's eventual bloom.
        time_elapsed - The amount of time that has passed since the flower was
                       planted. Note that this is a float value, in
                       anticipation of future enhancements that increase or
                       reduce the effect of a day for individual flowers.
        subscribers - List of all objects that are subscribed to receive
                      messages from the flower.
    """

    @staticmethod
    def determine_flower_color():
        """ Randomly determines the color of a flower.

        Flower colors are randomly determined using different weights for each
        color. The possible colors in order of increasing rarity are:

        white, pink, yellow, purple, orange, red, blue, green, black

        Returns:
            A string indicating the color of the flower.
        """
        # Ahoy, Brisket here! These first two methods are static methods.
        # What's a static method, you ask? It is a method that you call on the
        # class, not on an individual instance (object) of that class.
        # So, to get a random flower color, you must call:
        #
        #   some_flower_instance.color = Flower.determine_flower_color()
        #
        # Static methods are functions that aren't behaviors of a class's
        # instances, but that conceptually tied to the thing that the class
        # represents. In these cases, they determine starting values to assign
        # to an instance when it's created. You don't determine the color more
        # than once, so it's not really needed as a method of each individual
        # flower.
        color_val = rnd.randint(1, 34)

        # There's probably a better way to capture the weighted odds for each
        # color, but I hard-coded it for expediency. Maybe you can think of a
        # more sustainable way to capture that information?
        if color_val == 1:
            return "black"
        elif color_val == 2:
            return "green"
        elif color_val <= 4:
            return "blue"
        elif color_val <= 7:
            return "red"
        elif color_val <= 11:
            return "orange"
        elif color_val <= 15:
            return "purple"
        elif color_val <= 20:
            return "yellow"
        elif color_val <= 26:
            return "pink"
        else:
            return "white"


    @staticmethod
    def determine_flower_size():
        """ Randomly determines the size of a flower.

        Flower sizes are randomly determined using different weights for each
        size. The possible sizes in order of increasing rarity are:

        medium, large, small, tiny, giant

        Returns:
            A string indicating the size of the flower.
        """
        size_val = rnd.randint(1, 16)
        if size_val == 1:
            return "giant"
        elif size_val <= 3:
            return "tiny"
        elif size_val <= 6:
            return "small"
        elif size_val <= 10:
            return "large"
        else:
            return "medium"


    def __init__(self, name):
        self.name = name
        self.time_to_bloom = 4 + rnd.randint(0, 8)
        self.color = Flower.determine_flower_color()
        self.size = Flower.determine_flower_size()
        self.time_elapsed = 0.0
        self.subscribers = []

    def subscribe(self, callback):
        """ Adds a callback to the subscriber list """
        self.subscribers.append(callback)
    
    def bloom(self):
        """ Broadcasts a bloom to the subscribers. """
        for sub in self.subscribers:
            sub(self.name, self.size, self.color)
    
    def advance_time(self, increment=1.0):
        """ Adds elapsed time to the flower.

        When the elapsed time reaches the bloom threshold, the flower blooms.

        Arguments:
            increment - The amount of elapsed time to add. May be fractional,
                        because some conditions change the effective elapsed
                        time of a day.
        """
        self.time_elapsed += increment
        if self.time_elapsed >= self.time_to_bloom:
            self.bloom()


class FlowerGame:
    """ Management and UI class for the Flower Game.

    This class includes an undifferentiated mix of logic control and UI. That's
    fine at present, but if either one of those tasks evolves to become
    significantly more complicated, they should be separated into distinct sets
    of methods, or a different class entirely.

    Attributes:
        flowers - A list of Flower objects.
    """
    def __init__(self):
        self.flowers = []

        for i in range(10):
            self.flowers.append(Flower(i))
            self.flowers[i].subscribe(self.bloom_callback)


    def init_ui(self):
        """ Sets up the game screen.

        Initializes curses and configures the terminal settings to where they
        need to be. Also logs information about the terminal screen for use in
        other parts of the application.
        """
        stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        stdscr.keypad(True)


    def shut_down_ui(self):
        """ Resets the terminal state.

        Undoes all of the settings changes we made to the terminal on startup.
        """
        stdscr.keypad(False)
        curses.nocbreak()
        curses.echo()
        curses.endwin()


    def bloom_callback(self, name, size, color):
        print(f"A {size} {color} bloom appears on {name}!")
        for i in range(len(self.flowers)):
            if self.flowers[i].name == name:
                del self.flowers[i]
                break

    def draw_interface():
        pass
    
    def start(self):
        """ Runs the main game loop.

        In its current state, the game loop runs until all the flowers have
        bloomed. The text output is handled here, too.
        """
        print("Hello! You've just finsihed planting ten flowers in your garden.")
        print("Let's watch them grow!", end="\n\n")

        while len(self.flowers) > 0:
            input("Press enter to move to the next day.")

            for flower in self.flowers:
                flower.advance_time()
        
        print("That's all of your flowers finished.")



def main():
    """ Application entry point. """
    game = FlowerGame()

    game.start()
    

if __name__ == "__main__":
    main()