from django.db import models

# Lista wyboru miesięcy wydania
MONTHS = models.IntegerChoices(
    'Miesiace',
    'Styczeń Luty Marzec Kwiecień Maj Czerwiec Lipiec Sierpień Wrzesień Październik Listopad Grudzień'
)

# Lista wyboru formatu książki
BOOK_FORMATS = (
    ('P', 'Papierowa'),
    ('E', 'E-book'),
    ('A', 'Audiobook'),
)

class Plec(models.IntegerChoices):
    MEZCZYZNA = 1
    KOBIETA = 2
    INNA = 3

class Genre(models.Model):
    """Model reprezentujący gatunek literacki."""
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, help_text="Krótki opis gatunku literackiego.")
    typical_themes = models.CharField(
        max_length=200,
        blank=True,
        help_text="Typowe motywy i tematy występujące w tym gatunku."
    )
    is_fiction = models.BooleanField(default=True, help_text="Czy gatunek jest fikcyjny (literatura piękna).")
    popularity_rank = models.PositiveSmallIntegerField(
        default=0,
        help_text="Ocena popularności (0–10) według bibliotekarzy lub czytelników."
    )

    def __str__(self):
        return self.name


class Author(models.Model):
    """Model reprezentujący autora książki."""
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    country = models.CharField(max_length=2, help_text="Kod kraju, np. PL, US, GB")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    """Model reprezentujący książkę w bibliotece."""
    title = models.CharField(max_length=100)
    publication_month = models.IntegerField(choices=MONTHS.choices, default=MONTHS.Styczeń)
    book_format = models.CharField(max_length=1, choices=BOOK_FORMATS, default='P')
    author = models.ForeignKey(Author, null=True, blank=True, on_delete=models.SET_NULL)
    genre = models.ForeignKey(Genre, null=True, blank=True, on_delete=models.SET_NULL)
    available_copies = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title

# Nie trzeba dodawać null = False i blank = False, bo są one domyślne
class Osoba(models.Model):
    #PLEC = ( 
    #    ('K', 'kobieta'),
    #    ('M', 'mężczyzna'),
    #    ('I', 'inna')
    #) - poprzednia wersja
    imie = models.CharField(max_length = 50, null = False, blank = False)
    nazwisko = models.CharField(max_length = 100, null = False, blank = False)
    #plec = models.CharField(max_length = 1, choices = PLEC, default = 'I') - poprzednia wersja
    plec = models.IntegerField(choices=Plec.choices, default = 3)
    # można to jeszcze zrobić jako IntegerField(choices=PLCIE.choices, default = PLCIE.choices[0][2])
    stanowisko = models.ForeignKey('Stanowisko', on_delete = models.CASCADE)
    data_dodania = models.DateTimeField(auto_now_add = True, editable = False)
# Gdy definiowana klasa byłaby przed tą klasą to możemy zapisać ją bez '', ale trzeba uważać żeby dobrze zapisać nazwę :P

class Stanowisko(models.Model):
    nazwa = models.CharField(max_length = 70, null = False, blank = False)
    opis = models.TextField(null = True, blank = True)