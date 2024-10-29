from django.urls import path
from .import views

urlpatterns = [
   path('',views.home,name='home'),
   path('add_product/',views.add_product,name='add_product'),
   path('show_products/',views.show_products,name='show_products'),
    path('editpage/<int:pk>/',views.editpage,name='editpage'),
    path('deletepage/<int:pk>/',views.deletepage,name='deletepage'),
    path('products/<int:pk>/',views.edit_products,name='edit_products'),
]
