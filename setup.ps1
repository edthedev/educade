
pip install pygame

ssh pi@tmntcade -C 'mkdir ~/.ssh'
cd ~;scp .ssh/id_rsa.pub pi@tmntcade:~/.ssh/authorized_keys

ssh pi@tmntcade -C 'sudo apt-get install -y python3-pygame python3'
ssh pi@tmntcade -C 'sudo apt-get install -y dos2unix'