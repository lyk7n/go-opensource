#%%
from concurrent.futures import thread
import socket
import threading
from queue import Queue

target = "127.0.0.1"  #target= localhost 
queue = Queue()
open_ports = []


def portscan(port):
    try:    
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # af_inet specifies this is an internet conncection and not unix socket and sock_stream defines its an tcp and not udp
        sock.connect((target, port))
        return True
    except:
        return False

# print(portscan(98))
# for port in range(1,1024):
#     result = portscan(port)
#     if result:
#         print("port {} is open ". format(port))
#     else:
#         print("port {} is closed".format(port))    


def fill_que(port_list):
    for port in port_list:
        queue.put(port)




def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print("port {} is open".format(port))
            open_ports.append(port)

port_list = range(1,1024)
fill_que(port_list)  


thread_list = []

for t in range(500):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join() #join method waits until the thread is done



print("Open ports are:", open_ports)














# %%
