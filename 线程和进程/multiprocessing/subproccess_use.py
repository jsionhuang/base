#coding = 'utf-8
import subprocess
#如何在创建子进程之后，控制子进程的输入输出
print('nslookup www.python.org')
r = subprocess.call(['nslookup','www.python.org'])
p = subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
output,err = p.communicate(b'set q=mx\npython.org\nexit\n')
print('exit ',r)
print(output)
print('Exit code:', p.returncode)