

# $gameName = "joytest"
# $gameName = "inv4ders"
# $gameName = "bouncetest"

$scriptDir = "/home/pi/RetroPie/roms/ports"

Write-Host "Deploying Launcher Scripts"
scp "./scripts/*.sh" pi@tmntcade:"$scriptDir"
ssh pi@tmntcade -C "chmod +x $scriptDir/*.sh"
ssh pi@tmntcade -C "dos2unix $scriptDir/*.sh"

# $games = "joytest","inv4ders","peanut"
$games = "inv4ders","peanut"

Write-Host "Cleaning up Game Files"

Write-Host "Deploying Game Files"

foreach ($gameName in $games) {
    $gameDir = "/opt/retropie/ports/$gameName"
    ssh pi@tmntcade -C "sudo mkdir -p $gameDir"
    ssh pi@tmntcade -C "sudo chown pi $gameDir"
    ssh pi@tmntcade -C "rm -rf $gameDir/*"
    scp -r "./$gameName/*" pi@tmntcade:"$gameDir"
    ssh pi@tmntcade -C "dos2unix $gameDir/*"
    Write-Host "List of $gameName Files"
    ssh pi@tmntcade -C "ls -alR $gameDir"
}
Write-Host "List of Launcher Scripts"
ssh pi@tmntcade -C "ls -al /home/pi/RetroPie/roms/ports"