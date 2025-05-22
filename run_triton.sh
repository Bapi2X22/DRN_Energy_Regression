#!/bin/bash

# Set up the environment (if required)
source /cvmfs/cms.cern.ch/cmsset_default.sh

echo "Check 1"
pwd

# Copy model to /tmp (if using external models)
cp -r /eos/home-b/bbapi/Energy_regression/CMSSW_13_3_3/src/test/RecoEgamma-EgammaPhotonProducers/models/photonObjectCombined /tmp

echo "Check 2"

ls -l /tmp/photonObjectCombined


# Start the Triton server
singularity exec /cvmfs/unpacked.cern.ch/registry.hub.docker.com/fastml/triton-torchgeo:22.07-py3-geometric \
	tritonserver --model-repository=/tmp/photonObjectCombined \
	--http-port 9000 --grpc-port 9001 --metrics-port 9002 --allow-http=1 &

# Wait and log output
sleep 30
ps aux | grep tritonserver > triton_server.log

# Ensure job exits cleanly
if pgrep -x tritonserver > /dev/null; then
	echo "Triton server is running."
	exit 0
else
	echo "ERROR: Triton server failed to start." >&2
	exit 1
fi
