# dependencytrack-pywrap
This is a python wrapper for the dependency track REST API. 

## Quick Start

```python
dta = DependencyTrackAPI(apiurl = 'the api url', apikey = 'see dependency track')
# Return the Version
dta.version()
# Return a list of all projects
dta.list_projects()
# Return the UUID from a projectname
project_uuid = dta.get_uuid_from_projectname("TestProjectName")
# Return the Project from the uuid
dta.get_project(uuid=project_uuid)
```