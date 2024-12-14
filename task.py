class Tree:
    """Describes a tree with certain characteristics"""
    view: str = "simple"
    location: str = "Asia"

    def __init__(self, width: float, height: float, age: int) -> None:
        """Initialize object tree

        :param width: The width of the tree.
        :param height: The height of the tree.
        :param age: Age tree of years.
        """
        self.width: float = width
        self.height: float = height
        self.age: int = age

    def display_info(self) -> None:
        """Displays information about the tree: width, height, age"""
        print(f"Width: {self.width}  Height: {self.height}  Age: {self.age}")

    def determine_the_age(self, new_age: int) -> None:
        """
            Sets the new age of the tree and outputs it.

            :param new_age: New age tree of years.

            Example:
            >>> tree = Tree(5, 10, 20)
            >>> tree.determine_the_age(25)
            New age: 25
            >>> tree.age
            25
        """
        self.age = new_age
        print(f"New age: {self.age}")


class Person:
    """Describes a Person with certain characteristics"""
    skin_color: str = "white"
    eye_color: str = "blue"
    height: float = 170

    def __init__(self, name: str, age: int, sleep_hours: int) -> None:
        """Initialize object Person

        :param name: The name of the Person.
        :param age: The age of the Person.
        :param sleep_hours: number of hours of sleep per day.
        """
        self.name: str = name
        self.age: int = age
        self.sleep_hours: int = sleep_hours

    def display_info(self) -> None:
        """Displays information about the Person: name, age"""
        print(f"Name: {self.name}  Age: {self.age}")

    def say(self, message: str) -> str:
        """Displays the massage

        :param message: The message that needs to be voiced.
        :return: Returns the same message.
        """
        print(message)
        return message

    def hours_of_sleep(self, sleep_hours: int) -> None:

        """
        Sets the number of hours of sleep and outputs it.

                :param sleep_hours: The new number of hours of sleep.
        """

        self.sleep_hours = sleep_hours
        print(f"Hours of sleep: {self.sleep_hours}")


class Music:
    """Represents a musical composition."""
    name_song: str = "None"

    def __init__(self, name_artist: str, song_duration: float, album: str) -> None:
        """
        Initializes the Music object.

                :param name_artist: The name of the artist.
                :param song_duration: The duration of the song in minutes.
                :param album: The name of the album.
        """
        self.name_artist: str = name_artist
        self.song_duration: float = song_duration
        self.album: str = album

    def display_info(self) -> None:
        """Displays information about the song: artist, duration and album."""
        print(f"Artist: {self.name_artist}  Duration: {self.song_duration}  Album: {self.album}")

    def change_album(self, new_album: str) -> None:
        """
        Changes the album and displays it.

        :param new_album: New album.
        """
        self.album = new_album
        print(f"New album: {self.album}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()