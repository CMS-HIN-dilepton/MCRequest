import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *
from GeneratorInterface.EvtGenInterface.EvtGenSetting_cff import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
                         pythiaPylistVerbosity = cms.untracked.int32(0),
                         pythiaHepMCVerbosity = cms.untracked.bool(False),
                         comEnergy = cms.double(8160.0),
                         maxEventsToPrint = cms.untracked.int32(0),
                         ExternalDecays = cms.PSet(
        EvtGen130 = cms.untracked.PSet(
            decay_table = cms.string('GeneratorInterface/EvtGenInterface/data/DECAY_2010.DEC'),
            particle_property_file = cms.FileInPath('GeneratorInterface/EvtGenInterface/data/evt.pdl'),
            user_decay_file        = cms.vstring('GeneratorInterface/ExternalDecays/data/incl_BtoJpsi_mumu.dec'),
            list_forced_decays     = cms.vstring('MyB0', 
                                                 'Myanti-B0',
                                                 'MyB+',
                                                 'MyB-',
                                                 'MyB_s0', 
                                                 'Myanti-B_s0'),
            operates_on_particles = cms.vint32()
            ),
        parameterSets = cms.vstring('EvtGen130')
        ),
                         PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
        processParameters = cms.vstring(
            'HardQCD:gg2bbbar    = on ',
            'HardQCD:qqbar2bbbar = on ',
            'HardQCD:hardbbbar   = on',
            'PhaseSpace:pTHatMin = 2.',
          
            ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CUEP8M1Settings',
                                    'processParameters',
                                    )
        )
                         )

generator.PythiaParameters.processParameters.extend(EvtGenExtraParticles)


###########
# Filters #
###########
# Filter only pp events which produce a B->Jpsi(mumu)X


bfilter = cms.EDFilter("PythiaFilter",
                       ParticleID = cms.untracked.int32(5)
                       )


oniafilter = cms.EDFilter("MCSingleParticleFilter",
                          Status = cms.untracked.vint32(2,2),
                          MaxEta = cms.untracked.vdouble(1000.0,1000.0),
                          MinEta = cms.untracked.vdouble(-1000.0,-1000.0),
                          MinPt = cms.untracked.vdouble(0.0,0.0),
                          ParticleID = cms.untracked.vint32(443,100443)
                          )


mumugenfilter = cms.EDFilter("MCParticlePairFilter",
    Status = cms.untracked.vint32(1, 1),
    MinP = cms.untracked.vdouble(2.5, 2.5),
    MaxEta = cms.untracked.vdouble(2.5, 2.5),
    MinEta = cms.untracked.vdouble(-2.5, -2.5),
    ParticleCharge = cms.untracked.int32(-1),
    ParticleID1 = cms.untracked.vint32(13),
    ParticleID2 = cms.untracked.vint32(13),
    BetaBoost = cms.untracked.double(0.434)
)



ProductionFilterSequence = cms.Sequence(generator*bfilter*oniafilter*mumugenfilter)

