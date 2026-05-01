from django.shortcuts import render
from django.db.models import Q, Count, Sum, Avg, Max, Min
from .models import Book
from .models import Book, Publisher, Author

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

def getBooksList():
    book1 = {'id': 12344321, 'title': 'Continuous Delivery', 'author': 'J.Humble and D. Farley'}
    book2 = {'id': 56788765, 'title': 'Reversing: Secrets of Reverse Engineering', 'author': 'E. Eilam'}
    book3 = {'id': 43211234, 'title': 'The Hundred-Page Machine Learning Book', 'author': 'Andriy Burkov'}
    return [book1, book2, book3]

def search_page(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        
        # فلترة الكتب
        books = getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower(): 
                contained = True
            if not contained and isAuthor and string in item['author'].lower(): 
                contained = True
            
            if contained: 
                newBooks.append(item)
                
        return render(request, 'bookmodule/bookList.html', {'books': newBooks})
    
    # إذا كان الطلب عادي (GET) يعرض صفحة البحث
    return render(request, 'bookmodule/search.html')

from .models import Book

def simple_query(request):
    mybooks = Book.objects.filter(title__icontains='and')
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})

def complex_query(request):
    mybooks = Book.objects.filter(author__isnull=False).filter(title__icontains='and').filter(edition__gte=2).exclude(price__lte=100)[:10]
    if len(mybooks) >= 1:
        return render(request, 'bookmodule/bookList.html', {'books': mybooks})
    else:
        return render(request, 'bookmodule/index.html')
    
    #Lab 8 Tasks 

# Task 1: الكتب اللي سعرها 80 أو أقل
def task1(request):
    books = Book.objects.filter(Q(price__lte=80))
    return render(request, 'bookmodule/bookList.html', {'books': books})

# Task 2: الكتب اللي إصدارها أعلى من 3، واسمها أو مؤلفها فيه حرفين 'qu'
def task2(request):
    books = Book.objects.filter(Q(edition__gt=3) & (Q(title__icontains='qu') | Q(author__icontains='qu')))
    return render(request, 'bookmodule/bookList.html', {'books': books})

# Task 3: عكس Task 2 (إصدارها 3 أو أقل، ولا فيها 'qu')
def task3(request):
    books = Book.objects.filter(~Q(edition__gt=3) & ~(Q(title__icontains='qu') | Q(author__icontains='qu')))
    return render(request, 'bookmodule/bookList.html', {'books': books})

# Task 4: ترتيب الكتب أبجدياً حسب العنوان
def task4(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'bookmodule/bookList.html', {'books': books})

# Task 5: إحصائيات الكتب (المجموع، السعر الإجمالي، المتوسط، أعلى وأقل سعر)
def task5(request):
    stats = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'bookmodule/task5.html', {'stats': stats})

def task7(request):
    cities = Address.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodule/task7.html', {'cities': cities})

from django.shortcuts import render
from django.db.models import Sum, Count, Min, Max, Avg, Q
from .models import Book, Publisher

# Task 1: نسبة توفر الكتاب من الإجمالي
def task1(request):
    books = Book.objects.all()
    total_quantity = Book.objects.aggregate(total=Sum('quantity'))['total'] or 1 # تفادي القسمة على صفر
    for book in books:
        book.percentage = round((book.quantity / total_quantity) * 100, 2) # transient field[cite: 2]
    return render(request, 'bookmodule/lab9_task1.html', {'books': books})

# Task 2: الناشرين مع إجمالي المخزون[cite: 2]
def task2(request):
    publishers = Publisher.objects.annotate(total_stock=Sum('book__quantity'))
    return render(request, 'bookmodule/lab9_task2.html', {'publishers': publishers})

# Task 3: أقدم كتاب لكل ناشر[cite: 2]
def task3(request):
    publishers = Publisher.objects.annotate(oldest_book=Min('book__pubdate'))
    return render(request, 'bookmodule/lab9_task3.html', {'publishers': publishers})

# Task 4: حساب متوسط وأقل وأعلى سعر لكل ناشر[cite: 2]
def task4(request):
    publishers = Publisher.objects.annotate(
        avg_price=Avg('book__price'),
        min_price=Min('book__price'),
        max_price=Max('book__price')
    )
    return render(request, 'bookmodule/lab9_task4.html', {'publishers': publishers})

# Task 5: عدد الكتب ذات التقييم العالي لكل ناشر[cite: 2]
def task5(request):
    publishers = Publisher.objects.annotate(
        highly_rated_count=Count('book', filter=Q(book__rating__gte=4))
    )
    return render(request, 'bookmodule/lab9_task5.html', {'publishers': publishers})

# Task 6: تصفية الكتب حسب السعر والكمية لكل ناشر[cite: 2]
def task6(request):
    publishers = Publisher.objects.annotate(
        filtered_books_count=Count('book', filter=Q(book__price__gt=50, book__quantity__gte=1, book__quantity__lt=5))
    )
    return render(request, 'bookmodule/lab9_task6.html', {'publishers': publishers})