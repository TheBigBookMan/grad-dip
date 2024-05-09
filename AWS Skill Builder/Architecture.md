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