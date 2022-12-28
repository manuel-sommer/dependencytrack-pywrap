import requests
from apicomponents.analysis import Analysis
from apicomponents.badge import Badge
from apicomponents.ldap import LDAP
from apicomponents.licensegroup import LicenseGroup
from apicomponents.policy import Policy
from apicomponents.project import Project
from apicomponents.projectProperty import ProjectProperty
from apicomponents.repository import Repository
from apicomponents.service import Service
from apicomponents.violation import Violation
from apicomponents.violationAnalysis import ViolationAnalysis
from apicomponents.vulnerability import Vulnerability
from apicomponents.finding import Finding
from apicomponents.license import License
from apicomponents.metrics import Metrics
from apicomponents.acl import ACL
from apicomponents.bom import Bom
from apicomponents.cwe import CWE
from apicomponents.configproperty import ConfigProperty
from apicomponents.calculator import Calculator
from apicomponents.team import Team
from apicomponents.permission import Permission
from apicomponents.search import Search
from apicomponents.user import User

class DependencyTrackAPI(Project, ProjectProperty, Vulnerability, Finding, License, Metrics, ACL, Bom, CWE, ConfigProperty, Badge, Calculator, Team, Permission, LDAP, Service, Violation, Repository,Analysis, Policy, ViolationAnalysis,LicenseGroup,Search,User):
    def __init__(self, apiurl, apikey):
        self.apiurl = apiurl
        self.apikey = apikey
        self.apicall = self.apiurl + "/api"
        self.session = requests.Session()
        self.session.headers.update({"X-Api-Key": f"{self.apikey}"})
        self.session.headers.update({"Content-Type": "application/json"})

    def version(self):
        response = self.session.get(self.apicall + "/version")
        return response.json()

# TODO: user API
# TODO: violationanalysis API
# TODO: team API
# TODO: service API
# TODO: improve service API
# TODO: default API
# TODO: search API
# TODO: advance Repository API and put into apicomponents
# TODO: violation API
# TODO: policy API
# TODO: policyCondition API
# TODO: permission API
# TODO: oidc API
# TODO: licenseGroup API
# TODO: ladp API
# TODO: component API
# TODO: calculator API
# TODO: improve analysis API and put into apicomponents