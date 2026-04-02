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

def links_page(request):
    return render(request, 'bookmodule/links.html')

def formatting_page(request):
    return render(request, 'bookmodule/formatting.html')

def listing_page(request):
    return render(request, 'bookmodule/listing.html')

def tables_page(request):
    return render(request, 'bookmodule/tables.html')