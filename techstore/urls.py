from . import views
from django.urls import path

app_name = 'techstore'
urlpatterns = [
    #root store/
    path('', views.index, name="index"),
    path('<int:item_id>', views.detail, name="detail"),
    path('checkout.html/', views.checkout, name="checkout" ),
    path('laptops.html/', views.laptops, name="laptops"),
    path('laptops.html/<int:laptops_id>', views.detaillp, name="detaillp"),
    path('desktop.html/', views.desktops, name="desktops"),
    path('desktop.html/<int:desktops_id>', views.detaildt, name="detaildt"),
    path('cart.html/', views.cart_view, name ="cart")

]