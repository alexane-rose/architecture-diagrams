from diagrams import Cluster
from diagrams import Diagram
from diagrams import Edge
from diagrams.aws.compute import Lambda
from diagrams.aws.analytics import Athena
from diagrams.aws.management import CloudwatchEventTimeBased
from diagrams.aws.integration import Eventbridge
from diagrams.aws.security import SecretsManager
from diagrams.aws.security import IdentityAndAccessManagementIam as IAM
from diagrams.aws.general import GenericDatabase
from diagrams.aws.analytics import LakeFormation

import os

filename = os.path.basename(__file__).replace(".py", "")

graph_attr = {"fontsize": "12", "bgcolor": "white"}

with Diagram(
    filename,
    show=False,
    direction="LR",
    outformat="png",
    filename=f"output/{filename}",
    graph_attr=graph_attr,
):
    with Cluster("AWS"):
        schedule_rotation = CloudwatchEventTimeBased("Rotation Schedule")
        API_user = IAM("API User")
        API_user_secret = SecretsManager("API User Secrets")
        rotation_event = Eventbridge("Rotation Event")
        athena = Athena("Athena")
        lambda_fn = Lambda("Update Credentials")
        tableau_user_secret = SecretsManager("Tableau User")
        lake_formation = LakeFormation("Lake Formation")

        lake_formation  >> API_user
        schedule_rotation >> API_user >> API_user_secret >> rotation_event >> lambda_fn
        lambda_fn << Edge(style="dotted") << tableau_user_secret
    with Cluster("Tableau Online"):
        data_connection = GenericDatabase("Data Connection")

    lambda_fn >> data_connection
    data_connection >> athena
    data_connection << Edge(style="dotted") << API_user_secret
