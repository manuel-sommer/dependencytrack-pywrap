import requests
import json


class DependencyTrackAPI(object):
    def __init__(self, apiurl, apikey):
        self.apiurl = apiurl
        self.apikey = apikey
        self.apicall = self.apiurl + "/api"
        self.session = requests.Session()
        self.session.headers.update({"X-Api-Key": f"{self.apikey}"})

    def version(self):
        response = self.session.get(self.apicall + "/version")
        return response.json()

    def list_projects(self, pageSize=100):
        projectlist = list()
        pageNumber = 1
        response = self.session.get(
            self.apicall + "/v1/project", params={'pageSize': pageSize, 'pageNumber': pageNumber})
        for project in range(0, len(response.json())):
            projectlist.append(response.json()[project-1])
        while len(response.json()) == pageSize:
            pageNumber += 1
            response = self.session.get(
                self.apicall + "/v1/project", params={'pageSize': pageSize, 'pageNumber': pageNumber})
            for project in range(0, len(response.json())):
                projectlist.append(response.json()[project-1])
        if response.status_code == 200:
            return projectlist
        else:
            return (f"Unable to list projects", response.status_code)

    def get_project(self, uuid):
        response = self.session.get(self.apicall + f"/v1/project/{uuid}/")
        if response.status_code == 200:
            return response.json()
        else:
            return (f"Unable to find project", response.status_code)

    def get_project_lookup(self, name, version=None):
        if version == None:
            lookup = "name=" + name
        else:
            lookup = "name=" + name + "&version="+version
        response = self.session.get(
            self.apicall + f"/v1/project/lookup?{lookup}")
        if response.status_code == 200:
            return response.json()
        else:
            return (f"Unable to find project", response.status_code)

    def delete_project_uuid(self, uuid):
        response = self.session.delete(self.apicall + f"/v1/project/{uuid}/")
        if response.status_code == 204:
            return (f"Successfully deleted the project", response.status_code)
        else:
            return (f"Unable to delete the project", response.status_code)

    def create_project(self, name, classifier):
        # TODO add more options
        data = {
            "name": name,
            "classifier": classifier
        }
        response = self.session.put(self.apicall + f"/v1/project", json=data)
        if response.status_code == 201:
            return (f"Successfully created the project", response.status_code)
        elif response.status_code == 409:
            return (f"Project with specified name already exists", response.status_code)
        else:
            return (f"Unable to create the project", response.status_code)

    def update_project(self, uuid, name=None, classifier=None):
        # TODO add more options
        data = {
            "uuid": uuid
        }
        if name:
            data['name'] = name
        if classifier:
            data['classifier'] = classifier
        response = self.session.post(self.apicall + f"/v1/project", json=data)
        if response.status_code == 200:
            return (f"Successfully updated the project", response.status_code)
        elif response.status_code == 404:
            return (f"Project with specified uuid could not be found", response.status_code)
        elif response.status_code == 409:
            return (f"Project with specified name already exists", response.status_code)
        else:
            return (f"Unable to update the project", response.status_code)

    # This section is all about vulnerabilities

    def get_all_vulnerabilities(self, pageSize=100):
        vulnerability_list = list()
        pageNumber = 1
        response = self.session.get(self.apicall + f"/v1/vulnerability", params={
                                    'pageSize': pageSize, 'pageNumber': pageNumber})
        for vul in range(0, len(response.json())):
            vulnerability_list.append(response.json()[vul-1])
        while len(response.json()) == pageSize:
            pageNumber += 1
            response = self.session.get(self.apicall + f"/v1/vulnerability", params={
                                        'pageSize': pageSize, 'pageNumber': pageNumber})
            for vul in range(0, len(response.json())):
                vulnerability_list.append(response.json()[vul - 1])
        if response.status_code == 200:
            return vulnerability_list
        else:
            return (f"Unable to find any vulnerabilities ", response.status_code)

    def get_vulnerability(self, source, vuln):
        """
        this method returns a specific vulnerability
        source:string(to be filled later)
        vuln:string(to be filled later)
        """
        response = self.session.get(
            self.apicall + f"/v1/vulnerability/source/{source}/vuln/{vuln}")
        if response.status_code == 200:
            return response.json()
        else:
            if response.status_code == 401:
                return (f"Unauthorized ", response.status_code)
            else:
                return (f"The vulnerability could not be found ", response.status_code)

    def get_component_vulnerability(self, uuid, supressed=False, pageSize=100):
        """ 
        Returns a list of all vulnerabilities for a specific component.
        uuid:
        supprressed: optionally includes supressed vulnerabilities
        """
        vulnerability_list = list()
        pageNumber = 1
        response = self.session.get(self.apicall + f"/v1/vulnerability/component/{uuid}?supressed={supressed}", params={
                                    "pageSize": pageSize, "pageNumber": pageNumber})
        for vul in range(0, len(response.json())):
            vulnerability_list.append(response.json()[vul-1])
        while len(response.json()) == pageSize:
            pageNumber += 1
            response = self.session.get(self.apicall + f"/v1/vulnerability/component/{uuid}?supressed={supressed}", params={
                                        'pageSize': pageSize, 'pageNumber': pageNumber})
            for vul in range(0, len(response.json())):
                vulnerability_list.append(response.json()[vul - 1])
        if response.status_code == 200:
            return vulnerability_list
        else:
            if response.status_code == 401:
                return (f"Unauthorized", response.status_code)
            elif response.status_code == 403:
                return (f"Access to the specified component is forbidden ", response.status_code)
            else:
                return (f"The component could not be found", response.status_code)

    def get_project_vulnerability(self, uuid, supressed=False, pageSize=100):
        """ 
        Returns a list of all vulnerabilities for a specific project.
        uuid:
        supprressed: optionally includes supressed vulnerabilities(boolean)
        """
        vulnerability_list = list()
        pageNumber = 1
        response = self.session.get(self.apicall + f"/v1/vulnerability/project/{uuid}?supressed={supressed}", params={
                                    "pageSize": pageSize, "pageNumber": pageNumber})
        for vul in range(0, len(response.json())):
            vulnerability_list.append(response.json()[vul-1])
        while len(response.json()) == pageSize:
            pageNumber += 1
            response = self.session.get(self.apicall + f"/v1/vulnerability/project/{uuid}?supressed={supressed}", params={
                                        'pageSize': pageSize, 'pageNumber': pageNumber})
            for vul in range(0, len(response.json())):
                vulnerability_list.append(response.json()[vul - 1])
        if response.status_code == 200:
            return vulnerability_list
        else:
            if response.status_code == 401:
                return (f"Unauthorized", response.status_code)
            elif response.status_code == 403:
                return (f"Access to the specified project is forbidden ", response.status_code)
            else:
                return (f"The project could not be found", response.status_code)

    def get_vulnerability_uuid(self, uuid):
        """
        returns a specific vulnerability
        uuid: The UUID of the vulnerability 
        """
        response = self.session.get(self.apicall + f"/v1/vulnerability/{uuid}")
        if response.status_code == 200:
            return response.json()
        else:
            if response.status_code == 401:
                return (f"Unauthorized", response.status_code)
            else:
                return (f"The vulnerability could not be found ", response.status_code)

    def get_affected_project(self, source, vuln):
        """ 
        Returns a list of all projects affected by a specific vulnerability
        source:
        vuln:
        """
        response = self.session.get(
            self.apicall + f"/v1/vulnerability/source/{source}/vuln/{vuln}/projects")
        if response.status_code == 200:
            return response.json()
        else:
            if response.status_code == 401:
                return (f"Unauthorized", response.status_code)
            else:
                return (f"The vulnerability could not be found ", response.status_code)
    # TODO: POST,POST /v1/vulnerability
    # TODO: DELETE, POST  /v1/vulnerability/source/{source}/vuln/{vulnId}/component/{component}, DELETE, POST /v1/vulnerability/{uuid}/component/{component}

    # this section is all about findings

    def get_project_finding(self, uuid, supressed=False, pageSize=100):
        """ 
        Returns a list of all findings for a specific project.
        uuid:
        supprressed: optionally includes supressed vulnerabilities(boolean)
        """
        finding_list = list()
        pageNumber = 1
        response = self.session.get(self.apicall + f"/v1/finding/project/{uuid}?supressed={supressed}", params={
                                    "pageSize": pageSize, "pageNumber": pageNumber})
        for finding in range(0, len(response.json())):
            finding_list.append(response.json()[finding-1])
        while len(response.json()) == pageSize:
            response = self.session.get(self.apicall + f"/v1/finding/project/{uuid}?supressed={supressed}", params={
                                        "pageSize": pageSize, "pageNumber": pageNumber})
            for finding in range(0, len(response.json())):
                finding_list.append(response.json()[finding-1])
        if response.status_code == 200:
            return finding_list
        else:
            if response.status_code == 401:
                return (f"Unauthorized", response.status_code)
            elif response.status_code == 403:
                return (f"Access to the specified project is forbidden ", response.status_code)
            else:
                return (f"The project could not be found", response.status_code)

    # License

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
        else:
            return (f"Unauthorized ", response.status_code)

    # Metrics

    def get_all_metrics(self, pageSize=100):
        """
        Returns the sum of all vulnerabilities in the database by year and month
        """
        metrics_list = list()
        pageNumber = 1
        response = self.session.get(self.apicall + f"/v1/metrics/vulnerability", params={
                                    "pageSize": pageSize, "pageNumber": pageNumber})
        for metric in range(0, len(response.json())):
            metrics_list.append(response.json()[metric-1])
        while len(response.json()) == pageSize:
            pageNumber += 1
            response = self.session.get(self.apicall + f"/v1/metrics/vulnerability", params={
                                        "pageSize": pageSize, "pageNumber": pageNumber})
            for metric in range(0, len(response.json())):
                metrics_list.append(response.json()[metric-1])
        if response.status_code == 200:
            return metrics_list
        else:
            return (f"Unauthorized ", response.status_code)

    def get_metrics_portolio_bydate(self, date):
        """ 
        Returns historical metrics for the entire portfolio from a specific date.
        date: The start date to retrieve metric. Date format must be YYYYMMDD
        """
        response = self.session.get(
            self.apicall + f"/v1/metrics/portfolio/since/{date}")
        if response.status_code == 200:
            return response.json()
        else:
            return (f"Unauthorized", response.status_code)

    def get_metrics_project_bydate(self, uuid, date):
        """ 
        Returns historical metrics for a specific project from a specific date
        date: The start date to retrieve metric. Date format must be YYYYMMDD.
        uuid: The UUID of the project to retrieve metrics for.
        """
        response = self.session.get(
            self.apicall + f"/v1/metrics/project/{uuid}/since/{date}")
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            return (f"Unauthorized ", response.status_code)
        elif response.status_code == 403:
            return (f"Access to the specified project is forbidden ", response.status_code)
        elif response.status_code == 404:
            return (f"Project not found", response.status_code)
        else:
            return (response.status_code)

    def get_current_metrics_portfolio(self):
        """
        Returns current metrics for entire portfolio
        """
        response = self.session.get(
            self.apicall + f"/v1/metrics/portfolio/current")
        if response.status_code == 200:
            return response.json()
        else:
            return (f"Unauthorized ", response.status_code)

    def get_metrics_dayNumber(self, days):
        """ 
        Returns X days of historical metrics for the entire portfolio(int32)
        days: The number of days back to retrieve metrics for.
        """
        response = self.session.get(
            self.apicall + f"/v1/metrics/portfolio/{days}/days")
        if response.status_code == 200:
            return response.json()
        else:
            return (f"Unauthorized ", response.status_code)

    def get_metrics_refresh_portfolio(self):
        """ 
        Requests a refresh of the portfolio metrics
        """
        response = self.session.get(
            self.apicall + f"/v1/metrics/portfolio/refresh")
        if response.status_code == 200:
            return (f"successful operation ", response.status_code)
        else:
            return (f"Unauthorized ", response.status_code)

    def get_metrics_specific_project(self, uuid):
        """ 
        returns current metrics for a specific project.
        uuid: The UUID of the project to retrieve metrics for
        """
        response = self.session.get(
            self.apicall + f"/v1/metrics/project/{uuid}/current")
        if response.status_code == 200:
            return response.json()
        else:
            return (f"Unauthorized ", response.status_code)

    def get_metrics_specific_project_days(self, uuid, days):
        """ 
        Returns X days of historical metrics for a specific project
        uuid: The UUID of the project to retrieve metrics for.
        days: The number of days back to retrieve metrics for.
        """
        response = self.session.get(
            self.apicall + f"/v1/metrics/project/{uuid}/days/{days}")
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            return (f"Unauthorized ", response.status_code)
        elif response.status_code == 403:
            return (f"Access to the specified project is forbidden ", response.status_code)
        elif response.status_code == 404:
            return (f"Project not found", response.status_code)
        else:
            return (response.status_code)

    def get_metrics_refresh_project(self, uuid):
        """ 
        requests a refresh of a specific project metrics.
        uuid: The UUID of the project to retrieve metrics for.
        """
        response = self.session.get(
            self.apicall + f"/v1/metrics/project/{uuid}/refresh")
        if response.status_code == 200:
            return (f"successful operation ", response.status_code)
        elif response.status_code == 401:
            return (f"Unauthorized ", response.status_code)
        elif response.status_code == 403:
            return (f"Access to the specified project is forbidden ", response.status_code)
        elif response.status_code == 404:
            return (f"Project not found", response.status_code)
        else:
            return (response.status_code)

    def get_current_metrics_component(self, uuid):
        """ 
        Returns current metrics for a specific component
        uuid: The UUID of the component to retrieve metrics for.
        """
        response = self.session.get(
            self.apicall + f"/v1/metrics/component/{uuid}/current")
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            return (f"Unauthorized ", response.status_code)
        elif response.status_code == 403:
            return (f"Access to the specified project is forbidden ", response.status_code)
        elif response.status_code == 404:
            return (f"Project not found", response.status_code)
        else:
            return (response.status_code)

    def get_metrics_component_bydate(self, uuid, date, pageSize=100):
        """
        Returns historical metrics for a specific component from a specific date

        Args:
            uuid (string): The UUID of the component to retrieve metrics for.
            date (string): The start date to retrieve metrics for.(Date format must be YYYYMMDD)
        """
        metrics_list = list()
        pageNumber = 1
        response = self.session.get(self.apicall + f"/v1/metrics/component/{uuid}/since/{date}", params={
                                    "pageSize": pageSize, "pageNumber": pageNumber})
        for metric in range(0, len(response.json())):
            metrics_list.append(response.json()[metric-1])
        while len(response.json()) == pageSize:
            pageNumber += 1
            response = self.session.get(self.apicall + f"/v1/metrics/component/{uuid}/since/{date}", params={
                                        "pageSize": pageSize, "pageNumber": pageNumber})
            for metric in range(0, len(response.json())):
                metrics_list.append(response.json()[metric-1])
        if response.status_code == 200:
            return metrics_list
        else:
            return (f"Unauthorized ", response.status_code)

    def get_metrics_component_bydays(self, uuid, days, pageSize=100):
        """
        Returns X days of historical metrics for a specific component

        Args:
            uuid (string): The UUID of the component to retrieve metrics for.
            days (int32): The number of days back to retrieve metrics for.
        """
        metrics_list = list()
        pageNumber = 1
        response = self.session.get(self.apicall + f"/v1/metrics/component/{uuid}/since/{days}", params={
                                    "pageSize": pageSize, "pageNumber": pageNumber})
        for metric in range(0, len(response.json())):
            metrics_list.append(response.json()[metric-1])
        while len(response.json()) == pageSize:
            pageNumber += 1
            response = self.session.get(self.apicall + f"/v1/metrics/component/{uuid}/since/{days}", params={
                                        "pageSize": pageSize, "pageNumber": pageNumber})
            for metric in range(0, len(response.json())):
                metrics_list.append(response.json()[metric-1])
        if response.status_code == 200:
            return metrics_list
        else:
            return (f"Unauthorized ", response.status_code)

    def get_metrics_component_refresh(self, uuid):
        """[Requests a refresh of a specific components metrics]

        Args:
            uuid ([string]): [The UUID of the component to retrieve metrics for.]

        Returns:
            [string]: [status code]
        """
        response = self.session.get(
            self.apicall + f"/v1/metrics/component/{uuid}/refresh")
        if response.status_code == 200:
            return (f"successful operation ", response.status_code)
        elif response.status_code == 401:
            return (f"Unauthorized ", response.status_code)
        elif response.status_code == 403:
            return (f"Access to the specified project is forbidden ", response.status_code)
        elif response.status_code == 404:
            return (f"Project not found", response.status_code)
        else:
            return (response.status_code)

