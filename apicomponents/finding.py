class Finding(object):

    def get_project_finding(self, uuid, suppressed=False, pageSize=100):
        """ 
        Returns a list of all findings for a specific project.
        uuid:The UUID of the project.
        suppressed: optionally includes suppressed vulnerabilities(boolean)
        """
        finding_list = list()
        pageNumber = 1
        response = self.session.get(self.apicall + f"/v1/finding/project/{uuid}?suppressed={suppressed}", params={
                                    "pageSize": pageSize, "pageNumber": pageNumber})
        for finding in range(0, len(response.json())):
            finding_list.append(response.json()[finding-1])
        while len(response.json()) == pageSize:
            response = self.session.get(self.apicall + f"/v1/finding/project/{uuid}?suppressed={suppressed}", params={
                                        "pageSize": pageSize, "pageNumber": pageNumber})
            for finding in range(0, len(response.json())):
                finding_list.append(response.json()[finding-1])
        if response.status_code == 200:
            return finding_list
        elif response.status_code == 401:
            return (f"Unauthorized, {response.status_code}")
        elif response.status_code == 403:
            return (f"Access to the specified project is forbidden, {response.status_code}")
        elif response.status_code == 404:
            return (f"Project not found, {response.status_code}")
        else:
            return ((response.content).decode("utf-8"), response.status_code)
        
    def export_findings(self, uuid):
        """
        Returns the findings for the specified project as FPF
        Args:
            uuid (string): The UUID of the project
        """
        response = self.session.get(self.apicall + f"/v1/findings/project/{uuid}/export")
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            return (f"Unauthorized, {response.status_code}")
        elif response.status_code == 403:
            return (f"Access to the specified project is forbidden, {response.status_code}")
        elif response.status_code == 404:
            return (f"Project not found, {response.status_code}")
        else:
            return ((response.content).decode("utf-8"), response.status_code)
