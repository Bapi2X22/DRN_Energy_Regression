import FWCore.ParameterSet.Config as cms

process = cms.Process("DRNregression")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('root://cms-xrd-global.cern.ch//~/'),
    secondaryFileNames = cms.untracked.vstring(),
    skipEvents = cms.untracked.uint32(0)
)
process.CondDB = cms.PSet(
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        connectionTimeout = cms.untracked.int32(0),
        messageLevel = cms.untracked.int32(0),
        security = cms.untracked.string('')
    ),
    connect = cms.string('')
)

process.HFRecalParameterBlock = cms.PSet(
    HFdepthOneParameterA = cms.vdouble(
        0.004123, 0.00602, 0.008201, 0.010489, 0.013379,
        0.016997, 0.021464, 0.027371, 0.034195, 0.044807,
        0.058939, 0.125497
    ),
    HFdepthOneParameterB = cms.vdouble(
        -4e-06, -2e-06, 0.0, 4e-06, 1.5e-05,
        2.6e-05, 6.3e-05, 8.4e-05, 0.00016, 0.000107,
        0.000425, 0.000209
    ),
    HFdepthTwoParameterA = cms.vdouble(
        0.002861, 0.004168, 0.0064, 0.008388, 0.011601,
        0.014425, 0.018633, 0.023232, 0.028274, 0.035447,
        0.051579, 0.086593
    ),
    HFdepthTwoParameterB = cms.vdouble(
        -2e-06, -0.0, -7e-06, -6e-06, -2e-06,
        1e-06, 1.9e-05, 3.1e-05, 6.7e-05, 1.2e-05,
        0.000157, -3e-06
    )
)

process.ecalTrkCombinationRegression = cms.PSet(
    ecalTrkRegressionConfig = cms.PSet(
        ebHighEtForestName = cms.ESInputTag("","electron_eb_ECALTRK"),
        ebLowEtForestName = cms.ESInputTag("","electron_eb_ECALTRK_lowpt"),
        eeHighEtForestName = cms.ESInputTag("","electron_ee_ECALTRK"),
        eeLowEtForestName = cms.ESInputTag("","electron_ee_ECALTRK_lowpt"),
        forceHighEnergyTrainingIfSaturated = cms.bool(False),
        lowEtHighEtBoundary = cms.double(50.0),
        rangeMaxHighEt = cms.double(3.0),
        rangeMaxLowEt = cms.double(3.0),
        rangeMinHighEt = cms.double(-1.0),
        rangeMinLowEt = cms.double(-1.0)
    ),
    ecalTrkRegressionUncertConfig = cms.PSet(
        ebHighEtForestName = cms.ESInputTag("","electron_eb_ECALTRK_var"),
        ebLowEtForestName = cms.ESInputTag("","electron_eb_ECALTRK_lowpt_var"),
        eeHighEtForestName = cms.ESInputTag("","electron_ee_ECALTRK_var"),
        eeLowEtForestName = cms.ESInputTag("","electron_ee_ECALTRK_lowpt_var"),
        forceHighEnergyTrainingIfSaturated = cms.bool(False),
        lowEtHighEtBoundary = cms.double(50.0),
        rangeMaxHighEt = cms.double(0.5),
        rangeMaxLowEt = cms.double(0.5),
        rangeMinHighEt = cms.double(0.0002),
        rangeMinLowEt = cms.double(0.0002)
    ),
    maxEPDiffInSigmaForComb = cms.double(15.0),
    maxEcalEnergyForComb = cms.double(200.0),
    maxRelTrkMomErrForComb = cms.double(10.0),
    minEOverPForComb = cms.double(0.025)
)

process.egamma8XLegacyEtScaleSysModifier = cms.PSet(
    epCombConfig = cms.PSet(
        ecalTrkRegressionConfig = cms.PSet(
            ebHighEtForestName = cms.ESInputTag("","electron_eb_ECALTRK"),
            ebLowEtForestName = cms.ESInputTag("","electron_eb_ECALTRK_lowpt"),
            eeHighEtForestName = cms.ESInputTag("","electron_ee_ECALTRK"),
            eeLowEtForestName = cms.ESInputTag("","electron_ee_ECALTRK_lowpt"),
            forceHighEnergyTrainingIfSaturated = cms.bool(False),
            lowEtHighEtBoundary = cms.double(50.0),
            rangeMaxHighEt = cms.double(3.0),
            rangeMaxLowEt = cms.double(3.0),
            rangeMinHighEt = cms.double(-1.0),
            rangeMinLowEt = cms.double(-1.0)
        ),
        ecalTrkRegressionUncertConfig = cms.PSet(
            ebHighEtForestName = cms.ESInputTag("","electron_eb_ECALTRK_var"),
            ebLowEtForestName = cms.ESInputTag("","electron_eb_ECALTRK_lowpt_var"),
            eeHighEtForestName = cms.ESInputTag("","electron_ee_ECALTRK_var"),
            eeLowEtForestName = cms.ESInputTag("","electron_ee_ECALTRK_lowpt_var"),
            forceHighEnergyTrainingIfSaturated = cms.bool(False),
            lowEtHighEtBoundary = cms.double(50.0),
            rangeMaxHighEt = cms.double(0.5),
            rangeMaxLowEt = cms.double(0.5),
            rangeMinHighEt = cms.double(0.0002),
            rangeMinLowEt = cms.double(0.0002)
        ),
        maxEPDiffInSigmaForComb = cms.double(15.0),
        maxEcalEnergyForComb = cms.double(200.0),
        maxRelTrkMomErrForComb = cms.double(10.0),
        minEOverPForComb = cms.double(0.025)
    ),
    modifierName = cms.string('EGEtScaleSysModifier'),
    uncertFunc = cms.PSet(
        highEt = cms.double(46.5),
        highEtUncert = cms.double(-0.002),
        lowEt = cms.double(43.5),
        lowEtUncert = cms.double(0.002),
        name = cms.string('UncertFuncV1')
    )
)

process.egamma8XObjectUpdateModifier = cms.PSet(
    ecalRecHitsEB = cms.InputTag("reducedEgamma","reducedEBRecHits"),
    ecalRecHitsEE = cms.InputTag("reducedEgamma","reducedEERecHits"),
    modifierName = cms.string('EG8XObjectUpdateModifier')
)

process.egamma9X105XUpdateModifier = cms.PSet(
    allowGsfTrackForConvs = cms.bool(False),
    beamspot = cms.InputTag("offlineBeamSpot"),
    conversions = cms.InputTag("reducedEgamma","reducedConversions"),
    ecalRecHitsEB = cms.InputTag("reducedEgamma","reducedEBRecHits"),
    ecalRecHitsEE = cms.InputTag("reducedEgamma","reducedEERecHits"),
    eleCollVMsAreKeyedTo = cms.InputTag("slimmedElectrons","","@skipCurrentProcess"),
    eleTrkIso = cms.InputTag("heepIDVarValueMaps","eleTrkPtIso"),
    eleTrkIso04 = cms.InputTag("heepIDVarValueMaps","eleTrkPtIso04"),
    modifierName = cms.string('EG9X105XObjectUpdateModifier'),
    phoChargedHadIso = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
    phoChargedHadPFPVIso = cms.InputTag("egmPhotonIsolation","h+-DR030-"),
    phoChargedHadWorstVtxConeVetoIso = cms.InputTag("photonIDValueMapProducer","phoWorstChargedIsolationConeVeto"),
    phoChargedHadWorstVtxIso = cms.InputTag("photonIDValueMapProducer","phoWorstChargedIsolation"),
    phoCollVMsAreKeyedTo = cms.InputTag("slimmedPhotons","","@skipCurrentProcess"),
    phoNeutralHadIso = cms.InputTag("photonIDValueMapProducer","phoNeutralHadronIsolation"),
    phoPhotonIso = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
    updateChargedHadPFPVIso = cms.bool(True)
)

