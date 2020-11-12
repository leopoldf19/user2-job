#!/bin/bash
docker build -t l7f19/testscript .
#docker run --rm l7f19/testscript
docker push l7f19/testscript
ibmcloud ce project select -n leopold1
ibmcloud ce job delete -n testjob -f
ibmcloud ce job create -n testjob --image l7f19/testscript -r 0
ibmcloud ce jobrun delete -n testjob -f
ibmcloud ce jobrun submit -n testjob -j testjob --wait-timeout 60
ibmcloud ce jobrun logs -i testjob-0-0