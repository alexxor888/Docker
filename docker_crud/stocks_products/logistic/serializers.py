from rest_framework import serializers

from .models import StockProduct, Product, Stock


class ProductSerializer(serializers.ModelSerializer):
    # настройте сериализатор для продукта
    class Meta():
        model = Product
        fields = ['id', 'title', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):
    # настройте сериализатор для позиции продукта на складе
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']



class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    # настройте сериализатор для склада
    class Meta():
        model = Stock
        fields = ['address', 'positions']

    def create(self, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # создаем склад по его параметрам
        stock = super().create(validated_data)

        # здесь вам надо заполнить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions
        [StockProduct.objects.create(stock=stock, **position) for position in positions]

        return stock

    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)

        # здесь вам надо обновить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions
        [StockProduct.objects.update_or_create(product=pos.pop('product'), stock=stock, defaults=pos) for
         pos in positions]

        return stock
