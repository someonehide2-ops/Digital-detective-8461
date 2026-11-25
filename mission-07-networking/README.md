# Mission 7 — How computers communicate

## 1. Task / objective
Explain network concepts, observe connectivity and DNS lookup, and describe what happens when a website opens.

## 2. Work completed
### Task 7.1 — Network concepts
| Concept | Explanation | Example |
|---|---|---|
| LAN | A network covering a limited area. | Home or college lab network |
| MAN | A network spanning a city or large campus area. | City-wide institutional network |
| WAN | A network spanning large geographical areas. | The Internet |
| DNS | Translates domain names into IP addresses. | Looking up a website domain |
| Router | Connects networks and forwards data between them. | Home Wi-Fi router |
| Protocol | Rules that devices follow to communicate. | HTTPS, TCP or IP |
| Packet switching | Splits data into packets that can travel across a network. | Web data sent over the Internet |
| Client-server | A client requests a service and a server provides it. | Browser requesting a web page |

### Task 7.2 — Connectivity and DNS observations
On your own Mac, run a connectivity test and DNS lookup:

```bash
ping -c 4 example.com
nslookup example.com
```

- A connectivity test helps check whether a destination can be reached and gives an indication of response time or packet loss. Some hosts or networks may block ping.
- A DNS lookup shows DNS records, commonly including the IP address associated with a domain.
- DNS lets people use domain names instead of remembering numeric IP addresses.

My result : DNS is useful because we normally remember website names instead of IP addresses. DNS helps the browser find the address of the website.

### Task 7.3 — What happens when a website opens?
1. The user enters a website address in a browser; the browser acts as a client.
2. The client needs the server's network address, so it asks DNS to resolve the domain name.
3. The device sends network traffic through its local network and router.
4. Data is carried across networks using protocols such as IP and TCP; HTTPS protects web communication using encryption.
5. The browser sends a request to the website's server.
6. The server processes the request and sends a response, such as page content and related resources.
7. The browser interprets the response and displays the website to the user.

## 3. Commands / tools used
`ping -c 4 example.com`, `nslookup example.com`, and a web browser. 

## 4. My understanding
Networks let devices exchange information. DNS connects human-readable domain names to network addresses, routers forward traffic, and protocols define how devices communicate. In client-server communication, the browser requests information and a server responds.

## 5. Difficulties faced
 No major difficulties.
