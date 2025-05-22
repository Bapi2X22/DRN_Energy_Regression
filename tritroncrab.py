
from CRABClient.UserUtilities import config
import os
import subprocess

config = config()

# General CRAB Settings
config.General.requestName = 'triton_server_job'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

# Job Configuration
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'dummy.py'  # No CMS processing required
config.JobType.allowUndistributedCMSSW = True
config.JobType.outputFiles = ['triton_server.log']

# Input Files (Optional, if your model is external)
config.JobType.inputFiles = ['/eos/home-b/bbapi/Energy_regression/CMSSW_13_3_3/src/test/RecoEgamma-EgammaPhotonProducers/models/photonObjectCombined','image_folder.tar.gz']

# Data Management
config.Data.outputPrimaryDataset = 'TritonServerTest'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 1
config.Data.totalUnits = 1
config.Data.outLFNDirBase = '/store/user/bbapi/'
config.Data.publication = False


# Site Information
config.Site.storageSite = 'T3_CH_CERNBOX'

# Triton Execution Script
config.JobType.scriptExe = 'run_triton.sh'

if __name__ == '__main__':
    from CRABAPI.RawCommand import crabCommand
    crabCommand('submit', config=config)

