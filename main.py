
def alterConfigs(dirs, oldConfigs,newConfigs):
    """First arg: list of file directories you wish to alter
     Second arg: list of config names (or list of list of config names if you want to edit multiple configs in one file) you wish to alter (be exact or your getting fried). Make sure index matches
     Third arg: new config including the argument ex. TRUE, (this can also be a list if you changed multiple in previous argument)"""

    i = 0
    for dir in dirs:
        editedConfigs = []
        with open(dir, "r+") as f:
            if f.writable() and f.readable():
                config = f.readlines()
                configcpy = config[:]
                print(config)
                for line in config:
                    if isinstance(oldConfigs[i], str):
                        if oldConfigs[i] in line:
                            configcpy.remove(line)

                    else:
                        for subConfig in oldConfigs[i]:
                            if subConfig in line and line in configcpy:
                                configcpy.remove(line)
                editedConfigs = configcpy
            elif (not f.writable()) and f.readable():
                print(f"WARNING!!! Directiory {dir} is not writeable!")
                continue
            elif (not f.readable()) and f.writable():
                print(f"WARNING!!! Directiory {dir} is not readable!")
                continue
            else:
                print(f"WARNING!!! Directiory {dir} is neither writable nor readable! Your COOKED 🤣🤣🤣 (or somethings wrong with my code)")
                continue


            if isinstance(newConfigs[i], str):
                newConfigs[i] = newConfigs[i]
                editedConfigs.append("\n")
                editedConfigs.append(newConfigs[i])
            else:
                editedConfigs.append("\n")
                editedConfigs += [x + "\n" for x in newConfigs[i]]
                editedConfigs[-1].replace("\n","")
            print(editedConfigs)
            f.seek(0)
            f.truncate()
            f.writelines(editedConfigs)
        i+=1

#ssh configs
#alterConfigs(["/etc/ssh/sshd_config"],[["LoginGraceTime","PermitRootLogin","Protocol","PermitEmptyPasswords","PasswordAuthentication","X11Forwarding","UsePAM","UsePrivilegeSeparation"]],[["LoginGraceTime 60","PermitRootLogin no","Protocol 2","PermitEmptyPasswords no","PasswordAuthentication yes","X11Forwarding no","UsePAM yes","UsePrivilegeSeparation yes"]])
#sysctl configs
#alterConfigs(["/etc/sysctl.conf"],[["net.ipv4.conf.all.accept_redirects","net.ipv4.ip_forward","net.ipv4.conf.all.send_redirects","net.ipv4.conf.default.send_redirects","net.ipv4.conf.all.rp_filter","net.ipv4.conf.all.accept_source_route","net.ipv4.tcp_max_syn_backlog","net.ipv4.tcp_synack_retries","net.ipv4.tcp_syn_retries","net.ipv4.tcp_syncookies","net.ipv6.conf.all.disable_ipv6","net.ipv6.conf.default.disable_ipv6","net.ipv6.conf.lo.disable_ipv6"]],[["net.ipv4.conf.all.accept_redirects = 0","net.ipv4.ip_forward = 0","net.ipv4.conf.all.send_redirects = 0","net.ipv4.conf.default.send_redirects = 0","net.ipv4.conf.all.rp_filter=1","net.ipv4.conf.all.accept_source_route=0","net.ipv4.tcp_max_syn_backlog = 2048","net.ipv4.tcp_synack_retries = 2","net.ipv4.tcp_syn_retries = 5","net.ipv4.tcp_syncookies = 1","net.ipv6.conf.all.disable_ipv6 = 1","net.ipv6.conf.default.disable_ipv6 = 1","net.ipv6.conf.lo.disable_ipv6 = 1"]])
#pam configs
#alterConfigs(["/etc/login.defs"],[["FAILLOG_ENAB","LOG_UNKFAIL_ENAB","SYSLOG_SU_ENAB","SYSLOG_SG_ENAB","PASS_MAX_DAYS","PASS_MIN_DAYS","PASS_WARN_AGE"]],[["FAILLOG_ENAB yes","LOG_UNKFAIL_ENAB yes","SYSLOG_SU_ENAB yes","SYSLOG_SG_ENAB yes","PASS_MAX_DAYS 90","PASS_MIN_DAYS 10","PASS_WARN_AGE 7"]])
#lightdm configs
#alterConfigs(["/usr/share/lightdm/lightdm.conf.d/50-ubuntu.conf"],[["allow-guest","greeter-hide-users","greeter-show-manual-login","autologin-user"]],[["allow-guest=fals","greeter-hide-users=true","greeter-show-manual-login=true","autologin-user=none"]])

