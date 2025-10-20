class CWE:

    def get_cwe(self, pageSize=100):
        """
        Returns a list of all CWEs

        Args:
            pageSize (int, optional): size of the page. Defaults to 100.

        Returns:
            JSON: json object

        """
        cwe_list = list()
        pageNumber = 1
        response = self.session.get(self.apicall + "/v1/cwe", params={"pageSize": pageSize, "pageNumber": pageNumber})
        for cwe in range(len(response.json())):
            cwe_list.append(response.json()[cwe - 1])
        while len(response.json()) == pageSize:
            pageNumber += 1
            response = self.session.get(self.apicall + "/v1/cwe", params={"pageSize": pageSize, "pageNumber": pageNumber})
            for cwe in range(len(response.json())):
                cwe_list.append(response.json()[cwe - 1])
        if response.status_code == 200:
            return cwe_list
        if response.status_code == 401:
            return (f"Unauthorized, {response.status_code}")
        return ((response.content).decode("utf-8"), response.status_code)

    def get_cweById(self, cweId):
        """
        Returns a specific CWE

        Args:
            cweId (int32): The CWE ID of the CWE to retrieve

        Returns:
            JSON: {
                    "cweId": 0,
                    "name": "string"
                    }

        """
        response = self.session.get(self.apicall + f"/v1/cwe/{cweId}")
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            return ("Unauthorized ", response.status_code)
        if response.status_code == 404:
            return (f"The CWE could not be found, {response.status_code}")
        return ((response.content).decode("utf-8"), response.status_code)
