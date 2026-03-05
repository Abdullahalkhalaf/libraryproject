from django.shortcuts import render

# دالة الصفحة الرئيسية
def index(request):
    return render(request, "bookmodule/index.html") 

# دالة قائمة الكتب
def list_books(request):
    return render(request, 'bookmodule/list_books.html') 

# دالة تفاصيل كتاب واحد
def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html') 

# دالة عن المكتبة
def aboutus(request):
    return render(request, 'bookmodule/aboutus.html') 