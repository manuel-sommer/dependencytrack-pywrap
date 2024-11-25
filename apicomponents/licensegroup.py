import json


class LicenseGroup:

    def list_licensegroups(self, pageSize=100):
        grouplist = list()
        pageNumber = 1
        response = self.session.get(
            self.apicall + "/v1/licenseGroup", params={"pageSize": pageSize, "pageNumber": pageNumber})
        for group in range(len(response.json())):
            grouplist.append(response.json()[group - 1])
        while len(response.json()) == pageSize:
            pageNumber += 1
            response = self.session.get(
                self.apicall + "/v1/licenseGroup", params={"pageSize": pageSize, "pageNumber": pageNumber})
            for group in range(len(response.json())):
                grouplist.append(response.json()[group - 1])
        if response.status_code == 200:
            return grouplist
        if response.status_code == 401:
            return (f"Unauthorized, {response.status_code}")
        return (f"{(response.content).decode('utf-8')}, {response.status_code}")

    def get_licensegroup(self, uuid):
        response = self.session.get(self.apicall + f"/v1/licenseGroup/{uuid}")
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            return (f"Unauthorized, {response.status_code}")
        return (f"{(response.content).decode('utf-8')}, {response.status_code}")

    def delete_licensegroup(self, uuid):
        """
        Delete a license group
        Args:
            uuid ([type]): The UUID of the license group to delete
        """
        response = self.session.delete(self.apicall + f"/v1/licenseGroup/{uuid}")
        if response.status_code == 200:
            return "Successful operation"
        if response.status_code == 401:
            return (f"Unauthorized, {response.status_code}")
        return (f"{(response.content).decode('utf-8')}, {response.status_code}")

    def remove_license_from_licensegroup(self, licensegroup, license):

        response = self.session.delete(self.apicall + f"/v1/licenseGroup/{licensegroup}/license/{license}")
        if response.status_code == 200:
            return "Successful operation"
        if response.status_code == 401:
            return (f"Unauthorized, {response.status_code}")
        return (f"{(response.content).decode('utf-8')}, {response.status_code}")

    def add_license_to_group(self, licensegroup, license):

        response = self.session.post(
            self.apicall + f"/v1/licenseGroup/{licensegroup}/license/{license}")
        if response.status_code == 200:
            return "Successful operation"
        if response.status_code == 401:
            return (f"Unauthorized, {response.status_code}")
        if response.status_code == 304:
            return (f"The license group already has the specified license assigned, {response.status_code}")
        return (f"{(response.content).decode('utf-8')}, {response.status_code}")

    def create_licensegroup(self, name, licenses=None, riskWeight=0):
        data = {"name": name, "riskWeight": riskWeight}
        if licenses:
            if isinstance(license, list):
                data["licenses"] = licenses
            else:
                return "Error! Licenses should be a list"
        response = self.session.put(self.apicall + "/v1/licenseGroup", data=json.dumps(data))
        if response.status_code == 201:
            return response.json()
        if response.status_code == 401:
            return (f"Unauthorized, {response.status_code}")
        return (f"{(response.content).decode('utf-8')}, {response.status_code}")

    def update_licensegroup(self, uuid, name=None, licenses=None, riskWeight=None):
        data = {"uuid": uuid}
        if name:
            data["name"] = name
        if licenses:
            if isinstance(license, list):
                data["licenses"] = licenses
            else:
                return "Error! Licenses should be a list"
        if riskWeight:
            data["risk_weight"] = riskWeight
        response = self.session.post(self.apicall + "/v1/licenseGroup", data=json.dumps(data))
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            return (f"Unauthorized, {response.status_code}")
        if response.status_code == 304:
            return (f"The license group already has the specified license assigned, {response.status_code}")
        return (f"{(response.content).decode('utf-8')}, {response.status_code}")
