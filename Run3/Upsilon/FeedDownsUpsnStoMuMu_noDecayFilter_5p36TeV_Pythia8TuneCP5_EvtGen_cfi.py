# "inclusive" upsilon production, i.e. simulating all feed-downs to the three states

# from BPH MC fragments

# ------------------------------------
# GenXsecAnalyzer:
# ------------------------------------
# Before Filter: total cross section = 1.864e+06 +- 9.650e+03 pb
# Filter efficiency (taking into account weights)= (2861) / (10000) = 2.861e-01 +- 4.519e-03
# Filter efficiency (event-level)= (2861) / (10000) = 2.861e-01 +- 4.519e-03    [TO BE USED IN MCM]

# After filter: final cross section = 5.332e+05 +- 8.864e+03 pb
# After filter: final fraction of events with negative weights = 0.000e+00 +- 0.000e+00
# After filter: final equivalent lumi for 1M events (1/fb) = 1.875e-03 +- 3.123e-05

# 0.030 sec/event, 50 kB/event

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
     EtaMax = cms.vdouble(9999, 9999, 9999),
     EtaMin = cms.vdouble(-9999, -9999, -9999),
     PtMin = cms.vdouble(0.0, 0.0, 0.0),
     AcceptMore = cms.bool(True)
)

ProductionFilterSequence = cms.Sequence(generator*oniafilter)
