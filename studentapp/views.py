from django.shortcuts import render, redirect,get_object_or_404
from .models import Student 
from django.http import HttpRequest, JsonResponse

def main_menu(request: HttpRequest):
    return render(request, 'studentapp/index.html')

def add_student(request):
    if request.method == 'POST':
        # Get data from the form
        name = request.POST['name']
        maths_score = int(request.POST['maths_score'])
        physics_score = int(request.POST['physics_score'])
        computer_score = int(request.POST['computer_score'])
        
        # Save to database
        student = Student.objects.create(name=name, maths_score=maths_score, physics_score=physics_score, computer_score=computer_score)
        
        return render(request, 'studentapp/create.html', {'success': True, 'message': 'Student added successfully!'})
    else:
        return render(request, 'studentapp/create.html')

def retrieve_student(request):
    students = Student.objects.all()
    return render(request, 'studentapp/retrieve.html', {'students': students})

def update_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        # Get updated data from the form
        student.name = request.POST['name']
        student.maths_score = int(request.POST['maths_score'])
        student.physics_score = int(request.POST['physics_score'])
        student.computer_score = int(request.POST['computer_score'])
        
        # Save the updated student object
        student.save()
        return redirect('retrieve_student')
    else:
        return render(request, 'studentapp/update.html', {'student': student})
    
def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return redirect('retrieve_student')
 
def search_student_by_id(request):
    student = None
    not_found = False

    if request.method == 'POST':
        student_id = request.POST.get('id')
        try:
            student = Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            not_found = True

    return render(request, 'studentapp/search_by_id.html', {'student': student, 'not_found': not_found})

def search_student_by_name(request):
    students = None  # Default value
    if request.method == 'POST':
        name = request.POST['name']
        students = Student.objects.filter(name__icontains=name)
    return render(request, 'studentapp/search_by_name.html', {'students': students})

def highest_score_student(request):
    student = Student.objects.order_by('-total_score').first()
    return render(request, 'studentapp/highest_score.html', {'student': student})