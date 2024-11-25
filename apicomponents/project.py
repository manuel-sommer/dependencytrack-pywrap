class Project:
    def list_projects(self, pageSize=100):
        projectlist = list()
        pageNumber = 1
        response = self.session.get(
            self.apicall + "/v1/project", params={"pageSize": pageSize, "pageNumber": pageNumber})
        for project in range(len(response.json())):
            projectlist.append(response.json()[project - 1])
        while len(response.json()) == pageSize:
            pageNumber += 1
            response = self.session.get(
                self.apicall + "/v1/project", params={"pageSize": pageSize, "pageNumber": pageNumber})
            for project in range(len(response.json())):
                projectlist.append(response.json()[project - 1])
        if response.status_code == 200:
            return projectlist
        return ("Unable to list projects", response.status_code)

    def get_project(self, uuid):
        response = self.session.get(self.apicall + f"/v1/project/{uuid}")
        if response.status_code == 200:
            return response.json()
        return ("Unable to find project", response.status_code)

    def get_project_lookup(self, name, version=None):
        if version is None:
            lookup = "name=" + name
        else:
            lookup = "name=" + name + "&version=" + version
        response = self.session.get(
            self.apicall + f"/v1/project/lookup?{lookup}")
        if response.status_code == 200:
            return response.json()
        return ("Unable to find project", response.status_code)

    def delete_project_uuid(self, uuid):
        response = self.session.delete(self.apicall + f"/v1/project/{uuid}")
        if response.status_code == 204:
            return ("Successfully deleted the project", response.status_code)
        return ("Unable to delete the project", response.status_code)

    def create_project(self, name, classifier, version, active=True):
        # TODO add more options
        data = {
            "name": name,
            "classifier": classifier,
            "version": version,
            "active": active,
        }
        response = self.session.put(self.apicall + "/v1/project", json=data)
        if response.status_code == 201:
            print("Successfully created the project", response.status_code)
            return response.json()
        if response.status_code == 409:
            return ("Project with specified name already exists", response.status_code)
        return ("Unable to create the project", response.status_code)

    def update_project(self, uuid, name=None, classifier=None):
        # TODO add more options
        data = {
            "uuid": uuid,
        }
        if name:
            data["name"] = name
        if classifier:
            data["classifier"] = classifier
        response = self.session.post(self.apicall + "/v1/project", json=data)
        if response.status_code == 200:
            return ("Successfully updated the project", response.status_code)
        if response.status_code == 404:
            return ("Project with specified uuid could not be found", response.status_code)
        if response.status_code == 409:
            return ("Project with specified name already exists", response.status_code)
        return ("Unable to update the project", response.status_code)
