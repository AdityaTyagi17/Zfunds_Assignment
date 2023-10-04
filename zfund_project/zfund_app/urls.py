from django.urls import path
from . import views

urlpatterns = [
    path('advisor/signup', views.advisor_signup,name="AdvisorSignup"),
    path('advisor/add-client', views.add_client,name="AddClient"),
    path('advisor/list-clients/<int:advisor_id>/', views.list_clients, name='list-clients'),
    path('user/signup', views.user_signup,name="UserSignup"),
    path('add-product/', views.add_product, name='add_product'),
    path('advisor/purchase-product/<int:advisor_id>/<int:user_id>/', views.purchase_product, name='purchase-product')
]

