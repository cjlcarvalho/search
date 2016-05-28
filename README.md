Simple Search Engine
===

This is a simple search engine project working with Solr, built in Python 2.7 with [web.py](http://webpy.org/) and [PySolarized](https://github.com/izacus/pysolarized).

Requirements:
---

* Python 2.7+

* Solr 6.0.0+

* OpenJDK (because Solr needs it)
 
* Docker (if you want to run with the container)

Configuration commands:
---

* Downloading and configuring Solr:

    `wget http://ftp.unicamp.br/pub/apache/lucene/solr/6.0.0/solr-6.0.0.tgz`

    `tar zxvf solr-6.0.0.tgz`

    `cd solr-6.0.0`
 
    `bin/solr start`

    `bin/solr create -c entities`

    `cd ..`

* Cloning the project and installing the required libraries:
 
    `git clone https://github.com/cjlcarvalho/SimpleSearchEngine`

    `cd SimpleSearchEngine`

    `pip2 install -r requirements.txt`


Running the web server:
---

`python2 code.py`

After this command, your webserver will be running in http://0.0.0.0:8080/ or http://localhost:8080/.


Running the tests:
---

`(TO BE DONE)`


Running with Docker:
---

* Build the Docker image:

    `cd Dockerfile`
    
    `docker build -t=caiojcarvalho/container .`

* Create the container and use the container's terminal:

    `docker run -i -t -p 8080:8080 caiojcarvalho/container`

* In the container's terminal, run these commands:

    `# solr-6.0.0/bin/solr start`
    
    `# solr-6.0.0/bin/solr create -c entities`
    
    `# python SimpleSearchEngine/code.py`
