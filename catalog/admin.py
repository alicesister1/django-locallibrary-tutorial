# Register your models here.
from django.contrib import admin

from catalog.models import Book, Author, Genre, BookInstance, Language


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # author는 다대일 관계이기 때문에 __str__()값에 의해 표현됨
    # genre는 다대다 관계이기 때문에 DB 접근비용 때문에 display_genre 함수를 대신 호출함
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]


class BookInline(admin.TabularInline):
    model = Book
    extra = 0


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'imprint', 'due_back', 'status', 'id')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        })
    )


admin.site.register(Genre)
admin.site.register(Language)
