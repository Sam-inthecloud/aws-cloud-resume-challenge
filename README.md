# AWS Cloud Resume Challenge
This project is my submission for the AWS Cloud Resume Challenge. 
[The Cloud Resume Challenge](https://cloudresumechallenge.dev/docs/the-challenge/aws/) is designed to demonstrate the ability to create and deploy a dynamic resume website using various Cloud Services.

## Architecture
![Architecture](https://github.com/Sam-inthecloud/aws-cloud-resume-challenge/blob/main/AWS%20Cloud%20Resume%20Map.png?raw=true)

## Project Overview
- Website : https://saminthecloud.tech

**Services Used**:
- Amazon S3: Used to store and serve the static website files (html/css/js/img).
- CloudFront: For faster content delivery and global distribution.
- Certificate Manager: To provide a domain validated SSL/TLS certificate.
- IAM : For managing policies allowing services access to each other.
- Route 53: DNS service for domain registration and management.
- Lambda: Handles the serverless functions to update and retrieve the resume data (Visitor Count).
- API Gateway: Provides an API for interacting with the Lambda functions.
- DynamoDB: A NoSQL database for storing the retrieved resume data(Visitor Count).
- GitHub: For Source Control and CI/CD (continuous intergration and deployement of the website)
- Terraform: Used to deploy the lambda function as a code.
