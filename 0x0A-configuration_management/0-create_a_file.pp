# A puppet manifest that creates a file school in /tmp.
# The file school, has permission 0744 belonging to both the owner and group
file { '/tmp/school':
  ensure  => present,
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
