class DependencyTrackFinding(object):
    # this section is all about findings

    def get_project_finding(self, uuid, supressed=False, pageSize=100):
        """ 
        Returns a list of all findings for a specific project.
        uuid:
        supprressed: optionally includes supressed vulnerabilities(boolean)
        """
        finding_list = list()
        pageNumber = 1
        response = self.session.get(self.apicall + f"/v1/finding/project/{uuid}?supressed={supressed}", params={
                                    "pageSize": pageSize, "pageNumber": pageNumber})
        for finding in range(0, len(response.json())):
            finding_list.append(response.json()[finding-1])
        while len(response.json()) == pageSize:
            response = self.session.get(self.apicall + f"/v1/finding/project/{uuid}?supressed={supressed}", params={
                                        "pageSize": pageSize, "pageNumber": pageNumber})
            for finding in range(0, len(response.json())):
                finding_list.append(response.json()[finding-1])
        if response.status_code == 200:
            return finding_list
        else:
            if response.status_code == 401:
                return (f"Unauthorized", response.status_code)
            elif response.status_code == 403:
                return (f"Access to the specified project is forbidden ", response.status_code)
            else:
                return (f"The project could not be found", response.status_code)