# This is a simple example of how to use the exec resource to run a command on a node.

exec { 'fix_phpp':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => ['/bin', '/usr/bin/', '/usr/loca/bin/'],
}
