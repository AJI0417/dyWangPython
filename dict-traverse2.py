#!/usr/bin/python
#20240522 11227058 pythoneval8

dict_passwd = """
root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:23:4:adm:/var/adm:/sbin/nologin
lp:x:44:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:15:0:sync:/sbin:/bin/sync
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
mail:x:8:12:mail:/var/spool/mail:/sbin/nologin
operator:x:11:0:operator:/root:/sbin/nologin
games:x:12:100:games:/usr/games:/sbin/nologin
ftp:x:14:50:FTP User:/var/ftp:/sbin/nologin
nobody:x:99:99:Nobody:/:/sbin/nologin
dbus:x:81:81:System message bus:/:/sbin/nologin
polkitd:x:999:998:User for polkitd:/:/sbin/nologin
rpc:x:32:32:Rpcbind Daemon:/var/lib/rpcbind:/sbin/nologin
nscd:x:28:28:NSCD Daemon:/:/sbin/nologin
ntp:x:38:38::/etc/ntp:/sbin/nologin
nslcd:x:65:55:LDAP Client User:/:/sbin/nologin
rpcuser:x:29:29:RPC Service User:/var/lib/nfs:/sbin/nologin
nfsnobody:x:65534:65534:Anonymous NFS User:/var/lib/nfs:/sbin/nologin
avahi:x:70:70:Avahi mDNS/DNS-SD Stack:/var/run/avahi-daemon:/sbin/nologin
postfix:x:89:89::/var/spool/postfix:/sbin/nologin
sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
chrony:x:998:996::/var/lib/chrony:/sbin/nologin
apache:x:48:48:Apache:/usr/share/httpd:/sbin/nologin
"""

test_passwd_dict = {}

for line in dict_passwd.strip().split('\n'):
    parts = line.split(':')
    if len(parts) >= 3:
        username = parts[0]
        uid = int(parts[2])
        if 80 <= uid <=1000:
            test_passwd_dict[username] = uid

passwd_dict5 = dict(sorted(test_passwd_dict.items(), key=lambda item: item[1]))

keys = ""
valuesum = 0

for key in passwd_dict5.keys():
    if len(key) <= 4:
        keys += key
        valuesum += passwd_dict5[key]
    
print("%s\t%d" % (keys,valuesum))
