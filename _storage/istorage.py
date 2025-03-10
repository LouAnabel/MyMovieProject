from abc import ABC, abstractmethod


class IStorage(ABC):
    """An interface called IStorage that exposes all the 4 CRUD commands."""

    @abstractmethod
    def list_movies(self):
        pass


    @abstractmethod
    def add_movie(self, title, year, rating):
        pass


    @abstractmethod
    def delete_movie(self, title):
        pass


    @abstractmethod
    def update_movie(self, title, rating):
        pass