process.egammaHIPhotonIsolationModifier = cms.PSet(
    electron_config = cms.PSet(

    ),
    modifierName = cms.string('EGExtraInfoModifierFromHIPhotonIsolationValueMaps'),
    photon_config = cms.PSet(
        photonIsolationHI = cms.InputTag("reducedEgamma","photonIsolationHIProducerppGED")
    )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

process.maxLuminosityBlocks = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.mvaEleID_Fall17_iso_V1_producer_config = cms.PSet(
    categoryCuts = cms.vstring(
        'pt < 10. && abs(superCluster.eta) < 0.800',
        'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479',
        'pt < 10. && abs(superCluster.eta) >= 1.479',
        'pt >= 10. && abs(superCluster.eta) < 0.800',
        'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479',
        'pt >= 10. && abs(superCluster.eta) >= 1.479'
    ),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('Fall17IsoV1'),
    nCategories = cms.int32(6),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Fall17V1Variables.txt'),
    weightFileNames = cms.vstring(
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_5_2017_puinfo_iso_BDT.weights.root',
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_5_2017_puinfo_iso_BDT.weights.root',
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_5_2017_puinfo_iso_BDT.weights.root',
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_10_2017_puinfo_iso_BDT.weights.root',
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_10_2017_puinfo_iso_BDT.weights.root',
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_10_2017_puinfo_iso_BDT.weights.root'
    )
)

process.mvaEleID_Fall17_iso_V2_producer_config = cms.PSet(
    categoryCuts = cms.vstring(
        'pt < 10. && abs(superCluster.eta) < 0.800',
        'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479',
        'pt < 10. && abs(superCluster.eta) >= 1.479',
        'pt >= 10. && abs(superCluster.eta) < 0.800',
        'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479',
        'pt >= 10. && abs(superCluster.eta) >= 1.479'
    ),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('Fall17IsoV2'),
    nCategories = cms.int32(6),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
    weightFileNames = cms.vstring(
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB1_5.weights.root',
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB2_5.weights.root',
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EE_5.weights.root',
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB1_10.weights.root',
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB2_10.weights.root',
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EE_10.weights.root'
    )
)

process.mvaEleID_Fall17_noIso_V1_producer_config = cms.PSet(
    categoryCuts = cms.vstring(
        'pt < 10. && abs(superCluster.eta) < 0.800',
        'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479',
        'pt < 10. && abs(superCluster.eta) >= 1.479',
        'pt >= 10. && abs(superCluster.eta) < 0.800',
        'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479',
        'pt >= 10. && abs(superCluster.eta) >= 1.479'
    ),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('Fall17NoIsoV1'),
    nCategories = cms.int32(6),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Fall17V1Variables.txt'),
    weightFileNames = cms.vstring(
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_5_2017_puinfo_BDT.weights.root',
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_5_2017_puinfo_BDT.weights.root',
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_5_2017_puinfo_BDT.weights.root',
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_10_2017_puinfo_BDT.weights.root',
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_10_2017_puinfo_BDT.weights.root',
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_10_2017_puinfo_BDT.weights.root'
    )
)

process.mvaEleID_Fall17_noIso_V2_producer_config = cms.PSet(
    categoryCuts = cms.vstring(
        'pt < 10. && abs(superCluster.eta) < 0.800',
        'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479',
        'pt < 10. && abs(superCluster.eta) >= 1.479',
        'pt >= 10. && abs(superCluster.eta) < 0.800',
        'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479',
        'pt >= 10. && abs(superCluster.eta) >= 1.479'
    ),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('Fall17NoIsoV2'),
    nCategories = cms.int32(6),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
    weightFileNames = cms.vstring(
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB1_5.weights.root',
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB2_5.weights.root',
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EE_5.weights.root',
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB1_10.weights.root',
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB2_10.weights.root',
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EE_10.weights.root'
    )
)

process.mvaEleID_RunIIIWinter22_iso_V1_producer_config = cms.PSet(
    categoryCuts = cms.vstring(
        'pt < 10. && abs(superCluster.eta) < 0.800',
        'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479',
        'pt < 10. && abs(superCluster.eta) >= 1.479',
        'pt >= 10. && abs(superCluster.eta) < 0.800',
        'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479',
        'pt >= 10. && abs(superCluster.eta) >= 1.479'
    ),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('RunIIIWinter22IsoV1'),
    nCategories = cms.int32(6),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronIDVariablesRun3.txt'),
    weightFileNames = cms.vstring(
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Winter22IsoV1/EB1_5.weights.root',
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Winter22IsoV1/EB2_5.weights.root',
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Winter22IsoV1/EE_5.weights.root',
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Winter22IsoV1/EB1_10.weights.root',
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Winter22IsoV1/EB2_10.weights.root',
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Winter22IsoV1/EE_10.weights.root'
    )
)

process.mvaEleID_RunIIIWinter22_noIso_V1_producer_config = cms.PSet(
    categoryCuts = cms.vstring(
        'pt < 10. && abs(superCluster.eta) < 0.800',
        'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479',
        'pt < 10. && abs(superCluster.eta) >= 1.479',
        'pt >= 10. && abs(superCluster.eta) < 0.800',
        'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479',
        'pt >= 10. && abs(superCluster.eta) >= 1.479'
    ),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('RunIIIWinter22NoIsoV1'),
    nCategories = cms.int32(6),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronIDVariablesRun3NonIso.txt'),
    weightFileNames = cms.vstring(
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Winter22NoIsoV1/EB1_5.weights.root',
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Winter22NoIsoV1/EB2_5.weights.root',
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Winter22NoIsoV1/EE_5.weights.root',
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Winter22NoIsoV1/EB1_10.weights.root',
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Winter22NoIsoV1/EB2_10.weights.root',
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Winter22NoIsoV1/EE_10.weights.root'
    )
)

process.mvaEleID_Spring16_GeneralPurpose_V1_producer_config = cms.PSet(
    categoryCuts = cms.vstring(
        'abs(superCluster.eta) < 0.800',
        'abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479',
        'abs(superCluster.eta) >= 1.479'
    ),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('Spring16GeneralPurposeV1'),
    nCategories = cms.int32(3),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
    weightFileNames = cms.vstring(
        'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EB1_10.weights.root',
        'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EB2_10.weights.root',
        'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EE_10.weights.root'
    )
)

process.mvaEleID_Spring16_HZZ_V1_producer_config = cms.PSet(
    categoryCuts = cms.vstring(
        'pt < 10. && abs(superCluster.eta) < 0.800',
        'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479',
        'pt < 10. && abs(superCluster.eta) >= 1.479',
        'pt >= 10. && abs(superCluster.eta) < 0.800',
        'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479',
        'pt >= 10. && abs(superCluster.eta) >= 1.479'
    ),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('Spring16HZZV1'),
    nCategories = cms.int32(6),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
    weightFileNames = cms.vstring(
        'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB1_5.weights.root',
        'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB2_5.weights.root',
        'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EE_5.weights.root',
        'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB1_10.weights.root',
        'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB2_10.weights.root',
        'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EE_10.weights.root'
    )
)

process.mvaEleID_Summer16UL_ID_ISO_producer_config = cms.PSet(
    categoryCuts = cms.vstring(
        'pt < 10. & abs(superCluster.eta) < 0.800',
        'pt < 10. & abs(superCluster.eta) >= 0.800 & abs(superCluster.eta) < 1.479',
        'pt < 10. & abs(superCluster.eta) >= 1.479',
        'pt >= 10. & abs(superCluster.eta) < 0.800',
        'pt >= 10. & abs(superCluster.eta) >= 0.800 & abs(superCluster.eta) < 1.479',
        'pt >= 10. & abs(superCluster.eta) >= 1.479'
    ),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('Summer16ULIdIso'),
    nCategories = cms.int32(6),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
    weightFileNames = cms.vstring(
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_16UL_ID_ISO/EB1_5.weights.root',
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_16UL_ID_ISO/EB2_5.weights.root',
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_16UL_ID_ISO/EE_5.weights.root',
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_16UL_ID_ISO/EB1_10.weights.root',
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_16UL_ID_ISO/EB2_10.weights.root',
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_16UL_ID_ISO/EE_10.weights.root'
    )
)

process.mvaEleID_Summer17UL_ID_ISO_producer_config = cms.PSet(
    categoryCuts = cms.vstring(
        'pt < 10. & abs(superCluster.eta) < 0.800',
        'pt < 10. & abs(superCluster.eta) >= 0.800 & abs(superCluster.eta) < 1.479',
        'pt < 10. & abs(superCluster.eta) >= 1.479',
        'pt >= 10. & abs(superCluster.eta) < 0.800',
        'pt >= 10. & abs(superCluster.eta) >= 0.800 & abs(superCluster.eta) < 1.479',
        'pt >= 10. & abs(superCluster.eta) >= 1.479'
    ),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('Summer17ULIdIso'),
    nCategories = cms.int32(6),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
    weightFileNames = cms.vstring(
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_17UL_ID_ISO/EB1_5.weights.root',
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_17UL_ID_ISO/EB2_5.weights.root',
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_17UL_ID_ISO/EE_5.weights.root',
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_17UL_ID_ISO/EB1_10.weights.root',
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_17UL_ID_ISO/EB2_10.weights.root',
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_17UL_ID_ISO/EE_10.weights.root'
    )
)

process.mvaEleID_Summer18UL_ID_ISO_producer_config = cms.PSet(
    categoryCuts = cms.vstring(
        'pt < 10. & abs(superCluster.eta) < 0.800',
        'pt < 10. & abs(superCluster.eta) >= 0.800 & abs(superCluster.eta) < 1.479',
        'pt < 10. & abs(superCluster.eta) >= 1.479',
        'pt >= 10. & abs(superCluster.eta) < 0.800',
        'pt >= 10. & abs(superCluster.eta) >= 0.800 & abs(superCluster.eta) < 1.479',
        'pt >= 10. & abs(superCluster.eta) >= 1.479'
    ),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('Summer18ULIdIso'),
    nCategories = cms.int32(6),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
    weightFileNames = cms.vstring(
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_18UL_ID_ISO/EB1_5.weights.root',
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_18UL_ID_ISO/EB2_5.weights.root',
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_18UL_ID_ISO/EE_5.weights.root',
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_18UL_ID_ISO/EB1_10.weights.root',
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_18UL_ID_ISO/EB2_10.weights.root',
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_18UL_ID_ISO/EE_10.weights.root'
    )
)

process.options = cms.untracked.PSet(
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    TryToContinue = cms.untracked.vstring(),
    accelerators = cms.untracked.vstring('*'),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    deleteNonConsumedUnscheduledModules = cms.untracked.bool(True),
    dumpOptions = cms.untracked.bool(False),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(0)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    holdsReferencesToDeleteEarly = cms.untracked.VPSet(),
    makeTriggerResults = cms.obsolete.untracked.bool,
    modulesToCallForTryToContinue = cms.untracked.vstring(),
    modulesToIgnoreForDeleteEarly = cms.untracked.vstring(),
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(0),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

process.photonDRNModifier = cms.PSet(
    modifierName = cms.string('EGRegressionModifierDRN'),
    patPhotons = cms.PSet(
        correctionsSource = cms.InputTag("patPhotonsDRN"),
        energyFloat = cms.string('energyDRN'),
        resFloat = cms.string('resolutionDRN'),
        source = cms.InputTag("selectedPatPhotons")
    )
)

process.reducedEgammaEnergyScaleAndSmearingModifier = cms.PSet(
    electron_config = cms.PSet(
        ecalEnergyErrPostCorr = cms.InputTag("reducedEgamma","calibEleEcalEnergyErrPostCorr"),
        ecalEnergyErrPreCorr = cms.InputTag("reducedEgamma","calibEleEcalEnergyErrPreCorr"),
        ecalEnergyPostCorr = cms.InputTag("reducedEgamma","calibEleEcalEnergyPostCorr"),
        ecalEnergyPreCorr = cms.InputTag("reducedEgamma","calibEleEcalEnergyPreCorr"),
        ecalTrkEnergyErrPostCorr = cms.InputTag("reducedEgamma","calibEleEcalTrkEnergyErrPostCorr"),
        ecalTrkEnergyErrPreCorr = cms.InputTag("reducedEgamma","calibEleEcalTrkEnergyErrPreCorr"),
        ecalTrkEnergyPostCorr = cms.InputTag("reducedEgamma","calibEleEcalTrkEnergyPostCorr"),
        ecalTrkEnergyPreCorr = cms.InputTag("reducedEgamma","calibEleEcalTrkEnergyPreCorr"),
        energyScaleDown = cms.InputTag("reducedEgamma","calibEleEnergyScaleDown"),
        energyScaleGainDown = cms.InputTag("reducedEgamma","calibEleEnergyScaleGainDown"),
        energyScaleGainUp = cms.InputTag("reducedEgamma","calibEleEnergyScaleGainUp"),
        energyScaleStatDown = cms.InputTag("reducedEgamma","calibEleEnergyScaleStatDown"),
        energyScaleStatUp = cms.InputTag("reducedEgamma","calibEleEnergyScaleStatUp"),
        energyScaleSystDown = cms.InputTag("reducedEgamma","calibEleEnergyScaleSystDown"),
        energyScaleSystUp = cms.InputTag("reducedEgamma","calibEleEnergyScaleSystUp"),
        energyScaleUp = cms.InputTag("reducedEgamma","calibEleEnergyScaleUp"),
        energyScaleValue = cms.InputTag("reducedEgamma","calibEleEnergyScaleValue"),
        energySigmaDown = cms.InputTag("reducedEgamma","calibEleEnergySigmaDown"),
        energySigmaPhiDown = cms.InputTag("reducedEgamma","calibEleEnergySigmaPhiDown"),
        energySigmaPhiUp = cms.InputTag("reducedEgamma","calibEleEnergySigmaPhiUp"),
        energySigmaRhoDown = cms.InputTag("reducedEgamma","calibEleEnergySigmaRhoDown"),
        energySigmaRhoUp = cms.InputTag("reducedEgamma","calibEleEnergySigmaRhoUp"),
        energySigmaUp = cms.InputTag("reducedEgamma","calibEleEnergySigmaUp"),
        energySigmaValue = cms.InputTag("reducedEgamma","calibEleEnergySigmaValue"),
        energySmearNrSigma = cms.InputTag("reducedEgamma","calibEleEnergySmearNrSigma")
    ),
    modifierName = cms.string('EGExtraInfoModifierFromFloatValueMaps'),
    photon_config = cms.PSet(
        ecalEnergyErrPostCorr = cms.InputTag("reducedEgamma","calibPhoEcalEnergyErrPostCorr"),
        ecalEnergyErrPreCorr = cms.InputTag("reducedEgamma","calibPhoEcalEnergyErrPreCorr"),
        ecalEnergyPostCorr = cms.InputTag("reducedEgamma","calibPhoEcalEnergyPostCorr"),
        ecalEnergyPreCorr = cms.InputTag("reducedEgamma","calibPhoEcalEnergyPreCorr"),
        energyScaleDown = cms.InputTag("reducedEgamma","calibPhoEnergyScaleDown"),
        energyScaleGainDown = cms.InputTag("reducedEgamma","calibPhoEnergyScaleGainDown"),
        energyScaleGainUp = cms.InputTag("reducedEgamma","calibPhoEnergyScaleGainUp"),
        energyScaleStatDown = cms.InputTag("reducedEgamma","calibPhoEnergyScaleStatDown"),
        energyScaleStatUp = cms.InputTag("reducedEgamma","calibPhoEnergyScaleStatUp"),
        energyScaleSystDown = cms.InputTag("reducedEgamma","calibPhoEnergyScaleSystDown"),
        energyScaleSystUp = cms.InputTag("reducedEgamma","calibPhoEnergyScaleSystUp"),
        energyScaleUp = cms.InputTag("reducedEgamma","calibPhoEnergyScaleUp"),
        energyScaleValue = cms.InputTag("reducedEgamma","calibPhoEnergyScaleValue"),
        energySigmaDown = cms.InputTag("reducedEgamma","calibPhoEnergySigmaDown"),
        energySigmaPhiDown = cms.InputTag("reducedEgamma","calibPhoEnergySigmaPhiDown"),
        energySigmaPhiUp = cms.InputTag("reducedEgamma","calibPhoEnergySigmaPhiUp"),
        energySigmaRhoDown = cms.InputTag("reducedEgamma","calibPhoEnergySigmaRhoDown"),
        energySigmaRhoUp = cms.InputTag("reducedEgamma","calibPhoEnergySigmaRhoUp"),
        energySigmaUp = cms.InputTag("reducedEgamma","calibPhoEnergySigmaUp"),
        energySigmaValue = cms.InputTag("reducedEgamma","calibPhoEnergySigmaValue"),
        energySmearNrSigma = cms.InputTag("reducedEgamma","calibPhoEnergySmearNrSigma")
    )
)

process.egamma_modifications = cms.VPSet(
    cms.PSet(
        electron_config = cms.PSet(
            ElectronMVAEstimatorRun2Fall17IsoV1Values = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV1Values"),
            ElectronMVAEstimatorRun2Fall17IsoV2Values = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV2Values"),
            ElectronMVAEstimatorRun2Fall17NoIsoV1Values = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV1Values"),
            ElectronMVAEstimatorRun2Fall17NoIsoV2Values = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV2Values"),
            ElectronMVAEstimatorRun2RunIIIWinter22IsoV1Values = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2RunIIIWinter22IsoV1Values"),
            ElectronMVAEstimatorRun2RunIIIWinter22NoIsoV1Values = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2RunIIIWinter22NoIsoV1Values"),
            ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Values = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Values"),
            ElectronMVAEstimatorRun2Spring16HZZV1Values = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16HZZV1Values"),
            ElectronMVAEstimatorRun2Summer18ULIdIsoValues = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Summer18ULIdIsoValues")
        ),
        modifierName = cms.string('EGExtraInfoModifierFromFloatValueMaps'),
        photon_config = cms.PSet(
            PhotonMVAEstimatorRun2Spring16NonTrigV1Values = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring16NonTrigV1Values"),
            PhotonMVAEstimatorRunIIFall17v1p1Values = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1p1Values"),
            PhotonMVAEstimatorRunIIFall17v2Values = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v2Values"),
            PhotonMVAEstimatorRunIIIWinter22v1Values = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIIWinter22v1Values")
        )
    ),
    cms.PSet(
        electron_config = cms.PSet(
            ElectronMVAEstimatorRun2Fall17IsoV1Categories = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV1Categories"),
            ElectronMVAEstimatorRun2Fall17IsoV2Categories = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV2Categories"),
            ElectronMVAEstimatorRun2Fall17NoIsoV1Categories = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV1Categories"),
            ElectronMVAEstimatorRun2Fall17NoIsoV2Categories = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV2Categories"),
            ElectronMVAEstimatorRun2RunIIIWinter22IsoV1Categories = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2RunIIIWinter22IsoV1Categories"),
            ElectronMVAEstimatorRun2RunIIIWinter22NoIsoV1Categories = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2RunIIIWinter22NoIsoV1Categories"),
            ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Categories = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Categories"),
            ElectronMVAEstimatorRun2Spring16HZZV1Categories = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16HZZV1Categories"),
            ElectronMVAEstimatorRun2Summer18ULIdIsoCategories = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Summer18ULIdIsoCategories")
        ),
        modifierName = cms.string('EGExtraInfoModifierFromIntValueMaps'),
        photon_config = cms.PSet(
            PhotonMVAEstimatorRun2Spring16NonTrigV1Categories = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring16NonTrigV1Categories"),
            PhotonMVAEstimatorRunIIFall17v1p1Categories = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1p1Categories"),
            PhotonMVAEstimatorRunIIFall17v2Categories = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v2Categories"),
            PhotonMVAEstimatorRunIIIWinter22v1Categories = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIIWinter22v1Categories")
        )
    )
)

process.mvaConfigsForEleProducer = cms.VPSet(
    cms.PSet(
        categoryCuts = cms.vstring(
            'pt < 10. && abs(superCluster.eta) < 0.800',
            'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479',
            'pt < 10. && abs(superCluster.eta) >= 1.479',
            'pt >= 10. && abs(superCluster.eta) < 0.800',
            'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479',
            'pt >= 10. && abs(superCluster.eta) >= 1.479'
        ),
        mvaName = cms.string('ElectronMVAEstimatorRun2'),
        mvaTag = cms.string('Spring16HZZV1'),
        nCategories = cms.int32(6),
        variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
        weightFileNames = cms.vstring(
            'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB1_5.weights.root',
            'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB2_5.weights.root',
            'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EE_5.weights.root',
            'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB1_10.weights.root',
            'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB2_10.weights.root',
            'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EE_10.weights.root'
        )
    ),
    cms.PSet(
        categoryCuts = cms.vstring(
            'abs(superCluster.eta) < 0.800',
            'abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479',
            'abs(superCluster.eta) >= 1.479'
        ),
        mvaName = cms.string('ElectronMVAEstimatorRun2'),
        mvaTag = cms.string('Spring16GeneralPurposeV1'),
        nCategories = cms.int32(3),
        variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
        weightFileNames = cms.vstring(
            'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EB1_10.weights.root',
            'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EB2_10.weights.root',
            'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EE_10.weights.root'
        )
    ),
    cms.PSet(
        categoryCuts = cms.vstring(
            'pt < 10. && abs(superCluster.eta) < 0.800',
            'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479',
            'pt < 10. && abs(superCluster.eta) >= 1.479',
            'pt >= 10. && abs(superCluster.eta) < 0.800',
            'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479',
            'pt >= 10. && abs(superCluster.eta) >= 1.479'
        ),
        mvaName = cms.string('ElectronMVAEstimatorRun2'),
        mvaTag = cms.string('Fall17NoIsoV1'),
        nCategories = cms.int32(6),
        variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Fall17V1Variables.txt'),
        weightFileNames = cms.vstring(
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_5_2017_puinfo_BDT.weights.root',
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_5_2017_puinfo_BDT.weights.root',
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_5_2017_puinfo_BDT.weights.root',
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_10_2017_puinfo_BDT.weights.root',
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_10_2017_puinfo_BDT.weights.root',
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_10_2017_puinfo_BDT.weights.root'
        )
    ),
    cms.PSet(
        categoryCuts = cms.vstring(
            'pt < 10. && abs(superCluster.eta) < 0.800',
            'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479',
            'pt < 10. && abs(superCluster.eta) >= 1.479',
            'pt >= 10. && abs(superCluster.eta) < 0.800',
            'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479',
            'pt >= 10. && abs(superCluster.eta) >= 1.479'
        ),
        mvaName = cms.string('ElectronMVAEstimatorRun2'),
        mvaTag = cms.string('Fall17IsoV1'),
        nCategories = cms.int32(6),
        variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Fall17V1Variables.txt'),
        weightFileNames = cms.vstring(
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_5_2017_puinfo_iso_BDT.weights.root',
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_5_2017_puinfo_iso_BDT.weights.root',
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_5_2017_puinfo_iso_BDT.weights.root',
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_10_2017_puinfo_iso_BDT.weights.root',
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_10_2017_puinfo_iso_BDT.weights.root',
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_10_2017_puinfo_iso_BDT.weights.root'
        )
    ),
    cms.PSet(
        categoryCuts = cms.vstring(
            'pt < 10. && abs(superCluster.eta) < 0.800',
            'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479',
            'pt < 10. && abs(superCluster.eta) >= 1.479',
            'pt >= 10. && abs(superCluster.eta) < 0.800',
            'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479',
            'pt >= 10. && abs(superCluster.eta) >= 1.479'
        ),
        mvaName = cms.string('ElectronMVAEstimatorRun2'),
        mvaTag = cms.string('Fall17NoIsoV2'),
        nCategories = cms.int32(6),
        variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
        weightFileNames = cms.vstring(
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB1_5.weights.root',
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB2_5.weights.root',
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EE_5.weights.root',
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB1_10.weights.root',
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB2_10.weights.root',
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EE_10.weights.root'
        )
    ),
    cms.PSet(
        categoryCuts = cms.vstring(
            'pt < 10. && abs(superCluster.eta) < 0.800',
            'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479',
            'pt < 10. && abs(superCluster.eta) >= 1.479',
            'pt >= 10. && abs(superCluster.eta) < 0.800',
            'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479',
            'pt >= 10. && abs(superCluster.eta) >= 1.479'
        ),
        mvaName = cms.string('ElectronMVAEstimatorRun2'),
        mvaTag = cms.string('Fall17IsoV2'),
        nCategories = cms.int32(6),
        variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
        weightFileNames = cms.vstring(
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB1_5.weights.root',
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB2_5.weights.root',
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EE_5.weights.root',
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB1_10.weights.root',
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB2_10.weights.root',
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EE_10.weights.root'
        )
    ),
    cms.PSet(
        categoryCuts = cms.vstring(
            'pt < 10. && abs(superCluster.eta) < 0.800',
            'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479',
            'pt < 10. && abs(superCluster.eta) >= 1.479',
            'pt >= 10. && abs(superCluster.eta) < 0.800',
            'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479',
            'pt >= 10. && abs(superCluster.eta) >= 1.479'
        ),
        mvaName = cms.string('ElectronMVAEstimatorRun2'),
        mvaTag = cms.string('RunIIIWinter22NoIsoV1'),
        nCategories = cms.int32(6),
        variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronIDVariablesRun3NonIso.txt'),
        weightFileNames = cms.vstring(
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Winter22NoIsoV1/EB1_5.weights.root',
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Winter22NoIsoV1/EB2_5.weights.root',
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Winter22NoIsoV1/EE_5.weights.root',
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Winter22NoIsoV1/EB1_10.weights.root',
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Winter22NoIsoV1/EB2_10.weights.root',
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Winter22NoIsoV1/EE_10.weights.root'
        )
    ),
    cms.PSet(
        categoryCuts = cms.vstring(
            'pt < 10. && abs(superCluster.eta) < 0.800',
            'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479',
            'pt < 10. && abs(superCluster.eta) >= 1.479',
            'pt >= 10. && abs(superCluster.eta) < 0.800',
            'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479',
            'pt >= 10. && abs(superCluster.eta) >= 1.479'
        ),
        mvaName = cms.string('ElectronMVAEstimatorRun2'),
        mvaTag = cms.string('RunIIIWinter22IsoV1'),
        nCategories = cms.int32(6),
        variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronIDVariablesRun3.txt'),
        weightFileNames = cms.vstring(
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Winter22IsoV1/EB1_5.weights.root',
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Winter22IsoV1/EB2_5.weights.root',
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Winter22IsoV1/EE_5.weights.root',
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Winter22IsoV1/EB1_10.weights.root',
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Winter22IsoV1/EB2_10.weights.root',
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Winter22IsoV1/EE_10.weights.root'
        )
    ),
    cms.PSet(
        categoryCuts = cms.vstring(
            'pt < 10. & abs(superCluster.eta) < 0.800',
            'pt < 10. & abs(superCluster.eta) >= 0.800 & abs(superCluster.eta) < 1.479',
            'pt < 10. & abs(superCluster.eta) >= 1.479',
            'pt >= 10. & abs(superCluster.eta) < 0.800',
            'pt >= 10. & abs(superCluster.eta) >= 0.800 & abs(superCluster.eta) < 1.479',
            'pt >= 10. & abs(superCluster.eta) >= 1.479'
        ),
        mvaName = cms.string('ElectronMVAEstimatorRun2'),
        mvaTag = cms.string('Summer16ULIdIso'),
        nCategories = cms.int32(6),
        variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
        weightFileNames = cms.vstring(
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_16UL_ID_ISO/EB1_5.weights.root',
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_16UL_ID_ISO/EB2_5.weights.root',
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_16UL_ID_ISO/EE_5.weights.root',
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_16UL_ID_ISO/EB1_10.weights.root',
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_16UL_ID_ISO/EB2_10.weights.root',
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_16UL_ID_ISO/EE_10.weights.root'
        )
    ),
    cms.PSet(
        categoryCuts = cms.vstring(
            'pt < 10. & abs(superCluster.eta) < 0.800',
            'pt < 10. & abs(superCluster.eta) >= 0.800 & abs(superCluster.eta) < 1.479',
            'pt < 10. & abs(superCluster.eta) >= 1.479',
            'pt >= 10. & abs(superCluster.eta) < 0.800',
            'pt >= 10. & abs(superCluster.eta) >= 0.800 & abs(superCluster.eta) < 1.479',
            'pt >= 10. & abs(superCluster.eta) >= 1.479'
        ),
        mvaName = cms.string('ElectronMVAEstimatorRun2'),
        mvaTag = cms.string('Summer17ULIdIso'),
        nCategories = cms.int32(6),
        variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
        weightFileNames = cms.vstring(
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_17UL_ID_ISO/EB1_5.weights.root',
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_17UL_ID_ISO/EB2_5.weights.root',
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_17UL_ID_ISO/EE_5.weights.root',
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_17UL_ID_ISO/EB1_10.weights.root',
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_17UL_ID_ISO/EB2_10.weights.root',
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_17UL_ID_ISO/EE_10.weights.root'
        )
    ),
    cms.PSet(
        categoryCuts = cms.vstring(
            'pt < 10. & abs(superCluster.eta) < 0.800',
            'pt < 10. & abs(superCluster.eta) >= 0.800 & abs(superCluster.eta) < 1.479',
            'pt < 10. & abs(superCluster.eta) >= 1.479',
            'pt >= 10. & abs(superCluster.eta) < 0.800',
            'pt >= 10. & abs(superCluster.eta) >= 0.800 & abs(superCluster.eta) < 1.479',
            'pt >= 10. & abs(superCluster.eta) >= 1.479'
        ),
        mvaName = cms.string('ElectronMVAEstimatorRun2'),
        mvaTag = cms.string('Summer18ULIdIso'),
        nCategories = cms.int32(6),
        variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
        weightFileNames = cms.vstring(
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_18UL_ID_ISO/EB1_5.weights.root',
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_18UL_ID_ISO/EB2_5.weights.root',
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_18UL_ID_ISO/EE_5.weights.root',
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_18UL_ID_ISO/EB1_10.weights.root',
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_18UL_ID_ISO/EB2_10.weights.root',
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_18UL_ID_ISO/EE_10.weights.root'
        )
    )
)

process.MEtoEDMConverter = cms.EDProducer("MEtoEDMConverter",
    Frequency = cms.untracked.int32(50),
    MEPathToSave = cms.untracked.string(''),
    Name = cms.untracked.string('MEtoEDMConverter'),
    Verbosity = cms.untracked.int32(0)
)


process.ecalDrivenGsfElectrons = cms.EDProducer("GsfElectronProducer",
    EleDNNPFid = cms.PSet(
        enabled = cms.bool(False),
        extetaboundary = cms.double(2.65),
        inputTensorName = cms.string('FirstLayer_input'),
        modelsFiles = cms.vstring(
            'RecoEgamma/ElectronIdentification/data/Ele_PFID_dnn/Run3Summer21_120X/lowpT/lowpT_modelDNN.pb',
            'RecoEgamma/ElectronIdentification/data/Ele_PFID_dnn/Run3Summer21_120X/highpTEB/highpTEB_modelDNN.pb',
            'RecoEgamma/ElectronIdentification/data/Ele_PFID_dnn/Run3Summer21_120X/highpTEE/highpTEE_modelDNN.pb',
            'RecoEgamma/ElectronIdentification/data/Ele_PFID_dnn/Run3Winter22_122X/exteta1/modelDNN.pb',
            'RecoEgamma/ElectronIdentification/data/Ele_PFID_dnn/Run3Winter22_122X/exteta2/modelDNN.pb'
        ),
        outputDim = cms.vuint32(5, 5, 5, 5, 3),
        outputTensorName = cms.string('sequential/FinalLayer/Softmax'),
        scalersFiles = cms.vstring(
            'RecoEgamma/ElectronIdentification/data/Ele_PFID_dnn/Run3Summer21_120X/lowpT/lowpT_scaler.txt',
            'RecoEgamma/ElectronIdentification/data/Ele_PFID_dnn/Run3Summer21_120X/highpTEB/highpTEB_scaler.txt',
            'RecoEgamma/ElectronIdentification/data/Ele_PFID_dnn/Run3Summer21_120X/highpTEE/highpTEE_scaler.txt',
            'RecoEgamma/ElectronIdentification/data/Ele_PFID_dnn/Run3Winter22_122X/exteta1/scaler.txt',
            'RecoEgamma/ElectronIdentification/data/Ele_PFID_dnn/Run3Winter22_122X/exteta2/scaler.txt'
        ),
        useEBModelInGap = cms.bool(True)
    ),
    ElecMVAFilesString = cms.vstring(
        'RecoEgamma/ElectronIdentification/data/TMVA_Category_BDTSimpleCat_10_17Feb2011.weights.xml',
        'RecoEgamma/ElectronIdentification/data/TMVA_Category_BDTSimpleCat_12_17Feb2011.weights.xml',
        'RecoEgamma/ElectronIdentification/data/TMVA_Category_BDTSimpleCat_20_17Feb2011.weights.xml',
        'RecoEgamma/ElectronIdentification/data/TMVA_Category_BDTSimpleCat_22_17Feb2011.weights.xml'
    ),
    MaxElePtForOnlyMVA = cms.double(50),
    PreSelectMVA = cms.double(-0.1),
    SoftElecMVAFilesString = cms.vstring('RecoEgamma/ElectronIdentification/data/TMVA_BDTSoftElectrons_7Feb2014.weights.xml'),
    ambClustersOverlapStrategy = cms.uint32(1),
    ambSortingStrategy = cms.uint32(1),
    applyAmbResolution = cms.bool(False),
    applyPreselection = cms.bool(False),
    barrelRecHitCollectionTag = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    checkHcalStatus = cms.bool(True),
    combinationRegressionWeightFile = cms.vstring(),
    combinationRegressionWeightLabels = cms.vstring(),
    combinationWeightsFromDB = cms.bool(True),
    conversionsTag = cms.InputTag("allConversions"),
    crackCorrectionFunction = cms.string('EcalClusterCrackCorrection'),
    ctfTracksCheck = cms.bool(True),
    ctfTracksTag = cms.InputTag("generalTracks"),
    eMinBarrel = cms.double(0.095),
    eMinEndcaps = cms.double(0),
    ecalDrivenEcalEnergyFromClassBasedParameterization = cms.bool(True),
    ecalDrivenEcalErrorFromClassBasedParameterization = cms.bool(True),
    ecalRefinedRegressionWeightFiles = cms.vstring(),
    ecalRefinedRegressionWeightLabels = cms.vstring(),
    ecalWeightsFromDB = cms.bool(True),
    egmPFCandidatesTag = cms.InputTag("particleFlowEGamma"),
    endcapRecHitCollectionTag = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    etMinBarrel = cms.double(0),
    etMinEndcaps = cms.double(0.11),
    etMinHcal = cms.double(0),
    fillConvVtxFitProb = cms.bool(True),
    gsfElectronCoresTag = cms.InputTag("ecalDrivenGsfElectronCores"),
    gsfPfRecTracksTag = cms.InputTag("pfTrackElec"),
    hbheRecHits = cms.InputTag("hbhereco"),
    hcalRun2EffDepth = cms.bool(False),
    ignoreNotPreselected = cms.bool(True),
    intRadiusEcalBarrel = cms.double(3),
    intRadiusEcalEndcaps = cms.double(3),
    intRadiusHcal = cms.double(0.15),
    jurassicWidth = cms.double(1.5),
    maxHcalRecHitSeverity = cms.int32(9),
    mightGet = cms.optional.untracked.vstring,
    pfECALClusIsolCfg = cms.PSet(
        drMax = cms.double(0.3),
        drVetoBarrel = cms.double(0),
        drVetoEndcap = cms.double(0),
        energyBarrel = cms.double(0),
        energyEndcap = cms.double(0),
        etaStripBarrel = cms.double(0),
        etaStripEndcap = cms.double(0),
        pfClusterProducer = cms.InputTag("particleFlowClusterECAL")
    ),
    pfHCALClusIsolCfg = cms.PSet(
        drMax = cms.double(0.3),
        drVetoBarrel = cms.double(0),
        drVetoEndcap = cms.double(0),
        energyBarrel = cms.double(0),
        energyEndcap = cms.double(0),
        etaStripBarrel = cms.double(0),
        etaStripEndcap = cms.double(0),
        pfClusterProducerHCAL = cms.InputTag("particleFlowClusterHCAL"),
        pfClusterProducerHFEM = cms.InputTag(""),
        pfClusterProducerHFHAD = cms.InputTag(""),
        useEt = cms.bool(True),
        useHF = cms.bool(False)
    ),
    preselection = cms.PSet(
        hOverEConeSize = cms.double(0.15),
        isBarrel = cms.bool(False),
        isEndcaps = cms.bool(False),
        isFiducial = cms.bool(False),
        maxDeltaEtaBarrel = cms.double(0.02),
        maxDeltaEtaEndcaps = cms.double(0.02),
        maxDeltaPhiBarrel = cms.double(0.15),
        maxDeltaPhiEndcaps = cms.double(0.15),
        maxEOverPBarrel = cms.double(999999999),
        maxEOverPEndcaps = cms.double(999999999),
        maxFbremBarrel = cms.double(999999999),
        maxFbremEndcaps = cms.double(999999999),
        maxHBarrelBc = cms.double(0),
        maxHBarrelCone = cms.double(0),
        maxHEndcapsBc = cms.double(0),
        maxHEndcapsCone = cms.double(0),
        maxHOverEBarrelBc = cms.double(0.15),
        maxHOverEBarrelCone = cms.double(0.15),
        maxHOverEEndcapsBc = cms.double(0.15),
        maxHOverEEndcapsCone = cms.double(0.15),
        maxSigmaIetaIetaBarrel = cms.double(999999999),
        maxSigmaIetaIetaEndcaps = cms.double(999999999),
        maxTIP = cms.double(999999999),
        minEOverPBarrel = cms.double(0),
        minEOverPEndcaps = cms.double(0),
        minSCEtBarrel = cms.double(4),
        minSCEtEndcaps = cms.double(4),
        multThresEB = cms.double(1),
        multThresEE = cms.double(1.25),
        seedFromTEC = cms.bool(True)
    ),
    pureTrackerDrivenEcalErrorFromSimpleParameterization = cms.bool(True),
    recHitEThresholdHB = cms.vdouble(0.1, 0.2, 0.3, 0.3),
    recHitEThresholdHE = cms.vdouble(
        0.1, 0.2, 0.2, 0.2, 0.2,
        0.2, 0.2
    ),
    recHitFlagsToBeExcludedBarrel = cms.vstring(
        'kFaultyHardware',
        'kTowerRecovered',
        'kDead'
    ),
    recHitFlagsToBeExcludedEndcaps = cms.vstring(
        'kFaultyHardware',
        'kNeighboursRecovered',
        'kTowerRecovered',
        'kDead',
        'kWeird'
    ),
    recHitSeverityToBeExcludedBarrel = cms.vstring(
        'kWeird',
        'kBad',
        'kTime'
    ),
    recHitSeverityToBeExcludedEndcaps = cms.vstring(
        'kWeird',
        'kBad',
        'kTime'
    ),
    resetMvaValuesUsingPFCandidates = cms.bool(False),
    seedsTag = cms.InputTag("ecalDrivenElectronSeeds"),
    trkIsol03Cfg = cms.PSet(
        barrelCuts = cms.PSet(
            algosToReject = cms.vstring('jetCoreRegionalStep'),
            allowedQualities = cms.vstring(),
            maxDPtPt = cms.double(-1),
            maxDR = cms.double(0.3),
            maxDZ = cms.double(0.2),
            minDEta = cms.double(0.015),
            minDR = cms.double(0.0),
            minHits = cms.int32(-1),
            minPixelHits = cms.int32(-1),
            minPt = cms.double(0.7)
        ),
        endcapCuts = cms.PSet(
            algosToReject = cms.vstring('jetCoreRegionalStep'),
            allowedQualities = cms.vstring(),
            maxDPtPt = cms.double(-1),
            maxDR = cms.double(0.3),
            maxDZ = cms.double(0.2),
            minDEta = cms.double(0.015),
            minDR = cms.double(0.0),
            minHits = cms.int32(-1),
            minPixelHits = cms.int32(-1),
            minPt = cms.double(0.7)
        )
    ),
    trkIsol04Cfg = cms.PSet(
        barrelCuts = cms.PSet(
            algosToReject = cms.vstring('jetCoreRegionalStep'),
            allowedQualities = cms.vstring(),
            maxDPtPt = cms.double(-1),
            maxDR = cms.double(0.4),
            maxDZ = cms.double(0.2),
            minDEta = cms.double(0.015),
            minDR = cms.double(0.0),
            minHits = cms.int32(-1),
            minPixelHits = cms.int32(-1),
            minPt = cms.double(0.7)
        ),
        endcapCuts = cms.PSet(
            algosToReject = cms.vstring('jetCoreRegionalStep'),
            allowedQualities = cms.vstring(),
            maxDPtPt = cms.double(-1),
            maxDR = cms.double(0.4),
            maxDZ = cms.double(0.2),
            minDEta = cms.double(0.015),
            minDR = cms.double(0.0),
            minHits = cms.int32(-1),
            minPixelHits = cms.int32(-1),
            minPt = cms.double(0.7)
        )
    ),
    trkIsolHEEP03Cfg = cms.PSet(
        barrelCuts = cms.PSet(
            algosToReject = cms.vstring(),
            allowedQualities = cms.vstring(),
            maxDPtPt = cms.double(0.1),
            maxDR = cms.double(0.3),
            maxDZ = cms.double(0.1),
            minDEta = cms.double(0.005),
            minDR = cms.double(0.0),
            minHits = cms.int32(8),
            minPixelHits = cms.int32(1),
            minPt = cms.double(1.0)
        ),
        endcapCuts = cms.PSet(
            algosToReject = cms.vstring(),
            allowedQualities = cms.vstring(),
            maxDPtPt = cms.double(0.1),
            maxDR = cms.double(0.3),
            maxDZ = cms.double(0.5),
            minDEta = cms.double(0.005),
            minDR = cms.double(0.0),
            minHits = cms.int32(8),
            minPixelHits = cms.int32(1),
            minPt = cms.double(1.0)
        )
    ),
    trkIsolHEEP04Cfg = cms.PSet(
        barrelCuts = cms.PSet(
            algosToReject = cms.vstring(),
            allowedQualities = cms.vstring(),
            maxDPtPt = cms.double(0.1),
            maxDR = cms.double(0.4),
            maxDZ = cms.double(0.1),
            minDEta = cms.double(0.005),
            minDR = cms.double(0.0),
            minHits = cms.int32(8),
            minPixelHits = cms.int32(1),
            minPt = cms.double(1.0)
        ),
        endcapCuts = cms.PSet(
            algosToReject = cms.vstring(),
            allowedQualities = cms.vstring(),
            maxDPtPt = cms.double(0.1),
            maxDR = cms.double(0.4),
            maxDZ = cms.double(0.5),
            minDEta = cms.double(0.005),
            minDR = cms.double(0.0),
            minHits = cms.int32(8),
            minPixelHits = cms.int32(1),
            minPt = cms.double(1.0)
        )
    ),
    useCombinationRegression = cms.bool(False),
    useDefaultEnergyCorrection = cms.bool(True),
    useEcalRegression = cms.bool(False),
    useGsfPfRecTracks = cms.bool(True),
    useNumCrystals = cms.bool(True),
    vetoClustered = cms.bool(False),
    vtxTag = cms.InputTag("offlinePrimaryVertices")
)


process.egmGsfElectronIDs = cms.EDProducer("VersionedGsfElectronIdProducer",
    physicsObjectIDs = cms.VPSet(
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ),
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ),
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ),
                    cms.PSet(
                        cutName = cms.string('GsfEleEBEECut'),
                        cutString = cms.string('? superCluster.isNonnull && superCluster.seed.isNonnull ?abs(deltaEtaSuperClusterTrackAtVtx - superCluster.eta + superCluster.seed.eta) : 999999.'),
                        cutValueEB = cms.double(0.00377),
                        cutValueEE = cms.double(0.00674),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ),
                    cms.PSet(
                        cutName = cms.string('GsfEleEBEECut'),
                        cutString = cms.string('abs(deltaPhiSuperClusterTrackAtVtx)'),
                        cutValueEB = cms.double(0.0884),
                        cutValueEE = cms.double(0.169),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ),
                    cms.PSet(
                        cutName = cms.string('GsfEleEBEECut'),
                        cutString = cms.string('full5x5_sigmaIetaIeta'),
                        cutValueEB = cms.double(0.0112),
                        cutValueEE = cms.double(0.0425),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ),
                    cms.PSet(
                        barrelC0 = cms.double(0.05),
                        barrelCE = cms.double(1.16),
                        barrelCr = cms.double(0.0324),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMEnergyScaledCut'),
                        endcapC0 = cms.double(0.0441),
                        endcapCE = cms.double(2.54),
                        endcapCr = cms.double(0.183),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ),
                    cms.PSet(
                        cutName = cms.string('GsfEleEBEECut'),
                        cutString = cms.string('abs(1. - eSuperClusterOverP) / ecalEnergy'),
                        cutValueEB = cms.double(0.193),
                        cutValueEE = cms.double(0.111),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ),
                    cms.PSet(
                        barrelC0 = cms.double(0.112),
                        barrelCpt = cms.double(0.506),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleRelPFIsoScaledCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Fall17/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_94X.txt'),
                        endcapC0 = cms.double(0.108),
                        endcapCpt = cms.double(0.963),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ),
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ),
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(1),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    )
                ),
                idName = cms.string('cutBasedElectronID-Fall17-94X-V2-loose'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('5547e2c8b5c222192519c41bff05bc2e'),
            isPOGApproved = cms.untracked.bool(True)
        ),
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ),
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ),
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ),
                    cms.PSet(
                        cutName = cms.string('GsfEleEBEECut'),
                        cutString = cms.string('? superCluster.isNonnull && superCluster.seed.isNonnull ?abs(deltaEtaSuperClusterTrackAtVtx - superCluster.eta + superCluster.seed.eta) : 999999.'),
                        cutValueEB = cms.double(0.0032),
                        cutValueEE = cms.double(0.00632),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ),
                    cms.PSet(
                        cutName = cms.string('GsfEleEBEECut'),
                        cutString = cms.string('abs(deltaPhiSuperClusterTrackAtVtx)'),
                        cutValueEB = cms.double(0.0547),
                        cutValueEE = cms.double(0.0394),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ),
                    cms.PSet(
                        cutName = cms.string('GsfEleEBEECut'),
                        cutString = cms.string('full5x5_sigmaIetaIeta'),
                        cutValueEB = cms.double(0.0106),
                        cutValueEE = cms.double(0.0387),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ),
                    cms.PSet(
                        barrelC0 = cms.double(0.046),
                        barrelCE = cms.double(1.16),
                        barrelCr = cms.double(0.0324),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMEnergyScaledCut'),
                        endcapC0 = cms.double(0.0275),
                        endcapCE = cms.double(2.52),
                        endcapCr = cms.double(0.183),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ),
                    cms.PSet(
                        cutName = cms.string('GsfEleEBEECut'),
                        cutString = cms.string('abs(1. - eSuperClusterOverP) / ecalEnergy'),
                        cutValueEB = cms.double(0.184),
                        cutValueEE = cms.double(0.0721),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ),
                    cms.PSet(
                        barrelC0 = cms.double(0.0478),
                        barrelCpt = cms.double(0.506),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleRelPFIsoScaledCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Fall17/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_94X.txt'),
                        endcapC0 = cms.double(0.0658),
                        endcapCpt = cms.double(0.963),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ),
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ),
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(1),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    )
                ),
                idName = cms.string('cutBasedElectronID-Fall17-94X-V2-medium'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('48702f025a8df2c527f53927af8b66d0'),
            isPOGApproved = cms.untracked.bool(True)
        ),
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ),
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ),
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ),
                    cms.PSet(
                        cutName = cms.string('GsfEleEBEECut'),
                        cutString = cms.string('? superCluster.isNonnull && superCluster.seed.isNonnull ?abs(deltaEtaSuperClusterTrackAtVtx - superCluster.eta + superCluster.seed.eta) : 999999.'),
                        cutValueEB = cms.double(0.00255),
                        cutValueEE = cms.double(0.00501),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ),
                    cms.PSet(
                        cutName = cms.string('GsfEleEBEECut'),
                        cutString = cms.string('abs(deltaPhiSuperClusterTrackAtVtx)'),
                        cutValueEB = cms.double(0.022),
                        cutValueEE = cms.double(0.0236),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ),
                    cms.PSet(
                        cutName = cms.string('GsfEleEBEECut'),
                        cutString = cms.string('full5x5_sigmaIetaIeta'),
                        cutValueEB = cms.double(0.0104),
                        cutValueEE = cms.double(0.0353),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ),
                    cms.PSet(
                        barrelC0 = cms.double(0.026),
                        barrelCE = cms.double(1.15),
                        barrelCr = cms.double(0.0324),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMEnergyScaledCut'),
                        endcapC0 = cms.double(0.0188),
                        endcapCE = cms.double(2.06),
                        endcapCr = cms.double(0.183),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ),
                    cms.PSet(
                        cutName = cms.string('GsfEleEBEECut'),
                        cutString = cms.string('abs(1. - eSuperClusterOverP) / ecalEnergy'),
                        cutValueEB = cms.double(0.159),
                        cutValueEE = cms.double(0.0197),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ),
                    cms.PSet(
                        barrelC0 = cms.double(0.0287),
                        barrelCpt = cms.double(0.506),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleRelPFIsoScaledCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Fall17/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_94X.txt'),
                        endcapC0 = cms.double(0.0445),
                        endcapCpt = cms.double(0.963),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ),
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ),
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(1),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    )
                ),
                idName = cms.string('cutBasedElectronID-Fall17-94X-V2-tight'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('c06761e199f084f5b0f7868ac48a3e19'),
            isPOGApproved = cms.untracked.bool(True)
        ),
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ),
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ),
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ),
                    cms.PSet(
                        cutName = cms.string('GsfEleEBEECut'),
                        cutString = cms.string('? superCluster.isNonnull && superCluster.seed.isNonnull ?abs(deltaEtaSuperClusterTrackAtVtx - superCluster.eta + superCluster.seed.eta) : 999999.'),
                        cutValueEB = cms.double(0.00463),
                        cutValueEE = cms.double(0.00814),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ),
                    cms.PSet(
                        cutName = cms.string('GsfEleEBEECut'),
                        cutString = cms.string('abs(deltaPhiSuperClusterTrackAtVtx)'),
                        cutValueEB = cms.double(0.148),
                        cutValueEE = cms.double(0.19),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ),
                    cms.PSet(
                        cutName = cms.string('GsfEleEBEECut'),
                        cutString = cms.string('full5x5_sigmaIetaIeta'),
                        cutValueEB = cms.double(0.0126),
                        cutValueEE = cms.double(0.0457),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ),
                    cms.PSet(
                        barrelC0 = cms.double(0.05),
                        barrelCE = cms.double(1.16),
                        barrelCr = cms.double(0.0324),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMEnergyScaledCut'),
                        endcapC0 = cms.double(0.05),
                        endcapCE = cms.double(2.54),
                        endcapCr = cms.double(0.183),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ),
                    cms.PSet(
                        cutName = cms.string('GsfEleEBEECut'),
                        cutString = cms.string('abs(1. - eSuperClusterOverP) / ecalEnergy'),
                        cutValueEB = cms.double(0.209),
                        cutValueEE = cms.double(0.132),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ),
                    cms.PSet(
                        barrelC0 = cms.double(0.198),
                        barrelCpt = cms.double(0.506),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleRelPFIsoScaledCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Fall17/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_94X.txt'),
                        endcapC0 = cms.double(0.203),
                        endcapCpt = cms.double(0.963),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ),
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ),
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(2),
                        maxMissingHitsEE = cms.uint32(3),
                        needsAdditionalProducts = cms.bool(False)
                    )
                ),
                idName = cms.string('cutBasedElectronID-Fall17-94X-V2-veto'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('74e217e3ece16b49bd337026a29fc3e9'),
            isPOGApproved = cms.untracked.bool(True)
        )
    ),
    physicsObjectSrc = cms.InputTag("gedGsfElectrons")
)


