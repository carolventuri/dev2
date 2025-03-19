from django.core.validators import MinValueValidator, MaxValueValidator
from .base_model import BaseModel
from django.db import models


class Usuario(BaseModel):
    name = models.CharField(
        max_length=100, null=False, blank=False,
        help_text="Nome do usuário.",
        verbose_name="Nome:",
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        ordering = ("name",)

