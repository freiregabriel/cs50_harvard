# Harvard CS50x edx
Notes for CS50x Introduction to Computer Science.
## Week 1
### Compilation

**C** *>* **Assembly** *>* **010100011100** (binary read by the CPU)

### UNIX Commands
- `ls` list directories 
- `mkdir directoryname` make a new directory 
- `cp src.txt trgt.txt` copy file 
- `cp -r src trgt` copy directory. The `-r` stands for recursive
- `rm -f file.txt` remove file  
- `rm -r directory` remove directory
- `rm -rf directory` combine `-f` and `-r`

### C DataTypes and Variables
- `int ` Integer 4 bytes of memory(32 bits)
- `unsigned int ` Use unsigned if you know your value will never be negative.
- `char ` char data type stores single characters (8 bits|1 byte)
- `float` for storing floating-point numbers with decimal part that takes 4 bytes of memory (32 bits|4 bytes)
- `double` for storing floating-point numbers with decimal part that takes 8 bytes of memory (64 bits|8 bytes) [Double precision]
- `void` is not a data type, it's a type. it is a placeholder for "nothing"
- `struct` structures
- `typedefs` for creating custom data types

```c
    int number; // declaration
    number = 17; // assignment
    char letter; // declaration
    letter = 'H'; // assignment
    int x = 17; // initialization
    char y = 'X'; // initialization
```
> Included in <cs50.h>
- `bool` true or false values / 1 and 0.
- `string` string data type == array of characters `char str[size]`.
- `int x;` integer variable
- `x` x variable
- `&x` address of x

### Loops in C
while loop
```c
while(true) {
    // will execute forever
}
```
do-while loop
```c
int n = 0;
do {
    // will at least once and until user types n >= 1
    n = prompt();
} while (n < 1);
```
for loop
```c
int n = 10;
for(int i = 0; i < n; i++) { // for(start; expression; increment)
    printf("Hello %i", i); // will print "Hello {i}" ten times
}
```
### Operators
- `=` Assign value to a variable
- `+` Add
- `-` Subtract
- `*` Multiply
- `/` Devide
- `%` Mod
```c
int y = 1;
int x = y + 1; // 2
int z = x + y; // 3
int z1 = x % y // 0
int z2 = z % x // 1
// mult
x = x * 5;
x *= 5;
// add
x = x + 1;
x += 1;
x++;
// sub
x = x - 1;
x -= 1;
x--;
if (x > y) {
    // x is greater than y
} else if (x <= y){
    // x is less or equal than y
}
if (z % y == 0) {
    // do something
} else if (z % y == 1) {
    // do something else
}
bool x = true;
bool y = true;
if (x && y) {
    // x and y are true
} else {
    // one of them is false
}
if (!x) {
    // x is false
}
if (x == y) {
    // x is equals to y
}
if (x != y) {
    // x is not equals to y
}
```
### Sort algorithms
```c
/**
 * Selection sort worst case: On^2 best case: On^2
 * Bubble sort worst case: On^2 best case: On
 * Insertion sort worst case: On^2 best case: O n
 * Merge sort worst case: O n * log n best case: O n * log n
 * 
 * Linear search worst case: O n best case: O1
 * Binary search worst case: O log n best case: O1 (ARRAY MUST BE SORTED)
 */
```

### Pointers
```c
/*
    int: 4 bytes
    char: 1 byte
    float: 4 bytes
    double: 8 bytes
    long long: 8 bytes
    string: ??? bytes

    memory is a big array of byte-sized cells
    arrays are pointers and don't get copied when passed as parameters to functions (in C)
*/
int main(void) {
    int k;
    k = 5;
    int* pk; /* declare a pointer pk (the value of a pointer is a memory address / the type describes the data located at that memory address) */
    pk = &k; /* pk is the address of k (where k lives in memory) */
    printf("Memory address: %d\n", pk); /* print the address in memory */
    printf("Data Value: %d\n", *pk); /* print the value */
}
```

# Hypertext Transfer Protocol (HTTP)
is one such example of an application layer protocol, which specifically dictates the format by which clients request web pages from a server, and the format via which servers return information to clients
### Request
```
GET /cats.html HTTP/1.1
host: cats.com
```
### Response
```
HTTP 1.1 200 Ok
Content-Type: text/html
```
### Status
#### success
- 200 ok, all is well, valid request and response

