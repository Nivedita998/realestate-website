from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from django.shortcuts import render ,get_object_or_404 , redirect ,reverse
from .models import Post ,Contact ,ContactAgent

def index(request):
    queryset=Post.objects.all()[0:6]
    context={
        'object_list': queryset
    }
    return render(request,'index.html',context)



def contact(request ):
    if request.method=="POST":
        name=request.POST["name"]
        email=request.POST["email"]
        phone=request.POST["phone"]
        message=request.POST["message"]
        new_contact=Contact()
        new_contact.name=name
        new_contact.email=email
        new_contact.phone=phone
        new_contact.message=message
        new_contact.save()
        return redirect(reverse("contact_detail", ))
    
    


    return render(request,'contact.html',{})



def allproperty(request):
    data=Post.objects.all()
    paginator=Paginator(data , 6)
    page_request_var='page'
    page=request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page) 
    except PageNotAnInteger:
        paginated_queryset=paginator.page(1)
    except EmptyPage:
        paginated_queryset=paginator.page(paginator.num_pages)



    context={
        'queryset': paginated_queryset,
        'page_request_var': page_request_var

    }
    return render(request,'properties.html',context)

 

def about(request):
    return render(request,'about.html',{})




def details(request, id):
    
    post=get_object_or_404(Post,id=id)
    
    context={
        'post':post
    }
    if request.method=="POST":
        name=request.POST["name"]
        email=request.POST["email"]
        phone=request.POST["phone"]
        new_contact=ContactAgent()
        new_contact.name=name
        new_contact.email=email
        new_contact.phone=phone
        new_contact.save()
        return redirect(reverse("property_detail", kwargs={
                'id': post.id
            }))

    return render(request,'property-details.html',context)