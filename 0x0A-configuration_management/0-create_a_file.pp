# The code creates a file /tmp using puppet
file { '/tmp/school':
  ensure  => 'file',
  content => 'I love Puppet',
  path    => '/tmp/school',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
} 
