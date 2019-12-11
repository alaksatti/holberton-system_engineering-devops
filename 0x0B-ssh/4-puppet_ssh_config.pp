# using Puppet to make changes to our configuration file.
file_line { 'private key - ~/.ssh/holberton':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/holberton',
}


file_line { 'Refuse authentication via password':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
}