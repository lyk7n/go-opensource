

import dns.resolver
import sys


record_types = ['A', 'AAAA', 'NS', 'CNAME', 'MX' 'PTR', 'SOA', 'TXT']

try:
    domain = sys.argv[1]
except IndexError:
    print("Syntax Error - python dnsenumerationpy.py <domainname>")
for records in record_types:
    try:
        rslv = dns.resolver.resolve(domain, records)
        print("{} record Found".format(records))
        print("-"*100)
        
        for server in rslv:
            
            print(server.to_text()+ "\n")

    except dns.resolver.NoAnswer:
        print(f"no record found for {records}" )
        pass           

        
        
# %%
