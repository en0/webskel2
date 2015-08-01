This is a basic template I like to keep on hand for starting new web based projects.  
It uses Python flask and AngularJS.  I attempted to separate the API
and UI code in the python in such a way that they are independent.
Modifications have been made to angular to so that it plays nice with jinja2.

# Quick Start
To get up and developing your new awesome project, the simplest thing to do is
build the docker file and mount the containers file system back onto your host. This
provides a consistent platform and avoids library dependencies while maintaining
portability.

```bash
# Build the docker container
$ docker build -t MyAwesomeProject:devel .
# Run with mount on port 80 (might need to use a diffrent port)
$ docker run -ti -d -p 80:5000 -v $(pwd)/src:/srv/http MyAwesomeProject:devel

# Project Structure
WIP: Define the project structure
