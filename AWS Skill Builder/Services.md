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

## Virtual Private Cloud (VPC)
- private cloud within the aws cloud and is virtual
- virtual network
- cofigure route tables, ip addresses, firewalls, subnets etc