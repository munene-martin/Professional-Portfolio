from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    github_url = models.URLField(max_length=500)
    # Since we aren't using images yet, we can leave this out or make it optional
    technologies = models.CharField(max_length=500, help_text="Separate with commas")

    def __str__(self):
        return self.title

    @property
    def technologies_list(self):
        """Helper to turn the string into a list for our template"""
        return [t.strip() for t in self.technologies.split(',')]