#usr/bin/bash

echo "made by raveen"
echo "made for lazy hackers i recommend correct way"
echo " "
echo "invite link"
curl -s -XPOST https://www.hackthebox.eu/api/invite/generate | sed -e 's/{"success":1,"data":{"code":"//g'|sed -e 's/","format":"encoded"},"0":200}//g' | base64 -d

echo
