# http://diagrams.mingrams.mingrammer.com/docs/getting-started/examples

from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.analytics import Spark
from diagrams.onprem.compute import Server
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.logging import FluentBit 
from diagrams.onprem.monitoring import Grafana, Prometheus 
from diagrams.onprem.queue import Kafka  
from diagrams.onprem.network import Nginx

from diagrams.aws.compute import EC2
from diagrams.aws.compute import ECS
from diagrams.aws.database import ElastiCache, RDS
from diagrams.aws.network import ELB
from diagrams.aws.network import Route53

# ELB - Elastic Load Balancer

############################
# download & install Graphviz from: https://graphviz.org/download/ 
# install module diagrams in cmd: pip install diagrams
# reset the VSCode !!!!
############################


# here we build diagram

# diagram name is: Grouped workers 
# when we run script the diagram will be shown right away 
# direction from top to buttom

def exp_1():
    with Diagram("Grouped workers", show=True, direction="TB"): 
        lb = ELB("Load Balancer")
        workers = [EC2("Worker 1"), EC2("Worker 2"), EC2("Worker 3"), EC2("Worker 4"), EC2("Worker 5")]
        my_db = RDS("Database")

        # lb >> workers >> my_db

        lb >> workers  # Connect Load Balancer to EC2 workers
        for worker in workers:
            worker >> my_db  # Connect each worker to the Database


def exp_2_with_clusters():
    with Diagram("Cluster Web Services", show=True):
        dns = Route53("dns")
        lb = ELB("lb")
        memcached = ElastiCache("memcached")

        with Cluster("Services"):
            svc_group = [ECS("web1"),
                         ECS("web2"),
                         ECS("web3")]   
            
        with Cluster("DB Cluster"):            
            db_master = [RDS("userdb1"), 
                         RDS("userdb2")]        
        
        
        dns >> lb >> svc_group >> memcached 
        memcached >> db_master
        
def exp_3_more_elements():
    with Diagram(name="Advanced Web Service with On-Premice (colored)", show=True):
        ingress = Nginx("ingress")
        matrics = Prometheus("metric")
        grafana = Grafana("monitoring")
        

        # Edge is a arrow (dashed and at the arrow side )
        matrics << Edge(color="firebrick", style="dashed") << grafana

        with Cluster("Service Cluster"): 
            grpcsvc = [Server("grpc1"), 
                       Server("grpc2"), 
                       Server("grpc3")]
        
        with Cluster("Session HA"): 
            session = Redis("session") 
            replica = Redis("replica")
            session_set = session - Edge(color="brown", style="dashed") - replica

            # here we will connect all other elements to this cluster !! 
            session_set << Edge(label="collect") << matrics
            grpcsvc >> Edge(color="brown") >> session 
        
        with Cluster("Database HA"): 
            users = PostgreSQL("users")
            slave = PostgreSQL("slave") 
            users - Edge(color="brown", style="dotted") - slave << Edge(label="collect") << matrics
            grpcsvc >> Edge(color="black") >> users           
        
        aggregator = FluentBit("logging")
        aggregator >> Edge(lable ="parse") >> Kafka("stream") >> Edge(color="black", style = "bold") >> Spark("analitics")

        ingress >> Edge(color="darkgreen") << grpcsvc >> Edge(color="darkorange") >> aggregator




# exp_1()
# exp_2_with_clusters()
exp_3_more_elements()
