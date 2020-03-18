Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.provision :shell, path: "setup.sh", :privileged => false 
  #config.vm.network :public_network, ip: "192.168.50.6"
  config.vm.network :private_network, ip: "192.168.50.6"
  config.vm.network :forwarded_port, guest: 5000, host: 5000
  config.vm.provider "virtualbox" do |v|
    v.gui = false
    v.name = "Edison"
    v.memory = 1024
    v.cpus = 2
  end 

end
