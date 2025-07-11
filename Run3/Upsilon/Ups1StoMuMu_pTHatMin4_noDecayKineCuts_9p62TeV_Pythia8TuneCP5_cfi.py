import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunesRun3ECM13p6TeV.PythiaCP5Settings_cfi import *

_generator = cms.EDFilter("Pythia8GeneratorFilter",
                         pythiaPylistVerbosity = cms.untracked.int32(0),
                         pythiaHepMCVerbosity = cms.untracked.bool(False),
                         comEnergy = cms.double(9617.0), # for 2025 pO run, 6.8 TeV per charge
                         maxEventsToPrint = cms.untracked.int32(0),
                         PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP5SettingsBlock,
        processParameters = cms.vstring(
            'Bottomonium:states(3S1) = 553', # filter on 553 and prevents other onium states decaying to 553, so we should turn the others off
            'Bottomonium:O(3S1)[3S1(1)] = 9.28',
            'Bottomonium:O(3S1)[3S1(8)] = 0.15',
            'Bottomonium:O(3S1)[1S0(8)] = 0.02',
            'Bottomonium:O(3S1)[3P0(8)] = 0.02',
            'Bottomonium:gg2bbbar(3S1)[3S1(1)]g = on',
            'Bottomonium:gg2bbbar(3S1)[3S1(8)]g = on',
            'Bottomonium:qg2bbbar(3S1)[3S1(8)]q = on',
            'Bottomonium:qqbar2bbbar(3S1)[3S1(8)]g = on',
            'Bottomonium:gg2bbbar(3S1)[1S0(8)]g = on',
            'Bottomonium:qg2bbbar(3S1)[1S0(8)]q = on',
            'Bottomonium:qqbar2bbbar(3S1)[1S0(8)]g = on',
            'Bottomonium:gg2bbbar(3S1)[3PJ(8)]g = on',
            'Bottomonium:qg2bbbar(3S1)[3PJ(8)]q = on',
            'Bottomonium:qqbar2bbbar(3S1)[3PJ(8)]g = on',
            'Bottomonium:gg2bbbar(3S1)[3S1(1)]gm = on',#added Colour-singlet production of 3S1 bottomonium states via gg to bbbar[3S1(1)] g with a hard gamma.
            '553:onMode = off',            # ignore cross-section re-weighting (CSAMODE=6) since selecting wanted decay mode
            '553:onIfAny = 13 -13',         # only decay to dimuon
            'PhaseSpace:pTHatMin = 4.'
            ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CP5Settings',
                                    'processParameters',
                                    )
        )
)

from GeneratorInterface.Core.ExternalGeneratorFilter import ExternalGeneratorFilter
generator = ExternalGeneratorFilter(_generator)

oniafilter = cms.EDFilter("PythiaFilter",
    Status = cms.untracked.int32(2),
    MaxEta = cms.untracked.double(100.0),
    MinEta = cms.untracked.double(-100.0),
    MinPt = cms.untracked.double(0.0),
    ParticleID = cms.untracked.int32(553),
    BetaBoost = cms.untracked.double(0.346) # for 2025 pO run, 6.8 TeV per charge
)

ProductionFilterSequence = cms.Sequence(generator*oniafilter)
