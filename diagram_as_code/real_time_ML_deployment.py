from diagrams import Cluster
from diagrams import Diagram
from diagrams.aws.compute import Lambda
from diagrams.aws.ml import SagemakerTrainingJob
from diagrams.aws.ml import Sagemaker
from diagrams.aws.ml import SagemakerModel
from diagrams.aws.mobile import APIGateway
from diagrams.aws.database import Dynamodb as  DDB

import os

filename = os.path.basename(__file__).replace(".py", "")

graph_attr = {"fontsize": "12", "bgcolor": "white"}

with Diagram(
    filename,
    show=False,
    direction="LR",
    outformat = "png",
    filename=f"output/{filename}",
    graph_attr=graph_attr,
):
    with Cluster("Sagemaker"):
        process_job = Sagemaker("Processing Job")
        training_job = SagemakerTrainingJob("Training Job")
        model_creation = SagemakerModel("Create Model")
        model_registration = SagemakerModel("Register Model")
        sagemaker_endpoint = APIGateway("API Gateway")
        process_job >> training_job >> model_creation >> model_registration >> sagemaker_endpoint

    api_gateway = APIGateway("API Request")
    lambda_fn = Lambda("Update Credentials")
    dynamo_db = DDB("Dynamo DB")
    api_gateway >> lambda_fn >> dynamo_db
    sagemaker_endpoint << lambda_fn
