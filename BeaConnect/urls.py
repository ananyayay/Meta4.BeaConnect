"""Meta4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from BeaConnect import views

urlpatterns = [
	path('view_table/<str:table_name>', views.view_table),
	path('add_request', views.insert_request),
	path('new_request', views.new_request_page),
	
	path('attend_to', views.attend_to),
	path('appreciation', views.appreciation),
	path('call_volunteer', views.call_volunteer),
	path('elderly_details/<int:request_id>', views.elderly_details, name="elderly_details"),
	path('elderly_home', views.elderly_home, name="elderly_home"),
	path('submit_request', views.insert_request),
	path('feedback/<int:request_id>', views.feedback),
	path('submit_feedback', views.insert_feedback),
	path('requests', views.requests),
	path('volunteer_details/<int:request_id>', views.volunteer_details),
	path('volunteer_home', views.volunteer_home),
	path('appreciation/<int:request_id>', views.appreciation),
]
