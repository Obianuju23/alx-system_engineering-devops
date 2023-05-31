A SERVER is a virtual device(hardware) or a computer program (software) that provides functionality for other programs or devices. They are usually referred to as “clients”.  It is located in a data center and runs an operating system.

THE ROLE OF THE DOMAIN NAME is that it provides human readable that users use to access websites. It s mapped in the DNS(Domain Name System). In this case the domain name is “foobar.com”.

THE TYPE OF DNS RECORD www IS IN www.foobar.com is A record because it resolves to an IP address.  This Address Mapping Record (A record) stores hostname and its corresponding IPV4 Address. It is also known as a DNS host record.

THE ROLE OF A WEB SERVER is to serve web pages(static content) to clients over the protocol HTTP/HTTPS upon their request.

THE ROLE OF THE APPLICATION SERVER is to interact with application files(code base) to generate dynamic codes to html page.

THE ROLE OF DATABASE is  to store and organize collection of  this website’s information for easier access, update and management.
WHAT THE SERVER IS USING TO COMMUNICATE WITH THE COMPUTER OF THE USER REQUESTING THE WEBSITE is internet network  via Transmission Control Protocol(TCIP) or Internet  Protocol(IP)  .

ISSUES WITH THIS WEB INFRASTRUCTURE DESIGN ARE AS FOLLOWS:
SPOF(SINGLE POINT OF FAILURE) Since we are using a single server, If the server goes down or encounters any issues, the website will become inaccessible. To address this, a more resilient infrastructure could be implemented, such as using multiple servers in a load-balanced setup.

THE DOWNTIME WHEN MAINTENANCE SUCH AS DEPLOYING NEW CODE SERVER IS NEEDED is  since there is only one server, it will have to be put off and restarted when maintenance check needs to be carried out on any component. This will lead to the website experiencing downtime and temporarily inaccessible to users. We need to implement multiple servers  to minimize this downtime.

THIS INFRASTRUCTURE CANNOT BE SCALE UP IF  THERE IS TOO MUCH INCOMING TRAFFIC BECAUSE the single server may not be able to handle a high volume of concurrent requests efficiently. To address scalability concerns, a load-balancing  setup with multiple servers or utilizing cloud-based infrastructure can be considered. 
