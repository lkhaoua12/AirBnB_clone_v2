from fabric.api import local
from datetime import datetime

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
