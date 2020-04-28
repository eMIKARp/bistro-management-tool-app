from django.utils.timezone import now
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','BistroManagementTool.settings')

import django
django.setup()

from BistroManagementToolApp.models import *
import csv


def add_ingredient_category(cat_name):
    ing_category = IngredientCategory.objects.get_or_create(name=cat_name)[0]
    ing_category.date_created = now()
    ing_category.save()
    return ing_category

def add_ingredient_subcategory(subcat_name,cat_name):
    ing_subcategory = IngredientSubcategory.objects.get_or_create(name=subcat_name,category=add_ingredient_category(cat_name))[0]
    ing_subcategory.date_created = now()
    ing_subcategory.save()
    return ing_subcategory

def add_ingredient_aisle(aisle_name, subcat_name, cat_name):
    ing_aisle = IngredientAisle.objects.get_or_create(name=aisle_name,subcategory=add_ingredient_subcategory(subcat_name,cat_name),category=add_ingredient_category(cat_name))[0]
    ing_aisle.date_created = now()
    ing_aisle.save()
    return ing_aisle

def populate_magazyn():
    with open("magazyn.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            ingredient = Ingredient(
                ext_id = row[0],
                date_created = now(),
                status= True,
                category = add_ingredient_category(row[1]),
                subcategory = add_ingredient_subcategory(row[2],row[1]),
                aisle = add_ingredient_aisle(row[3],row[2],row[1]),
                name = row[4],
                unit = row[5],
                grammature_per_package = row[6],
                netto_price_per_package = row[7],
                netto_price_per_unit = float(row[7]) / float(row[6]),
                vat_rate = row[8],
                brutto_price_per_package = row[9],
                brutto_price_per_unit = float(row[9]) / float(row[6]),
                amount_in_storage= 0
            )
            ingredient.save()
            print("Done!")
        print("All done!")

def add_product_type(pro_type):
    pro_type = ProductType.objects.get_or_create(name=pro_type)[0]
    pro_type.date_created = now()
    pro_type.save()

    return pro_type

def add_product_group(group,type):
    pro_group = ProductGroup.objects.get_or_create(name=group,type=add_product_type(type))[0]
    pro_group.date_created = now()
    pro_group.save()

    return pro_group


def populate_menu():
    with open('menu.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            product = Product(
                ext_id = row[0],
                status = True if row[1]=='Active' else False,
                date_created=now(),
                type=add_product_type(row[2]),
                group=add_product_group(row[3],row[2]),
                vat_rate=row[8],
                name=row[4],
                monthly_potential=row[5],
                share_in_sales=row[6],
                brutto_price=row[7],
                netto_price=row[9],
                unit_cost=row[10],
                food_cost=row[11],
                unit_margin=row[12],
                product_margin=row[13],
                total_income=row[14],
                total_cost=row[17],
                total_profit=row[18],
                vat_paid=row[15],
                vat_due=row[16]
            )
            product.save()
            print('Done!')
        print("All done!")


def populate_ingredients_in_products():
    with open('product_ingredient.csv') as csv_file:
        csv_reader = csv.reader(csv_file,delimiter=',')
        for row in csv_reader:
            ingredient_in_product = IngredientsInProduct(
                product=Product.objects.get(ext_id=row[0]),
                ingredient=Ingredient.objects.get(ext_id=row[1]),
                grammature=row[2])
            ingredient_in_product.save()
            print("Done!")
        print("All done!")

populate_magazyn()
populate_menu()
populate_ingredients_in_products()
