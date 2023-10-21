# dependencytrack-pywrap
[Dependency-Track](https://docs.dependencytrack.org/integrations/rest-api/) is a platform to analyse risks in your dependencies.
This project is a python wrapper for the [Dependency-Track REST API](https://docs.dependencytrack.org/integrations/rest-api/). 

## Quick Start

```python
# Import DependencyTrackAPI and use the right port for apiurl. 
from main import DependencyTrackAPI
dta = DependencyTrackAPI(apiurl = 'the api url', apikey = 'see dependency track')
# Return the Version
dta.version()
# Return a list of all projects
dta.list_projects()
# Return the project from a projectname and version
dta.get_project_lookup(name="project", version="1.0")
# Return the Project from the uuid
dta.get_project(uuid='project_uuid')
# Delete project with uuid
dta.delete_project_uuid('project_uuid')
# Create a new project
dta.create_project(name="testproject",classifier = "APPLICATION")
# Update a new project
dta.update_project(uuid="project_uuid",name="newprojectname")
```