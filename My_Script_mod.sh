#!/bin/bash

#cd /eos/user/b/bbapi/Energy_regression/CMSSW_13_3_3/src/test


# List of input files
#input_files=('root://cms-xrd-global.cern.ch//store/user/bmarzocc/ECAL_GNN_Regression/FourElectronsGunPt1-500_13TeV-pythia8_RunIISummer20UL18_pfThresTL235_pedTL235_AODSIM/AODSIM/240522_123019#/0000/step4_513.root' 'root://cms-xrd-global.cern.ch//store/user/bmarzocc/ECAL_GNN_Regression/FourElectronsGunPt1-500_13TeV-pythia8_RunIISummer20UL18_pfThresTL235_pedTL235_AODSIM/AODSIM/2405#22_123019/0000/step4_444.root') 

source /cvmfs/cms.cern.ch/cmsset_default.sh
#source /cvmfs/unpacked.cern.ch/registry.hub.docker.com/fastml

cp -r /afs/cern.ch/user/b/bbapi/models /tmp

singularity exec --nv /cvmfs/unpacked.cern.ch/registry.hub.docker.com/fastml/triton-torchgeo:22.07-py3-geometric \
tritonserver --model-repository /tmp/models --http-port 9000 --grpc-port 9001 --metrics-port 9002 --allow-http=1 > triton.log 2>&1 &

input_list="input_files.txt"

# Iterate through each input file and set output file name
counter=1
max_count=2
cmsenv

while IFS= read -r input_file; do
    cd /eos/user/b/bbapi/Energy_regression/CMSSW_13_3_3/src/test
    [[ -z "$input_file" || "$input_file" == \#* ]] && continue
    output_file="NTuple_$(printf "%03d" $counter).root"
    echo "Processing input: $input_file"
   # echo "Output will be: $output_file"
    
    # Call cmsRun with the dynamic inputFile and outputFile arguments
    cmsRun Zee_dumper_MINIAOD_MC_cfg_copy.py inputFile="$input_file"
    cd /eos/user/b/bbapi/Energy_regression/CMSSW_13_3_3/src/EM_Skimmer/ZeeAnalyzer/test
    cmsenv
    cmsRun Electron_RecHit_AODSIM_cfg_mod.py 
    mv ElectronRecHits_Ntuple.root $output_file
    mv $output_file /eos/user/b/bbapi/Energy_regression/CMSSW_13_3_3/src/EM_Skimmer/ZeeAnalyzer/test/Data/
   
    if (( counter == max_count )); then
        break
    fi

    ((counter++))
done < "$input_list"


