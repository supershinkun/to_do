from django.conf.urls import url
from django.urls import path
from kanban import views

app_name = 'kanban'

urlpatterns = [
    path('', views.TopPage.as_view(), name='top'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('signup/', views.SignUp.as_view(), name='signup'),

    path("users/<int:pk>/", views.UserDetailView.as_view(), name="users_detail"),
    path("users/<int:pk>/update/", views.UserUpdateView.as_view(), name="users_update"),

    path("lists/", views.ListListView.as_view(), name="lists_list"),
    path("lists/<int:pk>/", views.ListDetailView.as_view(), name="lists_detail"),
    path("lists/create/", views.ListCreateView.as_view(), name="lists_create"),
    path("lists/<int:pk>/update/", views.ListUpdateView.as_view(), name="lists_update"),
    path("lists/<int:pk>/delete/", views.ListDeleteView.as_view(), name="lists_delete"),

    path("cards/create/", views.CardCreateView.as_view(), name="cards_create"),
    path("cards/create/<int:list_pk>", views.CardCreateFromHomeView.as_view(), name="cards_create_from_home"),
    path("cards/", views.CardListView.as_view(), name="cards_list"),
    path("cards/<int:pk>/", views.CardDetailView.as_view(), name="cards_detail"),
    path("cards/<int:pk>/update/", views.CardUpdateView.as_view(), name="cards_update"),
    path("cards/<int:pk>/delete/", views.CardDeleteView.as_view(), name="cards_delete"),
]
