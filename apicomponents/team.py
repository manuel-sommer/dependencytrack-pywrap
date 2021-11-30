import json


class DependencyTrackTeam(object):

    def get_teamByUUID(self, uuid):
        """Returns a specific team
        Args:
            uuid (string): The UUID of the team to retrieve
        """
        response = self.session.get(self.apicall + f"/v1/team/{uuid}")
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            return (f"Unauthorized, {response.status_code}")
        elif response.status_code == 404:
            return (f"The team could not be found, {response.status_code}")
        else:
            return response.status_code

    def generate_team_apikey(self, uuid):
        """Generate an API key and returns its value

        Args:
            uuid (string): The UUID of the team to generate a key for.
        """
        response = self.session.put(self.apicall + f"/v1/team/{uuid}/key")
        if response.status_code == 201:
            return response.json()
        elif response.status_code == 401:
            return (f"Unauthorized, {response.status_code}")
        elif response.status_code == 404:
            return (f"The team could not be found, {response.status_code}")
        else:
            return (response.status_code)

    def delete_team(self, name, uuid, key=[]):
        """ Deletes a team

        Args:
            name (string): name of the team.
            uuid (string): The UUID of the team.
            apikeys (list of dict): API key of the team. [{"key": apikeys}]
        """
        data = {
            "name": name,
            "uuid": uuid,
        }
        if len(key) > 0:
            data['apikeys'] = key
        response = self.session.delete(
            self.apicall + "/v1/team", data=json.dumps(data))
        if response.status_code == 204:
            return (f"Successfully operation")
        elif response.status_code == 401:
            return (f"Unauthorized, {response.status_code}")
        elif response.status_code == 404:
            return (f"The team could not be found, {response.status_code}")
        else:
            return response.status_code

    def update_team(self, name, uuid, key=[], ldapUsers=[], managedUsers=[], oidcUsers=[], mappedLdapGroups=[], mappedOidcGroups=[], permissions=[]):
        """ 
        Updates a team's fields including
        Model:{
            "uuid": "string",
            "name": "string",
            "apiKeys": [
                {
                "key": "string"
                }
            ],
            "ldapUsers": [
                {
                "username": "string",
                "dn": "string",
                "teams": [
                    null
                ],
                "email": "string",
                "permissions": [
                    {
                    "name": "string",
                    "description": "string"
                    }
                ]
                }
            ],
            "managedUsers": [
                {
                "username": "string",
                "newPassword": "string",
                "confirmPassword": "string",
                "lastPasswordChange": "2021-11-29T23:21:55.571Z",
                "fullname": "string",
                "email": "string",
                "suspended": true,
                "forcePasswordChange": true,
                "nonExpiryPassword": true,
                "teams": [
                    null
                ],
                "permissions": [
                    {
                    "name": "string",
                    "description": "string"
                    }
                ]
                }
            ],
            "oidcUsers": [
                {
                "username": "string",
                "subjectIdentifier": "string",
                "email": "string",
                "teams": [
                    null
                ],
                "permissions": [
                    {
                    "name": "string",
                    "description": "string"
                    }
                ]
                }
            ],
            "mappedLdapGroups": [
                {
                "dn": "string",
                "uuid": "string"
                }
            ],
            "mappedOidcGroups": [
                {
                "group": {
                    "uuid": "string",
                    "name": "string"
                },
                "uuid": "string"
                }
            ],
            "permissions": [
                {
                "name": "string",
                "description": "string"
                }
            ]
            } 
        """
        data = {
            "name": name,
            "uuid": uuid,
        }
        if len(key) > 0:
            data['apikeys'] = key
        if len(ldapUsers) > 0:
            data['ldapusers'] = ldapUsers
        if len(managedUsers) > 0:
            data['managedUsers'] = managedUsers
        if len(oidcUsers) > 0:
            data['oidcUsers'] = oidcUsers
        if len(mappedLdapGroups) > 0:
            data["mappedLdapGroups"] = mappedLdapGroups
        if len(mappedOidcGroups) > 0:
            data["mappedOidcGroups"] = mappedOidcGroups
        if len(permissions) > 0:
            data["permissions"] = permissions
        response = self.session.post(
            self.apicall + "/v1/team", data=json.dumps(data))
        if response.status_code == 200:
            return (f"successful operation, {response.status_code}")
        elif response.status_code == 401:
            return (f"Unauthorized, {response.status_code}")
        elif response.status_code == 404:
            return (f"The team could not be found, {response.status_code}")
        else:
            return response.status_code

    def create_team(self, name, uuid=None, key=[], ldapUsers=[], managedUsers=[], oidcUsers=[], mappedLdapGroups=[], mappedOidcGroups=[], permissions=[]):
        """ 
        Updates a team's fields including
        Model:{
            "uuid": "string",
            "name": "string",
            "apiKeys": [
                {
                "key": "string"
                }
            ],
            "ldapUsers": [
                {
                "username": "string",
                "dn": "string",
                "teams": [
                    null
                ],
                "email": "string",
                "permissions": [
                    {
                    "name": "string",
                    "description": "string"
                    }
                ]
                }
            ],
            "managedUsers": [
                {
                "username": "string",
                "newPassword": "string",
                "confirmPassword": "string",
                "lastPasswordChange": "2021-11-29T23:21:55.571Z",
                "fullname": "string",
                "email": "string",
                "suspended": true,
                "forcePasswordChange": true,
                "nonExpiryPassword": true,
                "teams": [
                    null
                ],
                "permissions": [
                    {
                    "name": "string",
                    "description": "string"
                    }
                ]
                }
            ],
            "oidcUsers": [
                {
                "username": "string",
                "subjectIdentifier": "string",
                "email": "string",
                "teams": [
                    null
                ],
                "permissions": [
                    {
                    "name": "string",
                    "description": "string"
                    }
                ]
                }
            ],
            "mappedLdapGroups": [
                {
                "dn": "string",
                "uuid": "string"
                }
            ],
            "mappedOidcGroups": [
                {
                "group": {
                    "uuid": "string",
                    "name": "string"
                },
                "uuid": "string"
                }
            ],
            "permissions": [
                {
                "name": "string",
                "description": "string"
                }
            ]
            } 
        """
        data = {
            "name": name,
        }
        if uuid:
            data["uuid"] = uuid
        if len(key) > 0:
            data['apikeys'] = key
        if len(ldapUsers) > 0:
            data['ldapusers'] = ldapUsers
        if len(managedUsers) > 0:
            data['managedUsers'] = managedUsers
        if len(oidcUsers) > 0:
            data['oidcUsers'] = oidcUsers
        if len(mappedLdapGroups) > 0:
            data["mappedLdapGroups"] = mappedLdapGroups
        if len(mappedOidcGroups) > 0:
            data["mappedOidcGroups"] = mappedOidcGroups
        if len(permissions) > 0:
            data["permissions"] = permissions
        response = self.session.put(
            self.apicall + "/v1/team", data=json.dumps(data))
        if response.status_code == 201:
            return (f"successful operation, {response.status_code}")
        elif response.status_code == 401:
            return (f"Unauthorized, {response.status_code}")
        else:
            return response.status_code

    def list_teams(self, pageSize=100):
        """Returns a list of all teams
        """
        teamlist = list()
        pageNumber = 1
        response = self.session.get(
            self.apicall + "/v1/team", params={'pageSize': pageSize, 'pageNumber': pageNumber})
        for team in range(0, len(response.json())):
            teamlist.append(response.json()[team-1])
        while len(response.json()) == pageSize:
            pageNumber += 1
            response = self.session.get(
                self.apicall + "/v1/team", params={'pageSize': pageSize, 'pageNumber': pageNumber})
            for team in range(0, len(response.json())):
                teamlist.append(response.json()[team-1])
        if response.status_code == 200:
            return teamlist
        else:
            return (f"Unable to list projects", response.status_code)
        
    def delete_apikey(self, apikey):
        """Delete specified API key

        Args:
            apikey (string): The API key to delete.
        """
        response = self.session.delete(self.apicall + f"/v1/team/key/{apikey}")
        if response.status_code == 200:
            return (f"successful operation, {response.status_code}")
        elif response.status_code == 401:
            return (f"Unauthorized, {response.status_code}")
        elif response.status_code == 404:
            return (f"The API key could not be found, {response.status_code}")

    def update_apikey(self, apikey):
        """Regenerates an API key by removing the specified key, generating a new one and returning its value

        Args:
            apikey (string): The API key to regenerate.
        """
        response = self.session.post(self.apicall + f"/v1/team/key/{apikey}")
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            return (f"Unauthorized, {response.status_code}")
        elif response.status_code == 404:
            return (f"The API key could not be found, {response.status_code}")
        else:
            return response.status_code
