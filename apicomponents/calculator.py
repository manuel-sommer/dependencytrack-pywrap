class Calculator:

    def get_calculator(self, cvss):
        """
        Returns the CVSS base score, impact sub-score and exploitability sub-score

        Args:
            cvss (string): A valid CVSSv2 or CVSSv3 vector. Example "CVSS:3.0/AV:L/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:H"

        """
        response = self.session.get(self.apicall + "/v1/calculator/cvss", params={"vector": cvss})
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            return (f"Unauthorized, {response.status_code}")
        return ((response.content).decode("UTF-8"), response.status_code)
