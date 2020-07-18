

# $gameName = "joytest"
# $gameName = "inv4ders"
# $gameName = "bouncetest"


Write-Host "Deploying Launcher Scripts"
scp "./scripts/*.sh" pi@tmntcade:"$scriptDir"
ssh pi@tmntcade -C "chmod +x /home/pi/RetroPie/roms/ports/*.sh"
ssh pi@tmntcade -C "dos2unix /home/pi/RetroPie/roms/ports/*.sh"

Write-Host "Deploying Game Files"

$games = "joytest","inv4ders"

foreach ($gameName in $games) {
    $gameDir = "/opt/retropie/ports/$gameName"
    ssh pi@tmntcade -C "sudo mkdir -p $gameDir"
    ssh pi@tmntcade -C "sudo chown pi $gameDir"
    scp "./$gameName/*" pi@tmntcade:"$gameDir"
    ssh pi@tmntcade -C "dos2unix $gameDir/*"
    ssh pi@tmntcade -C "ls -al $gameDir"
}
ssh pi@tmntcade -C "ls -al /home/pi/RetroPie/roms/ports"