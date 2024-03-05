# Install nginx
package { 'nginx':
	ensure => installed,
}

# Configure nginx to listen on port 80
file { '/etc/nginx/sites-available/default':
	ensure  => file,
	content => "server {\n  listen 80;\n  server_name _;\n\n  location / {\n    return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\n  }\n\n  location /redirect_me {\n    return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\n  }\n\n  error_page 404 /404.html;\n  location = /404.html {\n    root /usr/share/nginx/html;\n    internal;\n    return 404 'Ceci n\'est pas une page';\n  }\n}\n",
	notify  => Exec['restart_nginx'],
}

# Restart nginx
exec { 'restart_nginx':
	command     => '/etc/init.d/nginx restart',
	refreshonly => true,
}

# Create custom 404 page
file { '/usr/share/nginx/html/404.html':
	ensure  => file,
	content => 'Ceci n\'est pas une page',
}
