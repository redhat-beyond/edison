db_file_exists    = "test -f /vagrant/edison/db.sql"
restore_db        = "sudo -u postgres psql edison < /vagrant/edison/db.sql"
db_restored_msg   = "echo \"Database restored.\""
db_not_exists_msg = "echo \"db.sql not exists.\""
try_restore_db    = "bash -c '#{db_file_exists} && #{restore_db} && #{db_restored_msg} || #{db_not_exists_msg}'"
save_db_data      = "sudo -u postgres pg_dump edison > /vagrant/edison/db.sql"

Vagrant.configure("2") do |config|
  config.trigger.before :destroy do |trigger|
    trigger.info = "Saving database data inside synced folder..."
    trigger.run_remote = {inline: "#{save_db_data}"}
  end

  config.trigger.after :up do |trigger|
    trigger.info = "Trying to restore database from /vagrant/edison/db.sql..."
    trigger.run_remote = {inline: "#{try_restore_db}"}
  end

  config.vm.box = "ubuntu/bionic64"
  config.vm.provision :shell, path: "setup.sh"
  config.vm.network "private_network", type: "dhcp"
  config.vm.provider "virtualbox" do |v|
    v.gui = false
    v.name = "Edison_test"
    v.memory = 1024
    v.cpus = 2
  end 

end

# Fixes a dhcp configuration conflict of the private network.
# Issue: https://github.com/hashicorp/vagrant/issues/8878
class VagrantPlugins::ProviderVirtualBox::Action::Network
  def dhcp_server_matches_config?(dhcp_server, config)
    true
  end
end
