# xtfghrs dhtsrt hdrt hsrt
exec { 'killmenow':
  command     => 'pkill -f killmenow || true',
  refreshonly => true,
  onlyif      => 'pgrep -f killmenow',
}
