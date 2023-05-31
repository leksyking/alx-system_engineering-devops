# Here is a puppet manuscript to replace a line in a file on a server

# replace line containing 'phpp' with 'php'

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}