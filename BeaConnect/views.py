import datetime
import json
import textwrap

import pandas as pandas
from django.apps import apps
from django.db.models import Model
from django.http import HttpRequest, HttpResponseBadRequest, HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.http import require_POST, require_GET
from django.forms.models import model_to_dict

from .models import Request, Volunteer, User, VolunteerReview

@require_POST
def insert_request(request: HttpRequest) -> HttpResponse:
	data = json.loads(request.body)
	user_id = 2  # STUB
	# volunteer_default = None
	volunteer_default = 102  # STUB
	try:
		toadd = Request(content=data["req_content"], time=str(datetime.datetime.now()),
		                category=data["category"], requester=user_id, volunteer=volunteer_default)
		toadd.save()
	except ValueError:
		return HttpResponseBadRequest("<h1>Invalid Data submitted</h1>")
	
	return redirect(f'volunteer_details/{toadd.request_id}')

@require_POST
def insert_feedback(request: HttpRequest) -> HttpResponse:
	data = json.loads(request.body)
	user_req = Request.objects.get(request_id=data["request_id"])
	try:
		toadd = VolunteerReview(volunteer_id=user_req.volunteer, elderly_id=user_req.requester,
		                        review_contents=data["feedback"], star_rating=3)
		toadd.save()
	except ValueError:
		return HttpResponseBadRequest("<h1>Invalid Data submitted</h1>")
	
	return redirect(reverse("elderly_home"))

@require_POST
def find_volunteer(request: HttpRequest) -> HttpResponse:
	data = json.loads(request.body)
	user_id = 2  # STUB
	try:
		toadd = Request(content=data["req_content"], time=str(datetime.datetime.now()),
		                category=data["category"], requester=user_id, volunteer=None)
		toadd.save()
	except ValueError:
		return HttpResponseBadRequest("<h1>Invalid Data submitted</h1>")
	
	return redirect(f'volunteer_details/{toadd.request_id}')

@require_GET
def view_table(request: HttpRequest, table_name: str) -> HttpResponse:
	try:
		model: Model = apps.get_model(app_label="BeaConnect", model_name=table_name)
	except (LookupError, ValueError):
		return HttpResponseNotFound("<h1>Invalid Table Name</h1>")
	parsed = [model_to_dict(x) for x in model.objects.all()]
	toret: pandas.DataFrame = pandas.DataFrame(parsed)
	# toret["bio"] = toret["bio"].str.wrap(40)
	# toret["bio"] = toret["bio"].apply(lambda x: "\n".join(textwrap.wrap(x, 40)))
	return render(request, "BeaConnect/display_table.html", {"data": toret.to_html(
		formatters={"photograph": lambda x: f"<img src={str(x)}></img>"}, justify="center", index=False
	)})

@require_GET
def new_request_page(request: HttpRequest) -> HttpResponse:
	return render(request, "BeaConnect/new_request.html")

@require_GET
def call_volunteer(request: HttpRequest) -> HttpResponse:
	return render(request, "BeaConnect/call_volunteer.html")

@require_GET
def elderly_home(request: HttpRequest) -> HttpResponse:
	return render(request, "BeaConnect/elderly_home.html")

@require_GET
def feedback(request: HttpRequest, request_id: int) -> HttpResponse:
	user_req = Request.objects.get(request_id=request_id)
	volunteer_user = User.objects.get(id=user_req.volunteer)
	return render(request, "BeaConnect/feedback.html",
	              {
		              "request_id": request_id,
		              "pfp": "BeaConnect/media/"+volunteer_user.photograph,
		              "name": volunteer_user.username,
		              "req_content": user_req.content
	              }
	              )

@require_GET
def requests(request: HttpRequest) -> HttpResponse:
	return render(request, "BeaConnect/requests.html")

@require_GET
def elderly_details(request: HttpRequest) -> HttpResponse:
	return render(request, "BeaConnect/elderly_details.html")

@require_GET
def volunteer_details(request: HttpRequest, request_id: int) -> HttpResponse:
	user_req = Request.objects.get(request_id=request_id)
	if (user_req.volunteer is None):
		return render(request, "BeaConnect/volunteer_details_empty.html")
	volunteer = Volunteer.objects.get(id=user_req.volunteer)
	volunteer_user = User.objects.get(id=user_req.volunteer)
	return render(request, "BeaConnect/volunteer_details.html",
	              {
		              "request_id": request_id,
		              "pfp": "BeaConnect/media/"+volunteer_user.photograph,
		              "name": volunteer_user.username,
		              "about": volunteer_user.bio,
	              }
	              )

@require_GET
def volunteer_home(request: HttpRequest) -> HttpResponse:
	return render(request, "BeaConnect/volunteer_home.html")

@require_GET
def appreciation(request: HttpRequest) -> HttpResponse:
	return render(request, "BeaConnect/appreciation.html")
