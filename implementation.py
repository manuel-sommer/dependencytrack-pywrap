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

    def create_project(self, name, classifier):
        #TODO add more options
        data ={
            "name": name,
            "classifier": classifier
            }
        response = self.session.put(self.apicall + f"/v1/project", json=data)
        if response.status_code == 201:
            return (f"Successfully created the project", response.status_code)
        elif response.status_code == 409:
            return (f"Project with specified name already exists", response.status_code)
        else:
            return (f"Unable to create the project", response.status_code)

    def update_project(self, uuid, name=None, classifier=None):
        #TODO add more options
        data = {
            "uuid": uuid
        }
        if name:
            data['name'] = name
        if classifier:
            data['classifier'] = classifier
        response = self.session.post(self.apicall + f"/v1/project", json=data)
        if response.status_code == 200:
            return (f"Successfully updated the project", response.status_code)
        elif response.status_code == 404:
            return (f"Project with specified uuid could not be found", response.status_code)
        elif response.status_code == 409:
            return (f"Project with specified name already exists", response.status_code)
        else:
            return (f"Unable to update the project", response.status_code)
    #This section is all about vulnerabilities
    
    def get_all_vulnerabilities(self, pageSize = 100):
        vulnerability_list = list()
        pageNumber = 1
        response = self.session.get(self.apicall +f"/v1/vulnerability", params = {'pageSize': pageSize, 'pageNumber': pageNumber})
        for vul in range(0,len(response.json())):
            vulnerability_list.append(response.json()[vul-1])
        while len(response.json()) == pageNumber:
            pageNumber += 1
            response = self.session.get(self.apicall +f"/v1/vulnerability", params = {'pageSize': pageSize, 'pageNumber': pageNumber})
            for vul in range(0,len(response.json())):
                vulnerability_list.append(response.json()[vul - 1])
        if response.status_code == 200:
            return vulnerability_list
        else:
            return (f"Unable to find any vulnerabilities ", response.status_code)

    def get_vulnerability(self,source,vuln,):
        """
        this method returns a specific vulnerability
        source:string(to be filled later)
        vuln:string(to be filled later)
        """
        response = self.session.get(self.apicall +f"/v1/vulnerability/source/{source}/vuln/{vuln}")
        if response.status_code == 200:
            return response.json()
        else:
            if response.status_code == 401:
                return (f"Unauthorized",response.status_code)
            else:
                return (f"The vulnerability could not be found ", response.status_code)
    
    def get_component_vulnerability(self,uuid,supressed=False):
        """ 
        Returns a list of all vulnerabilities for a specific component.
        uuid:
        supprressed: optionally includes supressed vulnerabilities
        """
        response = self.session.get(self.apicall +f"/v1/vulnerability/component/{uuid}?supressed={supressed}")
        if response.status_code == 200:
            return response.json()
        else:
            if response.status_code == 401:
                return (f"Unauthorized", response.status_code)
            elif response.status_code == 403:
                return (f"Access to the specified component is forbidden ", response.status_code)
            else:
                return (f"The component could not be found", response.status_code)
    
    def get_project_vlnerability(self, uuid,supressed=False):
        """ 
        Returns a list of all vulnerabilities for a specific project.
        uuid:
        supprressed: optionally includes supressed vulnerabilities(boolean)
        """
        response = self.session.get(self.apicall +f"/v1/vulnerability/project/{uuid}?supressed={supressed}")
        if response.status_code == 200:
            return response.json()
        else:
            if response.status_code == 401:
                return (f"Unauthorized", response.status_code)
            elif response.status_code == 403:
                return (f"Access to the specified project is forbidden ", response.status_code)
            else:
                return (f"The project could not be found", response.status_code)
    
    def get_vulnerability_uuid(self,uuid):
        """
        returns a specific vulnerability
        uuid: The UUID of the vulnerability 
        """
        response = self.session.get(self.apicall + f"/v1/vulnerability/{uuid}")
        if response.status_code == 200:
            return response.json()
        else:
            if response.status_code == 401:
                return (f"Unauthorized", response.status_code)
            else:
                return (f"The vulnerability could not be found ", response.status_code)

    def get_affected_project(self,source,vuln):
        """ 
        Returns a list of all projects affected by a specific vulnerability
        source:
        vuln:
        """
        response = self.session.get(self.apicall +f"/v1/vulnerability/source/{source}/vuln/{vuln}/projects")
        if response.status_code == 200:
            return response.json()
        else:
            if response.status_code == 401:
                return (f"Unauthorized", response.status_code)
            else:
                return (f"The vulnerability could not be found ", response.status_code)
    #TODO: POST,POST /v1/vulnerability
    #TODO: DELETE, POST  /v1/vulnerability/source/{source}/vuln/{vulnId}/component/{component}, DELETE, POST /v1/vulnerability/{uuid}/component/{component}
    
    #this section is all about findings
    
    def get_project_vlnerability(self, uuid,supressed=False):
        """ 
        Returns a list of all findings for a specific project.
        uuid:
        supprressed: optionally includes supressed vulnerabilities(boolean)
        """
        response = self.session.get(self.apicall +f"/v1/vulnerability/project/{uuid}?supressed={supressed}")
        if response.status_code == 200:
            return response.json()
        else:
            if response.status_code == 401:
                return (f"Unauthorized", response.status_code)
            elif response.status_code == 403:
                return (f"Access to the specified project is forbidden ", response.status_code)
            else:
                return (f"The project could not be found", response.status_code)

    #all about lincese 
    def list_license(self, pageSize = 100):
        license_list=list()
        pageNumber = 1
        response = self.session.get(self.apicall + f"/v1/license", params = {"pageSize": pageSize,"pageNumber": pageNumber})
        for lice in range(0,len(response.json())):
            license_list.append(response.json()[lice-1])
        while len(response.json()) == pageSize:
            pageNumber += 1
            response = self.session.get(self.apicall + f"/v1/license", params = {"pageSize": pageSize, "pageNumber": pageNumber})
            for lice in range(0, len(response.json())):
                license_list.append(response.json()[lice-1])
        if response.status_code == 200:
            return license_list
        else:
            return (f"Unauthorized ", response.status_code)

dt=DependencyTrackAPI("http://localhost:8081","Z0g4jvxF1Yek3R8balySFj5kGahjR3oj")
print(dt.list_license())