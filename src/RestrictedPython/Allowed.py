import diagrams.aws.analytics as analytics
import diagrams.aws.ar as ar
import diagrams.aws.blockchain as blockchain
import diagrams.aws.business as business
import diagrams.aws.compute as compute
import diagrams.aws.cost as cost
import diagrams.aws.database as database
import diagrams.aws.devtools as devtools
import diagrams.aws.enablement as enablement
import diagrams.aws.enduser as enduser
import diagrams.aws.engagement as engagement
import diagrams.aws.game as game
import diagrams.aws.general as general
import diagrams.aws.integration as integration
import diagrams.aws.iot as iot
import diagrams.aws.management as management
import diagrams.aws.media as media
import diagrams.aws.migration as migration
import diagrams.aws.ml as ml
import diagrams.aws.mobile as mobile
import diagrams.aws.network as network
import diagrams.aws.quantum as quantum
import diagrams.aws.robotics as robotics
import diagrams.aws.satellite as satellite
import diagrams.aws.security as security
import diagrams.aws.storage as storage

from diagrams import Diagram as Diagram
from diagrams import Cluster as Cluster

from inspect import getmembers, isclass, ismodule


diagram_builtins = {}

def load_classes(module):
    try:
        for name, obj in getmembers(module):
            if isclass(obj):
                name = obj.__name__
                diagram_builtins[name] = obj
    except ImportError as e:
        print(e)

load_classes(analytics)
load_classes(ar)
load_classes(blockchain)
load_classes(business)
load_classes(compute)
load_classes(cost)
load_classes(database)
load_classes(devtools)
load_classes(enablement)
load_classes(enduser)
load_classes(engagement)
load_classes(game)
load_classes(general)
load_classes(integration)
load_classes(iot)
load_classes(management)
load_classes(media)
load_classes(migration)
load_classes(ml)
load_classes(mobile)
load_classes(network)
load_classes(quantum)
load_classes(robotics)
load_classes(satellite)
load_classes(security)
load_classes(storage)

diagram_builtins['Diagram'] = Diagram
diagram_builtins['Cluster'] = Cluster



