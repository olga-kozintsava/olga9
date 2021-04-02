from django.urls import path
from my_test_app import views
from my_test_app.views import NameListView

urlpatterns = [
    path('', views.input_name, name='input'),
    path('names', NameListView.as_view(),  name='names'),
      ]