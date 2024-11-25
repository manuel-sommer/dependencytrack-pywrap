class Search:

    def general_search(self, query=None):
        if query:
            response = self.session.get(self.apicall + "/v1/search", params={"query": query})
        else:
            response = self.session.get(self.apicall + "/v1/search")
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            return (f"Unauthorized, {response.status_code}")
        return (f"{(response.content).decode('utf-8')}, {response.status_code}")

    def project_search(self, query=None):
        if query:
            response = self.session.get(self.apicall + "/v1/search/project", params={"query": query})
        else:
            response = self.session.get(self.apicall + "/v1/search/project")
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            return (f"Unauthorized, {response.status_code}")
        return (f"{(response.content).decode('utf-8')}, {response.status_code}")

    def component_search(self, query=None):
        if query:
            response = self.session.get(self.apicall + "/v1/search/component", params={"query": query})
        else:
            response = self.session.get(self.apicall + "/v1/search/component")
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            return (f"Unauthorized, {response.status_code}")
        return (f"{(response.content).decode('utf-8')}, {response.status_code}")

    def service_search(self, query=None):
        if query:
            response = self.session.get(self.apicall + "/v1/search/service", params={"query": query})
        else:
            response = self.session.get(self.apicall + "/v1/search/service")
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            return (f"Unauthorized, {response.status_code}")
        return (f"{(response.content).decode('utf-8')}, {response.status_code}")

    def license_search(self, query=None):
        if query:
            response = self.session.get(self.apicall + "/v1/search/license", params={"query": query})
        else:
            response = self.session.get(self.apicall + "/v1/search/license")
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            return (f"Unauthorized, {response.status_code}")
        return (f"{(response.content).decode('utf-8')}, {response.status_code}")

    def vulnerability_search(self, query=None):
        if query:
            response = self.session.get(self.apicall + "/v1/search/vulnerability", params={"query": query})
        else:
            response = self.session.get(self.apicall + "/v1/search/vulnerability")
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            return (f"Unauthorized, {response.status_code}")
        return (f"{(response.content).decode('utf-8')}, {response.status_code}")
