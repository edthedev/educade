

$gameDir = "/home/pi/RetroPie/roms/ports/joytest"

Write-Host "mkdir $gameDir"
ssh pi@tmntcade -C "mkdir $gameDir"
scp ./joytest/* pi@tmntcade:"$gameDir"
ssh pi@tmntcade -C "chmod +x $gameDir/joytest.sh"
ssh pi@tmntcade -C "ls -al $gameDir"