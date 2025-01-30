class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    @property
    def attribute_name_with_using_property(self):
        return self.name

    @property
    def attribute_author_with_using_property(self):
        return self.author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook (Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def attribute_pages_with_using_property(self):
        return self.pages

    @attribute_pages_with_using_property.setter
    def attribute_pages_with_using_property(self, probably_pages):
        if not isinstance(probably_pages, int):
            raise ValueError("Колличество страниц должно быть числом целым.")

        if probably_pages < 0:
            raise ValueError("Колличество страниц должно быть неотрицательным.")
        self.pages = probably_pages

    def __str__(self):
        return f"Бумажная {super().__str__()} с {self.pages} страницами."


class AudioBook (Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def attribute_duration_with_using_property(self):
        return self.duration

    @attribute_duration_with_using_property.setter
    def attribute_duration_with_using_property(self, probably_duration):
        if not isinstance(probably_duration, (int, float)):
            raise ValueError("Длительность должна быть числом (целым или дробным).")

        if probably_duration < 0:
            raise ValueError("Длительность должна быть неотрицательной.")
        self.duration = probably_duration

    def __str__(self):
        return f"Аудио - {super().__str__()}, длительностью {self.duration} часов."
