# D4N-S3Select-Caching

** **

## 1.   Vision and Goals Of The Project:

D4N is a a multi-layer cooperative caching solution which aims to improve performance in distributed systems by implementing a smart caching algorithm, which caches data on the access side of each layer hierarchical network topology, adaptively adjusting cache sizes of each layer based on observed workload patterns and network congestion.

The goal of this project is to enhance D4N to directly support S3 Select, a new S3 feature that allows applications to select, transform, and summarize data within S3 objects using SQL query commands. This will allow the clients to read and cache only a subset of object, stored in the Ceph cluster, rather than retrieving the entire object over the network, eventually reducing the traffic of data over the network.

## 2. Users/Personas Of The Project:

The only users in the D4N architecture are the Clients, which are the Spark jobs running on the server racks. The Spark jobs read and write data from the Ceph storage clusters.

The D4N Caching architecture is a caching middleware between the Clients and Ceph storage. 
<!-- The Rados Gatway(RGW) is the object storage interface of Ceph and it is responsible for the communication between the clients and  ceph.  -->

** **

## 3.   Scope and Features Of The Project:

1. Create client workloads that generate s3 select request traffic, and can measure throughput and latency of same.
2. Design and implement a prototype S3 select cache strategy or strategies within D4N; S3 Select to read subset of object from ceph.
3. Cache data and update the global directory, return formatted response in arrow. Hence, evaluating the result of the s3 select cache
4. Update the Spark jobs to read the response in arrow format.
 

** **

## 4. Solution Concept
<!-- Some technical descp about D4N -->
1. Ceph 
2. RGW
3. S3 
4. S3 Select
5. Apache Arrow
7. Global directory (REDIS)
<!-- 6. Read Cache -->
8. Compute Nodes/Spark jobs

<!-- System archictecture Diagram -->

## 5. Acceptance criteria

This section discusses the minimum acceptance criteria at the end of the project and stretch goals.

## 6.  Release Planning:

Release planning section describes how the project will deliver incremental sets of features and functions in a series of releases to completion. Identification of user stories associated with iterations that will ease/guide sprint planning sessions is encouraged. Higher level details for the first iteration is expected.

** **


For more help on markdown, see
https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

In particular, you can add images like this (clone the repository to see details):

![alt text](https://github.com/BU-NU-CLOUD-SP18/sample-project/raw/master/cloud.png "Hover text")



