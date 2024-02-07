from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib import messages 
from django.contrib.auth import logout
import requests, random
from django.core.mail import send_mail
from onlinebanner import settings



def index(request):
        
        try:
            puser = request.session.get('puserid')
            cuser = request.session.get('cuserid')
        except:
             pass
        item = banners_upload.objects.all()
        if puser:
            puser=publisher_signup.objects.get(id=puser)
            cuser = None
        elif cuser:
            cuser=client_signup.objects.get(id=cuser)
            puser = None
        
        return render(request,'index.html',{'cuser':cuser,'puser':puser,'item':item})





def about(request):
        
        try:
            puser = request.session.get('puserid')
            cuser = request.session.get('cuserid')
        except:
             pass
        if puser:
            puser=publisher_signup.objects.get(id=puser)
            cuser = None
        elif cuser:
            cuser=client_signup.objects.get(id=cuser)
            puser = None
      
        return render(request,'about.html',{'cuser':cuser,'puser':puser})


def contact(request):
        
        try:
            puser = request.session.get('puserid')
            cuser = request.session.get('cuserid')
        except:
             pass
        if puser:
            puser=publisher_signup.objects.get(id=puser)
            cuser = None
        elif cuser:
            cuser=client_signup.objects.get(id=cuser)
            puser = None


        if request.method=='POST':
            newfeedback=feedbackForm(request.POST)
            if newfeedback.is_valid():
                newfeedback.save()
                print("Your FEEDBACK has been submitted!")

                #Email Send
                send_mail(subject="Thank you!",message=f"Dear User\n\nThanks for connecting with us!\nIf you have any queries regarding service, Please contact on\n\n+919624144412 | rohitghatar@gmail.com | www.tops-int.com",from_email=settings.EMAIL_HOST_USER,recipient_list=[request.POST['email']])

                #SMS Send
                otp=random.randint(1111,9999)
                # url = "https://www.fast2sms.com/dev/voice"
                url = "https://www.fast2sms.com/dev/bulkV2"
                querystring = {"authorization":"jy1lum4IfY6henACTQa3wBZROiXtkDLocVU57GdrKM0HbSsxpv7Hp0ZtaeNj23drDVfoPu1KGQgsMB64","variables_values":f"{otp}","route":"otp","numbers":f"{request.POST['phone']}"}
                headers = {
                    'cache-control': "no-cache"
                }
                response = requests.request("GET", url, headers=headers, params=querystring)
                print(response.text)
            else:
                print(newfeedback.errors)

        
        return render(request,'contact.html',{'cuser':cuser,'puser':puser})


def banners(request):
        
        try:
            puser = request.session.get('puserid')
            cuser = request.session.get('cuserid')
        except:
             pass
        item = banners_upload.objects.all()

        #for filtering publisher name
        pub_name = set()
        location = set()

        for items in item:
            if items.pub_name not in pub_name:
                pub_name.add(items.pub_name)
            
            if items.location not in location:
                 location.add(items.location)

        # for filter data
        publisher_name = request.GET.get('publisher')
        banner_location = request.GET.get('location')
        banner_price = request.GET.get('price')

        if publisher_name != '' and publisher_name is not None:
            item = item.filter(pub_name = publisher_name)

        if banner_location != '' and banner_location is not None:
            item = item.filter(location = banner_location)

        if banner_price != '' and banner_price is not None:

            if banner_price == 'HIGHEST':
                item = item.order_by('-price')

            elif banner_price == 'LOWEST':
                item = item.order_by('price')
                

        if puser:
            puser=publisher_signup.objects.get(id=puser)
            cuser = None
        elif cuser:
            cuser=client_signup.objects.get(id=cuser)
            puser = None
     
        return render(request,'banners.html',{'cuser':cuser,'puser':puser,'item':item,'pub_name':pub_name,'location':location})


def testimonial(request):

        try:
            puser = request.session.get('puserid')
            cuser = request.session.get('cuserid')
        except:
             pass
        if puser:
            puser=publisher_signup.objects.get(id=puser)
            cuser = None
            return render(request,'testimonial.html',{'puser':puser,'cuser':cuser})
        elif cuser:
            cuser=client_signup.objects.get(id=cuser)
            puser = None
            return render(request,'testimonial.html',{'cuser':cuser,'puser':puser})
        else:
             return render(request,'testimonial.html',{'cuser':cuser,'puser':puser})

