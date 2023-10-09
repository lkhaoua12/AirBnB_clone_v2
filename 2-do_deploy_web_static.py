#!/usr/bin/python3
""" compress web_static folder before deployment """

from fabric.api import local, put, env, run
from datetime import datetime
from os.path import exists


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
    """ Distribute an archive to web servers """
    if not exists(archive_path):
        return False

    env.hosts = ['100.26.153.177', '34.201.165.226']
    try:
        # Upload the archive to /tmp/ directory
        put(archive_path, '/tmp/')

        # Extract the archive to /data/web_static/releases/
        archive_name = archive_path.split('/')[-1]
        folder_name = archive_path.replace('.tgz', '')
        releases_path = '/data/web_static/releases/'

        run('mkdir -p {}{}/'.format(releases_path, folder_name))
        run(f'tar -xzf /tmp/{archive_name} -C {releases_path}{folder_name}/')

        # delete archive from server
        run(f'rm -rf /tmp/{archive_name}')

        # delete old symlink and create new one
        current_path = '/data/web_static/current'
        run(f'rm -rf {current_path}')
        run(f'ln -s {releases_path}{folder_name}/ {current_path}')

        return True
    except Exception:
        return False
