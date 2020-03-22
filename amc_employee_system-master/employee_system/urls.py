
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from employee.views import HomePage, EmployeeList, \
EmployeAdd, EmployeDelete, ChatRoom
from employer.views import EmployerList
from job.views import JobList, JobAdd, JobRatingReview

from users.views import Register, Login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage),
    path('employee', EmployeeList),
    path('employer', EmployerList),
    path('employee-add', EmployeAdd),
    path('employee-delete', EmployeDelete),

    path('register/', Register),
    path('login/', Login),

    path('job', JobList),
    path('job-add', JobAdd),

    path('job/rating-review', JobRatingReview),

    path('chat-room', ChatRoom)


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
