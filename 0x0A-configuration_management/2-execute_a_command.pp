# This code createsa maifest that kills a process 'killmenow' using Puppet

exec { 'kill':
  command => 'pkill -f killmenow',
  path    => ['/bin', '/usr/bin'],
}
