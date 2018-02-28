# Install bridge builder

## Create a virtual environment
### Install virtual env into the os
#### ubuntu > 16.04
`sudo apt-get install virtualenv`

### install virtual env wrapper
[-> more on virtualenvwrapper](http://virtualenvwrapper.readthedocs.io/en/latest/install.html)  
`pip install --user virtualenvwrapper`

now make Bash load it automatically at login time:  
`echo "source virtualenvwrapper.sh" >> ~/.bashrc`  
Now when you *open a new shell* workon is ready for you to use.

### create a virtual env to use while working with bridge-builder
`mkvirtualenv --python=python3.6 bridgebuilder`  
We now can use this virtual environment by executing  
`workon bridgebuilder`  
and leave it again:  
`deactivate`  
or just run workon with the name of an other environment. Very handy!

As good python citizen we set up a test environment as our very next step now. To learn how to to that, head over to [Test/Readme.md](./tests/Readme.md)

## make bin/python and bin/pip point to ists correct environment
Activate a virtual env with `ẁorkon bridgebuilder`
execute `bin/set_python.py`

## create entries for pip and python in the bin directory
# this is not strictly nessecary, but ofthen convinient
`bin/set_python.py`

## install all libraries bridgebuilder needs
`pip install -r install/requirements.txt`


