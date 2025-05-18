from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from upload.models import Upload
from commision_work.models import Commission

from contac_us.models import Contact
from django.core.paginator import Paginator
def home(request):
    commisiondatas = Commission.objects.all()
  
    paginator = Paginator(commisiondatas,8)
    page_number = request.GET.get('page')
    final = paginator.get_page(page_number)

    phone1 = ''
    email1 = ''
    medium = ''
    price = ''
    image = ''
    custom = ''
    commisiondata = ''
    data = {}
    try:
        if request.method=='POST':
            phone1 = request.POST.get('phone1')
            email1 = request.POST.get('email1')
            medium = request.POST.get('medium')
            price = request.POST.get('price')
            image = request.FILES.get('image')
            custom = request.POST.get('custom')
       
        data = {'phone': phone1,'email' :email1, 'medium':medium,'price':price,'image':image,'custom':custom}
        commisiondata = Commission(phone=phone1,
email=email1,
medium=medium,
price=price,
image=image,
customization=custom)
        commisiondata.save()
        
    except:
        pass


    return render(request,"home.html",{"data":data , "artworks":final})

def artworks(request):
    myupload = Upload.objects.all()
  
    paginator = Paginator(myupload,8)
    page_number = request.GET.get('page')
    final = paginator.get_page(page_number)
   
    
    
    try:
        if request.method=='POST': 
            search = request.POST.get('search')
            if search!=None:
                final = Upload.objects.filter(title__icontains = search)      
    except:
        pass
    return render(request, "all_artworks.html", {'artworks': final})

def header(request):
    myupload = Upload.objects.all()
  
    paginator = Paginator(myupload,8)
    page_number = request.GET.get('page')
    final = paginator.get_page(page_number)
    
    try:
        if request.method == 'POST':
            search = request.POST.get('search')
            if search!=None:
                final = Upload.objects.filter(title__icontains = search)
  

           
        return render(request, "header.html", {'artworks': final})
    except:
        pass


def cart(request):
    
    myupload = Upload.objects.all()
  
    paginator = Paginator(myupload,8)
    page_number = request.GET.get('page')
    final = paginator.get_page(page_number)

        

    selltitle=''
    d=''
    p=''
    sellerartwork=''
    
    sellerart=''
    try:
        if request.method=='POST':
            selltitle = request.POST.get('selltitle')
            d = request.POST.get('d')
            p = request.POST.get('p')
            sellerartwork = request.FILES.get('sellerartwork')

            search = request.POST.get('search')
            if search!=None:
                final = Upload.objects.filter(title__icontains = search)
  
            sellerart=Upload(title=selltitle,
discription=d,
art=sellerartwork,
price=p)    
            sellerart.save()
        sellerdata = { "selltitle":selltitle, "d":d, "p":p, "sellerartwork":sellerartwork}
   
        
    except:
        pass           
    return render(request, "cart.html", {'artworks': final,'sellerdata':sellerdata})
   

      
    

  
   





def learn(request):
    return render(request,"learn.html")


def top(request):

    myupload = Upload.objects.all()
  
    paginator = Paginator(myupload,8)
    page_number = request.GET.get('page')
    final = paginator.get_page(page_number)
    
    try:
        if request.method == 'POST':
            search = request.POST.get('search')
            if search!=None:
                final = Upload.objects.filter(title__icontains = search)
  

           
        return render(request, "top_artist.html", {'artworks': final})
    except:
        pass



def profile(request):
    return render(request,"profile.html")






def data(request):
    data = {}

    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        if form_type == 'contact':
            # Handle contact form
            phonec = request.POST.get('phonec')
            emailc = request.POST.get('emailc')
            statec = request.POST.get('statec')
            cityc = request.POST.get('cityc')
            addressc = request.POST.get('addressc')
            feedbackc = request.POST.get('feedbackc')

            contactdata = Contact(
                phone=phonec,
                email=emailc,
                state=statec,
                city=cityc,
                address=addressc,
                feedback=feedbackc
            )
            contactdata.save()
            data.update({'phone': phonec, 'email': emailc, 'state': statec, 'city': cityc, 'address': addressc, 'feedback': feedbackc})

        elif form_type == 'commission':
            # Handle commission form
            phone1 = request.POST.get('phone1')
            email1 = request.POST.get('email1')
            medium = request.POST.get('medium')
            price = request.POST.get('price')
            image = request.FILES.get('image')
            custom = request.POST.get('custom')

            commisiondata = Commission(
                phone=phone1,
                email=email1,
                medium=medium,
                price=price,
                image=image,
                customization=custom
            )
            commisiondata.save()
            data.update({'phone': phone1, 'email': email1, 'medium': medium, 'price': price, 'image': image, 'custom': custom})

        elif form_type == 'upload':
            # Handle artwork upload form
            selltitle = request.POST.get('selltitle')
            d = request.POST.get('d')
            p = request.POST.get('p')
            sellerartwork = request.FILES.get('sellerartwork')

            sellerart = Upload(
                title=selltitle,
                discription=d,
                art=sellerartwork,
                price=p
            )
            sellerart.save()
            data.update({'title': selltitle, 'd': d, 'p': p, 'sellerartwork': sellerartwork})

    return render(request, "data.html", data)




def contact(request):
    phonec = ''
    emailc = ''
    statec = ''
    cityc = ''
    addressc = ''
    feedbackc = ''

    data = {}
    try:
        if request.method=='POST':
            phonec = request.POST.get('phonec')
            emailc = request.POST.get('emailc')
            statec = request.POST.get('statec')
            cityc = request.POST.get('cityc')
            addressc = request.POST.get('addressc')
            feedbackc = request.POST.get('feedbackc')
        
        data = {'phone': phonec,'email' :emailc, 'state':statec,'city':cityc,'address':addressc,'feedback':feedbackc}
      
    except:
        pass

    return render(request, "contact.html",data)



def purchase(request):
    return render(request,"purchase.html")


def index(request):
    return render(request,"index.html")