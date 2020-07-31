from django.shortcuts import render


def ecommerce_report_page(request):
   return render(request, 'retail_report.html', {})

# Create your views here.
