import FWCore.ParameterSet.Config as cms
from GeneratorInterface.EvtGenInterface.EvtGenSetting_cff import *

generator = cms.EDFilter("Pythia8PtGun",
                         ExternalDecays = cms.PSet(
        EvtGen130 = cms.untracked.PSet(
            decay_table = cms.string('GeneratorInterface/EvtGenInterface/data/DECAY_2010.DEC'),
            particle_property_file = cms.FileInPath('GeneratorInterface/EvtGenInterface/data/evt.pdl'),
            user_decay_file        = cms.vstring('GeneratorInterface/ExternalDecays/data/Onia_chic_jpsigamma.dec'),
            list_forced_decays     = cms.vstring('Mychi_c1'),
            operates_on_particles = cms.vint32(20443)
            ),
        parameterSets = cms.vstring('EvtGen130')
        ),
        PGunParameters = cms.PSet(
            ParticleID = cms.vint32(20443),
            AddAntiParticle = cms.bool(False),
            MinPhi = cms.double(-3.14159265359),
            MaxPhi = cms.double(3.14159265359),
            MinPt = cms.double(0.0),
            MaxPt = cms.double(50.0),
            MinEta = cms.double(-3.0),
            MaxEta = cms.double(3.0)
        ),
        PythiaParameters = cms.PSet(parameterSets = cms.vstring())
)

# Next two muon filter are derived from muon reconstruction

oniafilter = cms.EDFilter("MCParticlePairFilter",
    Status = cms.untracked.vint32(2, 1),
    MinPt = cms.untracked.vdouble(0.0, 0.2),
    MaxEta = cms.untracked.vdouble(10.0, 2.5),
    MinEta = cms.untracked.vdouble(-10.0, -2.5),
    ParticleCharge = cms.untracked.int32(0),
    MinP = cms.untracked.vdouble(0.,0.),
    ParticleID1 = cms.untracked.vint32(443),
    ParticleID2 = cms.untracked.vint32(22),
    BetaBoost = cms.untracked.double(i-0.434)
)

mumugenfilter = cms.EDFilter("MCParticlePairFilter",
    Status = cms.untracked.vint32(1, 1),
    MinPt = cms.untracked.vdouble(0.7, 0.7),
    MinP = cms.untracked.vdouble(2.5, 2.5),
    MaxEta = cms.untracked.vdouble(2.5, 2.5),
    MinEta = cms.untracked.vdouble(-2.5, -2.5),
    ParticleCharge = cms.untracked.int32(-1),
    ParticleID1 = cms.untracked.vint32(13),
    ParticleID2 = cms.untracked.vint32(13),
    BetaBoost = cms.untracked.double(-0.434)
)

ProductionFilterSequence = cms.Sequence(generator*oniafilter*mumugenfilter)
