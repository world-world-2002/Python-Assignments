"""
Object-Oriented Programming (OOP) is a programming paradigm that organizes code into
units called objects. Each object combines related data (attributes) and functions
(methods) that operate on that data.

In other words, OOP allows us to model real-world entities by representing their
behavior (methods) and characteristics (attributes) in a structured way. This makes
code more modular, reusable, and easier to understand.
"""



# The example of OOP:
# The example shows the combination of functions and attributes in one unit (song).

class Song:
    """
        Represents a musical song with a title and duration.

        Attributes:
            name (str): The name of the song.
            length (str): The duration of the song in a format like "3:45".
        """
    def __init__(self, name, length):
        """
               Initializes a new Song instance.

               Args:
                   name (str): The name of the song.
                   length (str): The duration of the song.
               """
        self.name = name
        self.length = length

    # the song has one behavior which is playing the song
    def play(self):
        """
               Plays the song and displays its name and duration.

               This method outputs the name and duration of the song
               to the console when called.

               Returns:
                   None
               """
        # Using a print statement to display the song's name and duration.
        print(f'the song name is: {self.name}\nthe duration of the song is: {self.length} min')


# creating an instance of the Song class and storing it in a variable named mySong
mySong = Song("city of stars", 5)
# Calling the play() function of the song on the instance
mySong.play()







