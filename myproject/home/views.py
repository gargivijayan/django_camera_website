from django.shortcuts import render,redirect
from . models import blog 
from django.utils import timezone
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


def index(request):
   
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def cameras(request):
    data={ 'obj': blog.objects.all()}
    return render(request,'cameras.html',(data))
def contact(request):
    return render(request,'contact.html')
def add(request):
    if request.method == "POST":
        brand = request.POST.get('bname')
        image = request.FILES.get('pic')
        if image:
            file_path = f"media/article_images/{image.name}"
            default_storage.save(file_path, ContentFile(image.read()))
       
        price= request.POST.get('amount')   
        description = request.POST.get('explain')
        date = timezone.now().date()
        query = blog(brand= brand, image=image,price=price, description=description, date=date)
        query.save()

    return render(request,'add.html')




def detailed(request,id):
    data={
        "subject":blog.objects.get(id=id)    
    }
    return render(request,'details.html',data)

def delete(request,id):
    dlt=blog.objects.get(id=id)
    dlt.delete()
    return redirect("/")

def edit(request, id):
    edit_post = blog.objects.get(id=id)
    if request.method == "POST":
        brand_name = request.POST.get('brand')
        new_image = request.FILES.get('image')  # Get the new image
        price=request.POST.get('price')
        description = request.POST.get('description')
        date = timezone.now().date()
        
       
        if new_image:
            if edit_post.image:
           
                default_storage.delete(edit_post.image.path)
     
            file_path = f"media/article_images/{new_image.name}"
            default_storage.save(file_path, ContentFile(new_image.read()))
        
        edit_post.brand = brand_name
        edit_post.image = new_image if new_image else edit_post.image
        edit_post.price=price 
        edit_post.description = description
        edit_post.date = date
        edit_post.save() 
    return render(request, 'edit.html', {"subject": edit_post})

def service(request):
    return render(request,'service.html')

def client(request):
    return render(request,'client.html')

    











