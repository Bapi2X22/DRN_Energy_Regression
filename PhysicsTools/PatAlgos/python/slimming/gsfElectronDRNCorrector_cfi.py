import FWCore.ParameterSet.Config as cms

from RecoEgamma.EgammaTools.gsfElectronDRNCorrectionProducer_cfi import gsfElectronDRNCorrectionProducer

print("Started patPhotonsDRN module")

gsfElectronsDRN = gsfElectronDRNCorrectionProducer.clone(
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

import os
full_model_config_path = os.popen('edmFileInPath RecoEgamma/EgammaElectronProducers/data/models/photonObjectCombined/config.pbtxt').read().strip()

print("Full Model Config Path:", full_model_config_path)