process.electronMVAValueMapProducer = cms.EDProducer("ElectronMVAValueMapProducer",
    mvaConfigurations = cms.VPSet(
        cms.PSet(
            categoryCuts = cms.vstring(
                'pt < 10. && abs(superCluster.eta) < 0.800',
                'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479',
                'pt < 10. && abs(superCluster.eta) >= 1.479',
                'pt >= 10. && abs(superCluster.eta) < 0.800',
                'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479',
                'pt >= 10. && abs(superCluster.eta) >= 1.479'
            ),
            mvaName = cms.string('ElectronMVAEstimatorRun2'),
            mvaTag = cms.string('Spring16HZZV1'),
            nCategories = cms.int32(6),
            variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
            weightFileNames = cms.vstring(
                'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB1_5.weights.root',
                'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB2_5.weights.root',
                'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EE_5.weights.root',
                'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB1_10.weights.root',
                'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB2_10.weights.root',
                'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EE_10.weights.root'
            )
        ),
        cms.PSet(
            categoryCuts = cms.vstring(
                'abs(superCluster.eta) < 0.800',
                'abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479',
                'abs(superCluster.eta) >= 1.479'
            ),
            mvaName = cms.string('ElectronMVAEstimatorRun2'),
            mvaTag = cms.string('Spring16GeneralPurposeV1'),
            nCategories = cms.int32(3),
            variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
            weightFileNames = cms.vstring(
                'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EB1_10.weights.root',
                'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EB2_10.weights.root',
                'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EE_10.weights.root'
            )
        ),
        cms.PSet(
            categoryCuts = cms.vstring(
                'pt < 10. && abs(superCluster.eta) < 0.800',
                'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479',
                'pt < 10. && abs(superCluster.eta) >= 1.479',
                'pt >= 10. && abs(superCluster.eta) < 0.800',
                'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479',
                'pt >= 10. && abs(superCluster.eta) >= 1.479'
            ),
            mvaName = cms.string('ElectronMVAEstimatorRun2'),
            mvaTag = cms.string('Fall17NoIsoV1'),
            nCategories = cms.int32(6),
            variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Fall17V1Variables.txt'),
            weightFileNames = cms.vstring(
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_5_2017_puinfo_BDT.weights.root',
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_5_2017_puinfo_BDT.weights.root',
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_5_2017_puinfo_BDT.weights.root',
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_10_2017_puinfo_BDT.weights.root',
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_10_2017_puinfo_BDT.weights.root',
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_10_2017_puinfo_BDT.weights.root'
            )
        ),
        cms.PSet(
            categoryCuts = cms.vstring(
                'pt < 10. && abs(superCluster.eta) < 0.800',
                'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479',
                'pt < 10. && abs(superCluster.eta) >= 1.479',
                'pt >= 10. && abs(superCluster.eta) < 0.800',
                'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479',
                'pt >= 10. && abs(superCluster.eta) >= 1.479'
            ),
            mvaName = cms.string('ElectronMVAEstimatorRun2'),
            mvaTag = cms.string('Fall17IsoV1'),
            nCategories = cms.int32(6),
            variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Fall17V1Variables.txt'),
            weightFileNames = cms.vstring(
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_5_2017_puinfo_iso_BDT.weights.root',
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_5_2017_puinfo_iso_BDT.weights.root',
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_5_2017_puinfo_iso_BDT.weights.root',
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_10_2017_puinfo_iso_BDT.weights.root',
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_10_2017_puinfo_iso_BDT.weights.root',
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_10_2017_puinfo_iso_BDT.weights.root'
            )
        ),
        cms.PSet(
            categoryCuts = cms.vstring(
                'pt < 10. && abs(superCluster.eta) < 0.800',
                'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479',
                'pt < 10. && abs(superCluster.eta) >= 1.479',
                'pt >= 10. && abs(superCluster.eta) < 0.800',
                'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479',
                'pt >= 10. && abs(superCluster.eta) >= 1.479'
            ),
            mvaName = cms.string('ElectronMVAEstimatorRun2'),
            mvaTag = cms.string('Fall17NoIsoV2'),
            nCategories = cms.int32(6),
            variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
            weightFileNames = cms.vstring(
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB1_5.weights.root',
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB2_5.weights.root',
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EE_5.weights.root',
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB1_10.weights.root',
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB2_10.weights.root',
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EE_10.weights.root'
            )
        ),
        cms.PSet(
            categoryCuts = cms.vstring(
                'pt < 10. && abs(superCluster.eta) < 0.800',
                'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479',
                'pt < 10. && abs(superCluster.eta) >= 1.479',
                'pt >= 10. && abs(superCluster.eta) < 0.800',
                'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479',
                'pt >= 10. && abs(superCluster.eta) >= 1.479'
            ),
            mvaName = cms.string('ElectronMVAEstimatorRun2'),
            mvaTag = cms.string('Fall17IsoV2'),
            nCategories = cms.int32(6),
            variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
            weightFileNames = cms.vstring(
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB1_5.weights.root',
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB2_5.weights.root',
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EE_5.weights.root',
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB1_10.weights.root',
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB2_10.weights.root',
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EE_10.weights.root'
            )
        ),
        cms.PSet(
            categoryCuts = cms.vstring(
                'pt < 10. && abs(superCluster.eta) < 0.800',
                'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479',
                'pt < 10. && abs(superCluster.eta) >= 1.479',
                'pt >= 10. && abs(superCluster.eta) < 0.800',
                'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479',
                'pt >= 10. && abs(superCluster.eta) >= 1.479'
            ),
            mvaName = cms.string('ElectronMVAEstimatorRun2'),
            mvaTag = cms.string('RunIIIWinter22NoIsoV1'),
            nCategories = cms.int32(6),
            variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronIDVariablesRun3NonIso.txt'),
            weightFileNames = cms.vstring(
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Winter22NoIsoV1/EB1_5.weights.root',
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Winter22NoIsoV1/EB2_5.weights.root',
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Winter22NoIsoV1/EE_5.weights.root',
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Winter22NoIsoV1/EB1_10.weights.root',
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Winter22NoIsoV1/EB2_10.weights.root',
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Winter22NoIsoV1/EE_10.weights.root'
            )
        ),
        cms.PSet(
            categoryCuts = cms.vstring(
                'pt < 10. && abs(superCluster.eta) < 0.800',
                'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479',
                'pt < 10. && abs(superCluster.eta) >= 1.479',
                'pt >= 10. && abs(superCluster.eta) < 0.800',
                'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479',
                'pt >= 10. && abs(superCluster.eta) >= 1.479'
            ),
            mvaName = cms.string('ElectronMVAEstimatorRun2'),
            mvaTag = cms.string('RunIIIWinter22IsoV1'),
            nCategories = cms.int32(6),
            variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronIDVariablesRun3.txt'),
            weightFileNames = cms.vstring(
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Winter22IsoV1/EB1_5.weights.root',
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Winter22IsoV1/EB2_5.weights.root',
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Winter22IsoV1/EE_5.weights.root',
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Winter22IsoV1/EB1_10.weights.root',
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Winter22IsoV1/EB2_10.weights.root',
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Winter22IsoV1/EE_10.weights.root'
            )
        ),
        cms.PSet(
            categoryCuts = cms.vstring(
                'pt < 10. & abs(superCluster.eta) < 0.800',
                'pt < 10. & abs(superCluster.eta) >= 0.800 & abs(superCluster.eta) < 1.479',
                'pt < 10. & abs(superCluster.eta) >= 1.479',
                'pt >= 10. & abs(superCluster.eta) < 0.800',
                'pt >= 10. & abs(superCluster.eta) >= 0.800 & abs(superCluster.eta) < 1.479',
                'pt >= 10. & abs(superCluster.eta) >= 1.479'
            ),
            mvaName = cms.string('ElectronMVAEstimatorRun2'),
            mvaTag = cms.string('Summer16ULIdIso'),
            nCategories = cms.int32(6),
            variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
            weightFileNames = cms.vstring(
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_16UL_ID_ISO/EB1_5.weights.root',
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_16UL_ID_ISO/EB2_5.weights.root',
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_16UL_ID_ISO/EE_5.weights.root',
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_16UL_ID_ISO/EB1_10.weights.root',
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_16UL_ID_ISO/EB2_10.weights.root',
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_16UL_ID_ISO/EE_10.weights.root'
            )
        ),
        cms.PSet(
            categoryCuts = cms.vstring(
                'pt < 10. & abs(superCluster.eta) < 0.800',
                'pt < 10. & abs(superCluster.eta) >= 0.800 & abs(superCluster.eta) < 1.479',
                'pt < 10. & abs(superCluster.eta) >= 1.479',
                'pt >= 10. & abs(superCluster.eta) < 0.800',
                'pt >= 10. & abs(superCluster.eta) >= 0.800 & abs(superCluster.eta) < 1.479',
                'pt >= 10. & abs(superCluster.eta) >= 1.479'
            ),
            mvaName = cms.string('ElectronMVAEstimatorRun2'),
            mvaTag = cms.string('Summer17ULIdIso'),
            nCategories = cms.int32(6),
            variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
            weightFileNames = cms.vstring(
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_17UL_ID_ISO/EB1_5.weights.root',
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_17UL_ID_ISO/EB2_5.weights.root',
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_17UL_ID_ISO/EE_5.weights.root',
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_17UL_ID_ISO/EB1_10.weights.root',
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_17UL_ID_ISO/EB2_10.weights.root',
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_17UL_ID_ISO/EE_10.weights.root'
            )
        ),
        cms.PSet(
            categoryCuts = cms.vstring(
                'pt < 10. & abs(superCluster.eta) < 0.800',
                'pt < 10. & abs(superCluster.eta) >= 0.800 & abs(superCluster.eta) < 1.479',
                'pt < 10. & abs(superCluster.eta) >= 1.479',
                'pt >= 10. & abs(superCluster.eta) < 0.800',
                'pt >= 10. & abs(superCluster.eta) >= 0.800 & abs(superCluster.eta) < 1.479',
                'pt >= 10. & abs(superCluster.eta) >= 1.479'
            ),
            mvaName = cms.string('ElectronMVAEstimatorRun2'),
            mvaTag = cms.string('Summer18ULIdIso'),
            nCategories = cms.int32(6),
            variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
            weightFileNames = cms.vstring(
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_18UL_ID_ISO/EB1_5.weights.root',
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_18UL_ID_ISO/EB2_5.weights.root',
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_18UL_ID_ISO/EE_5.weights.root',
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_18UL_ID_ISO/EB1_10.weights.root',
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_18UL_ID_ISO/EB2_10.weights.root',
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_18UL_ID_ISO/EE_10.weights.root'
            )
        )
    ),
    src = cms.InputTag("slimmedElectrons")
)


