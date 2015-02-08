# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
    config.vm.box = "parserby/wheezy64-ansible"
    config.vm.network :private_network, ip: "192.168.50.30"

    config.vm.provision :ansible do |ansible|
        ansible.playbook = "provisioning/machine.yml"
    end
end
