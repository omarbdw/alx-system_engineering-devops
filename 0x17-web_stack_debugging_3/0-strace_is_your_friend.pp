# 0-strace_is_your_friend.pp

# Install Apache package
package { 'apache2':
	ensure => installed,
}

# Configure Apache virtual host
file { '/etc/apache2/sites-available/your_website.conf':
	ensure  => present,
	content => "# Your Apache virtual host configuration goes here",
	require => Package['apache2'],
}

# Enable the virtual host
exec { 'enable_virtual_host':
	command     => 'a2ensite your_website.conf',
	path        => '/usr/sbin:/usr/bin:/sbin:/bin',
	refreshonly => true,
	require     => File['/etc/apache2/sites-available/your_website.conf'],
}

# Restart Apache service
service { 'apache2':
	ensure    => running,
	enable    => true,
	subscribe => Exec['enable_virtual_host'],
}