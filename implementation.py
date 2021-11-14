import requests

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

    def get_uuid_from_projectname(self, projectname):
        uuid=None
        json = self.list_projects()
        for iterator in json:
            if iterator['name']==projectname:
                uuid = iterator['uuid']
                break
        return uuid
