import FWCore.ParameterSet.Config as cms

defaultMuonParameters = cms.PSet(
    muChargeLabel                   = cms.InputTag("muons", "muCharge"), 
    muD0Label                       = cms.InputTag("muons", "muD0"), 
    muD0errLabel                    = cms.InputTag("muons", "muD0err"), 
    muDxyLabel                      = cms.InputTag("muons", "muDxy"), 
    muDxyerrLabel                   = cms.InputTag("muons", "muDxyerr"), 
    muDzLabel                       = cms.InputTag("muons", "muDz"), 
    muDzerrLabel                    = cms.InputTag("muons", "muDzerr"), 
    muELabel                        = cms.InputTag("muons", "muE"), 
    muEtaLabel                      = cms.InputTag("muons", "muEta"), 
    muGenMuonChargeLabel            = cms.InputTag("muons", "muGenMuonCharge"), 
    muGenMuonELabel                 = cms.InputTag("muons", "muGenMuonE"), 
    muGenMuonEtaLabel               = cms.InputTag("muons", "muGenMuonEta"), 
    muGenMuonPhiLabel               = cms.InputTag("muons", "muGenMuonPhi"), 
    muGenMuonPtLabel                = cms.InputTag("muons", "muGenMuonPt"), 
    muGenMuonYLabel                 = cms.InputTag("muons", "muGenMuonY"), 
    muGlbTrkNormChi2Label           = cms.InputTag("muons", "muGlbTrkNormChi2"), 
    muInTrkNormChi2Label            = cms.InputTag("muons", "muInTrkNormChi2"), 
    muIsGlobalMuonLabel             = cms.InputTag("muons", "muIsGlobalMuon"), 
    muIsLooseMuonLabel              = cms.InputTag("muons", "muIsLooseMuon"), 
    muIsPFMuonLabel                 = cms.InputTag("muons", "muIsPFMuon"), 
    muIsSoftMuonLabel               = cms.InputTag("muons", "muIsSoftMuon"), 
    muIsTightMuonLabel              = cms.InputTag("muons", "muIsTightMuon"), 
    muIsTrackerMuonLabel            = cms.InputTag("muons", "muIsTrackerMuon"), 
    muIso04Label                    = cms.InputTag("muons", "muIso04"), 
    muKeyLabel                      = cms.InputTag("muons", "muKey"), 
    muNumberMatchedStationsLabel    = cms.InputTag("muons", "muNumberMatchedStations"), 
    muNumberOfPixelLayersLabel      = cms.InputTag("muons", "muNumberOfPixelLayers"), 
    muNumberOfValidTrackerHitsLabel = cms.InputTag("muons", "muNumberOfValidTrackerHits"), 
    muNumberTrackerLayersLabel      = cms.InputTag("muons", "muNumberTrackerLayers"), 
    muNumberValidMuonHitsLabel      = cms.InputTag("muons", "muNumberValidMuonHits"), 
    muNumberValidPixelHitsLabel     = cms.InputTag("muons", "muNumberValidPixelHits"), 
    muPhiLabel                      = cms.InputTag("muons", "muPhi"), 
    muPtLabel                       = cms.InputTag("muons", "muPt"), 
    muSumChargedHadronPtLabel       = cms.InputTag("muons", "muSumChargedHadronPt"), 
    muSumNeutralHadronPtLabel       = cms.InputTag("muons", "muSumNeutralHadronPt"), 
    muSumPUPtLabel                  = cms.InputTag("muons", "muSumPUPt"), 
    muSumPhotonPtLabel              = cms.InputTag("muons", "muSumPhotonPt"), 
    muYLabel                        = cms.InputTag("muons", "muY"),
    )
