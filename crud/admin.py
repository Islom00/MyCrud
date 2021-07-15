from django.contrib import admin

from crud.models import AuthorModel, GenreModel, BookModel


@admin.register(AuthorModel)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ["name", "birth_date", "created_at"]
    list_filter = ["birth_date"]
    search_fields = ["name"]


@admin.register(GenreModel)
class GenreModelAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["title"]


@admin.register(BookModel)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "created_at"]
    list_filter = ["genres", "created_at"]
    search_fields = ["title"]

