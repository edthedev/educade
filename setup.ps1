

pip install pygame

ssh-keygen
ssh pi@tmntcade -C 'mkdir ~/.ssh'
cd ~;scp .ssh/id_rsa.pub pi@tmntcade:~/.ssh/id_rsa.pub
