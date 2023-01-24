from django.shortcuts import render , HttpResponse
from django.core import paginator
from django.core.paginator import Page, Paginator
from .models import Simulation_Project , Video_Project


# Create your views here.

def home(request):

     Simulation_project_object = Simulation_Project.objects.all()


     paginator= Paginator(Simulation_project_object,9) 
     page = request.GET.get('page')
     Simulation_project_object = paginator.get_page(page)

     return render(request ,'phyApp/simulations.html' , {'Simulation_project_object':Simulation_project_object})


def about(request):
    return render(request , 'phyApp/about.html' )


def hardware(request):
     Video_project_object = Video_Project.objects.all()

     project_search_name = request.GET.get('project_search_name')

     if  project_search_name != '' and  project_search_name is not None :
        Video_project_object = Video_project_object.filter(title__icontains=project_search_name)


     paginator= Paginator( Video_project_object,9) 
     page = request.GET.get('page')
     Video_project_object = paginator.get_page(page)

     return render(request ,'phyApp/videos.html' , {'Video_project_object':Video_project_object})

def detail(request , id):
     project = Simulation_Project.objects.filter(id=id)

     Video_project_object = Video_Project.objects.all()
     Simulation_project_object = Simulation_Project.objects.all()

     return render(request ,'phyApp/detail.html' , {'Simulation_project_object':Simulation_project_object , 'Video_project_object':Video_project_object , 'project' : project[0]})
     