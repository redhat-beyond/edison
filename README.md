# Edison - Automated house managment

### Overview

Edison is an open-source home management system.  
In its core, Edison is a regular automatic home management system: it reads data from humidity and light sensors and decides when to turn on the air condition and turn on the lights in different rooms. 

Edison allows users to write their own house management plans.   
Users can share their management plans through the Edison network and users can also download and review plans from other users.

Edison can also manage different sensors from different rooms with different management plans for each room.

## How to spin and tear down the environment

Edison makes the initial setup easy for you by including a provisioner file that runs automatically on **`vagrant up`**.  
You will have a fully ready-to-go work environment with a single command.

### How to get started

- Download the proper [VirtualBox](https://www.virtualbox.org/wiki/Downloads) and [Vagrant](https://www.vagrantup.com/downloads.html) package for your operating system and architecture.
- Download Edison to your machine and then open a console window on *edison* folder.
 - Write **`vagrant up`** and press enter.
 - That's it! Your virtual machine is up and running.  
 You can enter your virtual machine with **`vagrant ssh`**.
 > **Important!** In case that, after `vagrant ssh`, your virtual machine asks for a password the default  password is `vagrant`.
 
 ### How to save virtual machine state
 
 In order for your next **`vagrant up`** to execute quicker you should save your virtual machine state into a box file format.
 
 - If you are inside the virtual machine write **`exit`** and press enter. Now you are back on your host command line. 
 - Write **`vagrant halt`** and press enter.
 > **Note:** It will shut down the running machine Vagrant is managing.
 - Write **`vagrant package --output box-name.box`** and press enter. You can replace *box-name* with any name you want.
> **Note:** It will output your virtual machine into a box file format with .box extension.
- Write **`vagrant box add box-name box-name.box`** and press enter.  
  Make sure you replaced *box-name* with the name you have chosen on the previous step.
- Edit *Vagrantfile* inside the *edison* folder.  
Change the following line `config.vm.box = "ubuntu/xenial64"` to `config.vm.box = "box-name"` (replace *box-name* with the name of the box you have created).
- Run **`vagrant up --no-provision`** on future spins.

### How to tear down the environment

- If you are inside your virtual machine execute the **`exit`** command so you would get back to your host command line.
- Write **`vagrant destroy -f`** and press enter. It sould terminate your virtual machine.
> **Important!** If you have some unsaved work on your virtual machine your data will be lost! In order to save your data you should follow the steps we provided on **How to save virtual machine state**.

## FAQ

Here are some answers to some frequently asked questions:

**Why does `vagrant up` take so long ?**  
If you don't have a box to spin your environment from, **`vagrant up`** will take longer to be done.  
As part of this command execution our included file `setup.sh` starts to execute and configure Edison environment inside the virtual machine. It downloads all the dependencies Edison requires to run.

**What is box file format ?**  
Please read [box file format](https://www.vagrantup.com/docs/boxes/format.html) documentation for more information.