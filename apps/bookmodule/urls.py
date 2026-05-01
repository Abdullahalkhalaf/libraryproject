from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="books.index"),
    path('list_books/', views.list_books, name="books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('html5/links/', views.links_page, name='books.links'),
    path('html5/text/formatting/', views.formatting_page, name='books.formatting'),
    path('html5/listing/', views.listing_page, name='books.listing'),
    path('html5/tables/', views.tables_page, name='books.tables'),
    # Lab 5 Completed successfully
    path('search/', views.search_page, name='books.search'),
    path('simple/query/', views.simple_query),
    path('complex/query/', views.complex_query),
    path('lab8/task1', views.task1),
    path('lab8/task2', views.task2),
    path('lab8/task3', views.task3),
    path('lab8/task4', views.task4),
    path('lab8/task5', views.task5),
    path('lab8/task7', views.task7),
    path('lab9/task1', views.task1),
    path('lab9/task2', views.task2),
    path('lab9/task3', views.task3),
    path('lab9/task4', views.task4),
    path('lab9/task5', views.task5),
    path('lab9/task6', views.task6),
]