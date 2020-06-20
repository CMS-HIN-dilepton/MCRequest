import FWCore.ParameterSet.Config as cms
from GeneratorInterface.EvtGenInterface.EvtGenSetting_cff import *

generator = cms.EDFilter("Pythia8PtGun",
                         ExternalDecays = cms.PSet(
        EvtGen130 = cms.untracked.PSet(
            decay_table = cms.string('GeneratorInterface/EvtGenInterface/data/DECAY_2010.DEC'),
            particle_property_file = cms.FileInPath('GeneratorInterface/EvtGenInterface/data/evt.pdl'),
            user_decay_embedded    = cms.vstring(
"""
Particle Upsilon 9.4603000 0.00005402
Particle chi_b1 9.8927800 0.00000
Particle chi_b2 9.9122100 0.00000

Alias myUpsilon Upsilon
Alias mychi_b1 chi_b1
Alias mychi_b2 chi_b2

Decay myUpsilon
1.0   mu+  mu-          PHOTOS  VLL;
Enddecay

Decay mychi_b1
1.0   gamma  myUpsilon  HELAMP 1. 0. 1. 0. -1. 0. -1. 0.;
Enddecay

Decay mychi_b2
1.0   gamma  myUpsilon  PHSP;
Enddecay

End
"""
            ),
            list_forced_decays     = cms.vstring('mychi_b2'),
            operates_on_particles = cms.vint32(555)
            ),
        parameterSets = cms.vstring('EvtGen130')
        ),
        PGunParameters = cms.PSet(
            ParticleID = cms.vint32(555),
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

pwaveIDfilter = cms.EDFilter("MCSingleParticleFilter",
    ParticleID = cms.untracked.vint32(555),
    MinPt = cms.untracked.vdouble(0.0, 0.0),
    MinEta = cms.untracked.vdouble(-9., -9.),
    MaxEta = cms.untracked.vdouble(9., 9.),
    Status = cms.untracked.vint32(2, 2)
)

pwaveMassfilter = cms.EDFilter("MCParticlePairFilter",
    Status = cms.untracked.vint32(2, 1),
    MinPt = cms.untracked.vdouble(0.0, 0.2),
    MaxEta = cms.untracked.vdouble(10.0, 2.5),
    MinEta = cms.untracked.vdouble(-10.0, -2.5),
    ParticleCharge = cms.untracked.int32(0),
    MinP = cms.untracked.vdouble(0.,0.),
    ParticleID1 = cms.untracked.vint32(553),
    ParticleID2 = cms.untracked.vint32(22),
    MinInvMass = cms.untracked.double(9.88),
    MaxInvMass = cms.untracked.double(9.93),
    BetaBoost = cms.untracked.double(-0.434)
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

ProductionFilterSequence = cms.Sequence(generator*pwaveIDfilter*pwaveMassfilter*mumugenfilter)
