from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt

from employee.models import Employee
from employer.models import Employer

from job.models import Job, JobRating
from job.algo import getRecommendation, euclidean_distance

import pandas as pd
# jobs = pd.DataFrame(list(Job.objects.all().values()))
        # ratings = pd.DataFrame(list(
        #     JobRating.objects.all().values(
        #         'job__title', 'user__email', 'rating')
        #     ))

def HomePage(request):
	employee_count = Employee.objects.count()
	employer_count = Employer.objects.count()


	recommended_jobs = []

	rating_job = {
		"ratings": pd.DataFrame(list(
				JobRating.objects.all().values(
					'job__title', 'user__email', 'rating'
					)
			)),
		"jobs":pd.DataFrame(list(Job.objects.all().values()))
	}
	try:
		recommended_jobs = getRecommendation(
				rating_job,
				request.user.email,
				euclidean_distance
			)
	except Exception as ex:
		print(ex)
	#print(recommended_jobs)
	data = {
		"employee_count": employee_count,
		"employer_count": employer_count,
		"recommended_jobs":recommended_jobs
	}
	return render(request, "index.html", data)


def EmployeeList(request):
	employees = Employee.objects.all()
	data = {
		"employees": employees
	}
	return render(request, "employee.html", data)

@csrf_exempt
def EmployeAdd(request):
	data = { 
		"added": False,
		"message":"",
		"employee":None
		}

	if request.method == "POST":
		input_data = request.POST
		print(input_data)

		if "id" in request.GET:

			if request.GET["id"] != "":
				# update
				emp = Employee.objects.get(
						id=request.GET["id"]
						)
				emp.name = input_data["name"]
				emp.email = input_data["email"]
				emp.address = input_data["address"]
				emp.phone = input_data["phone"]
				emp.save()
			
			else:
				# Add 
				emp = Employee.objects.filter(
						email=input_data["email"]
						)
				if emp:
					data["message"] = "The email already exists"
				else:
					emp = Employee(
							name=input_data["name"],
							email=input_data["email"],
							address=input_data["address"],
							phone=input_data["phone"],
						)
					emp.save()
					data["added"] = True

	if "id" in request.GET:
		try:
			data["employee"] = Employee.objects.get(
					id=request.GET["id"]
					)
		except:
			pass
	return render(request, "employee-add.html", data)


def EmployeDelete(request):
	
	id = request.GET["id"]
	emp = Employee.objects.get(id=id)
	emp.delete()
	return redirect("/employee")


def ChatRoom(request):
	data = {
		"room_name": "Job_Chat_Box"
	}
	return render(request, "chat-room.html", data)