# TODO: user API

# TODO: violationanalysis API

# TODO: team API

# TODO: service API

# TODO: default API

# TODO: search API

# Repository API
    def get_repository(self, pageSize=100):
        """Returns a list of all repositories

        Args:
            pageSize (int, optional): [description]. Defaults to 100.

        Returns:
            list : list of repositories
        """
        repository_list = list()
        pageNumber = 1
        response = self.session.get(self.apicall + f"/v1/repository", params={"pageSize": pageSize, "pageNumber": pageNumber})
        for repos in range(0,len(response.json)):
            repository_list.append(response.json()[repos-1])
        while len(response.json()) == pageSize:
            pageNumber += 1
        response = self.session.get(
            self.apicall + f"/v1/repository", params={"pageSize": pageSize, "pageNumber": pageNumber})
        for repos in range(0, len(response.json)):
            repository_list.append(response.json()[repos-1])
        if response.status_code == 200:
            return repository_list
        elif response.status_code == 401:
                return (f"Unauthorized ", response.status_code)
    
# TODO: violation API

# TODO: policy API

# TODO: policyCondition API

# TODO: permission API

# TODO: oidc API

# TODO: licenseGroup API

# TODO: ladp API

# TODO: cwe API

# TODO: configProperty API

# TODO: component API

