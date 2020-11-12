import socket
import urllib.request
import threading
import time

hostname = socket.gethostname()
full_ip = socket.gethostbyname(hostname)
split_ip = full_ip.split(".")
ip_list = []
for i in range(0, 256):
    ip_list.append(split_ip[0] + "." + split_ip[1] + "." + split_ip[2] + "." + str(i) + ":8080")
succeeded = []

def ip_test(ip):
    time.sleep(1)
    try:
        urllib.request.urlopen("http://" + ip, data=None, timeout=5)
        print(ip + " - success")
        succeeded.append(ip)
    except:
        print(ip + " - failed")

threads = []
for ip in ip_list:
    t = threading.Thread(target=ip_test, args=[ip])
    t.start()
    threads.append(t)
    time.sleep(0.01)

for thread in threads:
    thread.join()

print("\n############################")  
print("Succeeded: \n" + " ".join(succeeded))
print("############################")