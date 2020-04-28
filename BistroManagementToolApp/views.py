from BistroManagementToolApp.models import *
from BistroManagementToolApp.forms import *

from datetime import date
from django.shortcuts import render
from django.shortcuts import redirect

from django.http.response import JsonResponse
from django.http.response import HttpResponse
from django.http.response import HttpResponseRedirect

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

# Widoki powiązane z poszczególnymi template'ami

# Widok odpowiedzalny za obsługę panelu administratora

@login_required
def panel_administratora(request):
    my_dict = {}
    return render(request, 'BistroManagementToolApp/panel_administratora.html',context=my_dict)

# Widok odpowiedzialny za obsługę panelu rejestracji

@login_required
def panel_zarzadzania_zespolem(request):

    forms = [UserForm(),ApplicationUserForm()]
    application_users = ApplicationUser.objects.order_by('-user__date_joined').all()
    my_dict = {'forms':forms,'application_users':application_users}

    return render(request, 'BistroManagementToolApp/panel_zarzadzania_zespolem.html', context=my_dict)

# Widok odpowiedzielany za wylogowanie urzytkownika

@login_required
def logout_user(request):
    logout(request)
    return redirect('/bistro/panel_logowania')

# Strona wyświetlana użytkownikom, którzy nie są zalogowani

def login_required_page(request):
    return render(request, 'BistroManagementToolApp/login_required_page.html')

# Strona wyświetlana użytkownikom, którzy podali błędne dane logowania

def wrong_credentials_page(request):
    return render(request, 'BistroManagementToolApp/wrong_credentials_page.html')

# Widok odpowiedzialny za obsługę panelu logowania

def panel_logowania(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return redirect('/bistro/panel_sprzedawcy')
            else:
                return HttpResponse('Account not active')
        else:
            return redirect('/bistro/wrong_credentials_page')
    else:
        application_users = ApplicationUser.objects.all()
        my_dict = {'application_users':application_users}
        return render(request, 'BistroManagementToolApp/panel_logowania.html', context=my_dict)

# Widok odpowiedzialny za obsługę panelu sprzedawcy

@login_required
def panel_sprzedawcy(request):

    my_dict = {}
    return render(request, 'BistroManagementToolApp/panel_sprzedawcy.html', context=my_dict)

# Widok opowiedzialny za obłsuge panelu transakcji

@login_required
def panel_transakcji(request):

    product_groups = ProductGroup.objects.all()
    product_items = Product.objects.all()

    my_dict = {'product_groups':product_groups,'product_items':product_items}
    return render(request, 'BistroManagementToolApp/panel_transakcji.html', context=my_dict)

# Widok odpowiedzialny za obsługę panelu magazynu

@login_required
def panel_magazynu(request):

        ingredients = Ingredient.objects.order_by('-date_created').all()
        ingredient_form = IngredientForm()
        my_dict = {'ingredients': ingredients, 'ingredient_form': ingredient_form}
        return render(request, 'BistroManagementToolApp/panel_magazynu.html', context=my_dict)

# Widoki obsługujące zapytania AJAX-owe

# Utworzenie nowego pracownika

@login_required
def create_user(request):

    if request.method == "POST":
        user_form = UserForm(request.POST)
        user_application_form = ApplicationUserForm(request.POST)

        if user_form.is_valid() and user_application_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            application_user = user_application_form.save(commit=False)
            application_user.user = user
            if 'picture' in request.FILES:
                application_user.picture = request.FILES['picture']

            application_user.save()

            return redirect('/bistro/panel_zarzadzania_zespolem')

        else:
            forms = [user_form, user_application_form]
            application_users = ApplicationUser.objects.order_by('-user__date_joined').all()
            my_dict = {'show_add_user_window': True, 'forms': forms, 'application_users': application_users}
            return render(request, 'BistroManagementToolApp/panel_zarzadzania_zespolem.html', context=my_dict)

# Skasuj istniejącego pracownika

@login_required
def delete_user(request):

    ApplicationUser.objects.get(user = User.objects.get(id=request.GET.get('user_id'))).delete()
    User.objects.get(id=request.GET.get('user_id')).delete()

    data = {
        'status':'User deleted!'
    }
    return JsonResponse(data)


# Wyedytuj wskazanego pracownika

@login_required
def edit_user(request):
   return JsonResponse({'Status':'Ok'})

# Utworzenie nowego składnika

@login_required
def create_ingredient(request):
    if request.method == "POST":
        ingredient_form = IngredientForm(request.POST)
    else:
        ingredient_form = IngredientForm()

    return save_ingredient(request,ingredient_form)

# Update istniejącego składnika

@login_required
def update_ingredient(request):
    ingredient_form = Ingredient.objects.get(ext_id=request.GET.get('ingredient_ext_id'))
    if request.method == "POST":
        ingredient_form = IngredientForm(request.POST,instance=ingredient_form)
    else:
        ingredient_form = IngredientForm(instance=ingredient_form)

    return save_ingredient(request,ingredient_form)

# Zapisz nowy składnik

@login_required
def save_ingredient(request,ingredient_form):

    if ingredient_form.is_valid():
            new_ingredient = ingredient_form.save(commit=False)
            new_ingredient.ext_id = "S"+str(len(Ingredient.objects.all())+1)
            new_ingredient.date_created = date.today()
            new_ingredient.status = True
            new_ingredient.brutto_price_per_unit = ingredient_form.cleaned_data['brutto_price_per_package'] / ingredient_form.cleaned_data['grammature_per_package']
            new_ingredient.amount_in_storage = 0
            new_ingredient.netto_price_per_package = ingredient_form.cleaned_data['brutto_price_per_package'] / (1 + (ingredient_form.cleaned_data['vat_rate']))
            new_ingredient.netto_price_per_unit = new_ingredient.netto_price_per_package / ingredient_form.cleaned_data['grammature_per_package']
            new_ingredient.save()

            ingredient_form = IngredientForm()
            ingredients = Ingredient.objects.order_by('-date_created').all()
            my_dict = {'show_add_ingredient_window':True, 'ingredients': ingredients,'ingredient_form': ingredient_form}
            return render(request, 'BistroManagementToolApp/panel_magazynu.html', context=my_dict)
    else:
        ingredient_form = IngredientForm()
        ingredients = Ingredient.objects.order_by('-date_created').all()
        my_dict = {'show_add_ingredient_window': True, 'ingredients': ingredients, 'ingredient_form': ingredient_form}
        return render(request, 'BistroManagementToolApp/panel_magazynu.html', context=my_dict)


# Zmiana zawartości listy z podkategoriami składników

@login_required
def change_ing_category(request):
    selected_category = IngredientCategory.objects.filter(name=request.GET.get('selected_category',None))[:1].get()
    data = {
        'corresponding_subcategories':list(IngredientSubcategory.objects.filter(category=selected_category).values()),
        'corresponding_aisle':list(IngredientAisle.objects.filter(subcategory=IngredientSubcategory.objects.filter(category=selected_category)[:1].get()).values())
    }
    return JsonResponse(data)

# Zmiana zawartości listy z segmentami składników

@login_required
def change_ing_subcategory(request):
    selected_subcategory = IngredientSubcategory.objects.filter(name=request.GET.get('selected_subcategory', None))[:1].get()
    data = {
        'corresponding_aisle': list(IngredientAisle.objects.filter(subcategory=selected_subcategory).values())
    }
    return JsonResponse(data)

@login_required
def delete_ingredient(request):

    Ingredient.objects.get(ext_id=request.GET.get('ingredient_ext_id')).delete()
    data = {
        'status':'Ingredient deleted!'
    }
    return JsonResponse(data)