def profile(request):
        
        try:
            puser = request.session.get('puserid')
            cuser = request.session.get('cuserid')
        except:
             pass
    

        if puser:
            puser=publisher_signup.objects.get(id=puser)
            cuser = None
            if request.method=='POST':
                newuser=publisher_Update_form(request.POST,instance=puser)
                if newuser.is_valid(): #true
                    newuser.save()
                    print("Record updated successfully!")
                    # return redirect('profile')
                    return render(request,'profile.html',{'puser':puser,'cuser':cuser})
                else:
                    print(newuser.errors)
            
            
        if cuser:
            cuser=client_signup.objects.get(id=cuser)
            puser = None
            if request.method=='POST':
                newuser=client_Update_form(request.POST,instance=cuser)
                if newuser.is_valid(): #true
                    newuser.save()
                    print("Record updated successfully!")

        return render(request,'profile.html',{'puser':puser,'cuser':cuser})



def c_login(request):
        
        if request.POST.get('clogin')=='clogin':
            unm = request.POST['email']
            pas = request.POST['password']

            try:
                cuser = client_signup.objects.filter(email=unm,password=pas)
                cuserid=client_signup.objects.get(email=unm)
            except:
                 messages.success(request,'invalid email or password')
            
            
            if cuser: #true
                print("Login Successfully!")
                request.session['cuser']=unm
                request.session['cuserid']=cuserid.id
                return redirect('/')
            else:
                print("Error")
                messages.success(request,'invalid email or password')
                
            cuser=request.session.get('cuser')
            cuserid=request.session.get('cuserid')
            try:
                cuser=client_signup.objects.get(id=cuserid)
                return render(request,'index.html',{'cuser':cuser,'cuserid':cuserid})
            except:
                 return render(request,'index.html',{'cuserid':cuserid})


        return render(request,'c_login.html')

def c_signup(request):

        if request.method=='POST':
            #signup code
            if request.POST.get('SignUp')=='SignUp':
                newuser = client_Signup_form(request.POST)
                if newuser.is_valid():
                    username = newuser.cleaned_data.get('email')
                    try:
                        un = client_signup.objects.get(email=username)
                        print("username is already exists")
                        messages.success(request,'this email is already exists...')

                    except client_signup.DoesNotExist:
                        newuser.save()
                        print('client signup successfully')
                        return redirect('c_login')
                else:
                    print(newuser.errors)


        return render(request,'c_signup.html')


def p_login(request):
        
        if request.POST.get('plogin')=='plogin':
            unm = request.POST['email']
            pas = request.POST['password']

            try:
                puser = publisher_signup.objects.filter(email=unm,password=pas)
                puserid=publisher_signup.objects.get(email=unm)
            except:
                messages.success(request,'invalid email or password')
            

            if puser: #true
                print("Login Successfully!")
                request.session['puser']=unm
                request.session['puserid']=puserid.id
                return redirect('/')
            else:
                print("Error")
                messages.success(request,'invalid email or password')
            puser=request.session.get('puser')
            puserid=request.session.get('puserid')
            try:
                puser=publisher_signup.objects.get(id=puserid)
                return render(request,'index.html',{'puser':puser,'puserid':puserid})
            except:
                # return render(request,'index.html',{'puser':puser})
                 return render(request,'index.html',{'puserid':puserid})


        return render(request,'p_login.html')

def p_signup(request):

        if request.method=='POST':
            #signup code
            if request.POST.get('SignUp')=='SignUp':
                newuser = publisher_Signup_form(request.POST)
                if newuser.is_valid():
                    username = newuser.cleaned_data.get('email')
                    try:
                        un = publisher_signup.objects.get(email=username)
                        print("username is already exists")
                        messages.success(request,"username is already exists")

                    except publisher_signup.DoesNotExist:
                        newuser.save()
                        print('client signup successfully')
                        return redirect('p_login')
                else:
                    print(newuser.errors)


        return render(request,'p_signup.html')



def userlogout(request):
        logout(request)
        return redirect('/')


def deleteclient(request,id):

    # cuser = request.session.get('cuserid')

    stid=client_signup.objects.get(id=id)
    client_signup.delete(stid)

    userlogout(request)

    return redirect('/')


def deletepublisher(request,id):

    # cuser = request.session.get('cuserid')

    stid=publisher_signup.objects.get(id=id)
    publisher_signup.delete(stid)

    userlogout(request)

    return redirect('/')


def upload_banner(request):
        
        try:
            puser = request.session.get('puserid')
            cuser = request.session.get('cuserid')
        except:
             pass
        
        if puser:
            puser=publisher_signup.objects.get(id=puser)
            cuser = None
            if request.method=='POST':
                    banner = banners_upload_form(request.POST,request.FILES)
                    if banner.is_valid():
                        banner.save()
                        print('banner uploaded successfully')
                        return redirect('banners')
                    else:
                        print(banner.errors)
                        return render(request,'upload_banner.html',{'puser':puser,'cuser':cuser})
            else:
                return render(request,'upload_banner.html',{'puser':puser,'cuser':cuser})
                

        else:
             return render(request,'upload_banner.html',{'cuser':cuser,'puser':puser})