process.gedGsfElectronCores = cms.EDProducer("GEDGsfElectronCoreProducer",
    GEDEMUnbiased = cms.InputTag("particleFlowEGamma"),
    ctfTracks = cms.InputTag("generalTracks"),
    mightGet = cms.optional.untracked.vstring
)


process.gedGsfElectronValueMapsTmp = cms.EDProducer("GEDGsfElectronValueMapProducer",
    egmPFCandidatesTag = cms.InputTag("particleFlowEGamma"),
    gedGsfElectrons = cms.InputTag("gedGsfElectronsTmp"),
    mightGet = cms.optional.untracked.vstring
)


process.gedGsfElectronsTmp = cms.EDProducer("GsfElectronProducer",
    EleDNNPFid = cms.PSet(
        enabled = cms.bool(False),
        extetaboundary = cms.double(2.65),
        inputTensorName = cms.string('FirstLayer_input'),
        modelsFiles = cms.vstring(
            'RecoEgamma/ElectronIdentification/data/Ele_PFID_dnn/Run3Summer21_120X/lowpT/lowpT_modelDNN.pb',
            'RecoEgamma/ElectronIdentification/data/Ele_PFID_dnn/Run3Summer21_120X/EB_highpT/barrel_highpT_modelDNN.pb',
            'RecoEgamma/ElectronIdentification/data/Ele_PFID_dnn/Run3Summer21_120X/EE_highpT/endcap_highpT_modelDNN.pb',
            'RecoEgamma/ElectronIdentification/data/Ele_PFID_dnn/Run3Winter22_122X/exteta1/modelDNN.pb',
            'RecoEgamma/ElectronIdentification/data/Ele_PFID_dnn/Run3Winter22_122X/exteta2/modelDNN.pb'
        ),
        outputDim = cms.vuint32(5, 5, 5, 5, 3),
        outputTensorName = cms.string('sequential_1/FinalLayer/Softmax'),
        scalersFiles = cms.vstring(
            'RecoEgamma/ElectronIdentification/data/Ele_PFID_dnn/Run3Summer21_120X/lowpT/lowpT_scaler.txt',
            'RecoEgamma/ElectronIdentification/data/Ele_PFID_dnn/Run3Summer21_120X/EB_highpT/barrel_highpT_scaler.txt',
            'RecoEgamma/ElectronIdentification/data/Ele_PFID_dnn/Run3Summer21_120X/EE_highpT/endcap_highpT_scaler.txt',
            'RecoEgamma/ElectronIdentification/data/Ele_PFID_dnn/Run3Winter22_122X/exteta1/scaler.txt',
            'RecoEgamma/ElectronIdentification/data/Ele_PFID_dnn/Run3Winter22_122X/exteta2/scaler.txt'
        ),
        useEBModelInGap = cms.bool(True)
    ),
    ElecMVAFilesString = cms.vstring(
        'RecoEgamma/ElectronIdentification/data/TMVA_Category_BDTSimpleCat_10_17Feb2011.weights.xml',
        'RecoEgamma/ElectronIdentification/data/TMVA_Category_BDTSimpleCat_12_17Feb2011.weights.xml',
        'RecoEgamma/ElectronIdentification/data/TMVA_Category_BDTSimpleCat_20_17Feb2011.weights.xml',
        'RecoEgamma/ElectronIdentification/data/TMVA_Category_BDTSimpleCat_22_17Feb2011.weights.xml'
    ),
    MaxElePtForOnlyMVA = cms.double(50),
    PreSelectMVA = cms.double(-0.1),
    SoftElecMVAFilesString = cms.vstring('RecoEgamma/ElectronIdentification/data/TMVA_BDTSoftElectrons_7Feb2014.weights.xml'),
    ambClustersOverlapStrategy = cms.uint32(1),
    ambSortingStrategy = cms.uint32(1),
    applyAmbResolution = cms.bool(False),
    applyPreselection = cms.bool(True),
    barrelRecHitCollectionTag = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    checkHcalStatus = cms.bool(True),
    combinationRegressionWeightFile = cms.vstring(),
    combinationRegressionWeightLabels = cms.vstring('gedelectron_p4combination_offline'),
    combinationWeightsFromDB = cms.bool(True),
    conversionsTag = cms.InputTag("allConversions"),
    crackCorrectionFunction = cms.string('EcalClusterCrackCorrection'),
    ctfTracksCheck = cms.bool(True),
    ctfTracksTag = cms.InputTag("generalTracks"),
    eMinBarrel = cms.double(0.095),
    eMinEndcaps = cms.double(0),
    ecalDrivenEcalEnergyFromClassBasedParameterization = cms.bool(False),
    ecalDrivenEcalErrorFromClassBasedParameterization = cms.bool(False),
    ecalRefinedRegressionWeightFiles = cms.vstring(),
    ecalRefinedRegressionWeightLabels = cms.vstring(
        'gedelectron_EBCorrection_offline_v1',
        'gedelectron_EECorrection_offline_v1',
        'gedelectron_EBUncertainty_offline_v1',
        'gedelectron_EEUncertainty_offline_v1'
    ),
    ecalWeightsFromDB = cms.bool(True),
    egmPFCandidatesTag = cms.InputTag("particleFlowEGamma"),
    endcapRecHitCollectionTag = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    etMinBarrel = cms.double(0),
    etMinEndcaps = cms.double(0.11),
    etMinHcal = cms.double(0),
    fillConvVtxFitProb = cms.bool(True),
    gsfElectronCoresTag = cms.InputTag("gedGsfElectronCores"),
    gsfPfRecTracksTag = cms.InputTag("pfTrackElec"),
    hbheRecHits = cms.InputTag("hbhereco"),
    hcalRun2EffDepth = cms.bool(False),
    ignoreNotPreselected = cms.bool(True),
    intRadiusEcalBarrel = cms.double(3),
    intRadiusEcalEndcaps = cms.double(3),
    intRadiusHcal = cms.double(0.15),
    jurassicWidth = cms.double(1.5),
    maxHcalRecHitSeverity = cms.int32(9),
    mightGet = cms.optional.untracked.vstring,
    pfECALClusIsolCfg = cms.PSet(
        drMax = cms.double(0.3),
        drVetoBarrel = cms.double(0),
        drVetoEndcap = cms.double(0),
        energyBarrel = cms.double(0),
        energyEndcap = cms.double(0),
        etaStripBarrel = cms.double(0),
        etaStripEndcap = cms.double(0),
        pfClusterProducer = cms.InputTag("particleFlowClusterECAL")
    ),
    pfHCALClusIsolCfg = cms.PSet(
        drMax = cms.double(0.3),
        drVetoBarrel = cms.double(0),
        drVetoEndcap = cms.double(0),
        energyBarrel = cms.double(0),
        energyEndcap = cms.double(0),
        etaStripBarrel = cms.double(0),
        etaStripEndcap = cms.double(0),
        pfClusterProducerHCAL = cms.InputTag("particleFlowClusterHCAL"),
        pfClusterProducerHFEM = cms.InputTag(""),
        pfClusterProducerHFHAD = cms.InputTag(""),
        useEt = cms.bool(True),
        useHF = cms.bool(False)
    ),
    preselection = cms.PSet(
        hOverEConeSize = cms.double(0.15),
        isBarrel = cms.bool(False),
        isEndcaps = cms.bool(False),
        isFiducial = cms.bool(False),
        maxDeltaEtaBarrel = cms.double(0.02),
        maxDeltaEtaEndcaps = cms.double(0.02),
        maxDeltaPhiBarrel = cms.double(0.15),
        maxDeltaPhiEndcaps = cms.double(0.15),
        maxEOverPBarrel = cms.double(999999999),
        maxEOverPEndcaps = cms.double(999999999),
        maxFbremBarrel = cms.double(999999999),
        maxFbremEndcaps = cms.double(999999999),
        maxHBarrelBc = cms.double(0),
        maxHBarrelCone = cms.double(0),
        maxHEndcapsBc = cms.double(0),
        maxHEndcapsCone = cms.double(0),
        maxHOverEBarrelBc = cms.double(0.15),
        maxHOverEBarrelCone = cms.double(0.15),
        maxHOverEEndcapsBc = cms.double(0.15),
        maxHOverEEndcapsCone = cms.double(0.15),
        maxSigmaIetaIetaBarrel = cms.double(999999999),
        maxSigmaIetaIetaEndcaps = cms.double(999999999),
        maxTIP = cms.double(999999999),
        minEOverPBarrel = cms.double(0),
        minEOverPEndcaps = cms.double(0),
        minSCEtBarrel = cms.double(4),
        minSCEtEndcaps = cms.double(4),
        multThresEB = cms.double(1),
        multThresEE = cms.double(1.25),
        seedFromTEC = cms.bool(True)
    ),
    pureTrackerDrivenEcalErrorFromSimpleParameterization = cms.bool(True),
    recHitEThresholdHB = cms.vdouble(0.1, 0.2, 0.3, 0.3),
    recHitEThresholdHE = cms.vdouble(
        0.1, 0.2, 0.2, 0.2, 0.2,
        0.2, 0.2
    ),
    recHitFlagsToBeExcludedBarrel = cms.vstring(
        'kFaultyHardware',
        'kTowerRecovered',
        'kDead'
    ),
    recHitFlagsToBeExcludedEndcaps = cms.vstring(
        'kFaultyHardware',
        'kNeighboursRecovered',
        'kTowerRecovered',
        'kDead',
        'kWeird'
    ),
    recHitSeverityToBeExcludedBarrel = cms.vstring(
        'kWeird',
        'kBad',
        'kTime'
    ),
    recHitSeverityToBeExcludedEndcaps = cms.vstring(
        'kWeird',
        'kBad',
        'kTime'
    ),
    resetMvaValuesUsingPFCandidates = cms.bool(True),
    seedsTag = cms.InputTag("ecalDrivenElectronSeeds"),
    trkIsol03Cfg = cms.PSet(
        barrelCuts = cms.PSet(
            algosToReject = cms.vstring('jetCoreRegionalStep'),
            allowedQualities = cms.vstring(),
            maxDPtPt = cms.double(-1),
            maxDR = cms.double(0.3),
            maxDZ = cms.double(0.2),
            minDEta = cms.double(0.015),
            minDR = cms.double(0.0),
            minHits = cms.int32(-1),
            minPixelHits = cms.int32(-1),
            minPt = cms.double(0.7)
        ),
        endcapCuts = cms.PSet(
            algosToReject = cms.vstring('jetCoreRegionalStep'),
            allowedQualities = cms.vstring(),
            maxDPtPt = cms.double(-1),
            maxDR = cms.double(0.3),
            maxDZ = cms.double(0.2),
            minDEta = cms.double(0.015),
            minDR = cms.double(0.0),
            minHits = cms.int32(-1),
            minPixelHits = cms.int32(-1),
            minPt = cms.double(0.7)
        )
    ),
    trkIsol04Cfg = cms.PSet(
        barrelCuts = cms.PSet(
            algosToReject = cms.vstring('jetCoreRegionalStep'),
            allowedQualities = cms.vstring(),
            maxDPtPt = cms.double(-1),
            maxDR = cms.double(0.4),
            maxDZ = cms.double(0.2),
            minDEta = cms.double(0.015),
            minDR = cms.double(0.0),
            minHits = cms.int32(-1),
            minPixelHits = cms.int32(-1),
            minPt = cms.double(0.7)
        ),
        endcapCuts = cms.PSet(
            algosToReject = cms.vstring('jetCoreRegionalStep'),
            allowedQualities = cms.vstring(),
            maxDPtPt = cms.double(-1),
            maxDR = cms.double(0.4),
            maxDZ = cms.double(0.2),
            minDEta = cms.double(0.015),
            minDR = cms.double(0.0),
            minHits = cms.int32(-1),
            minPixelHits = cms.int32(-1),
            minPt = cms.double(0.7)
        )
    ),
    trkIsolHEEP03Cfg = cms.PSet(
        barrelCuts = cms.PSet(
            algosToReject = cms.vstring(),
            allowedQualities = cms.vstring(),
            maxDPtPt = cms.double(0.1),
            maxDR = cms.double(0.3),
            maxDZ = cms.double(0.1),
            minDEta = cms.double(0.005),
            minDR = cms.double(0.0),
            minHits = cms.int32(8),
            minPixelHits = cms.int32(1),
            minPt = cms.double(1.0)
        ),
        endcapCuts = cms.PSet(
            algosToReject = cms.vstring(),
            allowedQualities = cms.vstring(),
            maxDPtPt = cms.double(0.1),
            maxDR = cms.double(0.3),
            maxDZ = cms.double(0.5),
            minDEta = cms.double(0.005),
            minDR = cms.double(0.0),
            minHits = cms.int32(8),
            minPixelHits = cms.int32(1),
            minPt = cms.double(1.0)
        )
    ),
    trkIsolHEEP04Cfg = cms.PSet(
        barrelCuts = cms.PSet(
            algosToReject = cms.vstring(),
            allowedQualities = cms.vstring(),
            maxDPtPt = cms.double(0.1),
            maxDR = cms.double(0.4),
            maxDZ = cms.double(0.1),
            minDEta = cms.double(0.005),
            minDR = cms.double(0.0),
            minHits = cms.int32(8),
            minPixelHits = cms.int32(1),
            minPt = cms.double(1.0)
        ),
        endcapCuts = cms.PSet(
            algosToReject = cms.vstring(),
            allowedQualities = cms.vstring(),
            maxDPtPt = cms.double(0.1),
            maxDR = cms.double(0.4),
            maxDZ = cms.double(0.5),
            minDEta = cms.double(0.005),
            minDR = cms.double(0.0),
            minHits = cms.int32(8),
            minPixelHits = cms.int32(1),
            minPt = cms.double(1.0)
        )
    ),
    useCombinationRegression = cms.bool(True),
    useDefaultEnergyCorrection = cms.bool(True),
    useEcalRegression = cms.bool(True),
    useGsfPfRecTracks = cms.bool(True),
    useNumCrystals = cms.bool(True),
    vetoClustered = cms.bool(False),
    vtxTag = cms.InputTag("offlinePrimaryVertices")
)


