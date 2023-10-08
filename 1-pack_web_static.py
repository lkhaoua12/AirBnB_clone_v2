#!/usr/bin/python3
""" using fabric to compress webstatic files"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """ compress files of webstatic for deployment """

    # get the timestamp for archive name.
    timestamp = datetime.now().strftime('Y%m%d%H%M%S')

    # set the archive full path
    full_path = f'versions/web_static_{timestamp}.tgz'

    # create folder versions if not exist
    local("mkdir -p versions/")

    # compress webstatic to the desired directory
    result = local(f'tar -cvzf {full_path} webstatic')
    if result.succeeded:
        return full_path
