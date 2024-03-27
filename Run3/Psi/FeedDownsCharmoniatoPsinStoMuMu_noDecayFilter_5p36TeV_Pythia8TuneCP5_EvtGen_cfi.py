# "inclusive" psi production, i.e. simulating all feed-downs to the J/psi and psi(2S) states

# from BPH MC fragments

# ------------------------------------
# GenXsecAnalyzer:
# ------------------------------------
# Before Filter: total cross section = 9.076e+07 +- 1.547e+05 pb
# Filter efficiency (taking into account weights)= (27960) / (100000) = 2.796e-01 +- 1.419e-03
# Filter efficiency (event-level)= (27960) / (100000) = 2.796e-01 +- 1.419e-03    [TO BE USED IN MCM]

# After filter: final cross section = 2.538e+07 +- 1.359e+05 pb
# After filter: final fraction of events with negative weights = 0.000e+00 +- 0.000e+00
# After filter: final equivalent lumi for 1M events (1/fb) = 3.941e-05 +- 2.146e-07

# 0.029 sec/event, 43 kB/event

import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunesRun3ECM13p6TeV.PythiaCP5Settings_cfi import *
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

generator.PythiaParameters.processParameters.extend(EvtGenExtraParticles)


oniafilter = cms.EDFilter("MCMultiParticleFilter",
     Status = cms.vint32(2, 2),
     ParticleID = cms.vint32(443,100443),
     NumRequired = cms.int32(1),
     EtaMax = cms.vdouble(9999, 9999),
     EtaMin = cms.vdouble(-9999, -9999),
     PtMin = cms.vdouble(0.0, 0.0),
     AcceptMore = cms.bool(True)
)

ProductionFilterSequence = cms.Sequence(generator*oniafilter)
