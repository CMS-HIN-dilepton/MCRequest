import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunesRun3ECM13p6TeV.PythiaCP5Settings_cfi import *

# ------------------------------------
# GenXsecAnalyzer:
# ------------------------------------
# Before Filter: total cross section = 3.342e+03 +- 1.759e+01 pb
# Filter efficiency (taking into account weights)= (1164) / (10000) = 1.164e-01 +- 3.207e-03
# Filter efficiency (event-level)= (1164) / (10000) = 1.164e-01 +- 3.207e-03    [TO BE USED IN MCM]

# After filter: final cross section = 3.890e+02 +- 1.091e+01 pb
# After filter: final fraction of events with negative weights = 0.000e+00 +- 0.000e+00
# After filter: final equivalent lumi for 1M events (1/fb) = 2.571e+00 +- 7.215e-02

# 0.386 sec / event, 300 kB /event

generator = cms.EDFilter("Pythia8GeneratorFilter",
                         maxEventsToPrint = cms.untracked.int32(0),
                         pythiaPylistVerbosity = cms.untracked.int32(0),
                         comEnergy = cms.double(5362.0),
                         PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP5SettingsBlock,
        processParameters = cms.vstring(
            'WeakSingleBoson:ffbar2gmZ = on',
            '23:onMode = off',
            '23:onIfAny = 13',
            ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CP5Settings',
                                    'processParameters',
                                    )
        )
)

mumugenfilter = cms.EDFilter("MCParticlePairFilter",
    Status         = cms.untracked.vint32(1, 1),
    MinPt          = cms.untracked.vdouble(10, 10),
    MaxEta         = cms.untracked.vdouble(2.5, 2.5),
    MinEta         = cms.untracked.vdouble(-2.5, -2.5),
    MinInvMass     = cms.untracked.double(60.0),
    MaxInvMass     = cms.untracked.double(120.0),
    ParticleCharge = cms.untracked.int32(-1),
    ParticleID1    = cms.untracked.vint32(13),
    ParticleID2    = cms.untracked.vint32(13)
)

ProductionFilterSequence = cms.Sequence(generator*mumugenfilter)
