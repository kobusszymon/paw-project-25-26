from django.contrib import admin

from .models import Genre, Author, Book, Osoba, Stanowisko

class OsobaAdmin(admin.ModelAdmin):
    list_display = ("imie", "nazwisko", "plec", "stanowisko", "data_dodania")
    list_filter = ("stanowisko", "data_dodania")
    
class StanowiskoAdmin(admin.ModelAdmin):
    list_display = ("nazwa", "opis")
    list_filter = ("nazwa")

admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Osoba, OsobaAdmin)
admin.site.register(Stanowisko, StanowiskoAdmin)