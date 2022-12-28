class License(object):

    def get_list_license(self, pageSize=100):
        """Returns a list of all licenses with complete metadata for each license"""
        license_list = list()
        pageNumber = 1
        response = self.session.get(
            self.apicall + f"/v1/license", params={"pageSize": pageSize, "pageNumber": pageNumber})
        for lice in range(0, len(response.json())):
            license_list.append(response.json()[lice-1])
        while len(response.json()) == pageSize:
            pageNumber += 1
            response = self.session.get(
                self.apicall + f"/v1/license", params={"pageSize": pageSize, "pageNumber": pageNumber})
            for lice in range(0, len(response.json())):
                license_list.append(response.json()[lice-1])
        if response.status_code == 200:
            return license_list
        else:
            return (f"Unauthorized ", response.status_code)

    def get_license(self, licenseId):
        """
        Returns specific license
        licenseID: (string) The SPDX License ID of the license to retrieve
        """
        response = self.session.get(self.apicall + f"/v1/license/{licenseId}")
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            return (f"Unauthorized ", response.status_code)
        elif response.status_code == 404:
            return(f"The license could not be found ", response.status_code)
        else:
            return response.status_code

    def get_license_concise(self, pageSize=100):
        """Returns a concise listing of all licenses"""
        license_list = list()
        pageNumber = 1
        response = self.session.get(
            self.apicall + f"/v1/license/concise", params={"pageSize": pageSize, "pageNumber": pageNumber})
        for lice in range(0, len(response.json())):
            license_list.append(response.json()[lice-1])
        while len(response.json()) == pageSize:
            pageNumber += 1
            response = self.session.get(
                self.apicall + f"/v1/license/concise", params={"pageSize": pageSize, "pageNumber": pageNumber})
            for lice in range(0, len(response.json())):
                license_list.append(response.json()[lice-1])
        if response.status_code == 200:
            return license_list
        elif response.status_code == 401:
            return (f"Unauthorized, {response.status_code}")
        else:
            return ((response.content).decode("utf-8"), response.status_code)
