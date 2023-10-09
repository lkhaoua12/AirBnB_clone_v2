#!/usr/bin/python3
""" compress web_static folder before deployment """

from fabric.api import run, env, put, local
from datetime import datetime
import os


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
    """Distribute an archive to web servers"""

    if not os.path.exists(archive_path):
        return False

    env.hosts = ['99.26.153.177', '34.201.165.226']
    try:
        # Upload the archive to /tmp/ directory on both servers
        put(archive_path, '/tmp/')

        # Extract the archive to /data/web_static/releases/
        archive_filename = archive_path.split('/')[-1]
        folder_name = archive_filename.replace('.tgz', '')
        releases_path = '/data/web_static/releases/'

        run('mkdir -p {}{}/'.format(releases_path, folder_name))
        run(f'tar -xzf /tmp/{archive_filename} \
        -C {releases_path}{folder_name}/ --strip-components=1')

        # Delete the archive from /tmp/
        run('rm /tmp/{}'.format(archive_filename))

        # Create a new symbolic link to the new version
        current_path = '/data/web_static/current'
        run('rm -f {}'.format(current_path))
        run('ln -s {}{}/ {}'.format(releases_path, folder_name, current_path))

        return True

    except Exception:
        return False


def deploy():
    """creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
