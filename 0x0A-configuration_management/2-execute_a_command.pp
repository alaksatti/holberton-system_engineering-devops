# kill a process using pkil
exec { 'killmenow':
  command => 'pkill killmenow',
  path    => [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ]
}