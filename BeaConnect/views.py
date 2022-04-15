import datetime
import json
import textwrap

import pandas as pandas
from django.apps import apps
from django.db.models import Model
from django.http import HttpRequest, HttpResponseBadRequest, HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.views.decorators.http import require_POST, require_GET
from django.forms.models import model_to_dict

from .models import Request

@require_POST
def insert_request(request: HttpRequest) -> HttpResponse:
	data = json.loads(request.body)
	user_id = -1  # STUB
	try:
		toadd = Request(content=data["req_content"], time=str(datetime.datetime.now()),
		                category=data["category"], requester=user_id, volunteer=None)
		toadd.save()
	except ValueError:
		return HttpResponseBadRequest("<h1>Invalid Data submitted</h1>")
	
	return HttpResponse(status=200, content="success")

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
