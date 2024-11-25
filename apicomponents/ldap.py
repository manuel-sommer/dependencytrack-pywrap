import json


class LDAP:

    def list_ldapgroups(self, pageSize=100):
        """
        This API performs a pass-thru query to the configured LDAP server. Search criteria results are cached using default Alpine CacheManager policy.
        Returns the DNs of all accessible groups within the directory
        """
        ldaplist = list()
        pageNumber = 1
        response = self.session.get(self.apicall + "/v1/ldap/groups", params={"pageSize": pageSize, "pageNumber": pageNumber})
        for ldap in range(len(response.json())):
            ldaplist.append(response.json()[ldap - 1])
        while len(response.json()) == pageSize:
            pageNumber += 1
            response = self.session.get(self.apicall + "/v1/ldap/groups", params={"pageSize": pageSize, "pageNumber": pageNumber})
            for ldap in range(len(response.json())):
                ldaplist.append(response.json()[ldap - 1])
        if response.status_code == 200:
            return ldaplist
        return (f"{(response.content).decode('utf-8')}, {response.status_code}")

    def get_ldapteam(self, uuid):
        """
        Returns the DNs of all groups mapped to the specified team

        Args:
            uuid (string): The UUID of the team to retrieve mappings for.
        """
        response = self.session.get(self.apicall + f"/v1/ldap/team/{uuid}")
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            return (f"Unauthorized , {response.status_code}")
        if response.status_code == 404:
            return (f"The UUID of the team could not be found , {response.status_code}")
        return (f"{(response.content).decode('utf-8')}, {response.status_code}")

    def create_ldap(self, team, dn):
        """
        Adds a mapping

        Args:
            team (string): The UUID of the team
            dn (string): DNs
        """
        data = {
            "team": team,
            "dn": dn,
        }
        response = self.session.put(self.apicall + "/v1/ldap/mapping", data=json.dumps(data))
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            return (f"Unauthorized , {response.status_code}")
        if response.status_code == 404:
            return (f"The UUID of the team could not be found, {response.status_code}")
        if response.status_code == 409:
            return (f"A mapping with the same team and dn already exists, {response.status_code}")
        return (f"{(response.content).decode('utf-8')}, {response.status_code}")

    def delete_ldap(self, uuid):
        """
            Removes a mapping

        Args:
            uuid (string): The UUID of the mapping to delete
        """
        response = self.session.delete(self.apicall + f"/v1/ldap/mapping/{uuid}")
        if response.status_code == 204:
            return (f"successful operation, {response.status_code}")
        if response.status_code == 401:
            return (f"Unauthorized , {response.status_code}")
        if response.status_code == 404:
            return (f"The UUID of the mapping could not be found, {response.status_code}")
        return (f"{(response.content).decode('utf-8')}, {response.status_code}")
