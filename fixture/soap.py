from suds.client import Client
from suds import WebFault
from model.project import Project

class SoapHelper:

    def __init__(self, app):
        self.app = app
        self.client = Client(app.config['web']['baseURL'] + "/api/soap/mantisconnect.php?wsdl")

    def can_login(self, username, password):
        client = self.client
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list(self):
        client = self.client
        list = []
        try:
            projects = client.service.mc_projects_get_user_accessible(
                self.app.config["webadmin"]["username"], self.app.config["webadmin"]["password"])
            for project in projects:
                list.append(Project(id=str(project.id), project_name=project.name))
            return list
        except WebFault:
            return None
