# Automated-Serverless-File-Transfer-and-Backup-System-on-AWS


This repository contains code and documentation for an automated file transfer and backup system using AWS Lambda and S3. It automates the process of uploading files from a local directory to an S3 bucket, implements backup strategies with versioning, and manages file lifecycle using S3 lifecycle rules.


Objectives

Automate File Transfers: Upload files from a local machine to an AWS S3 bucket using AWS CLI.
Implement Backup Strategy: Enable S3 versioning to maintain backup copies of files.
Lifecycle Management: Set up S3 lifecycle rules to archive and delete files based on a specified policy.


Prerequisites

AWS account
AWS CLI installed and configured
Basic understanding of AWS services (S3, Lambda, IAM)


Architecture

AWS S3: Used for storing files and managing backups with versioning and lifecycle rules.
AWS Lambda: Automates the file transfer process.
AWS CLI: Facilitates file uploads from the local machine.


Steps to Implement the Project

Create an S3 Bucket and enable S3 versoning

Create IAM Role for Lambda

Create a IAM Function

Configure Function code

Set up IAM Role Permissions

Test the lambda Function

Set Up Lifecycle Rules
