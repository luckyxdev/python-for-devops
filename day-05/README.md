# Day 05 – File Cleanup Automation with Python

## Task

Today’s goal is to understand **how Python can automate file and directory management**.

## File Cleanup using Python

I created a Python script that:

- Walks through a target directory recursively
- Checks each file for:
  - Age (files older than a set number of days)
  - Size (files larger than a specified size in MB)
- Deletes the files automatically or simulates deletion in **dry run mode**
- Logs all actions into a **log file (`cleanup.log`)**
- Prints a summary of deleted and skipped files in the **terminal**

This helps you understand how Python can automate repetitive system tasks and manage resources efficiently.


## Why This Matters for DevOps

In real DevOps work:
- Disk space management is critical for servers and applications
- Automation prevents manual errors and ensures consistency
- Logging actions ensures **auditability and traceability**