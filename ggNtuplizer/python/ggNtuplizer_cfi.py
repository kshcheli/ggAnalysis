import FWCore.ParameterSet.Config as cms

from HiggsAnalysis.HiggsTo2photons.hggPhotonIDCuts_cfi import *
from CMGTools.External.pujetidproducer_cfi import stdalgos, chsalgos
from PhysicsTools.SelectorUtils.pfJetIDSelector_cfi import pfJetIDSelector

ggNtuplizer = cms.EDProducer("ggNtuplizer",
                             hggPhotonIDConfiguration = hggPhotonIDCuts,
                             doGenParticles = cms.bool(True),
                             doSkim = cms.bool(False),
                             dumpESHits = cms.bool(False),
                             dumpESClusterInfo = cms.bool(False),
                             dumpTrks = cms.bool(True),
                             dumpJets = cms.bool(True),
                             runOnParticleGun = cms.bool(False),
                             development=cms.bool(False),
                             doCentrality=cms.bool(False),
                             METSrc = cms.InputTag("patMETs"),
                             pfMETLabel = cms.InputTag("patMETsPF"),
                             recoPfMETLabel = cms.InputTag("pfMet"),
                             #electronSrc = cms.InputTag("cleanPatElectrons"),
                             #electronSrc = cms.InputTag("eleRegressionEnergy"),
                             electronSrc = cms.InputTag("calibratedPatElectrons"),
                             photonSrc = cms.InputTag("cleanPatPhotons"),
                             Photons = cms.InputTag("photons"),
                             muonSrc = cms.InputTag("cleanPatMuons"),
                             jetSrc = cms.InputTag("cleanPatJets"),
                             genParticleSrc = cms.InputTag("genParticles"),
                             PFAllCandidates=cms.InputTag("particleFlow"),
                             PFCandidates=cms.InputTag("pfNoPileUpIso"),
                             PFCandidatePhotons=cms.InputTag("pfSelectedPhotons"),
                             triggerResults = cms.InputTag("TriggerResults::REDIGI36X"),
                             triggerEvent = cms.InputTag("patTriggerEvent"),
                             VtxLabel = cms.InputTag("offlinePrimaryVertices"),
                             TrackLabel = cms.InputTag("generalTracks"),
                             gsfElectronLabel = cms.InputTag("gsfElectrons"),
                             ebReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsEB"),
                             eeReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsEE"),
                             esRecHitCollection = cms.InputTag("reducedEcalRecHitsES"),
                             towerCollection = cms.InputTag("towerMaker"),
                             BeamSpotCollection = cms.InputTag("offlineBeamSpot"),
                             pileupCollection = cms.InputTag("addPileupInfo"),
                             rhoCollectionLepPFiso = cms.InputTag("kt6PFJetsCentralNeutral:rho"),
                             rhoCollection25 = cms.InputTag("kt6PFJets25:rho"),
                             rhoCollection25_neu = cms.InputTag("kt6PFJets25Neu:rho"),                             
                             rhoCollection44 = cms.InputTag("kt6PFJets44:rho"),
			     rho2011Label = cms.InputTag("kt6PFJetsForIsolation", "rho"),
                             ConvertedPhotonColl = cms.InputTag("allConversions"), # 42X
                             #ConvertedPhotonColl = cms.InputTag("trackerOnlyConversions"),
                             #PFElectrons = cms.InputTag("pfElectronTranslator:pf"),
                             PFPhotons = cms.InputTag("pfPhotonTranslator:pfphot"),
                             IsoDepElectron = cms.VInputTag(cms.InputTag('elPFIsoDepositChargedPFIso'),
                                                            cms.InputTag('elPFIsoDepositNeutralPFIso'),
                                                            cms.InputTag('elPFIsoDepositGammaPFIso')),
                             IsoValElectronPF = cms.VInputTag(cms.InputTag('elPFIsoValueCharged03PFIdPFIso'),
                                                              cms.InputTag('elPFIsoValueGamma03PFIdPFIso'),
                                                              cms.InputTag('elPFIsoValueNeutral03PFIdPFIso'),
                                                              cms.InputTag('elPFIsoValueCharged04PFIdPFIso'),
                                                              cms.InputTag('elPFIsoValueGamma04PFIdPFIso'),
                                                              cms.InputTag('elPFIsoValueNeutral04PFIdPFIso')),
                             IsoDepPhoton = cms.VInputTag(cms.InputTag('phPFIsoDepositChargedPFIso'),
                                                          cms.InputTag('phPFIsoDepositNeutralPFIso'),
                                                          cms.InputTag('phPFIsoDepositGammaPFIso')),
                             IsoValPhoton = cms.VInputTag(cms.InputTag('phPFIsoValueCharged03PFIdPFIso'),
                                                          cms.InputTag('phPFIsoValueNeutral03PFIdPFIso'),
                                                          cms.InputTag('phPFIsoValueGamma03PFIdPFIso')),
                             #photonCore=cms.InputTag("photonCore"),
                             gsfEleCore=cms.InputTag("gsfElectronCores"),
			     PhotonIsoDeposits = cms.VInputTag(cms.InputTag('isoDepPhotonWithCharged'),
                                                               cms.InputTag('isoDepPhotonWithPhotons'),
                                                               cms.InputTag('isoDepPhotonWithNeutral')),
                             puJetIDAlgos = cms.untracked.VPSet(stdalgos),
                             pfLooseId = pfJetIDSelector.clone(),
                             CaloTowerColl = cms.InputTag("towerMaker")

                             )

