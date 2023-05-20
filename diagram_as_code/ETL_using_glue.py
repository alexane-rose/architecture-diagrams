from diagrams import Cluster
from diagrams import Diagram
from diagrams import Edge
from diagrams.aws.analytics import Athena
from diagrams.aws.analytics import Glue
from diagrams.aws.storage import SimpleStorageServiceS3 as S3
from diagrams.aws.management import Cloudwatch
from diagrams.aws.management import CloudwatchEventTimeBased
import os
filename = os.path.basename(__file__).replace(".py","")

graph_attr = {
    "fontsize": "12",
    "bgcolor": "white"
}

with Diagram(filename, show= False, direction="TB", outformat="png", filename = f"output/{filename}", graph_attr=graph_attr):
    athena = Athena("Athena")
    event = CloudwatchEventTimeBased("Scheduled Trigger")

    with Cluster("State Machine") :
        job_1 = Glue("Transform, Join & Filter")
        job_2 = Glue("Aggregate")

        state_machine = [job_1]
        job_1>> job_2
        # state_machine >>

    bucket = S3("Output Tables")
    cloud_watch = Cloudwatch("Logs & Dashboard")

    event >> state_machine
    athena >> Edge(style="dotted", label='Read Data') >> job_1
    job_1 >> Edge(label='Write Table') >> bucket
    job_2 >> Edge(label='Write Table') >> bucket
    job_1 >> Edge(label='Write Logs') >> cloud_watch
    job_2 >> Edge(label='Write Logs') >> cloud_watch
