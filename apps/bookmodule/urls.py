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
    # Lab 10 - Part 1
    path('lab9_part1/listbooks', views.listbooks_part1, name='listbooks_part1'),
    path('lab9_part1/addbook', views.addbook_part1, name='addbook_part1'),
    path('lab9_part1/editbook/<int:id>', views.editbook_part1, name='editbook_part1'),
    path('lab9_part1/deletebook/<int:id>', views.deletebook_part1, name='deletebook_part1'),
    # Lab 10 - Part 2 (Django Forms)
    path('lab9_part2/listbooks', views.listbooks_part2, name='listbooks_part2'),
    path('lab9_part2/addbook', views.addbook_part2, name='addbook_part2'),
    path('lab9_part2/editbook/<int:id>', views.editbook_part2, name='editbook_part2'),
    path('lab9_part2/deletebook/<int:id>', views.deletebook_part2, name='deletebook_part2'),
]