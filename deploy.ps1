

# $gameName = "joytest"
# $gameName = "inv4ders"
# $gameName = "bouncetest"
$hostName = "pi@tmntcade"
# $hostName = "pi@rampage"

$scriptDir = "/home/pi/RetroPie/roms/ports"

Write-Host "Deploying Launcher Scripts"
scp "./scripts/*.sh" ${hostName}:"$scriptDir"
ssh ${hostName} -C "chmod +x $scriptDir/*.sh"
ssh ${hostName} -C "dos2unix $scriptDir/*.sh"

# $games = "joytest","inv4ders","peanut"
$games = "seahorse","inv4ders","peanut"

Write-Host "Cleaning up Game Files"

Write-Host "Deploying Game Files"

foreach ($gameName in $games) {
    $gameDir = "/opt/retropie/ports/$gameName"
    ssh ${hostName} -C "sudo mkdir -p $gameDir"
    ssh ${hostName} -C "sudo chown pi $gameDir"
    ssh ${hostName} -C "rm -rf $gameDir/*"
    scp -r "./$gameName/*" ${hostName}:"$gameDir"
    ssh ${hostName} -C "dos2unix $gameDir/*"
    Write-Host "List of $gameName Files"
    ssh ${hostName} -C "ls -alR $gameDir"
}
Write-Host "List of Launcher Scripts"
ssh ${hostName} -C "ls -al /home/pi/RetroPie/roms/ports"