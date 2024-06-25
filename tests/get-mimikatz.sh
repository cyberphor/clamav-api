mkdir tmp
wget https://github.com/gentilkiwi/mimikatz/releases/download/2.2.0-20220919/mimikatz_trunk.zip -O tmp/mimikatz.zip
cd tmp
unzip mimikatz.zip
cd ..
mv tmp/Win32/mimikatz.exe tests
rm -rf tmp