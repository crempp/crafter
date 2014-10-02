Crafter
=======

A web-based Minecraft status monitor.

Requirements
------------
* PHP (for the web interface)
* Python (for the polling script and overviewer)


Requirements
----
* Java
* Python 2.7+, 3.2+
* libmysqlclient-dev (```sudo apt-get install libmysqlclient-dev```)
* python-dev (```sudo apt-get install python-dev```)
* libjpeg-dev zlib1g-dev (```sudo apt-get install  libjpeg-dev zlib1g-dev```)
* pip (```sudo apt-get install  libjpeg-dev zlib1g-dev```)
* screen (for the minecraft server bootup script)
* ... the rest will be taken care of by pip

Quickstart
----

To bootstrap the project:
```
  cd path/to/crafter
  virtualenv env
  source env/bin/activate
  pip install -r requirements.txt
  cd crafter_project
  ./manage.py syncdb --migrate
  #./manage.py loaddata initial_vsn.json
```

Run tests
  ./manage.py test vsnlookup

Run the server
  ./manage.py runserver 8080

