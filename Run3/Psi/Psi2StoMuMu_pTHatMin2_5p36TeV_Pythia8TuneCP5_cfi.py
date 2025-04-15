# with command lines under CMSSW_13_0_18: --mc --eventcontent RAWSIM --pileup HiMixGEN --datatier GEN-SIM --conditions 130X_mcRun3_2023_realistic_HI_v18 --beamspot MatchHI --step GEN,SIM --scenario HeavyIons --geometry DB:Extended --era Run3_pp_on_PbPb --pileup_input "dbs:/MinBias_Drum5F_5p36TeV_hydjet/HINPbPbSpring23GS-130X_mcRun3_2023_realistic_HI_v18-v2/GEN-SIM"  --nThreads 4 --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 4000

# ------------------------------------
# GenXsecAnalyzer:
# ------------------------------------
# Before Filter: total cross section = 4.045e+06 +- 1.957e+04 pb
# Filter efficiency (taking into account weights)= (377.6) / (1660.72) = 2.274e-01 +- 4.707e-03
# Filter efficiency (event-level)= (2753) / (10000) = 2.753e-01 +- 4.467e-03    [TO BE USED IN MCM]

# After filter: final cross section = 9.197e+05 +- 1.955e+04 pb
# After filter: final fraction of events with negative weights = 0.000e+00 +- 0.000e+00
# After filter: final equivalent lumi for 1M events (1/fb) = 1.087e-03 +- 2.314e-05

# pp: 0.145 sec/event, 296 kB/event
# hydjet embedding: 0.347 sec/event, 827 kB/event

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
            'Charmonium:states(3S1) = 100443', # filter on 100443 and prevents other onium states decaying to 100443, so we should turn the others off
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
            '100443:onMode = off',            # ignore cross-section re-weighting (CSAMODE=6) since selecting wanted decay mode
            '100443:onIfAny = 13 -13',
            'PhaseSpace:pTHatMin = 2.',
            'PhaseSpace:bias2Selection = on',
            'PhaseSpace:bias2SelectionPow = 1.3',
            'PhaseSpace:bias2SelectionRef = 1'
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
    MaxRapidity = cms.untracked.double(3.0),
    MinRapidity = cms.untracked.double(-3.0),
    MinPt = cms.untracked.double(0.0),
    ParticleID = cms.untracked.int32(100443)
)

mumugenfilter = cms.EDFilter("MCParticlePairFilter",
    Status = cms.untracked.vint32(1, 1),
    MinPt = cms.untracked.vdouble(1., 1.),
    MinP = cms.untracked.vdouble(2.0, 2.0),
    MaxEta = cms.untracked.vdouble(2.5, 2.5),
    MinEta = cms.untracked.vdouble(-2.5, -2.5),
    ParticleCharge = cms.untracked.int32(-1),
    ParticleID1 = cms.untracked.vint32(13),
    ParticleID2 = cms.untracked.vint32(13)
)

ProductionFilterSequence = cms.Sequence(generator*oniafilter*mumugenfilter)
