This is a basic template I like to keep on hand for starting new web based projects.  
It uses Python flask and AngularJS. It uses the blueprints model and has some
handy wrappers for config parseing (as ini, i very much dislike flask native
configuration handling) and a generic structured data wrapper.

# Quick Start
To get up and developing your new awesome project, the simplest thing to do is
build the docker file and mount the containers file system back onto your host. This
provides a consistent platform and avoids library dependencies while maintaining
portability. If your editor has as completer, you might also benifit from
setting up a vertual environment and installing requirements.txt.

Note: env/ is excluded in .gitignore.

## Editor environment
Create a vertual environment for facilitate editor completers.

```bash
# From project root:
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

## Configuration Generation.
You will need [config-gen](https://github.com/en0/config-gen) setup and loaded with the appropriate keys.

```bash
# From project root:
$ config-gen
```

## Runtime Environment
Build the docker container and run it with a back-mount to your development
directory.

```bash
# From project root:
$ ./helper.sh build
$ ./helper.sh debug
```
