from django.db import models
from colour import Color
from colorfield.fields import ColorField


class Letter(models.Model):
    name = models.CharField(max_length=255)
    message = models.TextField(max_length=250)
    letter_date = models.DateField(auto_now_add=True)
    color = ColorField(default="#FFF")

    @property
    def text_color(self):
        color = Color(self.color)
        if color.luminance > 0.5:
            text_color = "black"
        else:
            text_color = "white"

        return Color(text_color).get_hex()

    def __str__(self):
        return f"{self.name}"
