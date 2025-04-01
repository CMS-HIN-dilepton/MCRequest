# ------------------------------------
# GenXsecAnalyzer:
# ------------------------------------
# Before Filter: total cross section = 1.781e+07 +- 1.043e+05 pb
# Filter efficiency (taking into account weights)= (3187) / (7000) = 4.553e-01 +- 5.952e-03
# Filter efficiency (event-level)= (3187) / (7000) = 4.553e-01 +- 5.952e-03    [TO BE USED IN MCM]

# After filter: final cross section = 8.107e+06 +- 1.161e+05 pb
# After filter: final fraction of events with negative weights = 0.000e+00 +- 0.000e+00
# After filter: final equivalent lumi for 1M events (1/fb) = 1.234e-04 +- 1.771e-06

# 0.286 sec/output event, 241 kB/output event

# generated with command line options: Configuration/GenProduction/python/JpsiEE_Tune2017.py --mc --eventcontent RAWSIM --datatier GEN-SIM --conditions 130X_mcRun3_2023_realistic_HI_v18 --beamspot Realistic2023PbPbCollision --step GEN,SIM --geometry DB:Extended --customise Configuration/DataProcessing/Utils.addMonitoring --era Run3_pp_on_PbPb --nThreads 4 --no_exec -n 2000

import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunesRun3ECM13p6TeV.PythiaCP5Settings_cfi import *

_generator = cms.EDFilter("Pythia8GeneratorFilter",
                         pythiaPylistVerbosity = cms.untracked.int32(0),
                         pythiaHepMCVerbosity = cms.untracked.bool(False),
                         comEnergy = cms.double(5362.0),
                         maxEventsToPrint = cms.untracked.int32(0),
                         PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP5SettingsBlock,
        processParameters = cms.vstring(
            'Charmonium:states(3S1) = 443', # filter on 443 and prevents other onium states decaying to 443, so we should turn the others off
            'Charmonium:O(3S1)[3S1(1)] = 1.16',
            'Charmonium:O(3S1)[3S1(8)] = 0.0119',
            'Charmonium:O(3S1)[1S0(8)] = 0.01',
            'Charmonium:O(3S1)[3P0(8)] = 0.01',
            'Charmonium:gg2ccbar(3S1)[3S1(1)]g = on',
            'Charmonium:gg2ccbar(3S1)[3S1(8)]g = on',
            'Charmonium:qg2ccbar(3S1)[3S1(8)]q = on',
            'Charmonium:qqbar2ccbar(3S1)[3S1(8)]g = on',
            'Charmonium:gg2ccbar(3S1)[1S0(8)]g = on',
            'Charmonium:qg2ccbar(3S1)[1S0(8)]q = on',
            'Charmonium:qqbar2ccbar(3S1)[1S0(8)]g = on',
            'Charmonium:gg2ccbar(3S1)[3PJ(8)]g = on',
            'Charmonium:qg2ccbar(3S1)[3PJ(8)]q = on',
            'Charmonium:qqbar2ccbar(3S1)[3PJ(8)]g = on',
            'Charmonium:gg2ccbar(3S1)[3S1(1)]gm = on',
            '443:onMode = off',            # ignore cross-section re-weighting (CSAMODE=6) since selecting wanted decay mode
            '443:onIfAny = 11 -11'
            ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CP5Settings',
                                    'processParameters',
                                    )
        )
)

from GeneratorInterface.Core.ExternalGeneratorFilter import ExternalGeneratorFilter
generator = ExternalGeneratorFilter(_generator)

# Filters

oniafilter = cms.EDFilter("PythiaFilter",
    Status = cms.untracked.int32(2),
    MaxEta = cms.untracked.double(10.0),
    MinEta = cms.untracked.double(-10.0),
    MinPt = cms.untracked.double(0.0),
    ParticleID = cms.untracked.int32(443)
)

elelgenfilter = cms.EDFilter("MCParticlePairFilter",
    Status = cms.untracked.vint32(1, 1),
    MinPt = cms.untracked.vdouble(0.5, 0.5),
    MinP = cms.untracked.vdouble(0., 0.),
    MaxEta = cms.untracked.vdouble(3.0, 3.0),
    MinEta = cms.untracked.vdouble(-3.0, -3.0),
    ParticleCharge = cms.untracked.int32(-1),
    ParticleID1 = cms.untracked.vint32(11),
    ParticleID2 = cms.untracked.vint32(11)
)

ProductionFilterSequence = cms.Sequence(generator*oniafilter*elelgenfilter)
