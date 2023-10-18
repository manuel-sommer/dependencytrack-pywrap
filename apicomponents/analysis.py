import json


class Analysis(object):

    def get_analysis(self, project, component, vulnerability):
        """Retrieves an analysis trail

        Args:
            project (string): The UUID of the project
            component (string): The UUID of the component
            vulnerability (string): The UUID of the vulnerability

        Returns:
            json: """
        response = self.session.get(self.apicall + "/v1/analysis/", params = {"project": project, "component": component, "vulnerability": vulnerability} )
        if response.status_code == 200:
            return response.json()
        else:
            return (f"{(response.content).decode('utf-8')}, {response.status_code}")
    
    def record_analysis(self, project, component, vulnerability, suppressed=False):
        """Retrieves an analysis trail

        Args:
            project (string): The UUID of the project
            component (string): The UUID of the component
            vulnerability (string): The UUID of the vulnerability

        Returns:
            dictionary: Example value model:
                                {
                    "analysisState": "EXPLOITABLE",
                    "analysisComments": [
                        {
                        "timestamp": "2021-12-02T17:14:26.654Z",
                        "comment": "string",
                        "commenter": "string"
                        }
                    ],
                    "isSuppressed": true
                    } """
        
        response = self.session.put(self.apicall + "/v1/analysis/", data=json.dump({"project": project, "component": component, "vulnerability": vulnerability, "suppressed":suppressed}))
        if response.status_code == 200:
            return response.json()
        else:
            return (f"{(response.content).decode('utf-8')}, {response.status_code}")
