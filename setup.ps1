
pip install pygame

# $hostName = "pi@tmntcade"
$hostName = "pi@rampage"

ssh ${hostName} -C 'mkdir ~/.ssh'
cd ~;scp .ssh/id_rsa.pub $hostName:~/.ssh/authorized_keys

ssh ${hostName} -C 'sudo apt-get install -y python3-pygame python3'
ssh ${hostName} -C 'sudo apt-get install -y dos2unix'