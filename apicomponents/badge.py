class Badge:

    def get_badgeByname(self, name, version):
        # TODO : follow up on response of this functionality
        """
        Returns current metrics for a specific project

        Args:
            name (string): The name of the project to query on
            version (string): The version of the project to query on

        Returns:
            xml: current metrics of specified object in xml
        """
        response = self.session.get(
            self.apicall + f"/v1/badge/vulns/project/{name}/{version}")
        if response.status_code == 200:
            return response.content
        if response.status_code == 401:
            return (f"Unauthorized, {response.status_code}")
        if response.status_code == 404:
            return (f"The project could not be found, {response.status_code}")
        if response.status_code == 204:
            return (f"Badge support is disabled. No content will be returned, {response.status_code}")
        return ((response.content).decode("utf-8"), response.status_code)

    def get_badgeByuuid(self, uuid):
        # TODO : follow up on response of this functionality
        """
        Returns current metrics for a specific project

        Args:
            uuid: The uuid of the project.

        Returns:
            xml: current metrics of specified object in xml
        """
        response = self.session.get(
            self.apicall + f"/v1/badge/vulns/project/{uuid}")
        if response.status_code == 200:
            return response.content
        if response.status_code == 401:
            return (f"Unauthorized, {response.status_code}")
        if response.status_code == 404:
            return (f"The project could not be found, {response.status_code}")
        if response.status_code == 204:
            return (f"Badge support is disabled. No content will be returned, {response.status_code}")
        return ((response.content).decode("utf-8"), response.status_code)
