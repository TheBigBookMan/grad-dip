## Monolithic
- Tightly coupled services and components
- usually in this type, if one component fails then the whole application fails

## Microservices
- application components are loosely coupled
- if one component fails then the other components continue to work independently from one another

## Messaging and Queuing
- When services are queued up in an order to process a specific event- eg if first service takes action, and  then the second service takes action etc
- **Tightly coupled**- if any of the services in the queue take action and fail, then the whole process fails and throws errors
- **Loosely coupled (AWS do this)**- if one service fails then its isolated so the whole queue doesnt fail with it, the service that fails will create a queue of messages for the action and wait until the service is working again to process

## Serverless Computing
- running the code on a virtual server hosted in the cloud
- no provisioning or managing of the servers
- removes the need of having to host the server yourself

## Containers
- great so you can run applications code on different environments as the code environment is saved within the image
- packaing code and dependencies into a single object
- great for reliability, scalability and security
- multiple instances of servers can manage the exact same code- great for scalability
- updating one block of code can then update all the instances through orchestration management when there are large amounts of servers hosting many containers

## Global Infrastructure and Reliability
- having the availability of your resources all the time due to AWS having many places where resources are stored so if one goes down, then the other place can serve the resources
- **Regions**- before choosing a region where you want resources to be stored, consider:
	- Compliance- requirements in the region that you must adhere by eg the data must remain within your country
	- Proximity- putting the resources closer to location of users to reduce any latency
	- Availability- checking if the services you want to use are available in the specific region you want
	- Pricing- different regions may require different costs so some are more expensive than others
- **Availability Zones**- Many data centers (availability zones) are in a region which can helpe to also split up the resources
	- availability zone is either a singular data center or a group of data centers
	- Always recommended to run across atleast 2 availability zones in a region
	- A region will contain minimum 3 avalability centers and these will be named like: region- North California (us-west-1), data center 1 (us-west-1a), data center 2 (us-west-1b), data center 3 (us-west-1c)
- **Edge Locations**- being able to cache or store copies of your files into a closer location to where users are- using AWS Cloudfront as a content delivery network (CDN)
	- They are sites deteremined by AWS that are different from regions
	- good for if you want some particular data or files to be easier access to a certain location, than setting up a full region
	- good for if your developing in another country thats far from where the userbase is
	- Can use AWS Outposts which is setting up an edge location device to be closer to where you are (could be in your building etc)- on-premise data center

## Working with AWS
- can work with the console in browser
- or the AWS CLI with scripts and easier typing for managing resources over using a GUI as less human error
- SDKs for any interaction with programming languages

## Networking
- create a VPC to manage the networking for all your applications and servers
- can have private for ones you dont want to be talking to clients or internet directly
- public for ones you do want to be talking to clients and itnernet directly
- control groups of servers with subnets that are groups of the IP addresses
- **Public facing**- 
	- directs traffic that flows through the network with internet gateway (IGW)
	- without an internet gateway, no one can access the resources within the VPC
	- internet gateway is how your network can interact with the internet
- **Private facing**- 
	- don't want anyone from anywhere to reach resources through an internet gateway
	- use a Virtual Private Gateway which can create a VPN connection between a private network and VPC
		- virtual private gateway is extra encryption and protection over any requests (VPN)
		- problem with VPN is it can still be slow because it is still run through a public network (just with encryption)
		- only comes through if its coming from an approved network
	- AWS Direct Connect- establush a completely private and dedicated fiber connection from data center to AWS
		- Physical line connecting your network to your AWS VPC
		- good for compliuance security
- Use subnets to control the traffic permissions
- **Network Access Control List (ACL)**- the packets that are within the message from the internet will be checked against the ACL to see if it has permission to enter or lave the network
	- This controls the in and out for a subnet
	- stateless, so it will check every packet coming
- Different instances may have different specifics about who can send them requests or recieve so need instance level network security
	- instances have security groups
	- doesnt allow any traffic into the instance by default, all ports blocked and all IP addresses are blocked
	- have to configure what incoming traffic you want
	- 