

$gameDir = "/opt/retropie/ports/joytest"
$scriptDir = "/home/pi/RetroPie/roms/ports"
$script = "/home/pi/RetroPie/roms/ports/joytest.sh"

ssh pi@tmntcade -C "sudo mkdir -p $gameDir"
ssh pi@tmntcade -C "sudo chown pi $gameDir"
scp ./joytest/joytest.sh pi@tmntcade:"$scriptDir"
scp ./joytest/* pi@tmntcade:"$gameDir"
ssh pi@tmntcade -C "chmod +x $script"
ssh pi@tmntcade -C "dos2unix $script"
ssh pi@tmntcade -C "dos2unix $gameDir/*"
ssh pi@tmntcade -C "ls -al $gameDir"
ssh pi@tmntcade -C "ls -al $scriptDir"