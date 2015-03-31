from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.template import RequestContext
from member.forms import RegistrationForm, LoginForm
from member.models import Member
from django.contrib.auth import autheticate, login, logout

def MemberRegistration(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/profile/')
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():            
            user = User.objects.create_user(username=form.cleaned_data['username'], email=form.cleaned_data['email'], password = form.cleaned_data['password'])
            #user.save()
            #member = user.get_profile()
            #member.first_name = form.cleaned_data['first_name']
            #member.last_name = form.cleaned_data['last_name']
            #member.save()
            member = Member(user=user, first_name = form.cleaned_data['first_name'], last_name = form.cleaned_data['last_name'])
            member.save()
            return HttpResponseRedirect('/profie/')
        else:
            return render_to_response('register.html', {'form': form}, context_instance=RequestContext(request))
        
        
    else:
        form = RegistrationForm()
        context = {'form': form}
        return render_to_response('register.html', context, context_instance=RequestContext(request))

def Profile(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    member = request.user.get_profile
    context = {'member': member}
    return render_to_response('profile.html', context, context_instance=RequestContext(request))
    
def LoginRequest(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/profile/')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            member = autheticate(username=username, password = password)
            if member is not None:
                login(request, member)
                return HttpResponseRedirect('/profile/')
            else:
                return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))
        else:
            return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))
            
    else:
        form = LoginForm()
        context = {'form': form}
        return render_to_response('login.html', context, context_instance=RequestContext(request))

def LogoutRequest(request):
    logout(request)
    return HttpResponseRedirect('/')