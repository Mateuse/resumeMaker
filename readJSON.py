import json
from resume import Resume

def load_resume_from_json(json_data):
    return Resume(**json_data)

def load_json(json_file):
    with open(json_file, 'r') as f: 
        data = json.load(f)

    resume = load_resume_from_json(data)

    return {
        'name': resume.name,
        'email': resume.email,
        'phone': resume.phoneNumber,
        'website': resume.website,
        'github': resume.website,
        'employment': resume.employment,
        'projects': resume.projects,
        'skills': resume.skills
    }