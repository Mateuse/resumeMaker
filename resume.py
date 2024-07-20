class Employment:
    def __init__(self, company, position, location, startDate, endDate, highlights):
        self.company = company
        self.position = position
        self.location = location
        self.startDate = startDate
        self.endDate = endDate
        self.highlights = highlights

class Project:
    def __init__(self, technologies, name, description, website):
        self.technologies = technologies
        self.name = name
        self.description = description
        self.website = website

class Skill:
    def __init__(self, name, items):
        self.name = name
        self.items = items

class Resume:
    def __init__(self, name, phoneNumber, email, website, github, employment, projects, skills):
        self.name = name
        self.phoneNumber = phoneNumber
        self.email = email
        self.website = website
        self.github = github
        self.employment = [Employment(**emp) for emp in employment]
        self.projects = [Project(**proj) for proj in projects]
        self.skills = [Skill(**skill) for skill in skills]
