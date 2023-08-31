from django.shortcuts import render
from .models import Services,Contact,Partner,Testimonial,Product,Photo,Achivement,About,Link,Track

def center(request):
    if request.method=="POST":
        name=request.POST['name']
        phone=request.POST['phone']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact=Contact(name=name,phone=phone,email=email,subject=subject,message=message)
        contact.save()
        print("data printed on db")
    image=Track.objects.all()
    link=Link.objects.all
    about=About.objects.all()
    services=Services.objects.all()
    partner=Partner.objects.all()
    testimonial=Testimonial.objects.all()
    product=Product.objects.all()
    photo=Photo.objects.all()
    achivement=Achivement.objects.all()

    return render(request, "index.html", {'image':image,'link':link,'about':about,'services': services,'partner':partner,'testimonial':testimonial,'photo':photo
                                          ,'product':product,'achivement':achivement})



