from django.db import models
from django.core import validators
from decimal import Decimal
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class ProductType(models.Model):
    date_created = models.DateTimeField(null=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ProductGroup(models.Model):
    date_created = models.DateTimeField(null=True)
    name = models.CharField(max_length=255)
    type = models.ForeignKey(ProductType,on_delete=models.CASCADE,related_name='groups')

    def __str__(self):
        return self.name


class IngredientCategory(models.Model):
    date_created = models.DateTimeField(null=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class IngredientSubcategory(models.Model):
    date_created = models.DateTimeField(null=True)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(IngredientCategory,on_delete=models.CASCADE,related_name='subcategories')

    def __str__(self):
        return self.name

class IngredientAisle(models.Model):
    date_created = models.DateTimeField(null=True)
    name = models.CharField(max_length=255)
    subcategory = models.ForeignKey(IngredientSubcategory,on_delete=models.CASCADE,related_name='aisles')
    category = models.ForeignKey(IngredientCategory, on_delete=models.CASCADE, related_name='aisles')

    def __str__(self):
        return self.name


class Ingredient(models.Model):

    ext_id = models.CharField(max_length=10, unique=True)
    date_created = models.DateTimeField(null=True)
    status = models.BooleanField(default=True)
    category = models.ForeignKey(IngredientCategory,on_delete=models.CASCADE,related_name='ingredients')
    subcategory = models.ForeignKey(IngredientSubcategory,on_delete=models.CASCADE,related_name='ingredients')
    aisle = models.ForeignKey(IngredientAisle,on_delete=models.CASCADE,related_name='ingredients')
    name = models.CharField(max_length=255)
    unit = models.CharField(max_length=10)
    grammature_per_package = models.DecimalField (max_digits=10,decimal_places=3,validators=[validators.MinValueValidator(Decimal('0.00001'))])
    netto_price_per_package = models.DecimalField (max_digits=10,decimal_places=2)
    netto_price_per_unit = models.DecimalField (max_digits=10,decimal_places=6)
    vat_rate = models.DecimalField (max_digits=10,decimal_places=2)
    brutto_price_per_package = models.DecimalField (max_digits=10,decimal_places=2,validators=[validators.MinValueValidator(Decimal('0.00001'))])
    brutto_price_per_unit = models.DecimalField (max_digits=10,decimal_places=6)
    amount_in_storage = models.DecimalField (max_digits=10,decimal_places=3)

    def __str__(self):
        return self.name

class Product(models.Model):

    ext_id = models.CharField(max_length=10,unique=True)
    date_created = models.DateTimeField(null=True)
    status = models.BooleanField(default=True)
    type = models.ForeignKey(ProductType,on_delete=models.CASCADE,related_name='products')
    group = models.ForeignKey(ProductGroup,on_delete=models.CASCADE,related_name='products')
    vat_rate = models.DecimalField(max_digits=10,decimal_places=2)
    name = models.CharField(max_length=255)
    ingredients = models.ManyToManyField(Ingredient,related_name='products',through='IngredientsInProduct')
    monthly_potential = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    share_in_sales = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    brutto_price = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    netto_price = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    unit_cost = models.DecimalField(max_digits=10,decimal_places=6,default=0.00)
    food_cost = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    unit_margin = models.DecimalField(max_digits=10,decimal_places=6,default=0.00)
    product_margin = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    total_income = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    total_cost = models.DecimalField(max_digits=10,decimal_places=6,default=0.00)
    total_profit = models.DecimalField(max_digits=10,decimal_places=6,default=0.00)
    vat_paid = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    vat_due = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)

    def __str__(self):
        return self.name


class IngredientsInProduct(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient,on_delete=models.CASCADE)
    grammature = models.DecimalField(max_digits=10,decimal_places=6)

    def __str__(self):
        return 'Gramature of: '+ self.ingredient.name + ' in product: ' + self.product.name + ' is: ' + str(self.grammature)


class WorkScheadule(models.Model):
    pass

class ApplicationUser (models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='additional_fields')
    picture = models.ImageField(upload_to='profile_pics',blank=True)
    salary = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    work_scheadule = models.OneToOneField(WorkScheadule,blank=True,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.username


class Transaction(models.Model):

    PAYMENT_TYPE = [('CASH','CASH'),('CARD','CARD')]

    date_created = models.DateTimeField(null=True,default=datetime.now)
    sales_person = models.ForeignKey(ApplicationUser, on_delete=models.SET_NULL, related_name='transactions', null=True,blank=True)
    payment_type = models.CharField(max_length=4,choices=PAYMENT_TYPE,default='CASH')
    products_in_transaction = models.ManyToManyField(Product,through='ProductsInTransaction',null=True,blank=True)
    number_of_products_in_transaction = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    netto_transaction_value = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    vat_due_in_transaction = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    brutto_transaction_value = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)

    def __str__(self):
        return "Transaction: " + str(self.date_created) + " amount: " + str(self.brutto_transaction_value)


class ProductsInTransaction(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name='product_in_transaction',null=True,blank=True)
    transaction = models.ForeignKey(Transaction,on_delete=models.CASCADE, related_name='transaction',null=True,blank=True)
    quantity = models.DecimalField(max_digits=10,decimal_places=2,default=0.00,null=True,blank=True)

    def __str__(self):
        return 'Transaction: ' +str(self.product.date_created)+ ' - Product: '+ str(self.product) + ' - Quantity: ' + str(self.quantity)