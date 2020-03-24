Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-18.04"
  config.vm.box_version = "202002.14.0"
  config.vm.provision :shell, path: "setup.sh", :privileged => false 
  config.vm.network :forwarded_port, guest: 5000, host: 5000, host_ip: "127.0.0.1"
  config.vm.provider "virtualbox" do |v|
    v.gui = false
    v.name = "Edison_test"
    v.memory = 1024
    v.cpus = 2
  end 

end
