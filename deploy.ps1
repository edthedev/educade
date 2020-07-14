

# $gameName = "joytest"
# $gameName = "in4ders"
$gameName = "bouncetest"

$gameDir = "/opt/retropie/ports/$gameName"
$scriptDir = "/home/pi/RetroPie/roms/ports"
$script = "/home/pi/RetroPie/roms/ports/$gameName.sh"

ssh pi@tmntcade -C "sudo mkdir -p $gameDir"
ssh pi@tmntcade -C "sudo chown pi $gameDir"
scp "./$gameName/$gameName.sh" pi@tmntcade:"$scriptDir"
scp "./$gameName/$gameName.py" pi@tmntcade:"$gameDir"
ssh pi@tmntcade -C "chmod +x $script"
ssh pi@tmntcade -C "dos2unix $script"
ssh pi@tmntcade -C "dos2unix $gameDir/*"
ssh pi@tmntcade -C "ls -al $gameDir"
ssh pi@tmntcade -C "ls -al $scriptDir"