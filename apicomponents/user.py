import json

class User(object):

    def get_user_oidc(self):
        """
        """
        response = self.session.get(self.apicall + f"/v1/user/oidc") #Retuns a list of all OIDC users
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            return (f"Unauthorized, {response.status_code}")
        elif response.status_code == 404:
            return (f"Could not be found, {response.status_code}")

    def join_team(self, username, uuid):
        """
        Adds a user to a team.
        
        Args:
            uuid (string): The uuid of the team.
            username (string): A valid username.
        """
        data = {
            "uuid": uuid,
        }
        response = self.session.post(self.apicall + f"/v1/user/{username}/membership", data=json.dumps(data))
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 304:
            return (f"The user is already a member of the specified team, {response.status_code}")
        elif response.status_code == 401:
            return (f"Unauthorized, {response.status_code}")
        elif response.status_code == 404:
            return (f"User or team could not be found, {response.status_code}")    

#TODO extend