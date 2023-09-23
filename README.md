# Cloud DevOps Engineer Capstone Project

This project represents the successful completion of the last final Capstone project and the Cloud DevOps Engineer Nanodegree at Udacity.
- Github: https://github.com/teogit01/project5-final
- Docker: hhttps://hub.docker.com/repository/docker/emb1605272/capstone-project
- CircleCI: [![CircleCI](https://circleci.com/gh/circleci/circleci-docs.svg?style=svg)](https://app.circleci.com/pipelines/github/teogit01/project5-final)
## What did I learn?

In this project, I applied the skills and knowledge I developed throughout the Cloud DevOps Nanodegree program. These include:
- Using Circle CI to implement Continuous Integration and Continuous Deployment
- Building pipelines
- Working with Ansible and CloudFormation to deploy clusters
- Building Kubernetes clusters
- Building Docker containers in pipelines
- Working in AWS

## Application

The Application is based on a python3 script using <a target="_blank" href="https://flask.palletsprojects.com">flask</a> to render a simple webpage in the user's browser (and base on project 4).
A requirements.txt is used to ensure that all needed dependencies come along with the Application.

## Kubernetes Cluster

I used AWS CloudFormation to deploy the Kubernetes Cluster.
The CloudFormation Deployment can be broken down into four Parts:
- **Networking**, to ensure new nodes can communicate with the Cluster
- **Elastic Kubernetes Service (EKS)** is used to create a Kubernetes Cluster
- **NodeGroup**, each NodeGroup has a set of rules to define how instances are operated and created for the EKS-Cluster
- **Toggle** is needed to configure and manage the Cluster and its deployments and services. I created two management hosts for extra redundancy if one of them fails.

#### List of deployed Stacks:
![CloudFormation](./screenshot-p5/stacks.png)

#### List of deployed Instances:
![Show Instances](./screenshot-p5/instances.png)

## CircleCi - CI/CD Pipelines

I used CircleCi to create a CI/CD Pipeline to test and deploy changes manually before they get deployed automatically to the Cluster using Ansible.

#### From Zero to Hero demonstration:

![CircleCi Pipeline](./screenshot-p5/circleci_pipeline.png)

## Linting using Pylint and Hadolint

Linting is used to check if the Application and Dockerfile is syntactically correct.
This process makes sure that the code quality is always as good as possible.

#### This is the output when the step fails:

![Linting step fail](./screenshot-p5/lint_fail.png)


#### This is the output when the step passes:

![Linting step fail](./screenshot-p5/lint_success.png)

## Upload Docker Image After Successful Build

![Upload Docker](./screenshot-p5/docker-repo.png)

## Access the Application

After the EKS-Cluster has been successfully configured using Ansible within the CI/CD Pipeline, I checked the deployment and service log on pipeline as follows:

```
    ##TASK [Get deployment] **********************************************************
    changed: [35.175.184.10] => {
        "changed": true,
        "cmd": "./bin/kubectl get deployments",
        "delta": "0:00:00.942928",
        "end": "2022-11-24 03:02:13.710358",
        "invocation": {
            "module_args": {
                "_raw_params": "./bin/kubectl get deployments",
                "_uses_shell": true,
                "argv": null,
                "chdir": "/root",
                "creates": null,
                "executable": null,
                "removes": null,
                "stdin": null,
                "stdin_add_newline": true,
                "strip_empty_ends": true,
                "warn": false
            }
        },
        "msg": "",
        "rc": 0,
        "start": "2022-11-24 03:02:12.767430",
        "stderr": "",
        "stderr_lines": [],
        "stdout": "NAME                          READY   UP-TO-DATE   AVAILABLE   AGE\n****************-deployment   2/2     2            2           8h",
        "stdout_lines": [
            "NAME                          READY   UP-TO-DATE   AVAILABLE   AGE",
            "****************-deployment   2/2     2            2           8h"
        ]
    }

    ##TASK [Get service] *************************************************************
    changed: [35.175.184.10] => {
        "changed": true,
        "cmd": "./bin/kubectl get services",
        "delta": "0:00:00.948712",
        "end": "2022-11-24 03:02:14.942635",
        "invocation": {
            "module_args": {
                "_raw_params": "./bin/kubectl get services",
                "_uses_shell": true,
                "argv": null,
                "chdir": "/root",
                "creates": null,
                "executable": null,
                "removes": null,
                "stdin": null,
                "stdin_add_newline": true,
                "strip_empty_ends": true,
                "warn": false
            }
        },
        "msg": "",
        "rc": 0,
        "start": "2022-11-24 03:02:13.993923",
        "stderr": "",
        "stderr_lines": [],
        "stdout": "NAME                          TYPE           CLUSTER-IP      EXTERNAL-IP                                                               PORT(S)        AGE\n****************-service      LoadBalancer   10.100.177.14   a703a68e7e0a5469583142ba70acb13b-495769207.*********.elb.amazonaws.com    80:31273/TCP   5h53m\nkubernetes                    ClusterIP      10.100.0.1      <none>                                                                    443/TCP        9h\nmy-****************-service   LoadBalancer   10.100.13.101   ac3d77f3a63ca414ea464fa3c0a69c53-1081686457.*********.elb.amazonaws.com   80:30097/TCP   8h",
        "stdout_lines": [
            "NAME                          TYPE           CLUSTER-IP      EXTERNAL-IP                                                               PORT(S)        AGE",
            "****************-service      LoadBalancer   10.100.177.14   a703a68e7e0a5469583142ba70acb13b-495769207.*********.elb.amazonaws.com    80:31273/TCP   5h53m",
            "kubernetes                    ClusterIP      10.100.0.1      <none>                                                                    443/TCP        9h",
            "my-****************-service   LoadBalancer   10.100.13.101   ac3d77f3a63ca414ea464fa3c0a69c53-1081686457.*********.elb.amazonaws.com   80:30097/TCP   8h"
        ]
    }   
```

Public LB DNS: http://ac3d77f3a63ca414ea464fa3c0a69c53-1081686457.us-east-1.elb.amazonaws.com/\

![Access LB DNS](./screenshot-p5/dns.png)
