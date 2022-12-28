class Permission(object):

    def list_permissions(self, pageSize=100):
        """
        Returns a list of all permissions
        """
        permissionlist = list()
        pageNumber = 1
        response = self.session.get(self.apicall + "/v1/permission", params={'pageSize': pageSize, 'pageNumber': pageNumber})
        for permission in range(0, len(response.json())):
            permissionlist.append(response.json()[permission-1])
        while len(response.json()) == pageSize:
            pageNumber += 1
            response = self.session.get(self.apicall + "/v1/permission", params={'pageSize': pageSize, 'pageNumber': pageNumber})
            for permission in range(0, len(response.json())):
                permissionlist.append(response.json()[permission-1])
        if response.status_code == 200:
            return permissionlist
        else:
            return (f"Unable to list permissions, {response.status_code}")

    def add_userpermission(self, permission, username):
        """Adds the permission to the specified username.

        Args:
            permission (string): A valid permission.
            username (string): A valid username.
        """
        response = self.session.post(self.apicall + f"/v1/permission/{permission}/user/{username}")
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            return (f"Unauthorized, {response.status_code}")
        elif response.status_code == 404:
            return (f" The user could not be found , {response.status_code}")
        elif response.status_code == 304:
            return ("The user already has the specified permission assigned, {response.status_code}")
        else:
            return ((response.content).decode("utf-8"), response.status_code)
        
    def delete_userpermission(self, permission, username):
        """Removes the permission to the specified username.

        Args:
            permission (string): A valid permission.
            username (string): A valid username.
        """
        response = self.session.delete(self.apicall + f"/v1/permission/{permission}/user/{username}")
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            return (f"Unauthorized , {response.status_code}")
        elif response.status_code == 404:
            return (f" The user could not be found, {response.status_code}")
        elif response.status_code == 304:
            return ("The user already has the specified permission assigned, {response.status_code}")
        else:
            return ((response.content).decode("utf-8"), response.status_code)
        
    def add_teampermission(self, permission, uuid):
        """Adds the permission to the specified username.

        Args:
            permission (string): A valid permission.
            uuid (string): A valid team uuid.
        """
        response = self.session.post(self.apicall + f"/v1/permission/{permission}/team/{uuid}")
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            return (f"Unauthorized, {response.status_code}")
        elif response.status_code == 404:
            return (f" The user could not be found, {response.status_code}")
        elif response.status_code == 304:
            return ("The user already has the specified permission assigned, {response.status_code}")
        else:
            return ((response.content).decode("utf-8"), response.status_code)

    def delete_userpermission(self, permission, uuid):
        """Removes the permission to the specified team.

        Args:
            permission (string): A valid permission.
            uuid (string): A valid team uuid.
        """
        response = self.session.delete(self.apicall + f"/v1/permission/{permission}/team/{uuid}")
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            return (f"Unauthorized, {response.status_code}")
        elif response.status_code == 404:
            return (f" The user could not be found, {response.status_code}")
        elif response.status_code == 304:
            return ("The user already has the specified permission assigned, {response.status_code}")
        else:
            return ((response.content).decode("utf-8"), response.status_code)
