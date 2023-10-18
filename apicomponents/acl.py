class ACL(object):

    def put_acl(self, team, project):
        """[Adds an ACL mapping]

        Args:
            team ([string]): [name of the team]
            project ([string]): [name of the project]
        """
        data = {"team": team, "project": project}
        response = self.session.put(
            self.apicall + "/v1/acl/mapping", json=data)

        if response.status_code == 200:
            return response.status_code
        elif response.status_code == 401:
            return (f"Unauthorized, {
                response.status_code
                }")
        elif response.status_code == 404:
            return (f"The UUID of the team or project could not be found, {
                response.status_code
                }")
        elif response.status_code == 409:
            return (f"A mapping with the same team and project already exists, {
                response.status_code
                }")
        else:
            return ((response.content).decode("UTF-8"),
                    response.status_code)

    def get_acl(self, uuid, excludeInactive=False):
        """[Returns the projects assigned to the specified team]

        Args:
            uuid ([string]): [The UUID of the team to retrieve mappings for]
        """
        response = self.session.get(self.apicall + f"/v1/acl/team/{uuid}?excludeInactive={excludeInactive}")
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            return (f"Unauthorized, {response.status_code}")
        elif response.status_code == 404:
            return (f"The UUID of the team could not be found, {response.status_code}")

    def delete_acl(self, teamUuid, projectUuid):
        """
        Remove an ACL mapping

        Args:
            teamUuid ([string]): [The UUID of the team to delete the mapping for]
            projectUuid ([string]): [The UUID of the project to delete the mapping for]
        """
        response = self.session.delete(
            self.apicall + f"/v1/acl/mapping/team/{teamUuid}/project/{projectUuid}")
        if response.status_code == 200:
            return (f"successful operation")
        elif response.status_code == 401:
            return (f"Unauthorized, 
                    {response.status_code}")
        elif response.status_code == 404:
            return (f"The UUID of the team or project could not be found, 
                    {response.status_code}")
        else:
            return ((response.content).decode("UTF-8"), 
                    response.status_code)
