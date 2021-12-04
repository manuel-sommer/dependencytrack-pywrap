import requests
from apicomponents.analysis import DependencyTrackAnalysis
from apicomponents.badge import DependencyTrackbadge
from apicomponents.ldap import DependencyTrackLDAP
from apicomponents.policy import DependencyTackPolicy
from apicomponents.project import DependencyTrackProject
from apicomponents.projectProperty import DependencyTrackProjectProperty
from apicomponents.repository import DependencyTrackRepository
from apicomponents.service import DependencyTrackService
from apicomponents.violation import DependencyTrackViolation
from apicomponents.violationAnalysis import DependencyTrackViolationAnalysis
from apicomponents.vulnerability import DependencyTrackVulnerability
from apicomponents.finding import DependencyTrackFinding
from apicomponents.license import DependencyTrackLicense
from apicomponents.metrics import DependencyTrackMetrics
from apicomponents.acl import DependencyTrackACL
from apicomponents.bom import DependencyTrackBom
from apicomponents.cwe import DependencyTrackCWE
from apicomponents.configproperty import DependencyTrackConfigProperty
from apicomponents.calculator import DependencyTrackCalculator
from apicomponents.team import DependencyTrackTeam
from apicomponents.permission import DependencyTrackPermission

class DependencyTrackAPI(DependencyTrackProject, DependencyTrackProjectProperty, DependencyTrackVulnerability, DependencyTrackFinding, DependencyTrackLicense, DependencyTrackMetrics, DependencyTrackACL, DependencyTrackBom, DependencyTrackCWE, DependencyTrackConfigProperty, DependencyTrackbadge, DependencyTrackCalculator, DependencyTrackTeam, DependencyTrackPermission, DependencyTrackLDAP, DependencyTrackService, DependencyTrackViolation, DependencyTrackRepository,DependencyTrackAnalysis, DependencyTackPolicy, DependencyTrackViolationAnalysis):
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

#// TODO: team API
# // TODO: service API
#  TODO: improve service API

# TODO: default API

# TODO: search API

# // TODO advance Repository API and put into apicomponents

# // TODO: violation API

# // TODO: policy API

# TODO: policyCondition API

#// TODO: permission API

# TODO: oidc API

# TODO: licenseGroup API

# // TODO: ladp API

# TODO: component API

# // TODO: calculator API

# // TODO improve analysis API and put into apicomponents
