- **Local area network (LAN)**- having computers being connected to each other through a Ethernet cable, so the cable transfers data between each other
	- Data can be transferred between each computer through the ethernet 
	- **Mac address**- headers have a prefix for data being sent so each computer in the LAN can see if the data is meant for them. Each computer has a MAC address
	- Carrier will be what sends the data between each computer, however if too many computers trying to send data at same time it can end up in a collision of data and things get messy
	- **Ethernet**- transmitting computers have a random period of waiting for the carrier to be silent so it can start transmitting again
	- **Collision domain**- the network for a particular gtroup of computers, having a switch which can split up the collision domains so multiple networks can be split up to allow concurrent talking between different networks
	- **Exponential backpff**- the seconds that the collision will wait after a collision before trying again, it exponential (times by 2 everytime) as well as arandom number of seconds
- **Routing**- connecting distinct computers/netwrosk-
	- where it determins which lines are connecting from one end to another- inflexible and expensive
	- **Message switching**- can go to multiple different spots before getting to the end destination, this is done concurrently with other similar requests by taking a different route than the other so multiple can happen same time
- **Packets**- splitting up data to go into packets
	- the packets have headers which store the destination target in the form of IP address
	- different packets from the same message can take different routes
	- **Packet switching**- decentralized and allows the transfer of the packets going through the packets allowing for all the internet data moving
- **Networking**- broken down into a set a layers and each separate layers has different technologies that do different things
- **Open Systems Interconnection Model (OSI)**- 7 layers which each help to standard of communcation functions
	1. **Physical Layer**- specifies how bits are repsented on the medium
		- Data- Bits
		- Layer- Media, signal and binary transmission
		- Used to send and receive data, these are the actual wires used to send the data 
	1. **Data Link Layer**- controls who can transmit on the medium at any given time
		- data- frames
		- Layer- MAC and LLC (physucal addressing)
	2. **Network Layer**- establishes pathways between devicves
		- data- packets
		- layer- path determination and IP (logical addressing)
	3. **Transport Layer**- error correction and flow control
		- data- segments
		- layer- end to end connections and reliability
	4. **Session Layer**- provides APIs for aplpication software to manage the connection
		- data- data
		- layer- interhost communication
	5. **Presentation Layer**- compression and encryption
		- data- data
		- layer- data representation and encryption
	6. **Application Layer**- application that isusing the data (web browsers etc)
		- data- data
		- layer- network process to application
	- Common protocols for each layer
		1. **Physiucal/DataLink layers (1, 2)**- 
			- Etherniet (over fibre or unshielded twisted pair)
			- 802.11 (wi-fi)
			- bluetooth
		2. **Network layer (3)**- 
			- IPv4- internet protcol version 4 (most of internet is using)
			- IPv6- internet protocol version 6 (most internet will move to)
		3. **Transport layer (4)**-
			- TCP- transmission control protocol
			- UDP- user datagram protocol
		4. **Application layer (5-7)**-
			- HTTP- hypertext transfer protocol- transmit websites
			- DNS- domain name system- convert domain name into IP address
			- SMTP- simple mail transfer protocol- email servers