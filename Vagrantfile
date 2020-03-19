Vagrant.configure("2") do |config|
  ## NOTE: Following initial 'vagrant up', after saving and configuring an image 
  ##    of the guest machine; change config.vm.box to the following: 
  ##    config.vm.box = "<image-name without .box suffix>"
  ## Eexample:
  ##    config.vm.box = "edison_ubuntu-xenial64"
  config.vm.box = "ubuntu/xenial64"
  config.vm.provision :shell, path: "setup.sh", :privileged => false 
  config.vm.network :private_network, ip: "192.168.50.6"
  config.vm.network :forwarded_port, guest: 5000, host: 5000
  config.vm.provider "virtualbox" do |v|
    v.gui = false
    v.name = "Edison"
    v.memory = 1024
    v.cpus = 2
  end 

end
