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
            user_decay_file        = cms.vstring('GeneratorInterface/ExternalDecays/data/Onia_chic_jpsigamma.dec'),
            list_forced_decays     = cms.vstring('Mychi_c0',
                                                 'Mychi_c1',
                                                 'Mychi_c2'),
            operates_on_particles = cms.vint32(10441,20443,445)
            ),
        parameterSets = cms.vstring('EvtGen130')
        ),
                         PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
        processParameters = cms.vstring(
            'Charmonium:states(3PJ) = 10441,20443,445', # filter on all Chi C states
            'Charmonium:O(3PJ)[3P0(1)] = 0.05,0.05,0.05',
            'Charmonium:O(3PJ)[3S1(8)] = 0.0031,0.0031,0.0031',
            'Charmonium:gg2ccbar(3PJ)[3PJ(1)]g = on,on,on',
            'Charmonium:qg2ccbar(3PJ)[3PJ(1)]q = on,on,on',
            'Charmonium:qqbar2ccbar(3PJ)[3PJ(1)]g = on,on,on',
            'Charmonium:gg2ccbar(3PJ)[3S1(8)]g = on,on,on',
            'Charmonium:qg2ccbar(3PJ)[3S1(8)]q = on,on,on',
            'Charmonium:qqbar2ccbar(3PJ)[3S1(8)]g = on,on,on',
            'PhaseSpace:pTHatMin = 2.'                   # be aware of this ckin(3) equivalent
            ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CUEP8M1Settings',
                                    'processParameters',
                                    )
        )
                         )

generator.PythiaParameters.processParameters.extend(EvtGenExtraParticles)

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

ProductionFilterSequence = cms.Sequence(generator*oniafilter*mumugenfilter)
