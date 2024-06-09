import paramiko

def connSSH(ip):
    rtnData = None
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip)
        
        stdin, stdout, stderr = ssh.exec_command("ls -l")
        print(stdout.read().decode())
        
        ssh.close()
        rtnData = True, stdout.read().decode()
    except Exception as e:
        rtnData = False, e
    
    return rtnData

if __name__ == "__main__":
    ip = '10.10.100.100'
