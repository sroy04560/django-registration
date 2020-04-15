from django.shortcuts import render

from register.form import userform,userformsinfo

from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse

from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request,'basic/index.html')

def register(request):
	registered=False

	if request.method=='POST':

	 	user_form=userform(data=request.POST)
	 	profile_form=userformsinfo(data=request.POST)

	 	if user_form.is_valid() and profile_form.is_valid():

	 		user=user_form.save()
	 		user.set_password(user.password) # this thing we done for hashing the password to the database
	 		user.save()

	 		profile=profile_form.save(commit=False) #bcz we use one to one and if we true then pic will overlap with another user
	 		profile.user=user# this line show  one to one relations

	 		if 'pics' in request.FILES:
	 			profile.pics=request.FILES['pics']

	 			profile.save()

	 		registered=True

	 	else:
	 		print(user_form.errors,profile_form.errors)

	else:
		user_form=userform()
		profile_form=userformsinfo()

	return render(request,'basic/register.html',
							{'user_form':user_form,
							'profile_form':profile_form,
							'register':registered})




def log(request):
	if request.method=='POST':
		username=request.POST.get('username')
		password=request.POST.get('password')

		user=authenticate(username=username,password=password)
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('basic:index'))

			else:
				return HttpResponse('account is not activ')

		else:
			print('Someone is tried to login but faild')
			print('username {} and password {}'.format(user,password))
			return HttpResponse('invalid details')
	else:
		return render(request,'basic/log.html')


@login_required
def special(request):
	return HttpResponse('you login ')


@login_required
def lout(request):
	logout(request)
	return HttpResponseRedirect(reverse('basic:index'))