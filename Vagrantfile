# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  # use default box
  config.vm.box = "ubuntu/trusty64"

  # port 5000 is flasks default port
  config.vm.network "forwarded_port", guest: 5000, host: 5000

  # install & configure required software
  config.vm.provision :shell, :path => "bootstrap.sh"
end
