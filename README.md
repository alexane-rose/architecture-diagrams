# Architecture Diagrams
Architecture Diagrams to deploy resources in AWS (Diagrams as code)✏️

## Running the repo
- To run this repository use `make init` to get graphviz and install the required libraries.
- To generate the charts run `make diagrams`.
- The diagrams are defined in code in the directory `diagram_as_code/`.

## In this repo...
In this repo you can find diagrams defined in code describing the following architecture blocks :
- ETL pipeline using glue
- Lambda function to process data manually added by a user
- Rotate API user credentials in Tableau

## Architecture Blocks
### ETL pipeline using glue
ETL pipelines are used to process raw data and make it usable for data science activities. In the picture below the raw data is made available through amazon Athena. Processed by Glue functions that are orchestrated by an AWS state machine. The state machine is triggered on a scheduled event. The output data is written as a tables into S3. The logs from the glue jobs are sent to cloud watch. A dashboard monitors the state machine's success and failures. This logic is pictured in the diagram below.
![alt text](https://github.com/alexane-rose/architecture-diagrams/blob/main/output/ETL_using_glue.png?raw=true)

### Lambda function to process data manually added by a user
On occasion, a data sources relies on a manual file. This file is added to an S3 bucket and needs to be verified and processed before it can be used by a data pipeline.
![alt text](https://github.com/alexane-rose/architecture-diagrams/blob/main/output/processing_new_s3_file.png?raw=true)
Steps :
- Users adds file to S3 input bucket
- An event triggers a lambda function
- The lambda function processes the file
- The processed data is written to s3, where it can be read from a data pipeline.


### Rotate API user credentials in Tableau
Tableau is a visualization tool to build dashboards. It is possible to connect tableau to Athena using the built in connector. When doing so credentials to an AWS API user need to be passed. For security purposes the credentials often have to be rotated. As there often multiple connections changing all credentials manually is very tedious. The method below automates the credential rotation.
![alt text](https://github.com/alexane-rose/architecture-diagrams/blob/main/output/rotate_tableau_api_user.png?raw=true)
Steps :
1. Create an API AWS IAM user.
2. Provide the API user access to the needed Athena databases and tables using lakeformation.
3. Create a scheduled event to trigger the key rotation and save new keys in secret managers.
4. On key rotation an event triggers a lambda function
5. The lambda functions

### Real Time Machine Learning Model deployment

![alt text](https://github.com/alexane-rose/architecture-diagrams/blob/main/output/real_time_ML_deployment.png?raw=true)
