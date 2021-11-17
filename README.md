# python
The exercise:

Implement a Python script, that searches for lines matching regular expression -r (--regex) in file/s -f (--files).

Use STDIN if file/s option wasn’t provided. 

Assume that input is ASCII, you don't need to deal with different encoding.

If a line matches, print it. Please print the file name and the line number for every match.



Script accept list optional parameters which are mutually exclusive:

-u ( --underscore ) which prints '^' under the matching text
-c ( --color ) which highlight matching text [1]
-m ( --machine ) which generate machine readable output
                  format: file_name:no_line:start_pos:matched_text

Multiple matches on single line are allowed, without overlapping.

The script should be compatible in line with PEP8 coding guidelines.


My Script:

Once you run the script (see attached files), you can query text file/s for specific words and the print will show you the line where the word located and the number 
of the line in the text document

Example:

mviderhorn@CHE100161 MINGW64 ~/Downloads/Ex_Files_Learning_Python_Upd/Ex_Files_Learning_Python_Upd/Exercise Files/Ch2
$ python lionel.py -f "IIS-Hardening.txt","Server_Hardening.txt"
IIS-Hardening.txt,Server_Hardening.txt
Enter a word you want to search in the document/s ?memory

The print will yield with the following:

Set-ItemProperty -Path "IIS:\AppPools\DefaultAppPool" -Name Recycling.periodicRestart.memory -Value 4194304
 Match word memory in line number 124 in the file IIS-Hardening.txt
Set-ItemProperty -Path "IIS:\AppPools\IdentityServerCore" -Name Recycling.periodicRestart.memory -Value 4194304
 Match word memory in line number 130 in the file IIS-Hardening.txt
Set-ItemProperty -Path "IIS:\AppPools\DefaultAppPool" -Name Recycling.periodicRestart.memory -Value 4194304
 Match word memory in line number 132 in the file IIS-Hardening.txt
Set-ItemProperty -Path "IIS:\AppPools\IdentityServerCore" -Name Recycling.periodicRestart.memory -Value 4194304
 Match word memory in line number 138 in the file IIS-Hardening.txt
Set-ItemProperty -Path "IIS:\AppPools\DefaultAppPool" -Name Recycling.periodicRestart.memory -Value 4194304
 Match word memory in line number 140 in the file IIS-Hardening.txt
Set-ItemProperty -Path "IIS:\AppPools\IdentityServerCore" -Name Recycling.periodicRestart.memory -Value 4294967295
 Match word memory in line number 146 in the file IIS-Hardening.txt
Set-ItemProperty -Path "IIS:\AppPools\DefaultAppPool" -Name Recycling.periodicRestart.memory -Value 4294967295
 Match word memory in line number 148 in the file IIS-Hardening.txt
    SeIncreaseQuotaPrivilege Adjust memory quotas for a process
 Match word memory in line number 1172 in the file Server_Hardening.txt
    SeLockMemoryPrivilege Lock pages in memory
 Match word memory in line number 1197 in the file Server_Hardening.txt
