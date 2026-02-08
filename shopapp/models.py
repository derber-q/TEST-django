from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Product(models.Model):
    class Unit(models.TextChoices):
        LITER = "L", "Литры"
        KILOGRAM = "KG", "Килограммы"
        PIECE = "PCS", "Штуки"

    # Основное изображение товара для списков и карточки.
    preview = models.ImageField(upload_to="products/previews/", verbose_name="Превью")
    # Название товара для отображения пользователю.
    name = models.CharField(max_length=255, verbose_name="Имя")
    # Базовая цена товара без учёта скидки.
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    # Подробное текстовое описание товара.
    description = models.TextField(blank=True, verbose_name="Описание")
    # Остаток товара на складе (допускаются дробные значения).
    quantity_remaining = models.DecimalField(
        max_digits=10,
        decimal_places=3,
        verbose_name="Сколько продукта осталось",
    )
    # Единица измерения остатка: литры, килограммы или штуки.
    quantity_unit = models.CharField(
        max_length=3,
        choices=Unit.choices,
        default=Unit.PIECE,
        verbose_name="Единица измерения",
    )
    # Текущая активная скидка в процентах (0-100), может отсутствовать.
    active_discount = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Текущая скидка в процентах",
        verbose_name="Действующая скидка",
    )
    # Признак архивного товара (не показывать как активный).
    is_archived = models.BooleanField(default=False, verbose_name="Заархивирован")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name


class ProductAdditionalPhoto(models.Model):
    # Связь дополнительного фото с конкретным товаром.
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="additional_photos",
        verbose_name="Продукт",
    )
    # Файл дополнительного изображения товара.
    image = models.ImageField(upload_to="products/additional/", verbose_name="Дополнительное фото")

    class Meta:
        verbose_name = "Дополнительное фото продукта"
        verbose_name_plural = "Дополнительные фото продуктов"

    def __str__(self):
        return f"Фото для {self.product.name}"
