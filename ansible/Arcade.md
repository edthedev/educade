# Arcade Build

These scripts help build one or more arcade machine hearts, in preparation for letting kids code their own MakeCode Arcade games and then play them on actual arcade hardware. As of Jan 2023, you will need to add the recipe in the McAirpos repository on top of this one in order to run MakeCode arcade games.

## Start

Start from an Armbian CLI disk image. I've seen 32GB SanDisk Micro SD cards recommended.
I use Raspberry Pi Imager, and the images for LePotato avaiable from LibreComputer.

## Setup Login for Ansible

Hook a keyboard directly to the new machine and perform the first login.
Take note of the root password - you will be prompted for it when you run `ansible-playbook new.yml`.

Run `armbian-config` to ensure that the new Armbian host is on the local network.
Get the IP address of the active network connection using `ifconfig`. Since I use a USB dongle, for me it's usually an IPv4 address attached to `wlan0`.

On your Ansible host - a different machine on the same network:

1. Add the new computers's IP address to your Ansible inventory file (typically `/etc/asible/hosts`).

	In `/etc/ansible/hosts`:

	```ini
	[new]
	<new IP here>
	```

2. On your Ansible computer, generate an SSH key by running `ssh-keygen`. 
3. Configure `/etc/ansible/hosts` with information for the new computer.

		- Add the path to your new .pub file to your ansible inventory file in a new section called `[new:vars]`. 
	  - Set the `add_ansible_admin` variable to `pi` to tell Ansible that we will use the `pi` user on the new computer.
    - Set the `ansible_user` variable to `root` to tell Ansible to use the `root` user for this first playbook.

	In `/etc/ansible/hosts`:

	```ini
	[new:vars]
	ansible_user = root
	add_ansible_admin = pi 
	add_ansible_pubkey = <path to your ssh public key .pub>
	```

3. On your Ansible computer, run `ansible-playbook new.yml`. This will create a non-root user on the new computer for you and Ansible to remote connect using SSH. The `root` user will be cleaned up in a later playbook.

> Tip: If the `ansible-playbook` command failes, you may need to SSH manually first to the new computer once to accept the SSH host key.

4. (Optional) Run `ansible-playbook hostname.yml` to assign a new hostname to the new computer.

## Install RetroPie

1. Add the new computer to the `[arcades]` group in `/etc/ansible/hosts`.
1. On the Ansible computer, run `ansible-playbook retropie_setup.yml`. This may take some time.
2. On the new computer, run `sudo retropie_setup.sh` in the `/home/pi/RetroPie/` directory.
3. Disconnect the keyboard from the new computer. Connect a game controller.
4. Reboot the new computer. It should now boot directly to EmultationStation.