process.gsfElectronDRNCorrectionProducer = cms.EDProducer("GsfElectronDRNCorrectionProducer",
    Client = cms.PSet(
        allowedTries = cms.untracked.uint32(0),
        compression = cms.untracked.string(''),
        mode = cms.string('PseudoAsync'),
        modelConfigPath = cms.required.FileInPath,
        modelName = cms.required.string,
        modelVersion = cms.string(''),
        outputs = cms.untracked.vstring(),
        preferredServer = cms.untracked.string(''),
        timeout = cms.required.untracked.uint32,
        useSharedMemory = cms.untracked.bool(True),
        verbose = cms.untracked.bool(False)
    ),
    mightGet = cms.optional.untracked.vstring,
    particleSource = cms.required.InputTag,
    reducedEcalRecHitsEB = cms.InputTag("reducedEcalRecHitsEB"),
    reducedEcalRecHitsEE = cms.InputTag("reducedEcalRecHitsEE"),
    reducedEcalRecHitsES = cms.InputTag("reducedEcalRecHitsES"),
    rhoName = cms.required.InputTag
)


process.gsfElectronsDRN = cms.EDProducer("GsfElectronDRNCorrectionProducer",
    Client = cms.PSet(
        allowedTries = cms.untracked.uint32(1),
        compression = cms.untracked.string(''),
        mode = cms.string('Async'),
        modelConfigPath = cms.FileInPath('RecoEgamma/EgammaElectronProducers/data/models/photonObjectCombined/config.pbtxt'),
        modelName = cms.string('photonObjectCombined'),
        modelVersion = cms.string(''),
        outputs = cms.untracked.vstring(),
        preferredServer = cms.untracked.string(''),
        timeout = cms.untracked.uint32(10),
        useSharedMemory = cms.untracked.bool(True),
        verbose = cms.untracked.bool(False)
    ),
    mightGet = cms.optional.untracked.vstring,
    particleSource = cms.InputTag("gedGsfElectrons"),
    reducedEcalRecHitsEB = cms.InputTag("reducedEcalRecHitsEB"),
    reducedEcalRecHitsEE = cms.InputTag("reducedEcalRecHitsEE"),
    reducedEcalRecHitsES = cms.InputTag("reducedEcalRecHitsES"),
    rhoName = cms.InputTag("fixedGridRhoFastjetAll")
)


