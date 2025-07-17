# urls.py
from django.urls import path
from .views import submit_report, view_reports
from .views import mark_report_done

urlpatterns = [
    path('submit-report/', submit_report, name='submit_report'),
    path('view-reports/', view_reports, name='view_reports'),
    path('report/done/<int:report_id>/', mark_report_done, name='mark_report_done'),
]
