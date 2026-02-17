from django.shortcuts import render # غيرنا HttpResponse إلى render
from django.http import HttpResponse

# Task 4 & 5: عرض صفحة HTML وإرسال الاسم لها
def index(request):
    name = request.GET.get("name") or "world!"
    # 'bookmodule/index.html' هو المسار داخل مجلد templates
    return render(request, "bookmodule/index.html", {"name": name})

# Task 3: لسه زي ما هو يعرض نص سادة 
def index2(request, val1=0):
    return HttpResponse("value1 = " + str(val1))

def viewbooks(request):
    return render(request, 'bookmodule/viewbooks.html')

def viewbook(request, bookId):
    # محاكاة لقاعدة بيانات بسيطة (قاموس)
    book1 = {'id':123, 'title':'Continuous Integration', 'author':'Jenkins'}
    book2 = {'id':456, 'title':'Continuous Delivery', 'author':'Humble'}
    
    targetBook = None
    if book1['id'] == bookId: targetBook = book1
    if book2['id'] == bookId: targetBook = book2
    
    context = {'book': targetBook}
    return render(request, 'bookmodule/show.html', context)