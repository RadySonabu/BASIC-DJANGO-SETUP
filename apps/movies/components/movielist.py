from django_unicorn.components import UnicornView, QuerySetType
from ..models import Movie


class MovielistView(UnicornView):
    name: str = ''
    search: str = ''
    movies: QuerySetType[Movie] = Movie.objects.none()

    def mount(self):
        """ On mount, populate the movies property w/ a QuerySet of all movies """
        self.movies = Movie.objects.all()
        print(self.movies)

    def add_movie(self):
        """ Create the new movie, get new list of all movies, and clear the 'name' property """
        Movie.objects.create(name=self.name)
        self.movies = Movie.objects.all()
        self.name = ''
    
    def search_movie(self):
        """Search the movie list"""
        search_result = Movie.objects.filter(name__icontains=self.search)
        self.movies = search_result

    def delete_all(self):
        """ Delete all movies and reset 'movies' property """
        Movie.objects.all().delete()
        self.movies = Movie.objects.none()

    def delete_movie(self, id):
        print(id)
        Movie.objects.filter(pk=id).delete()
        self.movies = Movie.objects.all()