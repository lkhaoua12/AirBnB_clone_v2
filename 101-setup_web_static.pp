# Puppet script to configure web servers for web_static deployment

# Update package repositories
exec { 'apt-update':
  command     => 'apt update -y',
  path        => '/usr/bin',
  refreshonly => true,
}

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
    Hlberton Coding School, Alx
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

# Add Nginx configuration
file { '/etc/nginx/sites-available/default':
  ensure  => 'file',
  content => template('your_module/nginx_config.erb'),
  notify  => Service['nginx'],
}

# Ensure the Nginx service is running
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  require   => File['/etc/nginx/sites-available/default'],
}
