class Violation:

    def list_violations(self, suppressed=False, pageSize=100):
        """
        Returns a list of all policy violations for the entire portfolio

        Args:
            suppressed (bool, optional): Optionally includes suppressed violations. Defaults to False.
            pageSize (int, optional): Size of the page. Defaults to 100.

        Returns:
            List: Returns a list of all policy violations for the entire portfolio

        """
        violationlist = list()
        pageNumber = 1
        response = self.session.get(self.apicall + "/v1/violation", params={
                                    "pageSize": pageSize, "pageNumber": pageNumber, "suppressed": suppressed})
        for violation in range(len(response.json())):
            violationlist.append(response.json()[violation - 1])
        while len(response.json()) == pageSize:
            pageNumber += 1
            response = self.session.get(self.apicall + "/v1/violation", params={
                "pageSize": pageSize, "pageNumber": pageNumber, "suppressed": suppressed})
            for violation in range(len(response.json())):
                violationlist.append(response.json()[violation - 1])
        if response.status_code == 200:
            return violationlist
        return ((response.content).decode("utf-8"), response.status_code)

    def get_project_violation(self, uuid, suppressed=False):
        """
        Returns a list of all policy violations for a specific project

        Args:
            uuid (string): The UUID of the project
            suppressed (bool, optional): Optionally includes suppressed violations. Defaults to False.

        Returns:
            List: Returns a list of all policy violations for a specific project

        """
        response = self.session.get(self.apicall + f"/v1/violation/project/{uuid}", params={"suppressed": suppressed})
        if response.status_code == 200:
            return response.json()
        return ((response.content).decode("utf-8"), response.status_code)

    def get_component_violation(self, uuid, suppressed=False):
        """
        Returns a list of all policy violations for a specific component

        Args:
            uuid (string): The UUID of the project
            suppressed (bool, optional): Optionally includes suppressed violations. Defaults to False.

        Returns:
            List: Returns a list of all policy violations for a specific component.

        """
        response = self.session.get(self.apicall + f"/v1/violation/component/{uuid}", params={"suppressed": suppressed})
        if response.status_code == 200:
            return response.json()
        return ((response.content).decode("utf-8"), response.status_code)
