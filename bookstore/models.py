from django.db import models
from django.urls import reverse


class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)
    bio = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)    
    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('author_detail', kwargs={'pk': self.pk})
        
    @property
    def book_count(self):
        return self.books.count()

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books',  # This enables author.books.all()
    )
    description = models.TextField(
        blank=True,
        null=True,
        help_text="Detailed description of the book"
    )
    published_date = models.DateField(null=True, blank=True)
    added_to_website = models.DateField(null=True, blank=True)
    isbn = models.CharField(max_length=13, unique=True, blank=True, null=True)
    page_count = models.IntegerField(null=True, blank=True)
    language = models.CharField(max_length=20, default='English')
    cover_image = models.ImageField(
        null=True,
        blank=True,
        help_text="Upload book cover image"
    )

    AGE_GROUP_CHOICES = [
        ('under_8', 'Under 8'),
        ('8_15', '8-15'),
        ('adults', 'Adults'),
    ]
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    age_group = models.CharField(
        max_length=10,
        choices=AGE_GROUP_CHOICES,
        default='adults'
    )
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'pk': self.pk})



