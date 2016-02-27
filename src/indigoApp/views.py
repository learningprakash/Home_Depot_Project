from django.shortcuts import render
from django.http import HttpResponse
from indigoApp.getProUsers import ProUsers
from indigoApp.getAssociates import Associates
from indigoApp.getDiyLinks import DiyLinks

# Create your views here.

#def index(request):
#    return HttpResponse("Hello, world!")

def index(request):
#	context = {'sample_text': "Hello World"}
#	return render(request, 'indigoApp/index.html', context)
#   return HttpResponse("Hello, world!")
    return render(request, 'indigoApp/index.html')

def pro(request):
	#if request type is POST, process data
	if request.method == 'POST':
		selection = request.POST.get('hInput')
		pro = ProUsers()
		""" selection = request.POST.get('byCategory')
		pro = ProUsers()
		
		if(selection == 'byProname'):
			proname = request.POST.get('txtProName')
			response = pro.getUserByName('Rala')

			context = {'response_obj' : response}
			return render(request, 'indigoApp/pro.html', context)
		elif(selection == 'byCategory'): 
			category = request.POST.get('hInput')
			pro = ProUsers()"""
		response = pro.getUsers(selection.lower(), None)
		context = {'response_obj' : response}
		return render(request, 'indigoApp/pro.html', context)
	return render(request, 'indigoApp/pro.html')
	
def help(request):
	if request.method == 'POST':
		searchQuery = request.POST.get('answer')
		link = DiyLinks()
		response = link.getDiyLinks(searchQuery)
		context = {'response_obj' : response}
		return render(request, 'indigoApp/help.html', context)
	return render(request, 'indigoApp/help.html')
	
def associate(request):
	if request.method == 'POST':
		selection = request.POST.get('hInput')
		associates = Associates()
		response = associates.getAssociatesFromCategory(selection.lower())
		context = {'response_obj' : response}
		return render(request, 'indigoApp/associate.html', context)
	return render(request, 'indigoApp/associate.html')

def demo(request):
	#orm = MyModelForm()
	text = "Hey there" #+ request.POST.get('txtName')
	context = {'response_text': text}
	return render(request, 'indigoApp/_demo.html', context)

