import requests
import json

class DependencyTrackAPI(object):
    def __init__(self, apiurl, apikey):
        self.apiurl = apiurl
        self.apikey = apikey
        self.apicall = self.apiurl + "/api"
        self.session = requests.Session()
        self.session.headers.update({"X-Api-Key": f"{self.apikey}"})

    def version(self):
        response = self.session.get(self.apicall + "/version")
        return response.json()

    def list_projects(self, pageSize = 100):
        projectlist = list()
        pageNumber = 1
        response = self.session.get(self.apicall + "/v1/project", params={'pageSize': pageSize, 'pageNumber': pageNumber})
        for project in range(0,len(response.json())):
            projectlist.append(response.json()[project-1])
        while len(response.json()) == pageSize:
            pageNumber += 1
            response = self.session.get(self.apicall + "/v1/project", params={'pageSize': pageSize, 'pageNumber': pageNumber})
            for project in range(0,len(response.json())):
                projectlist.append(response.json()[project-1])
        if response.status_code == 200:
            return projectlist
        else:
            return (f"Unable to list projects", response.status_code)

    def get_project(self, uuid):
        response = self.session.get(self.apicall + f"/v1/project/{uuid}/")
        if response.status_code == 200:
            return response.json()
        else:
            return (f"Unable to find project", response.status_code)

    def get_project_lookup(self, name, version=None):
        if version == None:
            lookup = "name=" + name
        else:
            lookup = "name=" + name +"&version="+version
        response = self.session.get(self.apicall + f"/v1/project/lookup?{lookup}")
        if response.status_code==200:
            return response.json()
        else:
            return (f"Unable to find project", response.status_code)

    def delete_project_uuid(self, uuid):
        response = self.session.delete(self.apicall + f"/v1/project/{uuid}/")
        if response.status_code ==204:
            return (f"Successfully deleted the project", response.status_code)
        else:
            return (f"Unable to delete the project", response.status_code)

    def create_project(self, name):
        data ={
            "name": name,
            "classifier": "APPLICATION"
            }
        response = self.session.put(self.apicall + f"/v1/project", json=data)
        if response.status_code == 201:
            return (f"Successfully created the project", response.status_code)
        elif response.status_code == 409:
            return (f"Project with specified name already exists", response.status_code)
        else:
            return (f"Unable to create the project", response.status_code)