process.nTuplelize = cms.EDAnalyzer("Electron_RefinedRecHit_NTuplizer",
    eleLooseIdMap = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-loose"),
    eleMediumIdMap = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-medium"),
    eleTightIdMap = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-tight"),
    electrons = cms.InputTag("gedGsfElectrons"),
    genParticles = cms.InputTag("genParticles"),
    gsfElectronsDRN = cms.InputTag("gsfElectronsDRN"),
    isMC = cms.bool(True),
    miniAODRun = cms.bool(False),
    refinedCluster = cms.bool(False),
    rhoFastJet = cms.InputTag("fixedGridRhoAll")
)


process.output = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('~//'),
    outputCommands = cms.untracked.vstring('keep *'),
    splitLevel = cms.untracked.int32(0)
)


process.DQMStore = cms.Service("DQMStore")


process.MessageLogger = cms.Service("MessageLogger",
    cerr = cms.untracked.PSet(
        FwkReport = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            reportEvery = cms.untracked.int32(24)
        ),
        FwkSummary = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            reportEvery = cms.untracked.int32(1)
        ),
        INFO = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000)
        ),
        enable = cms.untracked.bool(True),
        enableStatistics = cms.untracked.bool(False),
        lineLength = cms.optional.untracked.int32,
        noLineBreaks = cms.optional.untracked.bool,
        noTimeStamps = cms.untracked.bool(False),
        resetStatistics = cms.untracked.bool(False),
        statisticsThreshold = cms.untracked.string('WARNING'),
        threshold = cms.untracked.string('INFO'),
        allowAnyLabel_=cms.optional.untracked.PSetTemplate(
            limit = cms.optional.untracked.int32,
            reportEvery = cms.untracked.int32(1),
            timespan = cms.optional.untracked.int32
        )
    ),
    cout = cms.untracked.PSet(
        enable = cms.untracked.bool(False),
        enableStatistics = cms.untracked.bool(False),
        lineLength = cms.optional.untracked.int32,
        noLineBreaks = cms.optional.untracked.bool,
        noTimeStamps = cms.optional.untracked.bool,
        resetStatistics = cms.untracked.bool(False),
        statisticsThreshold = cms.optional.untracked.string,
        threshold = cms.optional.untracked.string,
        allowAnyLabel_=cms.optional.untracked.PSetTemplate(
            limit = cms.optional.untracked.int32,
            reportEvery = cms.untracked.int32(1),
            timespan = cms.optional.untracked.int32
        )
    ),
    debugModules = cms.untracked.vstring(),
    default = cms.untracked.PSet(
        limit = cms.optional.untracked.int32,
        lineLength = cms.untracked.int32(80),
        noLineBreaks = cms.untracked.bool(False),
        noTimeStamps = cms.untracked.bool(False),
        reportEvery = cms.untracked.int32(1),
        statisticsThreshold = cms.untracked.string('INFO'),
        threshold = cms.untracked.string('INFO'),
        timespan = cms.optional.untracked.int32,
        allowAnyLabel_=cms.optional.untracked.PSetTemplate(
            limit = cms.optional.untracked.int32,
            reportEvery = cms.untracked.int32(1),
            timespan = cms.optional.untracked.int32
        )
    ),
    files = cms.untracked.PSet(
        allowAnyLabel_=cms.optional.untracked.PSetTemplate(
            enableStatistics = cms.untracked.bool(False),
            extension = cms.optional.untracked.string,
            filename = cms.optional.untracked.string,
            lineLength = cms.optional.untracked.int32,
            noLineBreaks = cms.optional.untracked.bool,
            noTimeStamps = cms.optional.untracked.bool,
            output = cms.optional.untracked.string,
            resetStatistics = cms.untracked.bool(False),
            statisticsThreshold = cms.optional.untracked.string,
            threshold = cms.optional.untracked.string,
            allowAnyLabel_=cms.optional.untracked.PSetTemplate(
                limit = cms.optional.untracked.int32,
                reportEvery = cms.untracked.int32(1),
                timespan = cms.optional.untracked.int32
            )
        )
    ),
    suppressDebug = cms.untracked.vstring(),
    suppressFwkInfo = cms.untracked.vstring(),
    suppressInfo = cms.untracked.vstring(),
    suppressWarning = cms.untracked.vstring(),
    allowAnyLabel_=cms.optional.untracked.PSetTemplate(
        limit = cms.optional.untracked.int32,
        reportEvery = cms.untracked.int32(1),
        timespan = cms.optional.untracked.int32
    )
)


