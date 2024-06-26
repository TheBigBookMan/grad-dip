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
		- good for compliuance securityn
- Use subnets to control the traffic permissions
	- traffioc permissions will not look at the contents of the packet, just the sender to see if on the approved list
- subnets can pass packets of information from one another, depending if the instance of that subnet allows it
- **Network Access Control List (ACL)**- the packets that are within the message from the internet will be checked against the ACL to see if it has permission to enter or lave the network
	- Is a virtual firewall controlling inbound and outbound traffic
	- This controls the in and out for a subnet
	- stateless, so it will check every packet coming
	- it will check both outgoing and incoming
	- Important to know that even if an ACL from a different subnet granted permission for it to leave that subnet, an incoming ACL doesn't automatically give it permission to enter that subnet
	- by default it allows all incoming and outgoing traffic so need to configure what it doesnt allow
- Different instances may have different specifics about who can send them requests or recieve so need instance level network security
	- instances have security groups
		- doesnt allow any traffic into the instance by default, all ports blocked and all IP addresses are blocked
		- have to configure what incoming traffic you want
		- all traffic can go out of the security group, no restrictions on outbound
		- security groups are stateful so has some memory about who to allow in or out
		- security groups by default allow all return trafiic (from the stateful memory)
	- Can have a different security group for different EC2 instances within the same subnet
- **Public Subnets**- 
	- resources accessible for the public like internet- APIs, client
- **Private Subnets**-
	- resoruces only to interact with through private network like adatabase through API
- Can have a public subnet talk to a pirvate subnet (API to database)
- **Domain Name System (DNS)**- 
	- request goes from the client to the Customer DNS resolver which then gets then forwards the request to the DNS server to return the IP address based on the DNS name
	- the request returned from the IP address then goes to cloudfront to connect to load balancer which sends the packet to an EC2 instance

## Storage and Databases
- **Relational Database Service (RDS)**
	- relational database are managed here (MySQL, PostgreSQL, Oracle, Microsoft SQL server etc)
	- this is the kind of outer layer which Aurora and others are managed in
	- **Lift-and-Shift**- migrate your relational database to run on an EC2 instance
		- Gives same control over the same variables like OS, memory, CPU, storage capacity
	- this includes automated patching, backups, redundancy, failover, disaster recovery managed through AWS, rather than doing yourself
	- **Aurora**- compatible with MySQL and PostgreSQL and is the AWS kind of version of a relational database
- **Database Migration Service (DMS)**
	- helps customers migrate their existing database onto AWS
	- source database remains operational in the meantime while migrating to the target database on AWS
	- **Homogenous migration**- migration of the same database type- MySQL -> RDS MySQL
	- **Heterogenous migration**- migration of different database types
		- Need to convert the data with AWS Schema Conversion Tool
		- Then migrate the newly converted data
	- **Development and test database migrations** - testing against production data without impacting production users
	- D**atabase consolidation**- several databases you want to consolidate into one central database
	- **Continous database replication**- use DMS to perform continous data replication for disaster recovery or geographic separation

## Security
- **Shared responsibility model**- how AWS and customers work together to ensure top leve security
	- AWS constrols security of the cloud, like data centers, services and all the layers 
		- compute, storage, database, networking, regions, AZ, edge locations, global infrastructure
	- Users control the security within the cloud
		- in charge of the OS through the encryption key to login and create user accounts for an EC2 instance (AWS can only notify if the type of OS you are running is in-secure)
		- customer data, platforms, applications, IAM, OS, network, firewall config, client-side data encryption, server-side encryption, network trafficking protection
- **USer access**- 
	- when creating AWS, you have a root user which is the main of the account and ownder and has permissiion to do anything they want
	- create the IAM which has no permissions to start with and then add on- least privilege principle- give people access only to waht they need
	- **MFA**- random code sent to phone for authentication- can be hardware security key or phone app
- **Compliance**- company needs to ensure they are up to complaicen and auditing standards and regulations
- **Customer Compliance Center**- contains resources to learn more about AWS compliance
	- can access compliance whitepapers and documentation
	- contains auditor learning path
- **Distributed Denial of Service attach (DDOS)**- 
	- the idea of the attack is to shutdown your application by overwhelming the system by shooting many requests
	- use AWS Shield to protext against DDOS attacks
- **Key Management Service**- used to store encryption keys for transit between two servers
- **Web Application Firewall (WAF)**- monitor network requests coming into web appliocations
	- works together with Cloudfront and ALB

## Monitoring and Analytics
- able to monitor all the traffic that your services have
- can use the AWS Trusted Advisor for evaluating your seources against the five pillars- cost optimisation, performance, security, fault tolerance and service limits
	- can check things like if y o have wasted resources in a not-turned off ec2 instance etc
	- does checks to make sure everything is opztimise

## Pricing & Support
- **Free Tier**- good for getting started
	- Service 1- Alwasy free- doesnt expire, services will have a limit of free uses in a specific amount of time to use
	- Service 2 - 12 months free- 12 months to try out the service after creating the account
	- Service 3- trials- some services offer short-term free trial and then expire
- **Pay-As-You-Go Pricing**- 
	- Pay for what you use- pay exactly the amount of resources that you actually use without a long-term contract
	- Pay less when you reserve- reservation options that offer big discount compared to On-Demand instance pricing
	- Pay less with volume-based discounts when use more- sopme services offer tiered pricing, per-unit cost lower with usage (eg S3 storage, more space you use the less you pay for it)
- **AWS Pricing Calculator**- create estimate cost for use cases
	- good for selecting regions or instance types to suit the most cost-effective use case
- **Billing Dashboard**- view all your billing like month-to-month spending
- **Consolidating billing**- because there are multiple accounts shared under one business (organisation) you can consolidate all the billing into one bill for the main account to pay
- **Budgets**- set custom budhets for variety of scenarios like cost and usage
	- receive an alert when cost or usage exceed or are forecasted to exceed the budgeted amount
- **Cost Explorer**- shows which services you are spending most money
	- gives 12 months of historical data to track spending
	- filter by tags on services (group services with tags for easier identifier)
- **Support Plans**- help from AWS for your business needs
	- **Basic Suppoert**- access support like 24/7 customer service access, documentation, whitepapers, support forums, Trusted Advisor AWS and AWS personal health dashboard (view of the health of AWS services and any alerts you recieve if resources are impacted)- all free for everyone
	- **Developer Support**- includes everything in basic support, plan, plus can email customer support directly with 24 hour response time
		- responses of less than 12 hours for system impairment
	- **Business Support**- include everything from previous plans
		- directo phone access to support team with 4 hour response time for system impair
		- 1 hour response time if prod system is down
		- access to infrastructure event management
	- **Enterprise On-Ramp** for migrating business from development to production- 
		- have 30 min response times for business critial workloads
	- **Enterprise Support**- 15 minute response time for business and critical workloads
		- TAM Techincal-Account Manager is an AWS person actively monitoring your environment and help with optimization
		- they help provide the well architected framework- Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimzation, Sustainability
- **Marketplace**- resource to find third-party software that runs on AWS