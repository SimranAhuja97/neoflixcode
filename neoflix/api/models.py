from django.db import models
# Create your models here.


class MovieStore(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    rating = models.CharField(max_length=25, blank=True, unique=False)
    category = models.CharField(max_length=25, blank=True, unique=False)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)


class MovieList(models.Model):
    """This class represents the movielist model."""
    movie = models.ForeignKey(
        MovieStore, related_name='userlists',  on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User',
                              related_name='movielists',
                              on_delete=models.CASCADE)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    @staticmethod
    def storeinlist(name, owner):
        movie = MovieStore.objects.get(name=name)
        movielist = MovieList(movie=movie, owner=owner)
        movielist.save()


class Comment(models.Model):
    comment = models.CharField(max_length=255, blank=False, unique=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    movie = models.ForeignKey(
        MovieStore, related_name='comments',  on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User',
                              related_name='comments',
                              on_delete=models.CASCADE)

    @staticmethod
    def createcomment(comment, name, owner):
        movie = MovieStore.objects.get(name=name)
        comment = Comment(comment=comment, moview=movie, owner=owner)
        comment.save()
