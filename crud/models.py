from django.db import models

class AuthorModel(models.Model):
    name = models.CharField(max_length=60, verbose_name="name")
    birth_date = models.IntegerField(null=True, verbose_name="birth date")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created at")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "author"
        verbose_name_plural = "authors"


class GenreModel(models.Model):
    title = models.CharField(max_length=20, verbose_name="title")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created at")


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "genre"
        verbose_name_plural = "genres"


class BookModel(models.Model):
    title = models.CharField(max_length=128, verbose_name="title")
    author = models.ForeignKey(AuthorModel, on_delete=models.PROTECT, related_name="books", verbose_name="author")
    genres = models.ManyToManyField(GenreModel, related_name="books", verbose_name="genres")
    cover = models.ImageField(upload_to="images", blank=True)
    isbn = models.CharField(max_length=13, verbose_name="isbn")
    page_count = models.IntegerField(null=True, verbose_name="page count")
    summary = models.TextField(verbose_name="summary")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created at")


    def __str__(self):
        return  self.title

    class Meta:
        verbose_name = "book"
        verbose_name_plural = "books"