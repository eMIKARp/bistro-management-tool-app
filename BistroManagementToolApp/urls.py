from django.urls import path
from django.conf.urls import url
from BistroManagementToolApp import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'BistroManagementToolApp'

urlpatterns = [

    url(r'^panel_logowania',views.panel_logowania,name='panel_logowania'),
    url(r'^login_required_page',views.login_required_page,name='login_required_page'),
    url(r'^brak_uprawnien',views.brak_uprawnien,name='brak_uprawnien'),
    url(r'^wrong_credentials_page',views.wrong_credentials_page,name='wrong_credentials_page'),
    url(r'^panel_zarzadzania_zespolem',views.panel_zarzadzania_zespolem,name='panel_zarzadzania_zespolem'),
    url(r'^panel_sprzedawcy',views.panel_sprzedawcy,name='panel_sprzedawcy'),
    url(r'^panel_administratora',views.panel_administratora,name='panel_administratora'),
    url(r'^panel_transakcji',views.panel_transakcji,name='panel_transakcji'),
    url(r'^panel_magazynu',views.panel_magazynu,name='panel_magazynu'),
    url(r'^ajax/change_ing_category',views.change_ing_category,name='change_ing_category'),
    url(r'^ajax/change_ing_subcategory',views.change_ing_subcategory,name='change_ing_subcategory'),
    url(r'^ajax/delete_ingredient',views.delete_ingredient,name="delete_ingredient"),
    url(r'^ajax/create_ingredient',views.create_ingredient,name="create_ingredient"),
    url(r'^ajax/update_ingredient',views.update_ingredient,name="update_ingredient"),
    url(r'^ajax/create_user',views.create_user,name="create_user"),
    url(r'^ajax/delete_user',views.delete_user,name="delete_user"),
    url(r'^ajax/edit_user',views.edit_user,name="edit_user"),
    url(r'^logout_user',views.logout_user,name="logout_user"),
    url(r'^test',views.test_env,name="test_env")


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)