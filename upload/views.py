from .importer import *
from .models import Book
import csv
# Create your views here.


class Home(TemplateView):  # class based view
    template_name = 'home.html'

# simple upload
def upload(request):  # fbv  # httprequest  
    context = {}
    # print(request.method)
    # print(request.user)
    if request.method == 'POST':
        uploaded_file = request.FILES['document']  # name given in html file - in form
        # print(uploaded_file.name)
        # print(uploaded_file.size)
        file_store = FileSystemStorage()  # Advantage of FileSystemStorage is that dont having the overwrite risk. It wil rename while saving.
        name = file_store.save(uploaded_file.name, uploaded_file)
        print(file_store.url(name))
        context['url'] = file_store.url(name)  # {"url": /media/no_pass_meetings%20(1)%20(1).csv}
        # print(context)
    return render(request, 'upload.html', context) # url:file_link

#########################################################################

# Function based view

from .forms import BookForm

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books' : books})
# try below function without using django forms
def upload_book(request):   # Upload the book with title, author and file.
    if request.method == 'POST':
        # title = request.POST.get("title")   # 
        # pdf = request.FILES["pdf"]
        # cover = request.FILES["coverpage"]
        # Book.objects.create()
        form = BookForm(request.POST, request.FILES)   # As it is similar like request['name'], POST willl give the title and author & FILES give the uploaded file
        if form.is_valid():  # Data is cleaned in three processes, if data is not cleaned the it raises validation error.
            form.save()
            return redirect('book_list')  # redirected towards book_list function where we wil get all the books.
    else:
        form = BookForm()
        return render(request, 'upload_book.html', {'form': form})

def delete_book(request, pk):
    if request.method == 'POST':
        book = Book.objects.get(pk=pk)
        
        #Customised
        book.PDF.delete()             # For deleting the file or coverpage from localmachine as the only name will be deleted in database.
        book.coverpage.delete()

        # always keep after media deletion
        book.delete() # db delete
    return redirect('book_list')


# class based views

from django.views.generic import ListView, CreateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.shortcuts import HttpResponseRedirect

class BookListView(ListView):   # All methods are built-in in ListView
    model = Book
    template_name = 'class_book_list.html'
    context_object_name = 'books'   # This object name is passed to html page.


class UploadBookView(CreateView):
    model = Book 
    form_class = BookForm   # Or u can directly put the fields='__all__'
    success_url = reverse_lazy('class_book_list')   # It will redirect to class_book_list url.
    template_name = 'class_upload_book.html'



class DeleteBookView(DeleteView):
    model = Book
    success_url = reverse_lazy("class_book_list")

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()

        success_url = self.get_success_url()
        #Customised
        self.object.PDF.delete()     # For deleting the file or coverpage from localmachine as the only name will be deleted in database.
        if self.object.coverpage:
            self.object.coverpage.delete()
        self.object.delete()
        return HttpResponseRedirect(success_url)



def delete_all_book(request):
    all_books = Book.objects.all()
    print("In delete all book")
    print(all_books)
    print("Inside delete all book")
    for book in all_books:
        book.PDF.delete()
        book.coverpage.delete()
        book.delete()
    # return render(request, 'book_list.html')
    return redirect('book_list')

from django.shortcuts import (get_object_or_404, 
                              render, 
                              HttpResponseRedirect)

def edit(request, pk): 
    obj = get_object_or_404(Book, id = pk) 
    print('@@@@@')
    # pass the object as instance in form 
    form = BookForm(request.POST or None, request.FILES or None, instance = obj) 
  
    # save the data from the form and 
    # redirect to detail_view 
    if form.is_valid(): 
        form.save() 
        return redirect('book_list') 
  
    # add form dictionary to context 
    return render(request, "upload_book.html", {'form': form}) 



# def csv_read(request):
#     with open(r'S:\django\projects\File_Upload_Class\media\product.csv', 'r') as file:
#         reader = csv.reader(file)
#         data = list(reader)
#     return render(request, 'read.html', {'data': data})

def csv_read(request):
    if request.method == 'POST':
        file = request.FILES['csv_file']
        reader = csv.reader(file.read().decode('utf-8').splitlines())
        data = list(reader)
        return render(request, 'read.html', {'data': data})
    return render(request, 'read_csv.html')


from django.shortcuts import render


