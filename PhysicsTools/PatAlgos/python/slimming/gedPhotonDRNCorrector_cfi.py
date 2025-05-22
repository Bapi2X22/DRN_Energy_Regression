import FWCore.ParameterSet.Config as cms

from RecoEgamma.EgammaTools.gedPhotonDRNCorrectionProducer_cfi import gedPhotonDRNCorrectionProducer
print("Started patPhotonsDRN module")
gedPhotonsDRN = gedPhotonDRNCorrectionProducer.clone(
                            particleSource = 'gedPhotons',
                            rhoName = 'fixedGridRhoFastjetAll',
                            Client = gedPhotonDRNCorrectionProducer.Client.clone(
                              mode = 'Async',
                              allowedTries = 1,
                              modelName = 'photonObjectCombined',
                              modelConfigPath = 'RecoEgamma/EgammaPhotonProducers/data/models/photonObjectCombined/config.pbtxt',
                              timeout = 10
                            )
    )
import os
full_model_config_path = os.popen('edmFileInPath RecoEgamma/EgammaPhotonProducers/data/models/photonObjectCombined/config.pbtxt').read().strip()

print("Full Model Config Path:", full_model_config_path)
