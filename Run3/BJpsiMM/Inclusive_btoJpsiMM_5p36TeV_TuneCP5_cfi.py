import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *
from GeneratorInterface.EvtGenInterface.EvtGenSetting_cff import *

# fragment more "inclusive" in terms of decays from b hadrons, inspired from BPH's MC request https://its.cern.ch/jira/projects/CMSBPHMC/issues/CMSBPHMC-40?filter=allopenissues

# CAVEAT: very low efficiency!!! 10^-4

_generator = cms.EDFilter("Pythia8GeneratorFilter",
    pythiaPylistVerbosity = cms.untracked.int32(0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    maxEventsToPrint = cms.untracked.int32(0),
    comEnergy = cms.double(5362.0),
    ExternalDecays = cms.PSet(
        EvtGen200 = cms.untracked.PSet(
            decay_table = cms.string('GeneratorInterface/EvtGenInterface/data/DECAY_2020.DEC'),
            particle_property_file = cms.FileInPath('GeneratorInterface/EvtGenInterface/data/evt.pdl'),
            operates_on_particles = cms.vint32(),
            convertPythiaCodes = cms.untracked.bool(False),
            list_forced_decays = cms.vstring('MyJpsi'),
            user_decay_embedded = cms.vstring(
            """
            Particle   J/psi         3.0969000e+00   9.2600000e-05

            Alias      MyJpsi J/psi
            ChargeConj MyJpsi  MyJpsi

            Decay MyJpsi
            1.000    mu+    mu-     PHOTOS VLL;
            Enddecay
            End
            """
            )
        ),
        parameterSets = cms.vstring('EvtGen200')
    ),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP5SettingsBlock,
        processParameters = cms.vstring(
           'SoftQCD:nonDiffractive = on',
           'PTFilter:filter = on', # this turn on the filter
           'PTFilter:quarkToFilter = 5', # PDG id of q quark
           'PTFilter:scaleToFilter = 1.0'

            ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CP5Settings',
                                    'processParameters',
                                    )
    )
)


from GeneratorInterface.Core.ExternalGeneratorFilter import ExternalGeneratorFilter
generator = ExternalGeneratorFilter(_generator)

generator.PythiaParameters.processParameters.extend(EvtGenExtraParticles)


###########
# Filters #
###########

jpsifilter = cms.EDFilter(
    "PythiaDauVFilter",
    verbose         = cms.untracked.int32(0),
    NumberDaughters = cms.untracked.int32(2),
    ParticleID      = cms.untracked.int32(443),
    DaughterIDs     = cms.untracked.vint32(13, -13),
    MinPt           = cms.untracked.vdouble(0.5, 0.5),
    MinEta          = cms.untracked.vdouble(-2.5, -2.5),
    MaxEta          = cms.untracked.vdouble( 2.5,  2.5),
)


ProductionFilterSequence = cms.Sequence(generator*jpsifilter)