# TODO: calculator API

# TODO: bom API

    # analysis API

    def get_analysis(self, project, component, vulnerability):
        """Retrieves an analysis trail

        Args:
            project (string): The UUID of the project
            component (string): The UUID of the component
            vulnerability (string): The UUID of the vulnerability

        Returns:
            json: 
        """
        response = self.session.get(self.apicall + f"/v1/analysis?project={project}&component={component}&vulnerability={vulnerability}")
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            return (f"Unauthorized ", response.status_code)
        elif response.status_code == 404:
            return (f"The project, component, or vulnerability could not be found ", response.status_code)
        else:
            return response.status_code
    
    def put_analysis(self):
        #Improve the method
        pass


# TODO: badge API

# acl API

    def put_acl(self, team, project):
        """[Adds an ACL mapping]

        Args:
            team ([string]): [name of the team]
            project ([string]): [name of the project]
        """
        
        response = self.session.put(
            self.apicall + "/v1/acl/mappiing", data={"team": team, "project": project})
        
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            return (f"Unauthorized ", response.status_code)
        elif response.status_code == 404:
            return (f"The UUID of the team or project could not be found ", response.status_code)
        elif response.status_code == 409:
            return (f"A mapping with the same team and project already exists ", response.status_code)
        else:
            return response.status_code
            
    def get_acl(self, uuid, excludeInactive=False):
        """[Returns the projects assigned to the specified team]

        Args:
            uuid ([string]): [The UUID of the team to retrieve mappings for]
        """
        response = self.session.get(self.apicall + f"/v1/acl/team/{uuid}?excludeInactive={excludeInactive}")
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            return (f"Unauthorized ", response.status_code)
        elif response.status_code == 404:
            return (f"The UUID of the team could not be found ", response.status_code)

    def delete_acl(self, teamUuid,projectUuid):
        """
        Remove an ACL mapping

        Args:
            teamUuid ([string]): [The UUID of the team to delete the mapping for]
            projectUuid ([string]): [The UUID of the project to delete the mapping for]
        """
        response = self.session.delete(self.apicall + f"/v1/acl/mapping/team/{teamUuid}/project/{projectUuid}")
        if response.status_code == 200:
            return (f"successful operation")
        elif response.status_code == 401:
            return (f"Unauthorized ", response.status_code)
        elif response.status_code == 404:
            return (f"The UUID of the team or project could not be found ", response.status_code)
        else:
            return response.status_code
