from _datetime import datetime

from django.http import HttpResponse, JsonResponse, HttpResponseForbidden

from main.helpers import suggest_bundle
from .models import User, Goal
from rest_framework.views import APIView


class GoalView(APIView):

    def get(self, request):
        # HASURA API CALLS
        pass

    def post(self, request):

        _type = request.data["_type"]
        amount = float(request.data["amount"])
        investment_amount = float(request.data["investment_amount"])
        target_date = datetime.strptime(request.data["target_date"], "%d-%m-%Y").date() #dd-mm-YYYY
        diff_years = (target_date - datetime.today().date()).days // 365
        print(diff_years)
        b_alloc, t_alloc = suggest_bundle(diff_years, investment_amount, amount)

        return JsonResponse(
            {
                "bundle": {
                    "returns": "8.5",
                    "b_alloc": b_alloc,
                    "t_alloc": t_alloc,
                    "maturity_period": diff_years
                }
            }
        )
