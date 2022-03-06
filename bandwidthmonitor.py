import time
import psutil


last_recieved = psutil.net_io_counters().bytes_recv
last_sent = psutil.net_io_counters().bytes_sent

total = last_recieved + last_sent


while True:
      try:
         bytes_recieved = psutil.net_io_counters().bytes_recv
         bytes_sent = psutil.net_io_counters().bytes_sent

         total_bytes = bytes_recieved + bytes_sent

         new_recv = bytes_recieved - last_recieved
         new_sent = bytes_sent - last_sent
         new_total = total_bytes - total
      
      # this programs return the bandwidth in bytes so we convert bytes into megabytes 

         receieved_in_mb = new_recv /1024 / 1024
         sent_in_mb = new_sent /1024 /1024
         total_in_mb = receieved_in_mb + sent_in_mb
         
         print(f"{receieved_in_mb:.2f}MB recieved, {sent_in_mb:.2f} MB sent, {total_in_mb:.2f} Total")
         
         last_recieved = bytes_recieved
         last_sent = bytes_sent
         total_bytes = total
   


         time.sleep(2)
      except KeyboardInterrupt:
            quit()
