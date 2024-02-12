# "inclusive" upsilon production, i.e. simulating all feed-downs to the three states

# from BPH MC fragments

# ------------------------------------
# GenXsecAnalyzer:
# ------------------------------------
# Before Filter: total cross section = 1.861e+06 +- 4.301e+03 pb
# Filter efficiency (taking into account weights)= (174) / (50000) = 3.480e-03 +- 2.634e-04
# Filter efficiency (event-level)= (174) / (50000) = 3.480e-03 +- 2.634e-04    [TO BE USED IN MCM]

# After filter: final cross section = 6.475e+03 +- 4.903e+02 pb
# After filter: final fraction of events with negative weights = 0.000e+00 +- 0.000e+00
# After filter: final equivalent lumi for 1M events (1/fb) = 1.544e-01 +- 1.169e-02

# 0.023 sec/event, 316 kB/event

import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *
from GeneratorInterface.EvtGenInterface.EvtGenSetting_cff import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
                         pythiaPylistVerbosity = cms.untracked.int32(0),
                         pythiaHepMCVerbosity = cms.untracked.bool(False),
                         comEnergy = cms.double(5362.0),
                         maxEventsToPrint = cms.untracked.int32(0),
                         ExternalDecays = cms.PSet(
                         EvtGen200 = cms.untracked.PSet(
                             decay_table = cms.string('GeneratorInterface/EvtGenInterface/data/DECAY_2020.DEC'),
                             particle_property_file = cms.FileInPath('GeneratorInterface/EvtGenInterface/data/evt.pdl'),
                             user_decay_file = cms.vstring('GeneratorInterface/ExternalDecays/data/Onia_mumu.dec'),
                             list_forced_decays = cms.vstring('MyUpsilon','MyUpsilon(2S)','MyUpsilon(3S)'),
                             operates_on_particles = cms.vint32(553,100553,200553),
                             convertPythiaCodes = cms.untracked.bool(False)
                             ),
                        parameterSets = cms.vstring('EvtGen200')
                        ),
                        PythiaParameters = cms.PSet(
                            pythia8CommonSettingsBlock,
                            pythia8CP5SettingsBlock,
                            processParameters = cms.vstring(
                            'Bottomonium:all = on',                # Quarkonia, MSEL=62, allow feed-downs
                            'PhaseSpace:pTHatMin = 2.0'
                            ),
                        parameterSets = cms.vstring('pythia8CommonSettings',
                            'pythia8CP5Settings',
                            'processParameters',
                            )
        ),

)

generator.PythiaParameters.processParameters.extend(EvtGenExtraParticles)


oniafilter = cms.EDFilter("MCMultiParticleFilter",
     Status = cms.vint32(2, 2, 2),
     ParticleID = cms.vint32(553,100553,200553),
     NumRequired = cms.int32(1),
     EtaMax = cms.vdouble(100, 100, 100),
     EtaMin = cms.vdouble(-100, -100, -100),
     PtMin = cms.vdouble(0.0, 0.0, 0.0),
     AcceptMore = cms.bool(True)
)

mumugenfilter = cms.EDFilter("MCParticlePairFilter",
    Status = cms.untracked.vint32(1, 1),
    MinPt = cms.untracked.vdouble(2.5, 2.5),
    MinP = cms.untracked.vdouble(2.5, 2.5),
    MaxEta = cms.untracked.vdouble(2.5, 2.5),
    MinEta = cms.untracked.vdouble(-2.5, -2.5),
    ParticleCharge = cms.untracked.int32(-1),
    ParticleID1 = cms.untracked.vint32(13),
    ParticleID2 = cms.untracked.vint32(13)
)

ProductionFilterSequence = cms.Sequence(generator*oniafilter*mumugenfilter)
