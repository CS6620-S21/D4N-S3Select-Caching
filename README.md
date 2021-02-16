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
3. Cache data and update the global directory, return formatted response in Arrow. Hence, evaluating the result of the s3 select cache
4. Update the Spark jobs to read the response in arrow format.
 
** **

## 4. Solution Concept
<!-- Some technical descp about D4N -->
<!-- System archictecture Diagram -->
![System architecture]( D4N%20Block%20Diagram.png "D4N Architecture")

<div style="text-align: justify">

1. <b>Ceph</b> - Ceph is a distributed storage platform implemented as an object storage. It is highly scalable and distributed system running on a compute cluster. It stripes and distributes the file across multiple nodes for high throughput and fault-tolerance. It supports Object, Block, and File System storage by providing different layers over object storage, and a single interface to all the three storage types. It supports these functionalities using various daemons (cluster monitors, object storage devices, http gateways, etc.) running on top of each node.

2. <b> RGW </b> -

3. <b>S3</b> - S3 is a protocol that is used to store and retrieve any amount of data, on the web. Here S3 is being used to access the Ceph storage clusters using boto3 library.

4. <b>S3 Select</b> - S3 Select is a service that allows running simple queries on top of S3 Objects. This allows users to retrieve selective data from objects, as per the specified query, rather than fetching the entire object, thus saving network bandwith, processing time and resources.
In the current implementation of D4N, the client reads and caches the entire files from the storage although a subset of the object might be required.  With S3 Select, the goal is to enable the clients to retrieve and cache the data in D4N,resulting in reduced network data transfer, and efficient use of cache memory. 

5. <b>Apache Arrow</b> - Apache Arrow is a software development platform for building high performance applications that process and transport large data sets. It is designed to both improve the performance of analytical algorithms and the efficiency of moving data from one system or programming language to another. We aim to use Arrow as the format for communication from the cache to the clients, to make the transfer of cached data more efficient.

7. <b>Global directory (REDIS)</b> - 
Redis is an open source (BSD licensed), in-memory data structure store, used as a database, cache, and message broker. In contect of D4N, Redis is being used a Global directory to index that data stored in the distributed cache.
<!-- 6. Read Cache -->
8. <b>Compute Nodes/Clients</b> - The compute nodes are the spark jobs that run on the cluster. They are the users of the D4N caching mechanism and they request data from the Ceph storage. However, they do not directly communicate with the Ceph storage, they do that through the Rados gatway(RGW). Part of this project, also focuses on enhancing the clients to accept the results of S3 select, from the cache, in Arrow format.
9. <b> Spark </b> -  Apache Spark is an open-source, distributed processing system for big data workload. Spark utilizes in-memory caching, and optimized query execution for fast analytic queries against data of any size. Spark will enable code resuage across multiple workloads—batch processing and interactive queries.
Part of this project involves modifying Spark's System to request S3 Select queries where S3 Select allows applications to retrieve only a subset of data from an object.  
</div>
<!-- System archictecture Diagram -->
![System architecture]( Spark%20S3%20Select%20Pipeline.png "Spark - S3 Select Pipeline")


<!-- -->
To accomplish our overall goal, we will break it into these subtasks:
1. Modify Spark to make it request S3 Select queries 
2. Make Spark request and understand the Arrow file format
3. Combine S3 Select with D4N
4. Cache the results in D4N from remote Ceph cluster
5. Lookup in the cache before forwarding the request to the remote Ceph cluster
6. Retrieve the data found in D4N or generate a request to the remote Ceph

## 5. Acceptance criteria

We aim to complete the implementation of S3 Select in the D4N Caching mechanism, which is minimum acceptance criteria for the project. The product which satisfies the minumum acceptance criteria will support the following operations -

1. The Rados gateway(RGW) will be able to accept S3 select requests.
2. The RGW will be able to run the queries on the Ceph storage cluster and retrive the results.
3. The results of S3 select queries will be cached in the distributed cache and indexed in the global directory.

## 6.  Release Planning:

Detailed user stories, plan and backlog will be via Tiaga 

Week 1 & 2  
			- Set up Ceph and Spark; have D4N with S3 Select run basic queries 
              Individual Tasks 
								1. Build and run master Ceph
								2. Build Spark with S3 Select
		   						3. D4N and S3 Select codewalk; understand workflow for S3 Select on Spark and Arrow with Ceph 

Week 3,4,5,6 
			- Implementation 

Week 7 & 8 
			- Testing and Performance evaluation

Week 8 & 9 
			- Documentation





** **


For more help on markdown, see
https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

In particular, you can add images like this (clone the repository to see details):

![alt text](https://github.com/BU-NU-CLOUD-SP18/sample-project/raw/master/cloud.png "Hover text")



