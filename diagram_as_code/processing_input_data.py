from diagrams import Cluster
from diagrams import Diagram
from diagrams import Edge
from diagrams.aws.analytics import Athena
from diagrams.aws.analytics import Glue
from diagrams.aws.storage import SimpleStorageServiceS3 as S3
from diagrams.aws.compute import Lambda
from diagrams.aws.general import User
from diagrams.aws.integration import Eventbridge
from diagrams.aws.management import Cloudwatch
from diagrams.aws.management import CloudwatchEventTimeBased
import os
filename = os.path.basename(__file__).replace(".py","")

graph_attr = {
    "fontsize": "12",
    "bgcolor": "white"
}

with Diagram(filename, show= False, direction="LR", outformat="png", filename = f"output/{filename}", graph_attr=graph_attr):

    user = User("User")
    input_bucket = S3("Input Bucket")
    event = Eventbridge("New file detected")
    lambda_fn = Lambda("Process File")
    output_bucket = S3("Output Tables")
    cloud_watch = Cloudwatch("Monitoring")

    user>> input_bucket>> event >> lambda_fn >> output_bucket
    lambda_fn >> cloud_watch
