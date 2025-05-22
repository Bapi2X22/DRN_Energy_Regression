from CRABClient.UserUtilities import config

config = config()

config.section_("General")
config.General.requestName = ''
config.General.workArea = 'crab_projects_new'
config.General.transferOutputs = True
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'DRN_reg_final_cfg.py'
config.JobType.inputFiles = ['models']
#config.JobType.outputFiles = []
config.JobType.allowUndistributedCMSSW = True
#config.JobType.sendPythonFolder = True

config.section_("Data")
#config.Data.outputPrimaryDataset = 'DRN_output'
config.Data.inputDataset ='/DoublePhoton_Pt-5To300-gun/RunIISummer20UL18RECO-FlatPU0to70EdalIdealGT_EdalIdealGT_106X_upgrade2018_realistic_v11_L1v1_EcalIdealIC-v2/AODSIM'
#config.Data.splitting = 'Automatic'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 500  # Adjust depending on dataset size
config.Data.publication = False
config.Data.totalUnits =-1
#config.Data.inputDBS = 'phys03'

config.section_("Site")
config.Site.storageSite = 'T3_CH_CERNBOX'  # Update with appropriate Tier-2 site
#config.Data.outLFNDirBase = '/eos/user/b/bbapi/Energy_regression/CMSSW_13_3_3/src/CRAB_storage/'  # Update with your CMS username
config.Data.outLFNDirBase = '/store/user/bbapi/'

#config.JobType.maxJobRuntimeMin = 200
#config.Site.blacklist     = ['T2_US_Wisconsin','T2_US_Vanderbilt']

