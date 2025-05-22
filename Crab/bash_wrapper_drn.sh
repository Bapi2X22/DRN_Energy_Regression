#!/usr/bin/bash

singularity exec  /cvmfs/unpacked.cern.ch/registry.hub.docker.com/fastml/triton-torchgeo:22.07-py3-geometric tritonserver --model-repository models/ --http-port 7000 --grpc-port 7001 --metrics-port 7002 --allow-http=1 &>> triton.log &

cmsenv;
cmsRun DRN_reg_final_cfg.py 

cat <<EOF > FrameworkJobReport.xml
<FrameworkJobReport>
  <FrameworkJobReportVersion>1.1</FrameworkJobReportVersion>
  <GeneratorInfo>
    <CMSSWVersion>CMSSW_13_3_3</CMSSWVersion>
    <Generator>CustomScript</Generator>
  </GeneratorInfo>
  <JobPerformance>
    <EventThroughput>1</EventThroughput>
  </JobPerformance>
  <InputFile>
    <LFN></LFN>
  </InputFile>
  <File>
    <OutputModule>output</OutputModule>
    <OutputFile>output.root</OutputFile>
    <InputPFN></InputPFN>
    <InputSource>None</InputSource>
  </File>
  <FrameworkError ExitStatus="0">
    <Type>Success</Type>
    <Message>Job completed successfully</Message>
  </FrameworkError>
</FrameworkJobReport>
EOF
