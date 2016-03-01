from fabric.api import *

def pack():
    # create a new source distribution as tarball
    local('python setup.py sdist --formats=gztar', capture=False)

def local_store(sha):
    '''Stores application package into artifact repository and updates
    'current' symbolic link
    '''
    fullname = local('python setup.py --fullname', capture=True).strip()
    local(
            'mkdir -p /www/data/artifacts/{}/{}'.format(fullname, sha)
       )

    cmd = 'cp dist/{}.tar.gz '.format(fullname)
    cmd +=  '/www/data/artifacts/{}/{}/'.format(fullname, sha)
    local(cmd)

    with settings(warn_only=True):
        local('rm /www/data/artifacts/current') # can fail

    cmd = 'ln -s /www/data/artifacts/{}/{} '.format(fullname,sha)
    cmd += '/www/data/artifacts/current'
    local(cmd)

def deploy(sha, repository='http://sjudeu.sk/artifacts'):
    fullname = local('python setup.py --fullname', capture=True).strip()
    dist_url = '{repo}/{name}/{sha}/{name}.tar.gz'.format(
            repo=repository,
            sha=sha,
            name=fullname)

    # grab the notebook package from binary repository
    run('mkdir /tmp/notebook')
    run('wget -P /tmp/notebook/ {dist}'.format(dist=dist_url))

    with cd('/tmp/notebook'):
        run('tar xzf {}.tar.gz'.format(fullname))
        # now setup the package with our virtual environment's
        # python interpreter
        with cd(fullname):
            run('/www/notebook/venv/bin/python setup.py install')

    # now that all is set up, delete the folder again
    run('rm -rf /tmp/notebook')
    # restart uwsgi
    # sudo('service apache2 restart')

def clean():
    # remove sdist
    # remove build
    # remove unit tests reports
    pass

def init_server():
    # create virtualenv
    # install dependencies
    # set up nginx configuration
    # other things?
    pass
