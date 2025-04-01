# "inclusive" psi production, i.e. simulating all feed-downs to the J/psi and psi(2S) states

# from BPH MC fragments

# ------------------------------------
# GenXsecAnalyzer:
# ------------------------------------
# Before Filter: total cross section = 9.074e+07 +- 2.192e+05 pb
# Filter efficiency (taking into account weights)= (131) / (50000) = 2.620e-03 +- 2.286e-04
# Filter efficiency (event-level)= (131) / (50000) = 2.620e-03 +- 2.286e-04    [TO BE USED IN MCM]

# After filter: final cross section = 2.377e+05 +- 2.075e+04 pb
# After filter: final fraction of events with negative weights = 0.000e+00 +- 0.000e+00
# After filter: final equivalent lumi for 1M events (1/fb) = 4.206e-03 +- 3.672e-04

# 0.018 sec/event, 267 kB/event

import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunesRun3ECM13p6TeV.PythiaCP5Settings_cfi import *
from GeneratorInterface.EvtGenInterface.EvtGenSetting_cff import *

_generator = cms.EDFilter("Pythia8GeneratorFilter",
                         pythiaPylistVerbosity = cms.untracked.int32(0),
                         pythiaHepMCVerbosity = cms.untracked.bool(False),
                         comEnergy = cms.double(5362.0),
                         maxEventsToPrint = cms.untracked.int32(0),
                         ExternalDecays = cms.PSet(
                         EvtGen200 = cms.untracked.PSet(
                             decay_table = cms.string('GeneratorInterface/EvtGenInterface/data/DECAY_2020.DEC'),
                             particle_property_file = cms.FileInPath('GeneratorInterface/EvtGenInterface/data/evt.pdl'),
                             user_decay_file = cms.vstring('GeneratorInterface/ExternalDecays/data/Onia_mumu.dec'),
                             list_forced_decays = cms.vstring('MyJ/psi','Mypsi(2S)'),
                             operates_on_particles = cms.vint32(443,100443),
                             convertPythiaCodes = cms.untracked.bool(False)
                             ),
                        parameterSets = cms.vstring('EvtGen200')
                        ),
                        PythiaParameters = cms.PSet(
                            pythia8CommonSettingsBlock,
                            pythia8CP5SettingsBlock,
                            processParameters = cms.vstring(
                            'Charmonium:all = on',                # Quarkonia, MSEL=62, allow feed-down
                            'PhaseSpace:pTHatMin = 2.0'
                            ),
                        parameterSets = cms.vstring('pythia8CommonSettings',
                            'pythia8CP5Settings',
                            'processParameters',
                            )
        ),

)

from GeneratorInterface.Core.ExternalGeneratorFilter import ExternalGeneratorFilter
generator = ExternalGeneratorFilter(_generator)

generator.PythiaParameters.processParameters.extend(EvtGenExtraParticles)

# Filters

oniafilter = cms.EDFilter("MCMultiParticleFilter",
     Status = cms.vint32(2, 2),
     ParticleID = cms.vint32(443,100443),
     NumRequired = cms.int32(1),
     EtaMax = cms.vdouble(100, 100),
     EtaMin = cms.vdouble(-100, -100),
     PtMin = cms.vdouble(0.0, 0.0),
     AcceptMore = cms.bool(True)
)

mumugenfilter = cms.EDFilter("MCParticlePairFilter",
    Status = cms.untracked.vint32(1, 1),
    MinPt = cms.untracked.vdouble(0.5, 0.5),
    MinP = cms.untracked.vdouble(2.5, 2.5),
    MaxEta = cms.untracked.vdouble(2.5, 2.5),
    MinEta = cms.untracked.vdouble(-2.5, -2.5),
    ParticleCharge = cms.untracked.int32(-1),
    ParticleID1 = cms.untracked.vint32(13),
    ParticleID2 = cms.untracked.vint32(13)
)

ProductionFilterSequence = cms.Sequence(generator*oniafilter*mumugenfilter)
