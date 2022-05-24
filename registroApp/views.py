from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm #add this
from django.contrib.auth import login, authenticate #add this
from django.contrib import messages
from django.views.generic import View

# Create your views here.

class VRegistro(View):

	def get(self, request):
		form=UserCreationForm()
		return render(request, "registerApp/register.html", {"form":form})

	def post(self, request):
		pass



class VLogin(View):
	def get(self, request):
		form=UserCreationForm()
		return render(request, "registerApp/login.html", {"form":form})

	def post(self, request):
		pass


		# form=UserCreationForm(request.POST)
		# if form.is_valid():
		# 	usuario = form.save()
		# 	login(request, usuario)
		# 	return redirect('home')
		# else:
		# 	pass



	# if request.method == "POST":
	# 	form = UserCreationForm(request.POST)
	# 	if form.is_valid():
	# 		username = form.cleaned_data.get('username')
	# 		password = form.cleaned_data.get('password')
	# 		user = authenticate(username=username, password=password)
	# 		form.save()
	# 		if user is not None:
	# 			login(request, user)
	# 			messages.info(request, f"You are now logged in as {username}.")
	# 			return redirect("/")
	# 		else:
	# 			for msg in form.error_messages:
	# 				messages.error(request,form.error_messages[msg])
	# 	else:
	# 		for msg in form.error_messages:
	# 				messages.error(request,form.error_messages[msg])
	# 		form = UserCreationForm()
	# 		return render(request, "register/register.html", {"form":form})

# def Vlogin(request):
# 	if request.method == "POST":
# 		form = AuthenticationForm(request, data=request.POST)
# 		if form.is_valid():
# 			username = form.cleaned_data.get('username')
# 			password = form.cleaned_data.get('password')
# 			user = authenticate(username=username, password=password)
# 			if user is not None:
# 				login(request, user)
# 				messages.info(request, f"You are now logged in as {username}.")
# 				return redirect("/home")
# 			else:
# 				messages.error(request,"Usuario o password inválido.")
# 		else:
# 			messages.error(request,"usuario o password inv&aacute;lido.")
# 	form = AuthenticationForm()
# 	return render(request=request, template_name="register/login.html", context={"login_form":form})