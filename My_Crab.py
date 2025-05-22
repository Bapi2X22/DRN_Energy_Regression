from CRABClient.UserUtilities import config
import os
import subprocess
import time
import shutil

config = config()

# General request configuration
config.General.requestName = 'run_script_in_crab'
config.General.workArea = 'crab_projects_run_script'
config.General.transferOutputs = True
config.General.transferLogs = True

# JobType configuration to execute the code directly
config.JobType.pluginName = 'analysis'
config.JobType.psetName = 'my_config.py'  # This is a placeholder (not used in this case)
config.JobType.inputFiles = ['input_files.txt','RecoEgamma-EgammaPhotonProducers/models']

# Output files produced by the script (change accordingly)
config.JobType.outputFiles = []

# Data configuration for the CRAB job
config.Data.outputPrimaryDataset = 'sh_script_output'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1  # Each job processes 1 input file
#config.Data.totalUnits = 1  # Total units to process (adjust as needed)
#config.Data.outLFNDirBase = '/eos/user/b/bbapi/Energy_regression/CMSSW_13_3_3/src/'  # Change this to your desired location
config.Data.publication = False
config.Data.outputDatasetTag = 'sh_script_run'

# Site configuration for where the job will run
config.Site.storageSite = 'T2_CH_CERN'
