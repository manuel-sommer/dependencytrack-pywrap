import requests


class DependencyTrackAPI(object):
    def __init__(self, apiurl, apikey):
        self.apiurl = apiurl
        self.apikey = apikey
        self.apicall = self.apiurl + "/api"
        self.session = requests.Session()
        self.session.headers.update({"X-Api-Key": f"{self.apikey}"})
        self.session.headers.update({"Content-Type": "application/json"})

    def version(self):
        response = self.session.get(self.apicall + "/version")
        return response.json()

   
   

  

   

  

    

# TODO: user API

# TODO: violationanalysis API

# TODO: team API

# TODO: service API

# TODO: default API

# TODO: search API

# Repository API
    def get_repository(self, pageSize=100):
        """Returns a list of all repositories

        Args:
            pageSize (int, optional): [description]. Defaults to 100.

        Returns:
            list : list of repositories
        """
        repository_list = list()
        pageNumber = 1
        response = self.session.get(self.apicall + f"/v1/repository", params={"pageSize": pageSize, "pageNumber": pageNumber})
        for repos in range(0,len(response.json)):
            repository_list.append(response.json()[repos-1])
        while len(response.json()) == pageSize:
            pageNumber += 1
        response = self.session.get(
            self.apicall + f"/v1/repository", params={"pageSize": pageSize, "pageNumber": pageNumber})
        for repos in range(0, len(response.json)):
            repository_list.append(response.json()[repos-1])
        if response.status_code == 200:
            return repository_list
        elif response.status_code == 401:
                return (f"Unauthorized ", response.status_code)
    
# TODO: violation API

# TODO: policy API

# TODO: policyCondition API

# TODO: permission API

# TODO: oidc API

# TODO: licenseGroup API

# TODO: ladp API

    #cwe API

    def get_cwe(self,pageSize=100):
        """Returns a list of all CWEs

        Args:
            pageSize (int, optional): size of the page. Defaults to 100.

        Returns:
            JSON: json object 
        """
        cwe_list= list()
        pageNumber = 1
        response = self.session.get(self.apicall + f"/v1/cwe",params={"pageSize":pageSize, "pageNumber": pageNumber})
        for cwe in range(0,len(response.json())):
            cwe_list.append(response.json()[cwe-1])
        while len(response.json())== pageSize:
            pageNumber += 1
            response = self.session.get(self.apicall + f"/v1/cwe", params={"pageSize": pageSize, "pageNumber": pageNumber})
            for cwe in range(0, len(response.json())):
                cwe_list.append(response.json()[cwe - 1])
        if response.status_code == 200:
            return cwe_list
        elif response.status_code == 401:
            return (f"Unauthorized ", response.status_code)
        else:
            return response.status_code
        
    def get_cweById(self,cweId):
        """ Returns a specific CWE

        Args:
            cweId (int32): The CWE ID of the CWE to retrieve

        Returns:
            JSON: {
                    "cweId": 0,
                    "name": "string"
                    }
        """
        response = self.session.get(self.apicall + f"/v1/cwe/{cweId}")
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            return (f"Unauthorized ", response.status_code)
        elif response.status_code == 404:
            return (f"The CWE could not be found ", response.status_code)
        else:
            return response.status_code
        
    #configProperty API
    
    def get_configProperty(self, pageSize=100):
        """
        Returns a list of all ConfigProperties for the specified groupName

        Returns:
            list: list of all configProperty in json
        """
        config_list=list()
        pageNumber = 1
        response = self.session.get(self.apicall + f"/v1/configProperty",params={"pageSize":pageSize,"pageNumber":pageNumber})
        for config in range(0,len(response.json())):
            config_list.append(response.json()[config]-1)
        while len(response.json())==pageSize:
            pageNumber += 1
            response = self.session.get(self.apicall + f"/v1/configProperty", params={
                                        "pageSize": pageSize, "pageNumber": pageNumber})
            for config in range(0, len(response.json())):
                config_list.append(response.json()[config] - 1)
        if response.status_code == 200:
            return config_list
        elif response.status_code == 401:
            return (f"Unauthorized ", response.status_code)
        else:
            return (response.status_code)
        
    def post_configProperty(self,body):
        """Update a config property

        Args:
            body (JSON): {
                            "groupName": "string",
                            "propertyName": "string",
                            "propertyValue": "string",
                            "propertyType": "BOOLEAN",
                            "description": "string"
                            }

        Returns:
            JSON: Json object which was sent successful
        """
        response = self.session.post(self.apicall + f"/v1/configProperty",data=body)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            return (f"Unauthorized ", response.status_code)
        elif response.status_code == 404:
            return (f"The config property could not be found ", response.status_code)
        else:
            return response.status_code
    
    def post_configPropertyAgregate(self, body):
        """Update a config property

        Args:
            body (JSON): {
                            "groupName": "string",
                            "propertyName": "string",
                            "propertyValue": "string",
                            "propertyType": "BOOLEAN",
                            "description": "string"
                            }

        Returns:
            JSON: Json object which was sent successful
        """
        data=[body]
        response = self.session.post(
            self.apicall + f"/v1/configProperty", data=data)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            return (f"Unauthorized ", response.status_code)
        elif response.status_code == 404:
            return (f"One or more config properties could not be found ", response.status_code)
        else:
            return response.status_code
        
# TODO: component API

# TODO: calculator API

    
        


# TODO: badge API
