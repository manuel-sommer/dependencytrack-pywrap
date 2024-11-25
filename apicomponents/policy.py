import json


class Policy:

    def get_policy(self, uuid):
        """
        Returns a specific policy

        Args:
            uuid (string): The UUID of the policy to retrieve.

        Returns:
            dictionary: policy
        """
        response = self.session.get(self.apicall + f"/v1/policy/{uuid}")
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            return (f"Unauthorized, {response.status_code}")
        return (f"{(response.content).decode('utf-8')}, {response.status_code}")

    def list_policy(self, pageSize=100):
        """
        Returns a list of all policies

        Args:
            pageSize (int, optional): size of the page. Defaults to 100.

        Returns:
            List: list of all policies
        """
        policylist = list()
        pageNumber = 1
        response = self.session.get(
            self.apicall + "/v1/policy", params={"pageSize": pageSize, "pageNumber": pageNumber})
        for policy in range(len(response.json())):
            policylist.append(response.json()[policy - 1])
        while len(response.json()) == pageSize:
            pageNumber += 1
            response = self.session.get(
                self.apicall + "/v1/policy", params={"pageSize": pageSize, "pageNumber": pageNumber})
            for policy in range(len(response.json())):
                policylist.append(response.json()[policy - 1])
        if response.status_code == 200:
            return policylist
        if response.status_code == 401:
            return (f"Unauthorized, {response.status_code}")
        return (f"{(response.content).decode('utf-8')}, {response.status_code}")

    def delete_policy(self, uuid):
        """
        Deletes a specific policy

        Args:
            uuid (string): The UUID of the policy to delete.
        """
        response = self.session.delete(self.apicall + f"/v1/policy/{uuid}")
        if response.status_code >= 200 and response.status_code <= 299:
            return ("Successful operation")
        if response.status_code == 401:
            return (f"Unauthorized, {response.status_code}")
        return (f"{(response.content).decode('utf-8')}, {response.status_code}")

    def create_policy(self, name, operator="ANY", violationState="INFO", policyCondition=None, projects=None, globals=None):
        # TODO: create better comments explaining the args
        """
        Create a policy

        Args:
            name (string): Name of the policy
            operator (string, optional): Operator of the policy(ANY, ALL). Defaults to ANY.
            violationState (str, optional): [description]. Defaults to "INFO".
            policyCondition ([type], optional): [description]. Defaults to None.
            projects ([type], optional): [description]. Defaults to None.
            globals ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        data = {"name": name,
                "violationState": violationState}
        if operator:
            data["operator"] = operator
        if policyCondition:
            if isinstance(policyCondition, list):
                data["policyCondition"] = policyCondition
            else:
                return "Error! The policyCondition should be a list"
        if projects:
            if isinstance(projects, list):
                data["projects"] = projects
            else:
                return "Error! The projects should be a list"
        if globals:
            data["globals"] = globals
        response = self.session.put(
            self.apicall + "/v1/policy", data=json.dumps(data))
        if response.status_code == 201:
            return response.json()
        if response.status_code == 401:
            return (f"Unauthorized, {response.status_code}")
        return (f"{(response.content).decode('utf-8')}, {response.status_code}")

    def update_policy(self, uuid, name=None, operator=None, violationState=None, policyCondition=None, projects=None, globals=None):
        # TODO: create better comments explaining the args
        """
        Create a policy

        Args:
            name (string): Name of the policy
            operator ([type], optional): Operator of the policy. Defaults to None.
            violationState (str, optional): [description]. Defaults to "INFO".
            policyCondition ([type], optional): [description]. Defaults to None.
            projects ([type], optional): [description]. Defaults to None.
            globals ([type], optional): [description]. Defaults to None.

        """
        data = {"uuid": uuid}
        if name:
            data["name"] = name
        if violationState:
            data["violationState"] = violationState
        if operator:
            data["operator"] = operator
        if policyCondition:
            if isinstance(policyCondition, list):
                data["policyCondition"] = policyCondition
            else:
                return "Error! The policyCondition should be a list"
        if projects:
            if isinstance(projects, list):
                data["projects"] = projects
            else:
                return "Error! The projects should be a list"
        if globals:
            data["globals"] = globals
        response = self.session.post(self.apicall + "/v1/policy", data=json.dumps(data))
        if response.status_code == 200:
            return ("Successful operation")
        if response.status_code == 401:
            return (f"Unauthorized, {response.status_code}")
        return (f"{(response.content).decode('utf-8')}, {response.status_code}")

    def add_policyToproject(self, policyUuid, projectUuid):
        """
        Adds project to a policy.

        Args:
            policyUuid (string): The UUID of the policy
            projectUuid (string): The UUID of the project
        """
        response = self.session.post(self.apicall + f"/v1/policy/{policyUuid}/projects/{projectUuid}")
        if response.status_code == 200:
            return ("Successful operation")
        if response.status_code == 401:
            return (f"Unauthorized, {response.status_code}")
        if response.status_code == 304:
            return (f"The policy already has the specified project assigned, {response.status_code}")
        return (f"{(response.content).decode('utf-8')}, {response.status_code}")

    def delete_policyFromproject(self, policyUuid, projectUuid):
        """
        Removes a project from a policy.

        Args:
            policyUuid (string): The UUID of the policy
            projectUuid (string): The UUID of the project
        """
        response = self.session.delete(self.apicall + f"/v1/policy/{policyUuid}/projects/{projectUuid}")
        if response.status_code == 200:
            return ("Successful operation")
        if response.status_code == 401:
            return (f"Unauthorized, {response.status_code}")
        if response.status_code == 304:
            return (f"The policy does not have the specified project assigned, {response.status_code}")
        return (f"{(response.content).decode('utf-8')}, {response.status_code}")