process.TFileService = cms.Service("TFileService",
    closeFileFast = cms.untracked.bool(True),
    fileName = cms.string('/eos/user/b/bbapi/Energy_regression/CMSSW_13_3_3/src/crab_files/skimmed/~//')
)


process.TritonService = cms.Service("TritonService",
    fallback = cms.PSet(
        debug = cms.untracked.bool(False),
        enable = cms.untracked.bool(False),
        imageName = cms.untracked.string(''),
        instanceBaseName = cms.untracked.string('triton_server_instance'),
        instanceName = cms.untracked.string(''),
        retries = cms.untracked.int32(-1),
        sandboxName = cms.untracked.string(''),
        tempDir = cms.untracked.string(''),
        useDocker = cms.untracked.bool(False),
        useGPU = cms.untracked.bool(False),
        verbose = cms.untracked.bool(False),
        wait = cms.untracked.int32(-1)
    ),
    servers = cms.untracked.VPSet(cms.PSet(
        address = cms.untracked.string('lxplus913.cern.ch'),
        certificateChain = cms.untracked.string(''),
        name = cms.untracked.string('local_triton'),
        port = cms.untracked.uint32(9001),
        privateKey = cms.untracked.string(''),
        rootCertificates = cms.untracked.string(''),
        useSsl = cms.untracked.bool(False)
    )),
    verbose = cms.untracked.bool(False)
)


process.CSCGeometryESModule = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    debugV = cms.untracked.bool(False),
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.CaloGeometryBuilder = cms.ESProducer("CaloGeometryBuilder",
    SelectedCalos = cms.vstring(
        'HCAL',
        'ZDC',
        'EcalBarrel',
        'EcalEndcap',
        'EcalPreshower',
        'TOWER'
    )
)


process.CaloTopologyBuilder = cms.ESProducer("CaloTopologyBuilder")


process.CaloTowerGeometryFromDBEP = cms.ESProducer("CaloTowerGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.CaloTowerTopologyEP = cms.ESProducer("CaloTowerTopologyEP")


process.CastorDbProducer = cms.ESProducer("CastorDbProducer",
    appendToDataLabel = cms.string('')
)


process.CastorGeometryFromDBEP = cms.ESProducer("CastorGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.DTGeometryESModule = cms.ESProducer("DTGeometryESModule",
    DDDetector = cms.ESInputTag("",""),
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    attribute = cms.string('MuStructure'),
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(False),
    value = cms.string('MuonBarrelDT')
)


process.EcalBarrelGeometryFromDBEP = cms.ESProducer("EcalBarrelGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalElectronicsMappingBuilder = cms.ESProducer("EcalElectronicsMappingBuilder")


process.EcalEndcapGeometryFromDBEP = cms.ESProducer("EcalEndcapGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalLaserCorrectionService = cms.ESProducer("EcalLaserCorrectionService",
    maxExtrapolationTimeInSec = cms.uint32(0)
)


process.EcalLaserCorrectionServiceMC = cms.ESProducer("EcalLaserCorrectionServiceMC",
    appendToDataLabel = cms.string('')
)


process.EcalPreshowerGeometryFromDBEP = cms.ESProducer("EcalPreshowerGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalTrigTowerConstituentsMapBuilder = cms.ESProducer("EcalTrigTowerConstituentsMapBuilder",
    MapFile = cms.untracked.string('Geometry/EcalMapping/data/EndCap_TTMap.txt')
)


process.GlobalTrackingGeometryESProducer = cms.ESProducer("GlobalTrackingGeometryESProducer")


process.HcalAlignmentEP = cms.ESProducer("HcalAlignmentEP")


process.HcalGeometryFromDBEP = cms.ESProducer("HcalGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.MuonDetLayerGeometryESProducer = cms.ESProducer("MuonDetLayerGeometryESProducer")


process.MuonNumberingInitialization = cms.ESProducer("MuonNumberingInitialization")


process.ParabolicParametrizedMagneticFieldProducer = cms.ESProducer("AutoParametrizedMagneticFieldProducer",
    label = cms.untracked.string('ParabolicMf'),
    valueOverride = cms.int32(-1),
    version = cms.string('Parabolic')
)


process.RPCGeometryESModule = cms.ESProducer("RPCGeometryESModule",
    fromDD4hep = cms.untracked.bool(False),
    fromDDD = cms.untracked.bool(False)
)


process.SiStripRecHitMatcherESProducer = cms.ESProducer("SiStripRecHitMatcherESProducer",
    ComponentName = cms.string('StandardMatcher'),
    NSigmaInside = cms.double(3.0),
    PreFilter = cms.bool(False)
)


process.StripCPEfromTrackAngleESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('StripCPEfromTrackAngle'),
    ComponentType = cms.string('StripCPEfromTrackAngle'),
    parameters = cms.PSet(
        mLC_P0 = cms.double(-0.326),
        mLC_P1 = cms.double(0.618),
        mLC_P2 = cms.double(0.3),
        mTEC_P0 = cms.double(-1.885),
        mTEC_P1 = cms.double(0.471),
        mTIB_P0 = cms.double(-0.742),
        mTIB_P1 = cms.double(0.202),
        mTID_P0 = cms.double(-1.427),
        mTID_P1 = cms.double(0.433),
        mTOB_P0 = cms.double(-1.026),
        mTOB_P1 = cms.double(0.253),
        maxChgOneMIP = cms.double(6000.0),
        useLegacyError = cms.bool(False)
    )
)


process.TrackerRecoGeometryESProducer = cms.ESProducer("TrackerRecoGeometryESProducer",
    usePhase2Stacks = cms.bool(False)
)


process.VolumeBasedMagneticFieldESProducer = cms.ESProducer("VolumeBasedMagneticFieldESProducerFromDB",
    debugBuilder = cms.untracked.bool(False),
    label = cms.untracked.string(''),
    valueOverride = cms.int32(-1)
)


process.XMLFromDBSource = cms.ESProducer("XMLIdealGeometryESProducer",
    label = cms.string('Extended'),
    rootDDName = cms.string('cms:OCMS')
)


process.ZdcGeometryFromDBEP = cms.ESProducer("ZdcGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.caloSimulationParameters = cms.ESProducer("CaloSimParametersESModule",
    appendToDataLabel = cms.string(''),
    fromDD4hep = cms.bool(False)
)


process.ctppsBeamParametersFromLHCInfoESSource = cms.ESProducer("CTPPSBeamParametersFromLHCInfoESSource",
    appendToDataLabel = cms.string(''),
    beamDivX45 = cms.double(0.1),
    beamDivX56 = cms.double(0.1),
    beamDivY45 = cms.double(0.1),
    beamDivY56 = cms.double(0.1),
    lhcInfoLabel = cms.string(''),
    vtxOffsetX45 = cms.double(0.01),
    vtxOffsetX56 = cms.double(0.01),
    vtxOffsetY45 = cms.double(0.01),
    vtxOffsetY56 = cms.double(0.01),
    vtxOffsetZ45 = cms.double(0.01),
    vtxOffsetZ56 = cms.double(0.01),
    vtxStddevX = cms.double(0.02),
    vtxStddevY = cms.double(0.02),
    vtxStddevZ = cms.double(0.02)
)


process.ctppsInterpolatedOpticalFunctionsESSource = cms.ESProducer("CTPPSInterpolatedOpticalFunctionsESSource",
    appendToDataLabel = cms.string(''),
    lhcInfoLabel = cms.string(''),
    lhcInfoPerFillLabel = cms.string(''),
    lhcInfoPerLSLabel = cms.string(''),
    opticsLabel = cms.string(''),
    useNewLHCInfo = cms.bool(False)
)


process.ecalSimulationParametersEB = cms.ESProducer("EcalSimParametersESModule",
    appendToDataLabel = cms.string(''),
    fromDD4hep = cms.bool(False),
    name = cms.string('EcalHitsEB')
)


process.ecalSimulationParametersEE = cms.ESProducer("EcalSimParametersESModule",
    appendToDataLabel = cms.string(''),
    fromDD4hep = cms.bool(False),
    name = cms.string('EcalHitsEE')
)


process.ecalSimulationParametersES = cms.ESProducer("EcalSimParametersESModule",
    appendToDataLabel = cms.string(''),
    fromDD4hep = cms.bool(False),
    name = cms.string('EcalHitsES')
)


process.fakeForIdealAlignment = cms.ESProducer("FakeAlignmentProducer",
    appendToDataLabel = cms.string('fakeForIdeal')
)


process.hcalDDDRecConstants = cms.ESProducer("HcalDDDRecConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalDDDSimConstants = cms.ESProducer("HcalDDDSimConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalSimulationConstants = cms.ESProducer("HcalSimulationConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalSimulationParameters = cms.ESProducer("HcalSimParametersESModule",
    appendToDataLabel = cms.string(''),
    fromDD4hep = cms.bool(False)
)


process.hcalTopologyIdeal = cms.ESProducer("HcalTopologyIdealEP",
    Exclude = cms.untracked.string(''),
    MergePosition = cms.untracked.bool(False),
    appendToDataLabel = cms.string('')
)


process.hcal_db_producer = cms.ESProducer("HcalDbProducer",
    dump = cms.untracked.vstring(''),
    file = cms.untracked.string('')
)


process.idealForDigiCSCGeometry = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    debugV = cms.untracked.bool(False),
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.idealForDigiDTGeometry = cms.ESProducer("DTGeometryESModule",
    DDDetector = cms.ESInputTag("",""),
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    attribute = cms.string('MuStructure'),
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(False),
    value = cms.string('MuonBarrelDT')
)


process.idealForDigiTrackerGeometry = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.multipleScatteringParametrisationMakerESProducer = cms.ESProducer("MultipleScatteringParametrisationMakerESProducer",
    appendToDataLabel = cms.string('')
)


process.muonGeometryConstants = cms.ESProducer("MuonGeometryConstantsESModule",
    appendToDataLabel = cms.string(''),
    fromDD4hep = cms.bool(False)
)


process.muonOffsetESProducer = cms.ESProducer("MuonOffsetESProducer",
    appendToDataLabel = cms.string(''),
    fromDD4hep = cms.bool(False),
    names = cms.vstring(
        'MuonCommonNumbering',
        'MuonBarrel',
        'MuonEndcap',
        'MuonBarrelWheels',
        'MuonBarrelStation1',
        'MuonBarrelStation2',
        'MuonBarrelStation3',
        'MuonBarrelStation4',
        'MuonBarrelSuperLayer',
        'MuonBarrelLayer',
        'MuonBarrelWire',
        'MuonRpcPlane1I',
        'MuonRpcPlane1O',
        'MuonRpcPlane2I',
        'MuonRpcPlane2O',
        'MuonRpcPlane3S',
        'MuonRpcPlane4',
        'MuonRpcChamberLeft',
        'MuonRpcChamberMiddle',
        'MuonRpcChamberRight',
        'MuonRpcEndcap1',
        'MuonRpcEndcap2',
        'MuonRpcEndcap3',
        'MuonRpcEndcap4',
        'MuonRpcEndcapSector',
        'MuonRpcEndcapChamberB1',
        'MuonRpcEndcapChamberB2',
        'MuonRpcEndcapChamberB3',
        'MuonRpcEndcapChamberC1',
        'MuonRpcEndcapChamberC2',
        'MuonRpcEndcapChamberC3',
        'MuonRpcEndcapChamberE1',
        'MuonRpcEndcapChamberE2',
        'MuonRpcEndcapChamberE3',
        'MuonRpcEndcapChamberF1',
        'MuonRpcEndcapChamberF2',
        'MuonRpcEndcapChamberF3',
        'MuonEndcapStation1',
        'MuonEndcapStation2',
        'MuonEndcapStation3',
        'MuonEndcapStation4',
        'MuonEndcapSubrings',
        'MuonEndcapSectors',
        'MuonEndcapLayers',
        'MuonEndcapRing1',
        'MuonEndcapRing2',
        'MuonEndcapRing3',
        'MuonEndcapRingA',
        'MuonGEMEndcap',
        'MuonGEMSector',
        'MuonGEMChamber'
    )
)


process.siPixelQualityESProducer = cms.ESProducer("SiPixelQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(
        cms.PSet(
            record = cms.string('SiPixelQualityFromDbRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiPixelDetVOffRcd'),
            tag = cms.string('')
        )
    ),
    appendToDataLabel = cms.string(''),
    siPixelQualityFromDbLabel = cms.string('')
)


process.siStripBackPlaneCorrectionDepESProducer = cms.ESProducer("SiStripBackPlaneCorrectionDepESProducer",
    BackPlaneCorrectionDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    BackPlaneCorrectionPeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    )
)


process.siStripGainESProducer = cms.ESProducer("SiStripGainESProducer",
    APVGain = cms.VPSet(
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGainRcd')
        ),
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGain2Rcd')
        )
    ),
    AutomaticNormalization = cms.bool(False),
    appendToDataLabel = cms.string(''),
    printDebug = cms.untracked.bool(False)
)


