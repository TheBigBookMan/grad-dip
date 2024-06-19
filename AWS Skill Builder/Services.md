## Simple Storage Service (S3)
- Stores any type of data as an object
- Can be even static files like html, videos, images, stylesheets etc

## Elastic Compute Cloud (EC2)
- virtual server
- can run any sort of OS on it
- good to have multiple EC2 instances across different buildings
- can change instance type and size of resources wanted
- **Instance Connect**- allows you to connect to the Instace or an SSH client
- **Session Manager**- allows the session to begin connetion through client or SSH
- Terminal is used to talk with the EC2 instance
- **INstance types**- 
	- General purpose- good balance computte, memoery and networking resources- good for web service or code repo
	- Compute optimised- intensive tasks like game servers, high perofrmance computing and scientific modeling, better for batch processing- group data processing
	- Memory optimised- memory-intensive tasks, floating point calculations, graphics processing, data pattern matching, better for processing large datasets in memory
	- Storage optimized- high performance for locally stored data
- **EC2 Pricing**-
	- On-demand- pay for duration that instance runs for- ideal for short term and irregular workloads that cant be interrupted, utilise unused capacity at a discounted rate. No long-term commitment or upfront paments
	- Savings plan- low prices on EC2 usage for a commitment to consistent amount of usage- reduce your EC2 instance cost when making hourly spend commitment to instance family and region for 1-3 year planb, enter contract to get discounted rate
	- Reserved Instances- predictable usage and steady-state workloads- good for when you know the amount of usage and type, covered for 1 year or 3 year. Pay up front and reserve for one or 3 year
	- Spot instances- request for spare EC2 computing capacity- 90% off on-0demand price- AWS can reclaim the service anytime
	- Dedicated hosts- pay for physical host that is fully dedicated to running instance- pay by the hour for the instances that run on single-tenant hardware
- **Scale horizontally**- launch new EC2 instances and add to the pool
- **Scale vertically**- resize the instance
- **EC2 Auto-scaling**-
	- For horizontal scaling
	- having the beginning resources you have and then making it automatically scale responding to demand upwards or downwards
	- Not over paying for unused resources or having not enough resources at a high-deman period
	- **Dynamic scaling**- responds to changing demand
	- **Predictive scaling** - Automtically schdeul right number of EC2 instances based on predicted demand (higher demand periods or lower demand periods)
	- **Scale up**- increasing the size of the server
	- **Scale out** - increasing amount of servers
	- Can set desired capacity for a server and the amount of servers

## Elastic Load Balancer (ELB)
- Directing traffic
- Able to see which servers have lower amount of usage and can direct traffic to the underused ones so ones currently being used dont have too much traffic and cause problems
- auto-scaling lets the ELB know it needs to start directing traffic

## Simple Queue Service (SQS)
- send, store and receive messages between software components at any volume
- no losing messages or requiring other services to be available
- messages are the information related to data of what is being processed
- the SQS is where the messages are stored in a queue
- allows for queueing up of messages, when one service may be handling a lot of load, rather than waiting for it to finish to process the next load

## Simple Notification Service (SNS)
- used to send out messages to services or send notifications to users
- called publish/suibscribe model- create a SNS topic where chanel for messages are to be delievered
- configure subscribers to that topic and ginally publish messages for those subscribers
- send one message to a topic and then it fans out to all of the subscribers in a single go
- subscribers can be endpoints such as SQS, lambda functions, https and web hooks
- can be used for mobile push, SMS and email
- subscribers can subscribe to a single topic or multiple topics- and will only receive messages about those topics

## Lambda
- serverless functions that run code when the function is triggered by an event source
- only pay for the compute time that you consume
- good if a specific functionality isnt triggered all the time (eg some functions may only get triggered a few times during the day)
- bad if the functions are triggered a lot- then better to just host it on an EC2 instance

## Elastic Container Service (ECS)
- containerising application code and hosting on a server in AWS
- supports Docker images, so can deploy in development with docker and then host in ECS for production

## Elastic Kubernetes Service (EKS)
- run Kubernetes on AWS
- deploy and manage containerised applications at scale
- making sure that any sort of containerisation 

## Fargate
- serverless compute engine for containers
- works with both ECS and EKS
- dont need to provision or manage servers, Fargate manages the infrastructure for you
- pay only for resources required to run on your containers
## Amazon Machine Image (AMI)
- Template image that stores the software configuration
- Stores information about what sort of OS, application server and applications are on this virtual server

## Elastic Block Store (EBS)
- The hardware storage thats used in tandem with the EC2 instance 
- this is where you store your database and S3 stuff etc
- Solid state drive and hard disk storage selections
- storage remains even if the EC2 instance has stopped

## Identity Access Management (IAM)
- User permissions for restriction etc
- have the root owner and then they can provide permissions for workers to specific services
- where all the users credentials and security are stored
- important to be able to access specific services for things like read, write, delete etc

## Systems Manager
- able to view how the EC2 instances are working in terms of analytics
- able to control what sort of server and application management happen on the system

## Pricing Calculator
- Can make pricing estimates for aws use cases
- can make calculations based on how much usage estimating some services will have at periods of time (eg EC2 instances lower usage during weekends)
## CloudFront 
- a CDN that will host things in a specific location that may be closer to another location for faster delivery speeds
- Separate from regions so its not taking up as many resources and costing as it would to serve a whole isntance in another region
- They are sites which hold the storage
- they are located closer to where users are, so for example because im in adelaide, could have one closer to me like in adelaide as well or Melbourne (even though there is a region there)

## Elastic Beanstalk 
- helps with orchestrating multiple services together
- give it the application code and desired configurations and beanstalk will build and save the environment for easier deployment
- gives convenience of not provisioning and managing all the pieces separately while still giving visibility of underlying resources
- Adjust capacity, load balancing, automatic scaling, application health monitoring

## Cloudformation
- Infrastructure as code tool that defines variety of AWS resources using JSON or YAML- rather than using the GUI
- performs automatic for replicating the exact infrastructure environment
- specify what you want built without the details of how to build it
- it calls the APIs to get everything built
- Define the resources into a template and this template will be parsed and built the infrastructure
- replicating the infrastructure across multiple places if you want- removes human error chances for duplicating infrastructure

## Outposts
- an on-premise data center that can offer extending your resource allocation by having a specific device 
- This will act like a data-center, and may be beneficial if need another data center in a specific spot
- acts like an edge location

## Virtual Private Cloud (VPC)
- private cloud within the aws cloud and is virtual
- virtual network
- cofigure route tables, ip addresses, firewalls, subnets etc
- provision isolated section of the AWS cloud where can launch AWS resources in a virtual network that you define
- can be public facing with internet access or private facing with no internet access
- private and public grouping of resources is known as subnets and they are ranges of IP addresses in the VPC
- public subnet can be for interacting with the internet or client interaction
- private subnet can be for things you dont want touching the internet or clients directly

## Route 53
- AWS domain name service (DNS)
- translates the website name into an IP for computers to read
- Route 53 can direct traiffic to different endpoints using a routing policy like geolocation- this helps routing to closer regions from where the customer is
- can buy and register your own domain names
- works with the load balanacers and EC2 instances