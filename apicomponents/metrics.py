class Metrics:

    def get_all_metrics(self, pageSize=100):
        """
        Returns the sum of all vulnerabilities in the database by year and month
        """
        metrics_list = list()
        pageNumber = 1
        response = self.session.get(self.apicall + "/v1/metrics/vulnerability", params={
                                    "pageSize": pageSize, "pageNumber": pageNumber})
        for metric in range(len(response.json())):
            metrics_list.append(response.json()[metric - 1])
        while len(response.json()) == pageSize:
            pageNumber += 1
            response = self.session.get(self.apicall + "/v1/metrics/vulnerability", params={
                                        "pageSize": pageSize, "pageNumber": pageNumber})
            for metric in range(len(response.json())):
                metrics_list.append(response.json()[metric - 1])
        if response.status_code == 200:
            return metrics_list
        return (f"Unauthorized, {response.status_code}")

    def get_metrics_portolio_bydate(self, date):
        """
        Returns historical metrics for the entire portfolio from a specific date.
        date: The start date to retrieve metric. Date format must be YYYYMMDD
        """
        response = self.session.get(
            self.apicall + f"/v1/metrics/portfolio/since/{date}")
        if response.status_code == 200:
            return response.json()
        return (f"Unauthorized, {response.status_code}")

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
        if response.status_code == 401:
            return (f"Unauthorized , {response.status_code}")
        if response.status_code == 403:
            return (f"Access to the specified project is forbidden, {response.status_code}")
        if response.status_code == 404:
            return (f"Project not found, {response.status_code}")
        return (response.status_code)

    def get_current_metrics_portfolio(self):
        """
        Returns current metrics for entire portfolio
        """
        response = self.session.get(
            self.apicall + "/v1/metrics/portfolio/current")
        if response.status_code == 200:
            return response.json()
        return (f"Unauthorized , {response.status_code}")

    def get_metrics_dayNumber(self, days):
        """
        Returns X days of historical metrics for the entire portfolio(int32)
        days: The number of days back to retrieve metrics for.
        """
        response = self.session.get(
            self.apicall + f"/v1/metrics/portfolio/{days}/days")
        if response.status_code == 200:
            return response.json()
        return (f"Unauthorized , {response.status_code}")

    def get_metrics_refresh_portfolio(self):
        """
        Requests a refresh of the portfolio metrics
        """
        response = self.session.get(
            self.apicall + "/v1/metrics/portfolio/refresh")
        if response.status_code == 200:
            return (f"successful operation , {response.status_code}")
        return (f"Unauthorized , {response.status_code}")

    def get_metrics_specific_project(self, uuid):
        """
        Returns current metrics for a specific project.
        uuid: The UUID of the project to retrieve metrics for
        """
        response = self.session.get(
            self.apicall + f"/v1/metrics/project/{uuid}/current")
        if response.status_code == 200:
            return response.json()
        return (f"Unauthorized , {response.status_code}")

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
        if response.status_code == 401:
            return (f"Unauthorized , {response.status_code}")
        if response.status_code == 403:
            return (f"Access to the specified project is forbidden, {response.status_code}")
        if response.status_code == 404:
            return (f"Project not found, {response.status_code}")
        return (response.status_code)

    def get_metrics_refresh_project(self, uuid):
        """
        Requests a refresh of a specific project metrics.
        uuid: The UUID of the project to retrieve metrics for.
        """
        response = self.session.get(
            self.apicall + f"/v1/metrics/project/{uuid}/refresh")
        if response.status_code == 200:
            return (f"successful operation , {response.status_code}")
        if response.status_code == 401:
            return (f"Unauthorized , {response.status_code}")
        if response.status_code == 403:
            return (f"Access to the specified project is forbidden , {response.status_code}")
        if response.status_code == 404:
            return (f"Project not found, {response.status_code}")
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
        if response.status_code == 401:
            return (f"Unauthorized , {response.status_code}")
        if response.status_code == 403:
            return (f"Access to the specified project is forbidden , {response.status_code}")
        if response.status_code == 404:
            return (f"Project not found, {response.status_code}")
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
        for metric in range(len(response.json())):
            metrics_list.append(response.json()[metric - 1])
        while len(response.json()) == pageSize:
            pageNumber += 1
            response = self.session.get(self.apicall + f"/v1/metrics/component/{uuid}/since/{date}", params={
                                        "pageSize": pageSize, "pageNumber": pageNumber})
            for metric in range(len(response.json())):
                metrics_list.append(response.json()[metric - 1])
        if response.status_code == 200:
            return metrics_list
        return (f"Unauthorized , {response.status_code}")

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
        for metric in range(len(response.json())):
            metrics_list.append(response.json()[metric - 1])
        while len(response.json()) == pageSize:
            pageNumber += 1
            response = self.session.get(self.apicall + f"/v1/metrics/component/{uuid}/since/{days}", params={
                                        "pageSize": pageSize, "pageNumber": pageNumber})
            for metric in range(len(response.json())):
                metrics_list.append(response.json()[metric - 1])
        if response.status_code == 200:
            return metrics_list
        return (f"Unauthorized, {response.status_code}")

    def get_metrics_component_refresh(self, uuid):
        """
        [Requests a refresh of a specific components metrics]

        Args:
            uuid ([string]): [The UUID of the component to retrieve metrics for.]

        Returns:
            [string]: [status code]
        """
        response = self.session.get(
            self.apicall + f"/v1/metrics/component/{uuid}/refresh")
        if response.status_code == 200:
            return (f"successful operation, {response.status_code}")
        if response.status_code == 401:
            return (f"Unauthorized, {response.status_code}")
        if response.status_code == 403:
            return (f"Access to the specified project is forbidden, {response.status_code}")
        if response.status_code == 404:
            return (f"Project not found, {response.status_code}")
        return (response.status_code)
