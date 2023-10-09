# Puppet script to configure web servers for web_static deployment

# Install Nginx
package { 'nginx':
  ensure => 'installed',
}

# Create directories
file { ['/data/web_static/releases/test/', '/data/web_static/shared']:
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0755',
  recurse => true,
}

# Create index.html
file { '/data/web_static/releases/test/index.html':
  content => '<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0644',
}

# Create a symbolic link
file { '/data/web_static/current':
  ensure  => 'link',
  target  => '/data/web_static/releases/test/',
  owner   => 'ubuntu',
  group   => 'ubuntu',
}
# Add the location block to the Nginx configuration
exec { 'add_location_block':
  command => '/bin/echo "        location /hbnb_static {\n                alias /data/web_static/current;\n        }" >> /etc/nginx/sites-enabled/default',
  unless  => '/bin/grep -q "location /hbnb_static {" /etc/nginx/sites-enabled/default',
  require => Package['nginx'],
}

# Ensure the Nginx service is running
service { 'nginx':
  ensure    => 'running',
  enable    => true,
}
