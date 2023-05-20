# architecture-diagrams
Architecture Diagrams to deploy resources in AWS (Diagrams as code)✏️

In this repo you can find diagrams defined in code describing the following architecture blocks :
- ETL pipeline using glue
- Lambda function to process data manually added by a user
- Rotate API user credentials in Tableau


# Architecture Blocks
## ETL pipeline using glue
![alt text](https://github.com/alexane-rose/architecture-diagrams/blob/main/output/ETL_using_glue.png?raw=true)

## Lambda function to process data manually added by a user
![alt text](https://github.com/alexane-rose/architecture-diagrams/blob/main/output/processing_new_s3_file.png?raw=true)

## Rotate API user credentials in Tableau
Tableau is a visualization tool to build dashboards. It is possible to connect tableau to Athena using the built in connector. When doing so credentials to an AWS API user need to be passed. For security purposes the credentials often have to be rotated. As there often multiple connections changing all credentials manually is very tedious. The method below automates the credential rotation.

![alt text](https://github.com/alexane-rose/architecture-diagrams/blob/main/output/rotate_tableau_api_user.png?raw=true)

Steps :
1. Create an API AWS IAM user.
2. Provide the API user access to the needed Athena databases and tables using lakeformation.
3. Create a scheduled event to trigger the key rotation and save new keys in secret managers.
4. On key rotation an event triggers a lambda function
5. The lambda functions
