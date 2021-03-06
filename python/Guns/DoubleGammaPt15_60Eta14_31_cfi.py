import FWCore.ParameterSet.Config as cms

generator = cms.EDProducer("FlatRandomPtGunProducer",
    PGunParameters = cms.PSet(
        MaxPt = cms.double(60.0),
        MinPt = cms.double(15.0),
        PartID = cms.vint32(22),
        MaxEta = cms.double(3.1),
        MaxPhi = cms.double(3.14159265359),
        MinEta = cms.double(1.4),
        MinPhi = cms.double(-3.14159265359) ## in radians

    ),
    Verbosity = cms.untracked.int32(0), ## set to 1 (or greater)  for printouts

    psethack = cms.string('single gamma pt 15 - 60'),
    AddAntiParticle = cms.bool(True),
    firstRun = cms.untracked.uint32(1)
)

