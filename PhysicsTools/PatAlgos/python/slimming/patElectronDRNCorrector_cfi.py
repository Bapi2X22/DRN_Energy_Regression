import FWCore.ParameterSet.Config as cms

from RecoEgamma.EgammaTools.gsfElectronDRNCorrectionProducer_cfi import gsfElectronDRNCorrectionProducer

patElectronsDRN = gsfElectronDRNCorrectionProducer.clone(
                            particleSource = 'gedGsfElectrons',
                            rhoName = 'fixedGridRhoFastjetAll',
                            Client = gsfElectronDRNCorrectionProducer.Client.clone(
                              mode = 'Async',
                              allowedTries = 1,
                              modelName = 'photonObjectCombined',
                              modelConfigPath = 'RecoEgamma/EgammaElectronProducers/data/models/photonObjectCombined/config.pbtxt',
                              timeout = 10
                            )
    )
