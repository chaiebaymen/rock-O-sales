from rest_framework import serializers

from api.models import *


class UserSerializer(serializers.ModelSerializer):
    transactions = serializers.PrimaryKeyRelatedField(many=True, queryset=Transaction.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'transactions')


class ProductSerializer(serializers.ModelSerializer):
    sales_person = serializers.Field(source='sales_person.username')

    class Meta:
        model = Product
        fields = ('prod_id', 'display_name', 'cost', 'brand', 'sales_person')


class CustomerSerializer(serializers.ModelSerializer):
    sales_person = serializers.Field(source='sales_person.username')

    class Meta:
        model = Customer
        fields = ('cust_id', 'cust_name', 'email', 'contact', 'address', 'sales_person')


class TransactionSerializer(serializers.ModelSerializer):
    product = serializers.Field(source='product.display_name')
    sales_person = serializers.Field(source='sales_person.username')
    customer = serializers.Field(source='customer.cust_name')
    class Meta:
        model = Transaction
        fields = ('trans_id', 'customer', 'product', 'sales_person', 'cost', 'transaction_time')
