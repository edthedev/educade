

$gameDir = "/opt/retropi/ports/joytest"
$scriptDir = "/home/pi/RetroPie/roms/ports"
$script = "/home/pi/RetroPie/roms/ports/joytest.sh"

ssh pi@tmntcade -C "mkdir $gameDir"
scp ./joytest/joytest.sh pi@tmntcade:"$gameDir"
ssh pi@tmntcade -C "chmod +x $script"
ssh pi@tmntcade -C "ls -al $gameDir"
ssh pi@tmntcade -C "ls -al $scriptDir"