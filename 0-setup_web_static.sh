#!/usr/bin/env bash
# setup nginx for webstatic deployment

# Install nginx if not alredy installed.
if ! command -v nginx &> /dev/null
then
	apt-get -y update
	apt-get install -y nginx
fi

# create directory data and it subdirectories
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

# create an index.html to check on nginx 
echo "Hello From webstatic" | tee -a /data/web_static/releases/test/index.html

# create a symnolic link. If the symbolic link already exists, it should be deleted and recreated every time the script is ran. 
rm -rf /data/web_static/current
ln -s /data/web_static/releases/test/ /data/web_static/current

#Give ownership of the /data/ folder to the ubuntu user AND group (you can assume this user and group exist). 
#This should be recursive; everything inside should be created/owned by this user/group
chown -R mehdi:mehdi /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static 
# (ex: https://mydomainname.tech/hbnb_static). Don’t forget to restart Nginx after updating the configuration:
# Use alias inside your Nginx configuration
config_file="/etc/nginx/sites-available/default"
if ! grep -q "location /hbnb_static" $config_file
then
	sed -i '/server {/a \
    location /hbnb_static {\
        alias /data/web_static/current/;\
    }' $config_file
fi

# restart Nginx to apply the changes
service nginx restart



