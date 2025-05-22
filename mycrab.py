from CRABClient.UserUtilities import config
from CRABAPI.RawCommand import crabCommand
from CRABClient.UserUtilities import config
config = config()
import os
import subprocess
import time

config.General.requestName = ''
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'Analysis'
config.JobType.outputFiles = ['myfile.root', "my_log.log"]
config.JobType.psetName = 'Zee_dumper_MINIAOD_MC_cfg_copy.py'

config.JobType.allowUndistributedCMSSW = True

config.JobType.inputFiles = ['/eos/home-b/bbapi/Energy_regression/CMSSW_13_3_3/src/test/RecoEgamma-EgammaPhotonProducers/models/photonObjectCombined']
config.Data.inputDataset = '/FourElectronsGunPt1-500_13TeV-pythia8_RunIISummer20UL18_pfThresTL235_pedTL235_AODSIM/bmarzocc-AODSIM-e4ec85f40300f50bb7065e30c2f64326/USER'
config.Data.inputDBS = 'phys03'
#config.Data.splitting = 'Automatic'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/user/bbapi/'
config.Data.publication = False
config.Data.outputDatasetTag = ''

config.Site.storageSite = 'T3_CH_CERNBOX'

if __name__ == '__main__':
    from CRABAPI.RawCommand import crabCommand
#    process.load("HeterogeneousCore.SonicTriton.TritonService_cff")


    log_file = open("my_log.log", "w")

    current_directory = os.getcwd()

    print("Current Directory:", current_directory, file=log_file)

    log_file.close()
    crabCommand('submit', config=config)
'''

    # Copy models directory
   # subprocess.run(['cp', '-r', '/models/photonObjectCombined', '/tmp'])
    subprocess.run(['cp', '-r', '/eos/home-b/bbapi/Energy_regression/CMSSW_13_3_3/src/test/RecoEgamma-EgammaPhotonProducers/models/photonObjectCombined', '/tmp'])

    #os.chdir('/tmp/models/')
    #subprocess.run('ls -ltrh')
    os.chdir('/eos/user/b/bbapi/Energy_regression/CMSSW_13_3_3/src/')

    if os.path.exists('/tmp/models'):
        print("Model directory found", file=log_file)
    else:
        print("ERROR: Model directory missing", file=log_file)


    # Custom function to simulate Triton server and run jobs
    # 1. Start the Triton server (if required)
    triton_command = [
        "singularity", "exec", "/cvmfs/unpacked.cern.ch/registry.hub.docker.com/fastml/triton-torchgeo:22.07-py3-geometric",
        "tritonserver", "--model-repository", "/tmp/models/photonObjectCombined", "--http-port", "8000", "--grpc-port", "8001", "--metrics-port", "8002", "--allow-http=1"
    ]      



    triton_process = subprocess.run(triton_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    time.sleep(10)

    check_triton = subprocess.run(["ps", "aux"], capture_output=True, text=True)
    if "tritonserver" in check_triton.stdout:
        print("E Triton server is running!", file=log_file)
    else:
        print(" Triton server failed to start.", file=log_file)

    log_file.close(
            )
            '''
#    crabCommand('submit', config=config)
#    from CRABAPI.RawCommand import crabCommand
#    for dataset in [
#'/WHToAA_AToBB_AToGG_M-20_TuneCP5_13TeV_madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM',
#'/WHToAA_AToBB_AToGG_M-25_TuneCP5_13TeV_madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM',
#'/WHToAA_AToBB_AToGG_M-30_TuneCP5_13TeV_madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM',
#'/WHToAA_AToBB_AToGG_M-35_TuneCP5_13TeV_madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM',
#'/WHToAA_AToBB_AToGG_M-40_TuneCP5_13TeV_madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM',
#'/WHToAA_AToBB_AToGG_M-45_TuneCP5_13TeV_madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM',
#'/WHToAA_AToBB_AToGG_M-50_TuneCP5_13TeV_madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM',
#'/WHToAA_AToBB_AToGG_M-55_TuneCP5_13TeV_madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM',
#'/WHToAA_AToBB_AToGG_M-60_TuneCP5_13TeV_madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM',
#'/ZHToAA_AToBB_AToGG_M-20_TuneCP5_13TeV_madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM',
#'/ZHToAA_AToBB_AToGG_M-25_TuneCP5_13TeV_madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM',
#'/ZHToAA_AToBB_AToGG_M-30_TuneCP5_13TeV_madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM',
#'/ZHToAA_AToBB_AToGG_M-35_TuneCP5_13TeV_madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM',
#'/ZHToAA_AToBB_AToGG_M-40_TuneCP5_13TeV_madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM',
#'/ZHToAA_AToBB_AToGG_M-45_TuneCP5_13TeV_madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM',
#'/ZHToAA_AToBB_AToGG_M-50_TuneCP5_13TeV_madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM',
#'/ZHToAA_AToBB_AToGG_M-55_TuneCP5_13TeV_madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM',
#'/ZHToAA_AToBB_AToGG_M-60_TuneCP5_13TeV_madgraph_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM'
#                   ]:
#        config.Data.inputDataset = dataset
#        config.General.requestName = dataset.split('/')[1]
#        crabCommand('submit', config = config)

