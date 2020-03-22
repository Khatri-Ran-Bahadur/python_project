from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from job.models import Job, JobReview, JobRating


def JobList(request):
    data = {
        "job":None,
        "jobs":[]
    }

    if "id" in request.GET:
        data["job"] = Job.objects.get(
                        id=request.GET["id"]
                        )
        return render(
                request, 
                "job-detail.html", 
                data
                )
    else:
        data["jobs"] = Job.objects.all()
        return render(request, "job.html", data)



@csrf_exempt
def JobAdd(request):
    data = { 
        "added": False,
        "message":"",
        "job":None
        }

    if request.method == "POST":
        input_data = request.POST.copy()
        print(input_data)

        if "id" in request.GET:
            if request.GET["id"] != "":
                pass
            else:
                # Add 
                job = Job.objects.filter(
                        title=input_data["title"]
                        )
                if job:
                    data["message"] = "The job already exists"
                else:
                    input_data["experience_year"] = int(input_data["experience_year"])
                    input_data["salary"] = int(input_data["salary"])
                    print(input_data)
                    job = Job(
                            title=input_data["title"],
                            description=input_data["description"],
                            category=input_data["category"],
                            location=input_data["location"],
                            qualification=input_data["qualification"],
                            experience_year=input_data["experience_year"],
                            salary=input_data["salary"],
                            job_type=input_data["job_type"],
                            deadline=input_data["deadline"],
                            skills=input_data["skills"]
                        )
                    job.save()
                    data["added"] = True
                pass

    if "id" in request.GET:
        try:
            data["job"] = Job.objects.get(
                    id=request.GET["id"]
                    )
        except:
            pass
    return render(request, "job-add.html", data)



def JobRatingReview(request):
    data = {}
    if request.method == "POST":
        input_data = request.POST
        job = Job.objects.get(id=input_data["id"])
        JobRating.objects.get_or_create(
                user_id=request.user.id,
                job_id=job.id,
                defaults={
                    "rating":input_data["rating"]
                }
            )
        JobReview.objects.get_or_create(
                user_id=request.user.id,
                job_id=job.id,
                defaults={
                    "review":input_data["review"]
                }
            )
        data["job"] = job
        return render(request, "job-detail.html", data)

    return render(request, "job.html", data)


