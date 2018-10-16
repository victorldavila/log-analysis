# log-analysis

This is a project for Udacity's Backend Developer nanodegree

## Project description

Your task is to create a log system that will report some information based on the data in the database. 
This system will answer basicly to three questions:

- What are the most popular 3 articles of all time?
- Who are the most popular 3 article authors of all time?
- On witch day did 1% of requests lead to errors?

### Basic setup

This project runs in a virtual machine created using Vagrant. So, there are a few steps to follow:

- Install [Vagrant](https://www.vagrantup.com/downloads.html).
- Install [Virtual box](https://www.virtualbox.org/wiki/Downloads).
- Download the Vagrant setup files on [Udacity's Github](https://github.com/udacity/fullstack-nanodegree-vm). 
These files are necessary to configure the virtual machine with all necessary tolls to run this project.
- Download the database [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
- Unzip the file and get the .sql file.
- Put the .sql file inside the Vagrant shared directory.
- Download this project [Log Analysis](https://github.com/victorldavila/log-analysis).
- Put all the files inside the Vagrant shared directory.

#### Execute project

These are the steps to you follow up and execute the project:

- Open the terminal inside the Vagrant directory.
- Execute the command line `vagrant up` to build the VM.
- To connect to the VM just execute the command line `vagrant ssh`.
- To import the .sql file execute the command `psql -d news -f newsdata.sql` inside the directory where the file is.
- After that just run `python LogProject.py`.

##### Expected output

```
The 3 most popular articles of all time are:

Ursula La Multa ------ 507594
Rudolf von Treppenwitz ------ 423457
Anonymous Contributor ------ 170098

The 3 most popular article authors of all time are:

Candidate is jerk, alleges rival ------ 338647
Bears love berries, alleges bear ------ 253801
Bad things gone, say good people ------ 170098

Days with more than 1% of request that lead to an error:

2016-07-17 00:00:00+00:00 ------ 0.023
```
