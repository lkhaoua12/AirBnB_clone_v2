#!/usr/bin/python3
""" compress web_static folder before deployment """

from fabric.api import run, env, put, local
from datetime import datetime
import os


env.hosts = ['100.26.153.177', '34.201.165.226']


def do_pack():
    """
    Create a .tgz archive from the contents of the web_static folder.
    """

    # Get the current date and time
    now = datetime.now()

    # Create a formatted timestamp
    timestamp = now.strftime("%Y%m%d%H%M%S")

    # Define the archive path
    archive_path = "versions/web_static_{}.tgz".format(timestamp)

    # Create the versions directory if it doesn't exist
    local("mkdir -p versions")

    # Compress the web_static folder into a .tgz archive
    result = local("tar -cvzf {} web_static".format(archive_path))

    # Check if the archive was created successfully
    if result.succeeded:
        return archive_path
    else:
        return None

def do_deploy(archive_path):
    """ """
    arc_path = 'versions/web_static_20221214143240.tgz'
    filename = arc_path.split('/')[-1]
    no_ext = filename.split('.')[0]
    path = '/data/web_static/releases/'

    if os.path.exists(archive_path) is False:
        return False
    else:
        try:
            put(archive_path, '/tmp/')
            run(f'sudo mkdir -p {path}{filename}')
            run(f'sudo tar -xzf /tmp/{arc_path} -C {path}{no_ext}')
            run(f'sudo rm /tmp/{filename}')
            run(f'sudo mv {path}{no_ext}/web_static/* {path}{no_ext}/')
            run(f'sudo rm -rf {path}{no_ext}/web_static')
            run(f'sudo rm -rf /data/web_static/current')
            run(f'sudo ln -s {path}{no_ext} /data/web_static/current')
            return True
        except Exception:
            return False
