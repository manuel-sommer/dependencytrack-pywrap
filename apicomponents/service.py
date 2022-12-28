import json

class Service(object):

    def list_services(self, uuid, pageSize=100):
        """Returns a list of all services for a given project

        Args:
            uuid (string): The UUID of the project.
            pageSize (int, optional): page size. Defaults to 100.

        Returns:
            List: list of all services for a given service
        """
        servicelist = list()
        pageNumber = 1
        response = self.session.get(self.apicall + f"/v1/service/project/{uuid}", params={'pageSize': pageSize, 'pageNumber': pageNumber})
        try:
            for service in range(0, len(response.json())):
                servicelist.append(response.json()[service-1])
            while len(response.json()) == pageSize:
                pageNumber += 1
                response = self.session.get(self.apicall + f"/v1/service/project/{uuid}", params={'pageSize': pageSize, 'pageNumber': pageNumber})
                for service in range(0, len(response.json())):
                    servicelist.append(response.json()[service-1])
            if response.status_code == 200:
                return servicelist
        except :
            if response.status_code == 404:
                return (f"The project could not be found, {response.status_code}")
            elif response.status_code == 403:
                return (f"Access to the specified project is forbidden, {response.status_code}")
            elif response.status_code == 401:
                return (f"Unauthorized, {response.status_code}")
            else:
                return (f"{(response.content).decode('utf-8')}, {response.status_code}")
            
    def get_service(self,uuid):
        """Returns a specific service.

        Args:
            uuid (string): The UUID of the project.

        Returns:
            dict: Returns a specific service.
        """
        response = self.session.get(self.apicall + f"/v1/service/{uuid}")
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            return (f"Unauthorized, {response.status_code}")
        elif response.status_code == 404:
            return (f"The service could not be found, {response.status_code}")
        elif response.status_code == 403:
            return (f"Access to the specified project is forbidden, {response.status_code}")
        else:
            return ((response.content).decode("utf-8"), response.status_code)
        
    def delete_service(self, uuid):
        """Deletes a service

        Args:
            uuid (string): The UUID of the project. 
        """
        response = self.session.delete(self.apicall + f"/v1/service/{uuid}")
        if response.status_code == 200:
            return (f"Successful operation")
        elif response.status_code == 403:
            return (f"Access to the specified service is forbidden, {response.status_code}")
        elif response.status_code == 401:
            return (f"Unauthorized, {response.status_code}")
        elif response.status_code == 404:
            return (f"The UUID of the service could not be found, {response.status_code}")
        else:
            return (f"{(response.content).decode('utf-8')}, {response.status_code}")
        
    def create_service(self, uuid, providerName=None, providerURL=None, contactName=None, contactEmail=None, contactPhone=None):
        """
        Model: check on the official page
        """
        data={}
        contact={}
        if providerName:
            data['provider'] = {"name": providerName}
        if providerURL:
            data['provider'] = {"url": providerURL}
        if contactName:
            contact['name'] = contactName
        if contactEmail:
            contact['email'] = contactEmail
        if contactPhone:
            contact['phone']= contactPhone
        if not bool(contact):
            data['contact'] =[contact]
        #TODO: add more option
        response = self.session.put(self.apicall +f"/v1/service/project/{uuid}",data=json.dumps(data))
        if response.status_code == 201:
            return ("Successful operation")
        elif response.status_code == 401:
            return (f"Unauthorized, {response.status_code}")
        elif response.status_code == 404:
            return (f"The team could not be found, {response.status_code}")
        else:
            return (f"{(response.content).decode('utf-8')}, {response.status_code}")

def update_service(self,**args):
    data={}
    # TODO: improve the input parameters
    #? this wont return anything for now.
    response = self.session.post(self.apicall + "/v1/service", data=json.dumps(data))
    if response.status_code == 200:
        return ("Successful operation")
    else:
        return (f"{(response.content).decode('utf-8')}, {response.status_code}")
