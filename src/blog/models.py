
from datetime import date
from django.db.models import (
    CharField,
    DateField,
    ManyToManyField,
    Model,
    SlugField,
    TextField
)
from src.organizer.models import Startup,Tag
# Create your models here.

class Post(models.Model):
    title       = models.CharField(max_length=63)
    slug        = models.SlugField(max_length=66, helf_text="A label for URL config",unique_for_month="pub_date")
    text        = models.TextField()
    pub_date    = models.DateField("date publihed", default=date.today)
    tags        = models.ManyToManyField(Tag,related_date="blog_posts")
    startups    = models.ManyToManyField(Startup,related_name="blog_posts")

    class Meta:
        get_latest_by='pub_date'
        ordering =["pub_date","title"]
        verbose_name ="blog post"

    def __str__(self):
        date_string =self.pub_date.strftime("%Y-%m-%d")
        return f"{self.title} on {date_string}"