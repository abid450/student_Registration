from django.shortcuts import render,HttpResponseRedirect
from .forms import yellow_form
from .models import yellow_M
from .register import register_y,change_U
# Login form ----------------
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,update_session_auth_hash
# Create your views here.
# Form ---------------------------
def Y_llow(request):
    if request.method == 'POST':
        frm = yellow_form(request.POST)
        if frm.is_valid():
            Name = frm.cleaned_data['Name']
            Email = frm.cleaned_data['Email']
            Course = frm.cleaned_data['Course']
            Phone = frm.cleaned_data['Phone']
            College = frm.cleaned_data['College']
            contents = yellow_M(Name=Name, Email=Email, Course=Course, Phone=Phone, College=College)
            contents.save()
            return HttpResponseRedirect('/yellow_re')
        
    else:
        frm = yellow_form()
    return render(request,'y_llow.html',{'form':frm})

# Form redirect ----------------------------------
def yellow_re(request):
    return render(request,'yellow_re.html')

# Register form --------------------------------
def registration(request):
    if request.method == 'POST':
       frm = register_y(request.POST)
       if frm.is_valid():
           frm.save()
           HttpResponseRedirect('/Register_r_re')

    else:
        frm = register_y()
    return render(request,'r.html',{'form':frm})


# Register redirect----------------------------------
def Register_re(request):
    return render(request,'Register_re.html')


# Login -------------------------------------
def softTect_L(request):
    if request.method == 'POST':
        frm = AuthenticationForm(request=request, data= request.POST )
        if frm.is_valid():
            usern = frm.cleaned_data['username']
            passw = frm.cleaned_data['password']
            user = authenticate(username=usern, password=passw)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/softTech')
            
    else:
        frm = AuthenticationForm()
    return render(request,'login.html',{'form':frm})


def login_R(request):
    return render(request,'login_r.html')

# change password -----------------------------
def change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            frm = PasswordChangeForm(user=request.user, data=request.POST)
            if frm.is_valid():
                frm.save()
                update_session_auth_hash(request, frm.user)
                return HttpResponseRedirect('/softTect_L')
        
        else:
            frm = PasswordChangeForm(user=request.user)
        return render(request,'change_p.html',{'form':frm})
    
    else:
        return HttpResponseRedirect('/Change_pass')
    
# Change User --------------------------
def Change_user(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            frm = change_U(request.POST, instance = request.user)
            if frm.is_valid():
                frm.save()
                return HttpResponseRedirect('/registration')
        else:
            frm = change_U(instance = request.user)
        return render(request,'change_u.html',{'form':frm})
    
    else:
        return HttpResponseRedirect('/Change__userp')


        

