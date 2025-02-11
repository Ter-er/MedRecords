from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Patient  # Assuming you want to search the Patient model


def search_patients(request):
    # Default value for search results
    results = []
    
    if request.method == 'POST':
        search_type = request.POST.get('searchType')
        search_value = request.POST.get('searchValue')

        # Construct search query based on the search_type
        if search_type and search_value:
            if search_type == 'name':  # Search by name
                results = Patient.objects.filter(first_name__icontains=search_value) | Patient.objects.filter(last_name__icontains=search_value)
            elif search_type == 'id':  # Search by ID
                results = Patient.objects.filter(national_id__icontains=search_value)
            elif search_type == 'email':  # Search by email
                results = Patient.objects.filter(email__icontains=search_value)
            # Add more conditions here for other search types if needed

        # If no search query, show all patients (for example)
        if not results:
            results = Patient.objects.all()
        
        # Paginate the results (10 per page)
        paginator = Paginator(results, 10)
        page_number = request.GET.get('page', 1)  # Default to page 1
        page_obj = paginator.get_page(page_number)

        return render(request, 'search.html', {
            'results': page_obj.object_list,
            'has_previous': page_obj.has_previous(),
            'has_next': page_obj.has_next(),
            'previous_page_number': page_obj.previous_page_number() if page_obj.has_previous() else None,
            'next_page_number': page_obj.next_page_number() if page_obj.has_next() else None,
            'current_page': page_obj.number,
            'page_range': range(1, paginator.num_pages + 1),
            'search_type': search_type,  # To retain the search type in the form
            'search_value': search_value,  # To retain the search value in the form
        })
    
    return render(request, 'search.html')




def search_patients1(request):
    # Default value for search results
    results = []
    
    if request.method == 'POST':
        search_type = request.POST.get('searchType')
        search_value = request.POST.get('searchValue')

        # Construct search query based on the search_type
        if search_type and search_value:
            if search_type == 'name':  # Search by name
                results = Patient.objects.filter(first_name__icontains=search_value) | Patient.objects.filter(last_name__icontains=search_value)
            elif search_type == 'id':  # Search by ID
                results = Patient.objects.filter(national_id__icontains=search_value)
            elif search_type == 'email':  # Search by email
                results = Patient.objects.filter(email__icontains=search_value)
            # Add more conditions here for other search types if needed

        # If no search query, show all patients (for example)
        if not results:
            results = Patient.objects.all()
        
        # Paginate the results (10 per page)
        paginator = Paginator(results, 10)
        page_number = request.GET.get('page', 1)  # Default to page 1
        page_obj = paginator.get_page(page_number)

        return render(request, 'search1.html', {
            'results': page_obj.object_list,
            'has_previous': page_obj.has_previous(),
            'has_next': page_obj.has_next(),
            'previous_page_number': page_obj.previous_page_number() if page_obj.has_previous() else None,
            'next_page_number': page_obj.next_page_number() if page_obj.has_next() else None,
            'current_page': page_obj.number,
            'page_range': range(1, paginator.num_pages + 1),
            'search_type': search_type,  # To retain the search type in the form
            'search_value': search_value,  # To retain the search value in the form
        })
    
    return render(request, 'search1.html')


def dashboard(request):
    # patient = get_object_or_404(Patient, id=patient_id)
    return render(request, 'dashboard.html')
