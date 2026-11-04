from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View

# Create your views here.


class Aboutyou(View):
    def get(self, request):
        data = {
            "id": "1",
            "full_name": "Jorbin Mathew",
            "title": "Python Full Stack Developer",
            "bio": "BCA graduate currently learning Python Full Stack Development with Django, MySQL, HTML, CSS and JavaScript.",
            "email": "jorbinmathew@gmail.com",
            "mobile": "+91 9876543210",
            "linkedInURL": "https://www.linkedin.com/in/jorbinmathew/",
            "GitHubURL": "https://github.com/jorbinmathew"
        }

        return JsonResponse(data)

class education(View):
    def get(self,request):
       data = {
            'id': '1',
            'institution': 'Devagiri College',
            'university': 'University of Calicut',
            'location': 'Kozhikode, Kerala',
            'qualification': 'Bachelor of Computer Applications (BCA)',
            'start_date': '2023',
            'end_date': '2026',
            'grade_or_cgpa': '7.0 CGPA',
            'description': 'Completed a Bachelor of Computer Applications with a focus on computer science, programming, databases, and software development.'
        }
       return JsonResponse(data)




class project(View):
    def get(self, request):
        data = [
            {
                "id": "1",
                "title": "Tap2Eat",
                "short_description": "Smart college canteen ordering and delivery system.",
                "long_description": "A mobile-based platform for pre-ordering food from college canteens with pickup and delivery options.",
                "technologies_used": [
                    "Flutter",
                    "Firebase",
                    "Cloud Firestore"
                ],
                "live_url": "https://tap2eat-demo.example.com",
                "github_url": "https://github.com/example/tap2eat",
                "image_url": "https://images.example.com/tap2eat.jpg",
                "featured": True
            },
            {
                "id": "2",
                "title": "Blood Donor Management System",
                "short_description": "CRUD application for managing blood donor records.",
                "long_description": "A Python and MySQL based application for adding, viewing, updating, and deleting blood donor information.",
                "technologies_used": [
                    "Python",
                    "MySQL",
                    "Streamlit"
                ],
                "live_url": "https://blood-donor-demo.example.com",
                "github_url": "https://github.com/example/blood-donor-management",
                "image_url": "https://images.example.com/blood-donor.jpg",
                "featured": False
            },
            {
                "id": "3",
                "title": "Gym Management System",
                "short_description": "A system for managing gym members, plans, fees, and joining details.",
                "long_description": "A Python and MySQL based CRUD application that allows gym administrators to add, view, update, and delete member records, manage membership plans, and track fees and joining dates.",
                "technologies_used": [
                    "Python",
                    "MySQL"
                ],
                "live_url": "https://gym-management-demo.example.com",
                "github_url": "https://github.com/example/gym-management-system",
                "image_url": "https://images.example.com/gym-management.jpg",
                "featured": False
            }
        ]

        return JsonResponse(data, safe=False)
class skills(View):
    def get(self, request):
        data = [
            {
                "id": "1",
                "name": "Python",
                "category": "Programming Language",
                "level": "Intermediate",
                "description": "Used for backend development, automation, and database applications."
            },
            {
                "id": "2",
                "name": "Django",
                "category": "Backend Framework",
                "level": "Beginner",
                "description": "Used for developing web applications and REST APIs."
            },
            {
                "id": "3",
                "name": "MySQL",
                "category": "Database",
                "level": "Intermediate",
                "description": "Used for storing and managing application data."
            },
            {
                "id": "4",
                "name": "HTML",
                "category": "Frontend",
                "level": "Intermediate",
                "description": "Used for creating the structure of web pages."
            },
            {
                "id": "5",
                "name": "CSS",
                "category": "Frontend",
                "level": "Intermediate",
                "description": "Used for styling and designing web pages."
            },
            {
                "id": "6",
                "name": "Bootstrap",
                "category": "Frontend Framework",
                "level": "Intermediate",
                "description": "Used for creating responsive and modern web interfaces."
            },
            {
                "id": "7",
                "name": "Git & GitHub",
                "category": "Tools",
                "level": "Intermediate",
                "description": "Used for version control and managing source code."
            },
            {
                "id": "8",
                "name": "Flutter",
                "category": "Mobile Development",
                "level": "Beginner",
                "description": "Used for building cross-platform mobile applications."
            }
        ]

        return JsonResponse(data, safe=False)




class certificates(View):
    def get(self, request):
        data = [
            {
                "id": "1",
                "certificate_name": "Python Full Stack Development",
                "description": "Comprehensive training in Python, Django, HTML, CSS, Bootstrap, MySQL, and web development.",
                "duration": "6 Months",
                "year": "2026"
            },
            {
                "id": "2",
                "certificate_name": "Python Programming",
                "description": "Covered Python basics, functions, OOP, file handling, and database connectivity.",
                "duration": "2 Months",
                "year": "2025"
            },
            {
                "id": "3",
                "certificate_name": "Git & GitHub",
                "description": "Learned version control, repositories, commits, branches, and GitHub workflow.",
                "duration": "1 Month",
                "year": "2026"
            }
        ]

        return JsonResponse(data, safe=False)

class StudentView(View):
    def get(self, request):
        data = {
            "Name": "Anu",
            "Course": "Python Django",
            "Batch": "June 2026",
            "Institution": "Luminar Technolab",
            "joining_year": 2026,
            "joining_month": "May",
            "Location": "Kochi",
            "Mobile": 8976543210,
            "DOB": "20/08/2000"
        }

        return JsonResponse(data)