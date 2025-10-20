import json


class ViolationAnalysis:

    def record_violation(self, component, policyViolation, suppressed=True):
        """
        Record a violation analysis decision

        Args:
            component (string): The UUID of the component
            policyViolation (string): The UUID of the policy
            suppressed (bool, optional): [description]. Defaults to True.

        Returns:
            dict: decision

        """
        data = {
            "component": component,
            "policyViolation": policyViolation,
            "suppressed": suppressed,
        }
        response = self.session.put(self.apicall + "/v1/violation/analysis", data=json.dumps(data))
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            return (f"Unauthorized, {response.status_code}")
        return (f"{(response.content).decode('utf-8')}, {response.status_code}")

    def get_violation_analysis(self, component, policyViolation):
        """
        Retrieve a violation analysis trail

        Args:
            component (string): The UUID of the component
            policyViolation (string): The UUID of the policy
            suppressed (bool, optional): [description]. Defaults to True.

        Returns:
            dict: analysis

        """
        response = self.session.get(self.apicall + "/v1/violation/analysis", params={"component": component, "policyViolation": policyViolation})
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            return (f"Unauthorized, {response.status_code}")
        return (f"{(response.content).decode('utf-8')}, {response.status_code}")
