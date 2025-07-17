# views.py
from django.shortcuts import render, redirect
from .models import Report
from .forms import ReportForm

def submit_report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user
            report.save()
            
    else:
        form = ReportForm()
    return render(request, 'reports/submit_report.html', {'form': form})

def view_reports(request):
    reports = Report.objects.all().order_by('-created_at')
    return render(request, 'reports/view_report.html', {'reports': reports})

# views.py
from django.shortcuts import redirect, get_object_or_404
from .models import Report

def mark_report_done(request, report_id):
    report = get_object_or_404(Report, id=report_id)
    report.is_done = True
    report.save()
    return redirect('view_reports')  # Redirect back to the reports list

