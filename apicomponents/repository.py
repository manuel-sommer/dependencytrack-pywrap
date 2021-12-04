import json
class DependencyTrackRepository(object):
    
    def list_repository(self, pageSize=100):
        """Returns a list of all repositories

        Args:
            pageSize (int, optional): [description]. Defaults to 100.

        Returns:
            List: Returns a list of all repositories.
        """
        respositorylist = list()
        pageNumber = 1
        response = self.session.get(self.apicall + f"/v1/repository", params={'pageSize': pageSize, 'pageNumber': pageNumber})
        for repository in range(0, len(response.json())):
            respositorylist.append(response.json()[repository-1])
        while len(response.json()) == pageSize:
            pageNumber += 1
            response = self.session.get(self.apicall + f"/v1/repository", params={'pageSize': pageSize, 'pageNumber': pageNumber})
            for repository in range(0, len(response.json())):
                respositorylist.append(response.json()[repository-1])
        if response.status_code == 200:
            return respositorylist
        else:
            return (f"{(response.content).decode('utf-8')}, {response.status_code}")
        
    def update_repository(self, uuid, identifier, type, url, resolutionOrder=0, enable=True, internal=True):
        """Update a specific repository

        Args:
            uuid ([type]): [description]
            identifier (string): identity name of the repository
            type (string): The type of repositories to add. eg MAVEN, NPM, GEM, PYPI, NUGET, HEX, COMPOSER, CARGO, GO_MODULES, UNSUPPORTED
            url ([type]): [description]
            resolutionOrder (int, optional): . Defaults to 0.
            enable (bool, optional): . Defaults to True.
            internal (bool, optional): . Defaults to True.

        Returns:
            dictionary : example Value {
                                        "type": "MAVEN",
                                        "identifier": "string",
                                        "url": "string",
                                        "resolutionOrder": 6,
                                        "enabled": true,
                                        "internal": true,
                                        "uuid": "579720aa-e150-4b92-abff-2b6bb5dd7af9"
                                        }
        """
        data = {
            "uuid": uuid,
            "type": type,
            "url": url,
            "resolutionOder": resolutionOrder,
            "enable": enable,
            "internal": internal,
            "identifier": identifier
        }
        response = self.session.post(self.apicall + f"/v1/repository",data=json.dumps(data))
        if response.status_code == 200:
            return ("Successful operation")
        else:
            return (f"{(response.content).decode('utf-8')}, {response.status_code}")
        
    def create_repository(self, identifier, type, url, resolutionOrder=0, enable=True, internal=True):
        """ Create a new repository

        Args:
            identifier (string): identity name of the repository
            type (string): The type of repositories to add. eg MAVEN, NPM, GEM, PYPI, NUGET, HEX, COMPOSER, CARGO, GO_MODULES, UNSUPPORTED
            url ([type]): [description]
            resolutionOrder (int, optional): . Defaults to 0.
            enable (bool, optional): . Defaults to True.
            internal (bool, optional): . Defaults to True.

        Returns:
            dictionary : example Value {
                                        "type": "MAVEN",
                                        "identifier": "string",
                                        "url": "string",
                                        "resolutionOrder": 6,
                                        "enabled": true,
                                        "internal": true,
                                        "uuid": "579720aa-e150-4b92-abff-2b6bb5dd7af9"
                                        }
        """
        data = {
            "type": type,
            "url": url,
            "resolutionOder": resolutionOrder,
            "enable": enable,
            "internal": internal,
            "identifier": identifier
        }
        response = self.session.put(self.apicall + f"/v1/repository", data=json.dumps(data))
        if response.status_code == 201:
            return ("Successful operation")
        else:
            return (f"{(response.content).decode('utf-8')}, {response.status_code}")
        
    def get_latest_repository(self,purl):
        """Attempts to resolve the latest version of the component available in the configured repositories

        Args:
            purl (string): The Package URL for the component to query

        Returns:
            dictionary : example Value{
                            "repositoryType": "MAVEN",
                            "namespace": "string",
                            "name": "string",
                            "latestVersion": "string",
                            "published": "2021-12-02T16:50:56.704Z",
                            "lastCheck": "2021-12-02T16:50:56.704Z"
                            }
        """
        response = self.session.get(self.apicall + f"/v1/repository/latest", params={'purl':purl})
        if response.status_code==200:
            return response.json()
        else:
            return (f"{(response.content).decode('utf-8')}, {response.status_code}")

    def get_repositoryByType(self,type, pageSize=100):
        """
            Returns repositories that support the specific type

        Args:
            type (string): The type of repositories to retrieve. eg MAVEN, NPM, GEM, PYPI, NUGET, HEX, COMPOSER, CARGO, GO_MODULES, UNSUPPORTED  
            pageSize (int, optional): [description]. Defaults to 100.

        Returns:
            List : list of repositories that support the specific type.
        """
        respositorylist = list()
        pageNumber = 1
        response = self.session.get(self.apicall + f"/v1/repository/{type}", params={'pageSize': pageSize, 'pageNumber': pageNumber})
        for repository in range(0, len(response.json())):
            respositorylist.append(response.json()[repository-1])
        while len(response.json()) == pageSize:
            pageNumber += 1
            response = self.session.get(self.apicall + f"/v1/repository/{type}", params={'pageSize': pageSize, 'pageNumber': pageNumber})
            for repository in range(0, len(response.json())):
                respositorylist.append(response.json()[repository-1])
        if response.status_code == 200:
            return respositorylist
        else:
            return (f"{(response.content).decode('utf-8')}, {response.status_code}")
        
    def delete_repository(self, uuid):
        """Deletes a repository

        Args:
            uuid (string): the UUID of the repository to delete
        """
        response = self.session.delete(self.apicall + f"/v1/repository/{uuid}")
        if response.status_code >= 200 or response.status_code <= 299:
            return ("Successful operation")
        else:
            return (f"{(response.content).decode('utf-8')}, {response.status_code}")
