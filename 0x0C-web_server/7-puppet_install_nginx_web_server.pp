# Update the system using apt-get update
# Install the nginx package
exec { 'update system':
	command => '/usr/bin/apt-get update',
}

# Install the nginx package
package { 'nginx':
	ensure => 'installed',
	require => Exec['update system']
}

# Create the index.html file with "Hello World!" content
file {'/var/www/html/index.html':
	content => 'Hello World!'
}

# Add a redirect rule to the nginx configuration file
exec {'redirect_me':
	command => 'sed -i "24i\    rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4/ permanent;" /etc/nginx/sites-available/default',
	provider => 'shell'
}

# Add an HTTP header to the nginx configuration file
exec {'HTTP header':
	command => 'sed -i "25i\    add_header X-Served-By \$hostname;" /etc/nginx/sites-available/default',
	provider => 'shell'
}

# Ensure the nginx service is running
service {'nginx':
	ensure => running,
	require => Package['nginx']
}