#### redirect
- `301` (Moved permanentely): page is now at a new location, automatic redirects built in to most browsers. 
- `302` (Found): page is now at a new location temporarily
#### client error
- `401` (uniauthorized)
- `403` (forbidden)
- `404` (not found)
#### server error
- `500` (INnternal server error)

## Other application layer protocols include:
- File Transfer protocol **(FTP)**
- Simple mail transfer protocol **(SMTP)**
- Data distribution service **(DDS)**
- remote desktop protocol **(RDP)**
- Extensible message and presence protocol **(XMPP)** (used on chat applications)

# IP (internet protocol)
#### IPv4
- 127.0.0.1  (range from **0 to 255**)
#### IPv6
- 2001:4860:4860:0:0:0:0:8844 (range from **0 to 4 billion**) or 2001:4860:4860::8844 omitting the 0s

#### DHCP (Dynamic host configuration protocol) server 
is a program that assigns an IP address to you computer on the internet automatically that runs between you and the internet

#### DNS (Domain Name System)
exists to help us translate/map IP addresses to more memorable names that are more human-comprehensible
- ***2001:4860:4860::8844*** :-> ***google.com***

- 0.0.0.0 :-> ***info.host1.net***
- 74.125.202.138 :-> ***google.com***

DNS system doesn't keep records of all DNSs of the world, it is actually a decentralized block that keeps track of the many many DNSs addresses of the world, locally.

Different networks relly on routers to distribute their inter connections
##### Network 1
**IP:** 1.X.X.X
##### Network 2
**IP:** 2.X.X.X
##### Network 3
**IP:** 3.X.X.X
##### Network 4
**IP:** 4.X.X.X
##### Network 5
**IP:** 5.X.X.X

*Sending message from 1.208.12.37 to 5.188.109.14, **network 1** to **network 4**.*
 Steps:
1. Look for network 1
2. build message
3. Look for network 5
4. send message

IP is also known as a connectionless protocol. There is not necessarily a defined path from the sender to the receiver, and vice versa.
#### packets
- any slowdown that may be caused by sending such a large amount of data would have a ripple effect that would throttle the network for all the other users
- as such, another curcial part of IP is splitting data into packets

#### Access Point
- One of the ways we've dealt with the IPv4 addressing problem is to start assigning multiple people to the same IP address.
- The IP address is assigned to a router, whose job it is to act as a traffic cop that allows data requests from all of the devices on your local network (your home or business e.g)
- Modern home networks consist of access points that combine a router, a modem, a switch, and other technologies together into a single device.
- Modern business networks or large-scale wide-area networks (WANs) still frequently have these as separate devices to allow the size of their network to scale more easily

### Internet connection phases
**WE(users, companies, etc) -> DHCP Server -> DNS Server -> Access point -> Internet**

### Transmission control protocol (TCP)
- If the internet protocol (IP) is thought of as the protocol for getting information from a sending machine to a receiving machine, then Transmission control protocol (TCP) can be thought of as directing the transmitted packet to the correct program on the receiving machine.

- Each program/utility/service on a machine is assigned a port number. coupled with an IP address, we can now uniquely identify a specific program on a specific machine.
- The other thing that TCP is crucial for is guaranteeing delivery of packets, which IP alone does not do.
- TCP does this by including information about how many packets the receiver should expect to get, and in what order, and transmitting that information alongside the data.
Some ports are so commonly used that they have been standardized across all computers
- **FTP** (file transfer) uses port 21.
- **SMTP** (e-mail transfer) uses port 25.
- **DNS** (domain system) uses port 53.
- **HTTP** (web browsing) uses port 80
- **HTTPS** (secure web browsing) uses port 443

#### Steps of TCP/IP process
1. When a program goes to send data, tcp breaks it into smaller chunks and communicates those packets to the computer's network software, adding a TCP layer onto the packet
2. IP routes the individual packets from sender to receiver; this info is part of the IP layer surrounding the packet.
3. When the destination computer gets the packet, TCP looks at the header to see which program it belongs to.
4. If at any point along the way something go wrong, TCP can deal with it gracefully using additional information insde the headers to request that the sender passing the extra packet so it could complete assembly.
5. After the packets have arrived, TCP ensures they are organized the correct order and can then be reassembled into the intended unit of data and delivered to the correct service.