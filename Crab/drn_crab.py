from CRABClient.UserUtilities import config

config = config()

config.section_("General")
config.General.requestName = ''
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'DRN_reg_final_cfg.py'
config.JobType.scriptExe = 'bash_wrapper_drn.sh'  # actual script to run

config.JobType.inputFiles = ['models','DRN_reg_final_cfg.py']
config.JobType.outputFiles = ['output_crab.root','triton.log']
config.JobType.allowUndistributedCMSSW = True

#config.JobType.sendPythonFolder = True

config.section_("Data")
#config.Data.outputPrimaryDataset = 'DRN_output'
config.Data.inputDataset ='/FourElectronsGunPt1-500_13TeV-pythia8_RunIISummer20UL18_pfThresTL235_pedUL18_AODSIM/bmarzocc-AODSIM-cc069a36518b089f990f643770dd5f39/USER'
#config.Data.splitting = 'Automatic'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 500  # Adjust depending on dataset size
config.Data.publication = False
#config.Data.totalUnits =-1
config.Data.totalUnits = 100
config.Data.unitsPerJob = 5
config.Data.inputDBS = 'phys03'

config.section_("Site")
config.Site.storageSite = 'T3_CH_CERNBOX'  # Update with appropriate Tier-2 site
config.Data.outLFNDirBase = '/store/user/bbapi/'  # Update with your CMS username

#config.JobType.maxJobRuntimeMin = 200
#config.Site.blacklist     = ['T2_US_Wisconsin','T2_US_Vanderbilt']

