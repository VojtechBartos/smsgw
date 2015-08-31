# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
    config.vm.box = "/Users/vojtechbartos/Development/_boxes/debian-7.2.0.box"
    config.vm.network :private_network, ip: "192.168.50.100"

    config.vm.provision :ansible do |ansible|
        ansible.playbook = "provisioning/machine.yml"
    end

    config.vm.synced_folder "./", "/smsgw/",
      rsync__auto: true,
      rsync__exclude: [".git/", "node_modules/", "venv/"]
end
