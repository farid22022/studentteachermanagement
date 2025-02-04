from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    
    return HttpResponse('This is the profile page')
def profile(request):
    user_data = {
        "name": "John Doe",
        "age": 30,
    }
    marks = [
        {
            "id": 1,
            "subject": "Maths",
            "marks": 80
        },
        {
            "id": 2,
            "subject": "Science",
            "marks": 70
        },
        {
            "id": 3,
            "subject": "English",
            "marks": 85
        },
        {
            "id": 4,
            "subject": "Biology",
            "marks": 90
        }
    ]
    result = [
        {
            "id": 1,
            "name": "Md. Farid Hossen Rehad",
            "results": [
            { "subject": "Bangla", "marks": 80 },
            { "subject": "English", "marks": 75 },
            { "subject": "Mathematics", "marks": 90 },
            { "subject": "Science", "marks": 85 },
            { "subject": "Social Science", "marks": 78 }
            ],
            "totalMarks": 408,
            "averageMarks": 81.6,
            "grade": "A"
        },
        {
            "id": 2,
            "name": "Tanvir Hasan",
            "results": [
            { "subject": "Bangla", "marks": 85 },
            { "subject": "English", "marks": 88 },
            { "subject": "Mathematics", "marks": 92 },
            { "subject": "Science", "marks": 90 },
            { "subject": "Social Science", "marks": 84 }
            ],
            "totalMarks": 439,
            "averageMarks": 87.8,
            "grade": "A+"
        },
        {
            "id": 3,
            "name": "Nusrat Jahan",
            "results": [
            { "subject": "Bangla", "marks": 78 },
            { "subject": "English", "marks": 82 },
            { "subject": "Mathematics", "marks": 89 },
            { "subject": "Science", "marks": 75 },
            { "subject": "Social Science", "marks": 80 }
            ],
            "totalMarks": 404,
            "averageMarks": 80.8,
            "grade": "A"
        },
        {
            "id": 4,
            "name": "Asif Rahman",
            "results": [
            { "subject": "Bangla", "marks": 65 },
            { "subject": "English", "marks": 70 },
            { "subject": "Mathematics", "marks": 75 },
            { "subject": "Science", "marks": 68 },
            { "subject": "Social Science", "marks": 72 }
            ],
            "totalMarks": 350,
            "averageMarks": 70,
               "grade": "B"
        },
        {
            "id": 5,
            "name": "Fahmida Akter",
            "results": [
            { "subject": "Bangla", "marks": 88 },
            { "subject": "English", "marks": 85 },
            { "subject": "Mathematics", "marks": 90 },
            { "subject": "Science", "marks": 92 },
            { "subject": "Social Science", "marks": 87 }
            ],
            "totalMarks": 442,
            "averageMarks": 88.4,
            "grade": "A+"
        },
        {
            "id": 6,
            "name": "Rahim Uddin",
            "results": [
            { "subject": "Bangla", "marks": 72 },
            { "subject": "English", "marks": 68 },
            { "subject": "Mathematics", "marks": 74 },
            { "subject": "Science", "marks": 70 },
            { "subject": "Social Science", "marks": 75 }
            ],
            "totalMarks": 359,
            "averageMarks": 71.8,
            "grade": "B"
        },
        {
            "id": 7,
            "name": "Samira Hossain",
            "results": [
            { "subject": "Bangla", "marks": 95 },
            { "subject": "English", "marks": 90 },
            { "subject": "Mathematics", "marks": 98 },
            { "subject": "Science", "marks": 92 },
            { "subject": "Social Science", "marks": 96 }
            ],
            "totalMarks": 471,
            "averageMarks": 94.2,
            "grade": "A+"
        },
        {
            "id": 8,
            "name": "Sajib Ahmed",
            "results": [
            { "subject": "Bangla", "marks": 70 },
            { "subject": "English", "marks": 72 },
            { "subject": "Mathematics", "marks": 69 },
            { "subject": "Science", "marks": 75 },
            { "subject": "Social Science", "marks": 68 }
            ],
            "totalMarks": 354,
            "averageMarks": 70.8,
            "grade": "B"
        },
        {
            "id": 9,
            "name": "Tania Islam",
            "results": [
            { "subject": "Bangla", "marks": 85 },
            { "subject": "English", "marks": 88 },
            { "subject": "Mathematics", "marks": 92 },
            { "subject": "Science", "marks": 90 },
            { "subject": "Social Science", "marks": 89 }
            ],
            "totalMarks": 444,
            "averageMarks": 88.8,
            "grade": "A+"
        },
        {
            "id": 10,
            "name": "Hasan Mahmud",
            "results": [
            { "subject": "Bangla", "marks": 77 },
            { "subject": "English", "marks": 80 },
            { "subject": "Mathematics", "marks": 84 },
            { "subject": "Science", "marks": 82 },
            { "subject": "Social Science", "marks": 79 }
            ],
            "totalMarks": 402,
            "averageMarks": 80.4,
            "grade": "A"
        },
        {
            "id": 11,
            "name": "Sohail Rana",
            "results": [
            { "subject": "Bangla", "marks": 88 },
            { "subject": "English", "marks": 86 },
            { "subject": "Mathematics", "marks": 90 },
            { "subject": "Science", "marks": 85 },
            { "subject": "Social Science", "marks": 84 }
            ],
            "totalMarks": 433,
            "averageMarks": 86.6,
            "grade": "A+"
        },
        {
            "id": 12,
            "name": "Mithila Sultana",
            "results": [
            { "subject": "Bangla", "marks": 72 },
            { "subject": "English", "marks": 78 },
            { "subject": "Mathematics", "marks": 85 },
            { "subject": "Science", "marks": 80 },
            { "subject": "Social Science", "marks": 75 }
            ],
            "totalMarks": 390,
            "averageMarks": 78,
               "grade": "B+"
        },
        {
            "id": 13,
            "name": "Mahmudul Hasan",
            "results": [
            { "subject": "Bangla", "marks": 75 },
            { "subject": "English", "marks": 72 },
            { "subject": "Mathematics", "marks": 78 },
            { "subject": "Science", "marks": 80 },
            { "subject": "Social Science", "marks": 82 }
            ],
            "totalMarks": 387,
            "averageMarks": 77.4,
            "grade": "B+"
        },
        {
            "id": 14,
            "name": "Raihan Kabir",
            "results": [
            { "subject": "Bangla", "marks": 70 },
            { "subject": "English", "marks": 65 },
            { "subject": "Mathematics", "marks": 75 },
            { "subject": "Science", "marks": 72 },
            { "subject": "Social Science", "marks": 74 }
            ],
            "totalMarks": 356,
            "averageMarks": 71.2,
            "grade": "B"
        },
        {
            "id": 15,
            "name": "Tanjina Akter",
            "results": [
            { "subject": "Bangla", "marks": 82 },
            { "subject": "English", "marks": 88 },
            { "subject": "Mathematics", "marks": 92 },
            { "subject": "Science", "marks": 85 },
            { "subject": "Social Science", "marks": 83 }
            ],
            "totalMarks": 430,
            "averageMarks": 86,
               "grade": "A+"
        },
        {
            "id": 16,
            "name": "Nahid Alam",
            "results": [
            { "subject": "Bangla", "marks": 75 },
            { "subject": "English", "marks": 70 },
            { "subject": "Mathematics", "marks": 77 },
            { "subject": "Science", "marks": 72 },
            { "subject": "Social Science", "marks": 79 }
            ],
            "totalMarks": 373,
            "averageMarks": 74.6,
            "grade": "B+"
        },
        ]

    return render(request, 'student/index.html', {"result": result})
