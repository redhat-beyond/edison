CLIENT_PORT=5000
BE_PORT=3000

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/bionic64"
  config.vm.provision :shell, path: "setup.sh"
  config.vm.network :forwarded_port, guest: CLIENT_PORT, host: CLIENT_PORT
  config.vm.network :forwarded_port, guest: BE_PORT, host: BE_PORT
  config.vm.provider "virtualbox" do |v|
    v.gui = false
    v.name = "Edison_test"
    v.memory = 1024
    v.cpus = 2
  end 

end
