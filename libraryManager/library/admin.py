from django.contrib import admin

# Register your models here.

from library.models import Author, Book, BookCheckoutInfo

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author_name", "genre", "quantity_in_stock")
    list_filter = ("genre", "author__name")
    search_fields = (
        "title",
        "author",
    )

    raw_id_fields = ('author',)

    def author_name(self, obj):
        return obj.author.name


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "biography")
    list_filter = ("name",)
    search_fields = (
        "name",
    )

    raw_id_fields = ('biography',)


@admin.register(BookCheckoutInfo)
class BookCheckoutInfoAdmin(admin.ModelAdmin):
    list_display = ("book_name", "checkout_date", "is_returned")
    list_filter = ("book__title",)
    search_fields = (
        "book__title",
    )

    raw_id_fields = ('book',)
    def book_name(self, obj):
        return obj.title