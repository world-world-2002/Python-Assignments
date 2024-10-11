# 1. What is OOP?
'''
Object-Oriented Programming (OOP) is a programming paradigm that organizes code into
units called objects. Each object combines related data (attributes) and functions
(methods) that operate on that data.

In other words, OOP allows us to model real-world entities by representing their
behavior (methods) and characteristics (attributes) in a structured way. This makes
code more modular, reusable, and easier to understand.
'''



# 2. What is class?
'''A class is like a unit of code in which the code gets classified. 
It is used when we need a blueprint or a pre-defined block to use for each instance of our object, 
and we want to show the behavior and characteristics of that object inside that class.
'''

# 3. What is an Object?
'''
An object is an instance of a class. It is created based on the blueprint defined by the class.
Objects contain their own data (attributes) and can perform actions (methods) defined in the class.
For example, if "Song" is a class, then "mySong" is an object created from that class.
'''

# The example shows the combination of functions and attributes in one unit or class (song).

class Song:

    # 4. What is a constructor?
    '''
    A constructor is a method that creates an instance of a class.
    It specifies what parameters are needed to initialize the instance.
    The constructor assigns initial values to the instance variables.
    '''

    def __init__(self, name, length):


    # 7. What is the self keyword in a Class?
        '''
       The self keyword is a reference to the instance of the class.
       It allows us to refer to the instance and access its attributes and methods.
        '''

        self.name = name
        self.length = str(length)

    # the song has one behavior which is playing the song.
    # This is a function, but since it is inside a class we call it a method.
    def play(self):
            '''

               Plays the song and displays its name and duration.

               This method outputs the name and duration of the song
               to the console when called.

               Returns:
                   None
            '''


            #6. What is Concatenation?
            '''
            Concatenation is the process of combining two or more strings into one single string. 
            In Python, this is typically done using the `+` operator.
            '''

            print('the song name is: ' + self.name +'\nThe duration of the song is: ' +self.length +'min')


# creating an instance of the Song class and storing it in a variable named mySong
mySong = Song("city of stars", 5)
# Calling the play() function of the song on the instance
mySong.play()




#5. What is Inheritance?
'''
Inheritance is when a class inherits the behavior and characteristics of another class (the parent class). 
It allows the child class to have its own attributes and methods while also including those of the parent class.
'''

# PopSong is a child class of the Song class. It inherits the attributes and methods from the Song class.
class PopSong(Song):
    def __init__(self, name, length, year, singer):
        super().__init__(name, length)
        self.year = year
        self.singer = singer

    def play(self):
        print(f'The name of song is: {self.name}\nThe length is: {self.length}min\nReleased year is: {self.year}\nThe singer is: {self.singer}')


popSong1 = PopSong("City of stars", 3, 2020, "Emma Ston")

popSong1.play()


