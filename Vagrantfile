Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.provision :shell, path: "setup.sh"
  config.vm.network :forwarded_port, guest: 5000, host: 5000, host_ip: "127.0.0.1"
  config.vm.provider "virtualbox" do |v|
    v.name = "Edison"
    v.memory = 1024
    v.cpus = 2
  end 

end
