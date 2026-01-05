from django.shortcuts import render
from django.core.cache import cache
from .models import Project

def index(request):
    # Attempt to get projects from cache for high performance (Load Balancing ready)
    projects = cache.get('portfolio_projects_list')
    
    if not projects:
        # Check database
        projects = list(Project.objects.all())
        
        # If database is empty, use your provided hardcoded data
        if not projects:
            projects = [
                {
                    'title': "The Continental",
                    'description': 'This is an ongoing project built on Next JS. Reflecting on John Wick movies.',
                    'github_url': "https://github.com/munene-martin/The-Continental.git",
                    'technologies_list': ['Next JS', "Typescript", "Tailwind CSS"]
                },
                {
                    'title': 'asdf (Also Called Quagmire Cleaning Services)',
                    'description': 'Just A Cleaning Company Based on Glenn Quagmire from Family Guy.',
                    'github_url': "https://github.com/munene-martin/asdf.git",
                    'technologies_list': ['Typescript', "Next JS", "Tailwind CSS"]
                }, # Added missing comma
                {
                    'title': 'Stock Pred',
                    'description': 'This is a stock prediction application built with Django and React.',
                    'github_url': "https://github.com/munene-martin/stock-pred.git",
                    'technologies_list': ['Django', "Python", "Bootstrap", "React JS"]
                }, # Added missing comma
                {
                    'title': 'OCR_fastapi',
                    'description': 'A Project Showcasing how OCR Can be applied in document management and digitization.',
                    'github_url': "https://github.com/munene-martin/OCR_fastapi.git",
                    'technologies_list': ['FastAPI', "Python", "HTML", "CSS","Jinja2"]
                }, # Added missing comma
                {
                    'title': 'SimpleSTK',
                    'description': 'A simple mpesa daraja simulation showing how payments can be done using mpesa daraja api.',
                    'github_url': "https://github.com/munene-martin/simple-stk-.git",
                    'technologies_list': ['FastAPI', "Python", "HTML", "CSS","Bootstrap"]
                }, # Added missing comma
                {
                    'title': 'Karatasi Digital',
                    'description': 'One of My best projects that involves building a document management system for a local firm in Kenya.',
                    'github_url': "https://github.com/munene-martin/Karatasi-Digital.git",
                    'technologies_list': ['Django', "Python", "HTML", "CSS","Bootstrap", "Daraja API"]
                }, # Added missing comma
                {
                    'title': 'Legal Pro',
                    'description': 'Its still under development but It entails the application of AI in document management.',
                    'github_url': "https://github.com/munene-martin/legal_pro.git",
                    'technologies_list': ['Django', "Python", "HTML", "CSS","Bootstrap"]
                }
            ]
        
        # Store in cache for 24 hours (86400 seconds)
        cache.set('portfolio_projects_list', projects, 86400)
        
    return render(request, 'index.html', {'projects': projects})