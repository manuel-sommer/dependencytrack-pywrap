class DependencyTrackProjectProperty(object):
    # this section is all about projectProperty
    def get_projectproperty(self, uuid):
        response = self.session.get(self.apicall + f"/v1/project/{uuid}/property")
        if response.status_code == 200:
            return response.json()
        else:
            return (f"Unable to find project, {response.status_code}")

    def update_projectproperty(self, uuid, name=None, classifier=None):
        # TODO add more options
        data = {
            "uuid": uuid
        }
        if name:
            data['name'] = name
        if classifier:
            data['classifier'] = classifier
        response = self.session.post(self.apicall + f"/v1/project/{uuid}/property", json=data)
        if response.status_code == 200:
            return (f"Successfully updated the project, {response.status_code}")
        elif response.status_code == 404:
            return (f"Project with specified uuid could not be found, {response.status_code}")
        elif response.status_code == 409:
            return (f"Project with specified name already exists, {response.status_code}")
        else:
            return (f"Unable to update the project, {response.status_code}")

    def create_projectproperty(self, uuid,  propertyValue, groupName="integrations", propertyName="defectdojo.engagementId", propertyType="STRING", description="DefectDojo integration"):
        """
        name, classifier and more args to be added
        Args:
            uuid ([type]): uuid of the project
            groupName ([type]): group take a look at config properties you will see groups
            propertyName ([type]): same as above
            propertyValue ([type]): same as above
            propertyType (STRING, ENCRYPTEDSTRING, TIMESTAMP, BOOLEAN, NUMBER, UUID, INTEGER, URL): specify the value of inform of "STRING", "ENCRYPTEDSTRING", "TIMESTAMP", "BOOLEAN", "NUMBER", "UUID", "INTEGER", "URL"
            description (str, optional): [description]. Defaults to "DefectDojo integration".

        Returns:
            data sent in json
        """
        # TODO add more options
        data = {
            "groupName": groupName,
            "propertyName": propertyName,
            "propertyValue": propertyValue,
            "propertyType": propertyType,
            "description": description
        }
        response = self.session.put(
            self.apicall + f"/v1/project/{uuid}/property", json=data)
        if response.status_code == 201:
            return (f"Successfully created the project, {response.status_code}")
        elif response.status_code == 409:
            return (f"Project with specified name already exists, {response.status_code}")
        else:
            return (f"Unable to create the project, {response.status_code}")
    
    def delete_projectproperty_uuid(self, uuid):
        response = self.session.delete(self.apicall + f"/v1/project/{uuid}/property")
        if response.status_code == 204:
            return (f"Successfully deleted the project, {response.status_code}")
        else:
            return (f"Unable to delete the project, {response.status_code}")