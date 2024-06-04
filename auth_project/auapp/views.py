from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate

def uhome(request):
	if request.user.is_authenticated:
		if request.GET.get("marks"):
			marks = float(request.GET.get("marks"))
			if marks < 0:
				msg="Marks Cannot be Negative"
			elif marks > 100:
				msg="Marks Should be between 0 to 100"
			elif marks >80:
				msg ="Grade A"
			elif marks >60:
				msg ="Grade B"
			else:
				msg ="Grade C"
			return render(request, "home.html", {"msg":msg})
		else:
			return render(request, "home.html")
	else:
		return redirect("ulogin")
    
    
def ulogin(request):
    if request.user.is_authenticated:
        return redirect("uhome")
    elif request.method == "POST":
        un = request.POST.get("un")
        pw = request.POST.get("pw")
        usr = authenticate(username=un,password=pw)
        if usr is None:
            return render(request,"login.html",{"msg":"Invalid login"})
        else:
            login(request,usr)
            return redirect("uhome")
    else:
        return render(request,"login.html")

def usignup(request):
    if request.user.is_authenticated:
        return redirect("uhome")
    elif request.method == "POST":
        un = request.POST.get("un")
        pw1 = request.POST.get("pw1")
        pw2 = request.POST.get("pw2")
        if pw1 == pw2:
            try:
                usr = User.objects.get(username=un)
                return render(request,"signup.html",{"msg":"user already exists"})
            except User.DoesNotExist:
                usr = User.objects.create_user(username=un,password=pw1)
                usr.save()
                return redirect("ulogin")
        else:
            return render(request,"signup.html",{"msg":"Password does not match"})
    else:
        return render(request,"signup.html")
      
def ulogout(request):
    logout(request)
    return redirect("ulogin")

def ucpass(request):
    if not request.user.is_authenticated:
        return redirect("ulogin")
    elif request.method == "POST":
        pw1 = request.POST.get("pw1")
        pw2 = request.POST.get("pw2")
        if pw1 == pw2:
            usr = User.objects.get(username=request.user.username)
            usr.set_password(pw1)
            usr.save()
            return redirect("ulogin")
        else:
            return render(request,"cpass.html",{"msg":"Password did not match"})
    else:
        return render(request,"cpass.html")


