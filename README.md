# dependencytrack-pywrap
This is a python wrapper for the dependency track REST API. 

## Quick Start

```python
dta = DependencyTrackAPI(apiurl = 'the api url', apikey = 'see dependency track')
# Return the Version
dta.version()
# Return a list of all projects
dta.list_projects()
# Return the project from a projectname and version
dta.get_project_lookup(name="project", version="1.0")
# Return the Project from the uuid
dta.get_project(uuid=project_uuid)
```