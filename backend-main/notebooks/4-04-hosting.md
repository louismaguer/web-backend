# hosting

many online solutions are available for hosting your web apps

- static hosting
  - surge.sh
  - netlify.com
  - vercel.com

- CI/CD
  - github pages (powered by github actions)
  - readthedocs.io
  - ...

---

## Fast and easy: fly.io

It's rather easy to host you web app on fly.io; the repo below shows how to do
it using Continuous Deployment (CD) with Github Actions on a super-simple
FastAPI app.

https://github.com/ue22-p25/backend-fastapi-flyio

there are many advantages with this kind of service:

- you can deploy your app in a few minutes
- you pay as you use it
- and the machines get turned off automatically when not in use
- you can scale up and down easily

---

## Cloud operators

Many operators offer cloud services

- AWS
- Google Cloud
- Azure
- Digital Ocean
- Scaleway
- OVH
- etc..

---

## Cloud offerings

- metal
  - bare metal servers

- instances
  - virtual machines

- kubernetes
  - the substrate is ready for you
  - kube is about **container orchestration**
  - this means you just write yaml files
  - you describe **the state you want to reach**
  - not **the order in which to do things**
  - the kube engine will take care of it
  - offers a huge number of sophisticated features
  - e.g. load balancing, replicas, scaling, ...

k8s has a rather steep learning curve, but very much worth it;  
particularly as it is a standard and you can use it on any cloud provider

---

## Illustration on Scaleway

`````{div}
:class: columns
````{div}
:class: sixty
- web console
- docs & the API
- the CLI
- billing
- monitoring
  - prometheus
  - grafana
  - graphQL
````
````{div}
:class: fourty
```{image} media/scaleway-instances.png
:width: 100%
```

  ```{image} media/scaleway-grafana.png
:width: 100%
```
````
`````

---

## Docker: a container engine

- what is a container ? think of it as:

  - a root image (filesystem)
  - a set of processes (process group)
  - a network namespace (IP address)

- in short, it is a *lightwight* virtual machine
  - except that it **shares the kernel** with the host OS

- an app vendor can package their app
  - with all its dependencies
  - and ship it as a container image

- so in pratical terms:
  - instead of running a service inside an OS, you run it **inside a container**
  - e.g. you can run a linux-based nginx server inside a container in a Windows machine
  - **note** there are some gory tricks at work (does WSL rings a bell ?)

---

## CI/CD

### Continuous Integration / Continuous Deployment

- CI/CD is a set of practices that enable development teams to deliver code changes more frequently and reliably

- CI focuses on automating the integration of code changes from multiple contributors into a single software project

- CD automates the deployment of code changes to production

- example : github actions
  - look at the `.github/workflows` folder

- example: readthedocs (continuous documentation)
  - in the numerique course, see the `.readthedocs.yaml` file

---

## firewalls

- a firewall is a network security system that monitors and controls incoming and outgoing network traffic based on predetermined security rules
- typically it is configured to allow or deny traffic based on
  - IP addresses
  - ports
  - and protocols

- typically if you set up a web server in the cloud, you will
  - deny all traffic
  - except TCP incoming traffic on port 22 (SSH)
  - and on port 80 (HTTP) and/or port 443 (HTTPS)

any temporary need (join a debug endpoint on port 9000, for example) can be done
through a SSH tunnel
