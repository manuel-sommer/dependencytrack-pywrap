class DependencyTrackConfigProperty(object):
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