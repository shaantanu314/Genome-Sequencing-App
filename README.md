# AI Model Deployment 
(Genome sequencing)



## CS4.409. Data Foundation Systems




## Spring 2023



### Team Name: **Raccacoonie**

				Aakash Reddy Gorla - 2020102034
				Smruti Biswal - 2020112011


#### **Overview**
	The general use of AI is restricted to or at least promoted to tasks in which human intelligence is required, but in the case of genome sequencing the main purpose for the deployment of AI is to reduce the number of errors as it is a task extremely prone to human error considering the type of data being processed. Clinical genetic testing can also benefit from computer vision. As an illustration, deep learning of histological images of lung cancer can be used to recognise cancer cells, ascertain their type, and forecast which somatic mutations are present in the tumour. Similar to this, facial image recognition can help molecular diagnosis and help identify unusual genetic illnesses. In order to make suggestions for molecular testing in a way comparable to that carried out by an experienced pathologist or dysmorphologist, computer vision can thus extract phenotypic traits from medical photographs. In some situations, AI-based systems have outperformed human specialists. For instance, they have been able to reliably determine gender from retinal fundus images, a task that human experts would only be able to complete with a high degree of randomness. In this project we aim to provide a platform with both services: AI models and Computer Vision(Preprocessing) which is user friendly and scalable. The user will be able to mix-n-match different preprocessing stages in the pipeline as well as the AI model(restricted to a select few).


#### **Requirements**

**Functional Requirements:**

*AI Model*

* A deep learning model, preferably based on a Convolutional Neural Network (CNN) or Recurrent Neural Network (RNN) architecture, that is capable of accurately classifying sleep stages from sleep EEG signals should be able to: 

	* Train on a large dataset of Genome Sequences and be optimised for high accuracy
	* Process sleep EEG signals in real-time
Produce predictions of the sleep stage for each time step in the EEG signal.

*Web App*

* A simple online application that lets users submit their sleep EEG data and receive predictions from the AI model.
* The software will be hosted on a scalable cloud architecture and should be usable from any device with an internet connection.
* There will be multiple AI models available as microservices which the user can use in a ‘drag-n-drop’ fashion to best serve their needs according to their database.
* The proper preprocessing steps will be available in the same manner as above for the data.

*Data*

* Large set of genome data which will pass through multiple preprocessing stages in order to prepare it for the AI model.
* We will be using MySQL to store our database
* Below is an example of the data format(This data model is just an example and could be expanded or modified depending on the specific needs of the application):

Table Name	| Description
----------- | ------------
sample | Contains metadata for each genome sample, including unique sample ID, patient ID, sequencing platform, and sequencing date.
read | Contains information about the individual sequencing reads, including read ID, read sequence, read quality scores, and the sample ID to which the read belongs.
alignment | Contains the output of the alignment step, which maps each read to a reference genome, including alignment ID, reference genome ID, start position, and end position.
variant | Contains information about the genomic variants found in each sample, including variant ID, variant type (SNP, insertion, deletion), and genomic coordinates.
annotation | Contains functional annotations for each genomic variant, including gene ID, gene name, gene description, and variant effect (e.g. missense, nonsense, synonymous).
expression | Contains gene expression data for each sample, including gene ID, expression value, and sample ID.
phenotype | Contains phenotype data for each sample, including sample ID and any relevant phenotype information (e.g. disease status, age, sex).



*Preprocessing Stages:*

Stages should include generic preprocessing for data as well as CV stages relevant to genome images and microarrays.
	
*Non-Functional Requirements:*

These are the following non-functional requirements:
1. Performance
2. Security
3. Scalability
4. Compatibilty
5. User Interface

*Performace:* 
Trying to achieve the minimal response time for handling a high volume of traffic and queries. 

*Security:*
Security measures like user authentication, access control etc.

*Scalability:*
To handle rising traffic and database load, the system architecture will be scaled either horizontally or vertically.

*Compatibilty:*
The system must work with a variety of web browsers, gadgets, and screen sizes.

*User Interface:*
The system must run continuously with little downtime for upgrades and maintenance. For a positive user experience, the user interface must be simple to use, intuitive, and responsive.


***Process***


**Flow chart:**

Here is a flow chart containing the components relevant to our project:

'''mermaid
[![](https://mermaid.ink/img/pako:eNolkNGKwjAQRX8lzLP-QIUFNXYRLAh1n9I-DMnYBpukTFOWIv77ZpO3cM-BIecNOhiCCgbGeRQPeei8EEclMaJoY2AcqBf7_Zc4le3OQdOyWD_0WT1leFYN6tF6EjdC9omKmtHRb-BX8c7Zk6pJ5ybxYLTZQm-EpHkKmyMfiyqzelHH-7UMlzzU6mchFlcfiZ-oqbA6s2_Vkl7Zxq0_wA4csUNr0rfe_04HcSRHHVTpaZBfHXT-kzxcY2g3r6GKvNIO1tlgJGkx1XBQPXFa0krGphBN6ZRzff4AhaVkfw?type=png)](https://mermaid.live/edit#pako:eNolkNGKwjAQRX8lzLP-QIUFNXYRLAh1n9I-DMnYBpukTFOWIv77ZpO3cM-BIecNOhiCCgbGeRQPeei8EEclMaJoY2AcqBf7_Zc4le3OQdOyWD_0WT1leFYN6tF6EjdC9omKmtHRb-BX8c7Zk6pJ5ybxYLTZQm-EpHkKmyMfiyqzelHH-7UMlzzU6mchFlcfiZ-oqbA6s2_Vkl7Zxq0_wA4csUNr0rfe_04HcSRHHVTpaZBfHXT-kzxcY2g3r6GKvNIO1tlgJGkx1XBQPXFa0krGphBN6ZRzff4AhaVkfw)
'''

