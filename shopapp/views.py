from decimal import Decimal

from django.shortcuts import render

from .models import Product


def calculate_discounted_price(price: Decimal, discount_percent: Decimal | None) -> Decimal | None:
    """Рассчитывает итоговую цену товара с учетом скидки в процентах."""
    # Если скидка не задана или равна нулю, итоговую цену не вычисляем.
    if not discount_percent:
        return None

    # Преобразуем процент скидки в коэффициент уменьшения цены.
    discount_multiplier = Decimal("1") - (discount_percent / Decimal("100"))
    # Возвращаем цену после применения скидки, округленную до 2 знаков после запятой.
    return (price * discount_multiplier).quantize(Decimal("0.01"))


def index(request):
    """Отображает главную страницу магазина со списком товаров из базы данных."""
    # Получаем все неархивные товары для отображения в каталоге на главной странице.
    products = Product.objects.filter(is_archived=False)

    # Готовим данные товара для удобного вывода в шаблоне.
    products_for_template = []
    for product in products:
        # Рассчитываем итоговую цену, если у товара есть скидка.
        discounted_price = calculate_discounted_price(product.price, product.active_discount)

        # Добавляем словарь с данными, которые будут использованы в карточке товара.
        products_for_template.append(
            {
                "product": product,
                "has_discount": discounted_price is not None,
                "discounted_price": discounted_price,
            }
        )

    # Передаем подготовленные данные в django template главной страницы.
    return render(
        request,
        "shopapp/index.html",
        {
            "products_for_template": products_for_template,
        },
    )
