FLASK_PORT=5000
POSTGRESQL_PORT=5432

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/bionic64"
  config.vm.provision :shell, path: "setup.sh"
  config.vm.network :forwarded_port, guest: FLASK_PORT, host: FLASK_PORT
 config.vm.network :forwarded_port, guest: POSTGRESQL_PORT, host: POSTGRESQL_PORT
  config.vm.provider "virtualbox" do |v|
    v.gui = false
    v.name = "Edison_test"
    v.memory = 1024
    v.cpus = 2
  end 

end
