# erth eth etyh ety h
package { 'python3-pip':
  ensure => installed,
}

exec { 'install_flask_deps':
  command => '/usr/bin/pip3 install Flask==2.1.0 Werkzeug==2.1.1',
  require => Package['python3-pip'],
}
