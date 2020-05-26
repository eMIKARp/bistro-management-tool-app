
from django import forms
from django.contrib.auth.models import User
from BistroManagementToolApp.models import *

class TransactionForm(forms.ModelForm):
    class Meta():
        model = Transaction
        fields = '__all__'

class ProductsInTransactionForm(forms.ModelForm):
    class Meta():
        model = ProductsInTransaction
        fields = '__all__'

class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())


    class Meta():
        model = User
        fields = ('username','first_name','last_name','email','password')
        labels = {
            'username':'Nazwa użytkownika',
            'first_name':'Imię',
            'last_name':'Nazwisko',
            'email':'Adres email',
            'password':'Hasło'
        }

class ApplicationUserForm(forms.ModelForm):
    class Meta():
        model = ApplicationUser
        fields = ('picture',)

        labels = {
            'picture':'Zdjęcie pracownika',
            'salary':'Wynagrodzenie'
         }

class IngredientForm(forms.ModelForm):

    init_cat = IngredientCategory.objects.all()[:1].get()
    init_subcat = IngredientSubcategory.objects.all().filter(category=init_cat)[:1].get()

    category = forms.ModelChoiceField(initial=0,queryset=IngredientCategory.objects.all(),widget=forms.Select(attrs={'style': 'height:100%'}))
    subcategory = forms.ModelChoiceField(initial=0,queryset=IngredientSubcategory.objects.filter(category=init_cat),widget=forms.Select(attrs={'style': 'height:100%'}))
    aisle = forms.ModelChoiceField(initial=0,queryset=IngredientAisle.objects.filter(subcategory=init_subcat),widget=forms.Select(attrs={'style': 'height:100%'}))

    class Meta():
        model = Ingredient
        exclude = ['ext_id','date_created','status','netto_price_per_unit','netto_price_per_package','brutto_price_per_unit','amount_in_storage']

        UNITS = [("g", "g"), ("dag", "dag"), ("kg", "kg"), ("ml", "ml"), ("l", "l"), ("szt", "szt")]
        VAT_RATE = [('0.23', '23%'), ('0.08', '8%'), ('0.05', '5%')]

        widgets = {

            'unit':forms.Select(choices=UNITS, attrs={'style':'width:100%','style':'height:100%'}),
            'grammature_per_package':forms.NumberInput(attrs={'style':'width:100%'}),
            'vat_rate':forms.Select(choices=VAT_RATE,attrs={'style':'width:100%','style':'height:100%'}),
            'brutto_price_per_package':forms.NumberInput(attrs={'style':'width:100%'})
        }

        labels = {
            'category':'Kategoria',
            'subcategory':'Podkategoria',
            'aisle':'Segment',
            'name':'Produkt',
            'unit':'Jednostka',
            'grammature_per_package':'Ilość',
            'vat_rate':'Stawka VAT',
            'brutto_price_per_package':'Cena brutto'
         }