process.siStripLorentzAngleDepESProducer = cms.ESProducer("SiStripLorentzAngleDepESProducer",
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    ),
    LorentzAngleDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripLorentzAngleRcd')
    ),
    LorentzAnglePeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripLorentzAngleRcd')
    )
)


process.siStripQualityESProducer = cms.ESProducer("SiStripQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(
        cms.PSet(
            record = cms.string('SiStripDetVOffRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiStripDetCablingRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('RunInfoRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiStripBadChannelRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiStripBadFiberRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiStripBadModuleRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiStripBadStripRcd'),
            tag = cms.string('')
        )
    ),
    PrintDebugOutput = cms.bool(False),
    ReduceGranularity = cms.bool(False),
    ThresholdForReducedGranularity = cms.double(0.3),
    UseEmptyRunInfo = cms.bool(False),
    appendToDataLabel = cms.string('')
)


process.sistripconn = cms.ESProducer("SiStripConnectivity")


process.stripCPEESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('stripCPE'),
    ComponentType = cms.string('SimpleStripCPE'),
    parameters = cms.PSet(

    )
)


process.trackerGeometryDB = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False)
)


process.trackerNumberingGeometryDB = cms.ESProducer("TrackerGeometricDetESModule",
    appendToDataLabel = cms.string(''),
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.trackerTopology = cms.ESProducer("TrackerTopologyEP",
    appendToDataLabel = cms.string('')
)


process.GlobalTag = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        connectionTimeout = cms.untracked.int32(0),
        messageLevel = cms.untracked.int32(0),
        security = cms.untracked.string('')
    ),
    DumpStat = cms.untracked.bool(False),
    ReconnectEachRun = cms.untracked.bool(False),
    RefreshAlways = cms.untracked.bool(False),
    RefreshEachRun = cms.untracked.bool(False),
    RefreshOpenIOVs = cms.untracked.bool(False),
    connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
    globaltag = cms.string('131X_mcRun2_asymptotic_v3'),
    pfnPostfix = cms.untracked.string(''),
    pfnPrefix = cms.untracked.string(''),
    snapshotTime = cms.string(''),
    toGet = cms.VPSet()
)


process.HcalTimeSlewEP = cms.ESSource("HcalTimeSlewEP",
    appendToDataLabel = cms.string('HBHE'),
    timeSlewParametersM2 = cms.VPSet(
        cms.PSet(
            slope = cms.double(-3.178648),
            tmax = cms.double(16.0),
            tzero = cms.double(23.960177)
        ),
        cms.PSet(
            slope = cms.double(-1.5610227),
            tmax = cms.double(10.0),
            tzero = cms.double(11.977461)
        ),
        cms.PSet(
            slope = cms.double(-1.075824),
            tmax = cms.double(6.25),
            tzero = cms.double(9.109694)
        )
    ),
    timeSlewParametersM3 = cms.VPSet(
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        ),
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(15.5),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-3.2),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(32.0),
            tspar2_siPM = cms.double(0.0)
        ),
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        ),
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        )
    )
)


process.eegeom = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalMappingRcd')
)


process.es_hardcode = cms.ESSource("HcalHardcodeCalibrations",
    GainWidthsForTrigPrims = cms.bool(False),
    HBRecalibration = cms.bool(False),
    HBmeanenergies = cms.FileInPath('CalibCalorimetry/HcalPlugins/data/meanenergiesHB.txt'),
    HBreCalibCutoff = cms.double(20.0),
    HERecalibration = cms.bool(False),
    HEmeanenergies = cms.FileInPath('CalibCalorimetry/HcalPlugins/data/meanenergiesHE.txt'),
    HEreCalibCutoff = cms.double(20.0),
    HFRecalParameterBlock = cms.PSet(
        HFdepthOneParameterA = cms.vdouble(
            0.004123, 0.00602, 0.008201, 0.010489, 0.013379,
            0.016997, 0.021464, 0.027371, 0.034195, 0.044807,
            0.058939, 0.125497
        ),
        HFdepthOneParameterB = cms.vdouble(
            -4e-06, -2e-06, 0.0, 4e-06, 1.5e-05,
            2.6e-05, 6.3e-05, 8.4e-05, 0.00016, 0.000107,
            0.000425, 0.000209
        ),
        HFdepthTwoParameterA = cms.vdouble(
            0.002861, 0.004168, 0.0064, 0.008388, 0.011601,
            0.014425, 0.018633, 0.023232, 0.028274, 0.035447,
            0.051579, 0.086593
        ),
        HFdepthTwoParameterB = cms.vdouble(
            -2e-06, -0.0, -7e-06, -6e-06, -2e-06,
            1e-06, 1.9e-05, 3.1e-05, 6.7e-05, 1.2e-05,
            0.000157, -3e-06
        )
    ),
    HFRecalibration = cms.bool(False),
    SiPMCharacteristics = cms.VPSet(
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(36000)
        ),
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(2500)
        ),
        cms.PSet(
            crosstalk = cms.double(0.17),
            nonlin1 = cms.double(1.00985),
            nonlin2 = cms.double(7.84089e-06),
            nonlin3 = cms.double(2.86282e-10),
            pixels = cms.int32(27370)
        ),
        cms.PSet(
            crosstalk = cms.double(0.196),
            nonlin1 = cms.double(1.00546),
            nonlin2 = cms.double(6.40239e-06),
            nonlin3 = cms.double(1.27011e-10),
            pixels = cms.int32(38018)
        ),
        cms.PSet(
            crosstalk = cms.double(0.17),
            nonlin1 = cms.double(1.00985),
            nonlin2 = cms.double(7.84089e-06),
            nonlin3 = cms.double(2.86282e-10),
            pixels = cms.int32(27370)
        ),
        cms.PSet(
            crosstalk = cms.double(0.196),
            nonlin1 = cms.double(1.00546),
            nonlin2 = cms.double(6.40239e-06),
            nonlin3 = cms.double(1.27011e-10),
            pixels = cms.int32(38018)
        ),
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(0)
        )
    ),
    hb = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.19),
        gainWidth = cms.vdouble(0.0),
        mcShape = cms.int32(125),
        noiseCorrelation = cms.vdouble(0.0),
        noiseThreshold = cms.double(0.0),
        pedestal = cms.double(3.285),
        pedestalWidth = cms.double(0.809),
        photoelectronsToAnalog = cms.double(0.3305),
        qieOffset = cms.vdouble(-0.49, 1.8, 7.2, 37.9),
        qieSlope = cms.vdouble(0.912, 0.917, 0.922, 0.923),
        qieType = cms.int32(0),
        recoShape = cms.int32(105),
        seedThreshold = cms.double(0.1),
        zsThreshold = cms.int32(8)
    ),
    hbUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.01, 0.015),
        doRadiationDamage = cms.bool(True),
        gain = cms.vdouble(0.0006252),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(206),
        noiseCorrelation = cms.vdouble(0.26, 0.254),
        noiseThreshold = cms.double(0.0),
        pedestal = cms.double(17.3),
        pedestalWidth = cms.double(1.5),
        photoelectronsToAnalog = cms.double(40.0),
        qieOffset = cms.vdouble(0.0, 0.0, 0.0, 0.0),
        qieSlope = cms.vdouble(0.05376, 0.05376, 0.05376, 0.05376),
        qieType = cms.int32(2),
        radiationDamage = cms.PSet(
            depVsNeutrons = cms.vdouble(5.543e-10, 8.012e-10),
            depVsTemp = cms.double(0.0631),
            intlumiOffset = cms.double(150),
            intlumiToNeutrons = cms.double(367000000.0),
            temperatureBase = cms.double(20),
            temperatureNew = cms.double(-5)
        ),
        recoShape = cms.int32(208),
        seedThreshold = cms.double(0.1),
        zsThreshold = cms.int32(16)
    ),
    he = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.23),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(125),
        noiseCorrelation = cms.vdouble(0.0),
        noiseThreshold = cms.double(0.0),
        pedestal = cms.double(3.163),
        pedestalWidth = cms.double(0.9698),
        photoelectronsToAnalog = cms.double(0.3305),
        qieOffset = cms.vdouble(-0.38, 2.0, 7.6, 39.6),
        qieSlope = cms.vdouble(0.912, 0.916, 0.92, 0.922),
        qieType = cms.int32(0),
        recoShape = cms.int32(105),
        seedThreshold = cms.double(0.1),
        zsThreshold = cms.int32(9)
    ),
    heUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.01, 0.015),
        doRadiationDamage = cms.bool(True),
        gain = cms.vdouble(0.0006252),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(206),
        noiseCorrelation = cms.vdouble(0.26, 0.254),
        noiseThreshold = cms.double(0.0),
        pedestal = cms.double(17.3),
        pedestalWidth = cms.double(1.5),
        photoelectronsToAnalog = cms.double(40.0),
        qieOffset = cms.vdouble(0.0, 0.0, 0.0, 0.0),
        qieSlope = cms.vdouble(0.05376, 0.05376, 0.05376, 0.05376),
        qieType = cms.int32(2),
        radiationDamage = cms.PSet(
            depVsNeutrons = cms.vdouble(5.543e-10, 8.012e-10),
            depVsTemp = cms.double(0.0631),
            intlumiOffset = cms.double(75),
            intlumiToNeutrons = cms.double(29200000.0),
            temperatureBase = cms.double(20),
            temperatureNew = cms.double(5)
        ),
        recoShape = cms.int32(208),
        seedThreshold = cms.double(0.1),
        zsThreshold = cms.int32(16)
    ),
    hf = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.14, 0.135),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(301),
        noiseCorrelation = cms.vdouble(0.0),
        noiseThreshold = cms.double(0.0),
        pedestal = cms.double(9.354),
        pedestalWidth = cms.double(2.516),
        photoelectronsToAnalog = cms.double(0.0),
        qieOffset = cms.vdouble(-0.87, 1.4, 7.8, -29.6),
        qieSlope = cms.vdouble(0.359, 0.358, 0.36, 0.367),
        qieType = cms.int32(0),
        recoShape = cms.int32(301),
        seedThreshold = cms.double(0.1),
        zsThreshold = cms.int32(-9999)
    ),
    hfUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.14, 0.135),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(301),
        noiseCorrelation = cms.vdouble(0.0),
        noiseThreshold = cms.double(0.0),
        pedestal = cms.double(13.33),
        pedestalWidth = cms.double(3.33),
        photoelectronsToAnalog = cms.double(0.0),
        qieOffset = cms.vdouble(0.0697, -0.7405, 12.38, -671.9),
        qieSlope = cms.vdouble(0.297, 0.298, 0.298, 0.313),
        qieType = cms.int32(1),
        recoShape = cms.int32(301),
        seedThreshold = cms.double(0.1),
        zsThreshold = cms.int32(-9999)
    ),
    ho = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.006, 0.0087),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(201),
        noiseCorrelation = cms.vdouble(0.0),
        noiseThreshold = cms.double(0.0),
        pedestal = cms.double(12.06),
        pedestalWidth = cms.double(0.6285),
        photoelectronsToAnalog = cms.double(4.0),
        qieOffset = cms.vdouble(-0.44, 1.4, 7.1, 38.5),
        qieSlope = cms.vdouble(0.907, 0.915, 0.92, 0.921),
        qieType = cms.int32(0),
        recoShape = cms.int32(201),
        seedThreshold = cms.double(0.1),
        zsThreshold = cms.int32(24)
    ),
    iLumi = cms.double(-1.0),
    killHE = cms.bool(False),
    testHEPlan1 = cms.bool(False),
    testHFQIE10 = cms.bool(False),
    toGet = cms.untracked.vstring('GainWidths'),
    useHBUpgrade = cms.bool(False),
    useHEUpgrade = cms.bool(False),
    useHFUpgrade = cms.bool(False),
    useHOUpgrade = cms.bool(True),
    useIeta18depth1 = cms.bool(True),
    useLayer0Weight = cms.bool(False)
)


process.prefer("es_hardcode")

process.egmGsfElectronIDTask = cms.Task(process.egmGsfElectronIDs, process.electronMVAValueMapProducer)


process.gedGsfElectronTaskTmp = cms.Task(process.gedGsfElectronCores, process.gedGsfElectronValueMapsTmp, process.gedGsfElectronsTmp)


process.endOfProcess = cms.Sequence(process.MEtoEDMConverter)


process.egmGsfElectronIDSequence = cms.Sequence(process.egmGsfElectronIDTask)


process.p = cms.Path(process.gsfElectronsDRN+process.egmGsfElectronIDSequence+process.nTuplelize)


process.schedule = cms.Schedule(*[ process.p ])
