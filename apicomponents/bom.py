class DependencyTrackBom(object):
    # bom API
    def get_bom_token(self,uuid):
        """
        Determines if there are any tasks associated with the token that are being processed, or in the queue to be processed.
        This endpoint is intended to be used in conjunction with uploading a supported BOM document. Upon upload, a token will be returned. The token can then be queried using this endpoint to determine if any tasks (such as vulnerability analysis) is being performed on the BOM. A value of true indicates processing is occurring. A value of false indicates that no processing is occurring for the specified token. However, a value of false also does not confirm the token is valid, only that no processing is associated with the specified token.


        Args:
            uuid (string): The UUID of the token to query
        """
        response = self.session.get(self.apicall + f"/v1/bom/token/{uuid}")
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            return (f"Unauthorized ", response.status_code)
        else:
            return response.status_code
    
    def get_bom_project(self,uuid,format="json"):
        """Returns dependency metadata for a project in CycloneDX format

        Args:
            uuid (string): The UUID of the project to export
            format (str, optional): . Defaults to "json". However by default API is xml

        Returns:
            xml or json: returns dependency metadata for a project in CycloneDX format in xml or json
        """
        response = self.session.get(self.apicall + f"/v1/bom/cyclonedx/project/{uuid}",params={"format":format})
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            return (f"Unauthorized ", response.status_code)
        elif response.status_code == 403:
            return (f"Access to the specified project is forbidden", response.status_code)
        elif response.status_code == 404:
            return (f"Project not found", response.status_code)
        else:
            return (response.status_code)
    
    def get_bom_component(self,uuid,format="json"):
        """Returns dependency metadata for a component in CycloneDX format

        Args:
            uuid (string): The UUID of the component to export
            format (str, optional): . Defaults to "json". However by default API is xml

        Returns:
            xml or json: returns dependency metadata for a component in CycloneDX format in xml or json
        """
        response = self.session.get(self.apicall + f"/v1/bom/cyclonedx/component/{uuid}",params={"format":format})
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            return (f"Unauthorized ", response.status_code)
        elif response.status_code == 403:
            return (f"Access to the specified component is forbidden", response.status_code)
        elif response.status_code == 404:
            return (f"Component not found", response.status_code)
        else:
            return (response.status_code)
    
    def post_bom(self, project, projectName, projectVersion, body, autoCreate=True):
        #TODO: refactor for formadata
        """Upload a supported bill of material format document. Expects CycloneDX along and a valid project UUID. If a UUID is not specified then the projectName and projectVersion must be specified. Optionally, if autoCreate is specified and ‘true’ and the project does not exist, the project will be created. In this scenario, the principal making the request will additionally need the PORTFOLIO_MANAGEMENT or PROJECT_CREATION_UPLOAD permission.

        Args:
            project (string[formData]): project
            projectName (string[formData]): project name
            projectVersion ([type]): [description]
            body (json): BOM data
            autoCreate (bool, optional): create project if it does not exist", response". Defaults to True.

        Returns:
            response status code
        """
        data=dict()
        data["project"] = project
        data["projectName"] = projectName
        data["projectVersion"] = projectVersion
        data["body"] =body
        data["autoCreate"] = autoCreate
        response = self.session.post(self.apicall + f"/v1/bom", files=body)
        if response.status_code == 200:
            return (f"successful operation")
        elif response.status_code == 401:
            return (f"Unauthorized ", response.status_code)
        elif response.status_code == 403:
            return (f"Access to the specified project is forbidden", response.status_code)
        elif response.status_code == 404:
            return (f"Project not found", response.status_code)
        else:
            return (response.status_code)
        
    def put_bom(self, project, body):
        """Upload a supported bill of material format document. Expects CycloneDX along and a valid project UUID. If a UUID is not specified then the projectName and projectVersion must be specified. Optionally, if autoCreate is specified and ‘true’ and the project does not exist, the project will be created. In this scenario, the principal making the request will additionally need the PORTFOLIO_MANAGEMENT or PROJECT_CREATION_UPLOAD permission.

        Args:
            project (string): The UUID of the project
            body (json): BOM data
            autoCreate (bool, optional): create project if it does not exist", response". Defaults to True.

        Returns:
            response status code
        """
        data=dict()
        data["project"]=project
        data["bom"]=base64.b64encode(json.dumps(body).encode("utf-8")).decode("utf-8")
        response = self.session.put(
            self.apicall + f"/v1/bom", data=json.dumps(data))
        if response.status_code == 200:
            return (f"successful operation")
        elif response.status_code == 401:
            return (f"Unauthorized ", response.status_code)
        elif response.status_code == 403:
            return (f"Access to the specified project is forbidden", response.status_code)
        elif response.status_code == 404:
            return (f"Project not found", response.status_code)
        else:
            return (response.status_code)