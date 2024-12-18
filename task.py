import doctest

class Tree:
    """Describes a tree with certain characteristics."""

    def __init__(self, width: float, height: float, age: int) -> None:
        """Initialize object tree.

        :param width: The width of the tree.
        :param height: The height of the tree.
        :param age: Age of the tree in years.
        """
        self.width = self.validate_positive_float(width, "Width")
        self.height = self.validate_positive_float(height, "Height")
        self.age = self.validate_positive_int(age, "Age")

    @staticmethod
    def validate_positive_float(value, name):
        if not isinstance(value, (int, float)):
            raise TypeError(f"{name} must be of type int or float")
        if value <= 0:
            raise ValueError(f"{name} must be a positive number")
        return float(value)

    @staticmethod
    def validate_positive_int(value, name):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be of type int")
        if value <= 0:
            raise ValueError(f"{name} must be a positive number")
        return value

    def determine_the_width_and_height(self, new_height: float, new_width: float) -> None:
        """Sets the new height and width of the tree.

        :param new_height: The new height of the tree.
        :param new_width: The new width of the tree.

        Example:
        >>> tree = Tree(5, 10, 20)
        >>> tree.determine_the_width_and_height(15, 7)
        >>> tree.height
        15.0
        >>> tree.width
        7.0
        """
        self.height = self.validate_positive_float(new_height, "Height")
        self.width = self.validate_positive_float(new_width, "Width")

    def determine_the_age(self, new_age: int) -> None:
        """Sets the new age of the tree.

        :param new_age: New age of the tree in years.

        Example:
        >>> tree = Tree(5, 10, 20)
        >>> tree.determine_the_age(25)
        >>> tree.age
        25
        """
        self.age = self.validate_positive_int(new_age, "Age")


class Person:
    """Describes a Person with certain characteristics."""

    def __init__(self, name: str, age: int, sleep_hours: int) -> None:
        """Initialize object Person.

        :param name: The name of the Person.
        :param age: The age of the Person.
        :param sleep_hours: Number of hours of sleep per day.
        """

        if not isinstance(name, str):
            raise TypeError("Name must be of type str")

        self.name: str = name

        if not isinstance(age, int):
            raise TypeError("Age must be of type int")
        if age <= 0:
            raise ValueError("Age must be positive number")

        self.age: int = age

        if not isinstance(sleep_hours, int):
            raise TypeError("Sleep hours must be of type int")
        if sleep_hours <= 0:
            raise ValueError("Sleep hours must be positive number")

        self.sleep_hours: int = sleep_hours

    def say(self, message: str) -> str:
        """Displays the message.

        :param message: The message that needs to be voiced.
        :return: Returns the same message.

        Example:
        >>> person = Person("Alice", 30, 8)
        >>> person.say("Hello!")
        Hello!
        'Hello!'
        """
        if not isinstance(message, str):
            raise TypeError("Message must be of type str")

        print(message)
        return message

    def hours_of_sleep(self, new_sleep_hours: int) -> None:
        """
        Sets the number of hours of sleep.

        :param new_sleep_hours: The new number of hours of sleep.

        Example:
        >>> person = Person("Alice", 30, 8)
        >>> person.hours_of_sleep(7)
        Hours of sleep: 7
        """
        if not isinstance(new_sleep_hours, int):
            raise TypeError("Sleep hours must be of type int")
        if new_sleep_hours <= 0:
            raise ValueError("Sleep hours must be positive number")

        self.sleep_hours = new_sleep_hours
        print(f"Hours of sleep: {self.sleep_hours}")

class Music:
    """Represents a musical composition."""

    def __init__(self, name_artist: str, song_duration: float, album: str) -> None:
        """Initializes the Music object.

        :param name_artist: The name of the artist.
        :param song_duration: The duration of the song in minutes.
        :param album: The name of the album.
        """
        if not isinstance(name_artist, str):
            raise TypeError("Name artist must be of type str")

        self.name_artist: str = name_artist

        if not isinstance(song_duration, (int, float)):
            raise TypeError("Song duration must be of type int or float")
        if song_duration <= 0:
            raise ValueError("Song duration must be a positive number")

        self.song_duration: float = song_duration

        if not isinstance(album, str):
            raise TypeError("Album must be of type str")

        self.album: str = album

    def change_song_duration(self, new_song_duration: float) -> None:
        """Changes the song duration and displays the new duration.

        :param new_song_duration: The new duration of the song (in minutes).

        Example:
        >>> music = Music("Artist", 3.5, "Album")
        >>> music.change_song_duration(4.0)
        New song duration: 4.0
        """
        if not isinstance(new_song_duration, (int, float)):
            raise TypeError("Song duration must be of type int or float")
        if new_song_duration <= 0:
            raise ValueError("Song duration must be a positive number")

        self.song_duration = new_song_duration
        print(f"New song duration: {self.song_duration}")

    def change_album(self, new_album: str) -> None:
        """Changes the album and displays it.

        :param new_album: New album.

        Example:
        >>> music = Music("Artist", 3.5, "Old Album")
        >>> music.change_album("New Album")
        New album: New Album
        """
        if not isinstance(new_album, str):
            raise TypeError("Album must be of type str")

        self.album = new_album
        print(f"New album: {self.album}")


if __name__ == "__main__":
    doctest.testmod() 
