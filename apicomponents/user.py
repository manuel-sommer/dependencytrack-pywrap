class DependencyTrackUser(object):
    
    def get_user_oidc(self):
        """
        """
        response = self.session.get(self.apicall + f"/v1/user/oidc")
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            return (f"Unauthorized, {response.status_code}")
        elif response.status_code == 404:
            return (f"The UUID of the team could not be found, {response.status_code}")

    #TODO extend