import random

banners = [
"""
     [EXPLOTATION-FRAMEWORK-DATABASE] (EXFDB)

                          ######
         #####           ######    #####
        #####           ######      #####
       #####           ######        #####
      #####           ######          #####
     #####           ######            #####
      #####         ######            #####
       #####       ######            #####
        #####     ######            #####
         ####    ######             ####
                ######
""",
"""
******************************************************************************
*                                                                            *
*              /---<<**  *)/)                                                *
*             /            )-)                                               *
*         ---------       )/;                                                *
*        -#########-     -/--#####                                           *
*       -###########-    #########      _________________________________    *
*       -#|EXPLOIT|#-    |LIGHTER| <-- | EXFDB                           |   *
*       -###########-    #########     |(EXPLOITATION-FRAMEWORK-DATABASE)|   *
*        -#########-     #########     -----------------------------------   *
*         ---------      #########                                           *
******************************************************************************
""",
"""
(EXFDB) [EXPLOIT-FRAMEWORK-DATABASE] Processing...
(EXFDB) [EXPLOIT-FRAMEWORK-DATABASE] 01010010101010101010101010101010
(EXFDB) [EXPLOIT-FRANEWORK-DATABASE] 01011010110110111001110111010101
(EXFDB) [EXPLOIT-FRAMEWORK-DATABASE] 10101111101101010110010001011011
(EXFDB) [EXPLOIT-FRAMEWORK-DATABASE] 11000111101101010101101100111101
""",
"""
(EXFDB) [EXPLOIT-FRAMEWORK-DATABASE] Injecting shellcode... (BUFFEROVERFLOW)
-INJECTED-SHELLCODE----------------------------------------------------------
[+] [ \\x56\\x72\\x78\\x72\\x72\\x28\\x08\\x72\\x62\\x21\\x91\\x65\\x31\\x67 ]
[+] [ \\x92\\x71\\x02\\x31\\x12\\x82\\x09\\x31\\x21\\x91\\x51\\x04\\x72\\x31 ]
[+] [ \\x32\\x75\\x72\\x53\\x01\\x62\\x01\\x23\\x76\\x12\\x13\\x41\\x53\\x31 ]
[+] [ \\x24\\x25\\x91\\x64\\x63\\x82\\x91\\x54\\x45\\x74\\x56\\x82\\x53\\x23 ]
[+] [ \\x13\\x31\\x31\\x24\\x91\\x92\\x71\\x53\\x24\\x92\\x31\\x31\\x12\\x35 ]
-INJECTED-SHELLCODE----------------------------------------------------------
"""
]

def get_banner():
	return random.choice(banners)
