# [django-toggle-m2m](https://pypi.org/project/django-toggle-m2m/)

## Installation

```bash
pip install django_toggle_m2m
```

## Usage in models

```python
from django.db import models

from django_toggle_m2m.toggle import ToggleManyToMany


class Publication(models.Model):
    title = models.CharField(max_length=32)


class Article(models.Model, ToggleManyToMany):
    # ______________________^
    # Extend ToggleManyToMany class
    headline = models.CharField(max_length=256)
    publications = models.ManyToManyField(Publication)

    # Define M2M fields that are toggleable
    TOGGLEABLE_FIELDS = ('publications',)
```

## Relation toggling
```python
article = Article.objects.create(...)
publication = Publication.objects.create(...)

article.toggle_publications(instance=publication) # Will be added
article.toggle_publications(instance=publication) # Will be removed
```

## Development

```bash
git clone https://github.com/wencakisa/django-toggle-m2m.git
pip install django_toggle_m2m
```

---

*Interesting fact* - https://code.djangoproject.com/ticket/20686
