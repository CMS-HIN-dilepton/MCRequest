from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunesRun3ECM13p6TeV.PythiaCP5Settings_cfi import *

# with CMSSW_13_0_18_HeavyIon, Hydjet embedding
# Before Filter: total cross section = 7.081e+01 +- 3.993e-01 pb
# Filter efficiency (taking into account weights)= (3011) / (10000) = 3.011e-01 +- 4.587e-03
# Filter efficiency (event-level)= (3011) / (10000) = 3.011e-01 +- 4.587e-03    [TO BE USED IN MCM]

generator = cms.EDFilter("Pythia8GeneratorFilter",
                         pythiaPylistVerbosity = cms.untracked.int32(0),
                         pythiaHepMCVerbosity = cms.untracked.bool(False),
                         comEnergy = cms.double(5362.0),
                         maxEventsToPrint = cms.untracked.int32(0),
                         PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP5SettingsBlock,
        processParameters = cms.vstring(
            'Charmonium:gg2doubleccbar(3S1)[3S1(1)] = on,off,off',
            'Charmonium:qqbar2doubleccbar(3S1)[3S1(1)] = on,off,off',
            'Charmonium:states(3S1)1  = 443,443,100443',
            'Charmonium:states(3S1)2  = 443,100443,100443',
            '443:onMode = off',
            '443:onIfMatch = 13 -13',
            'PhaseSpace:pTHatMin = 5.'
            'PartonLevel:MPI = on',
            'PartonLevel:ISR = on',
            'PartonLevel:FSR = on',
            'HadronLevel:all = on',
            'HadronLevel:Hadronize = on',
            'HadronLevel:Decay = on',
        ),
        parameterSets = cms.vstring(
            'pythia8CommonSettings', 
            'pythia8CP5Settings', 
            'processParameters'
        )
    )
)

FourMuonFilter = cms.EDFilter("FourLepFilter", # require 4-mu in the final state
        MinPt = cms.untracked.double(1.2),
        #MaxPt = cms.untracked.double(4000.0),
        MaxEta = cms.untracked.double(2.5),
        #MinEta = cms.untracked.double(-2.5),
        ParticleID = cms.untracked.int32(13)
)

DiJpsiFilter = cms.EDFilter("MCParticlePairFilter",
        MinPt = cms.untracked.vdouble(1.0,1.0),
        #MaxPt = cms.untracked.vdouble(4000.0,4000.0),
        MaxEta = cms.untracked.vdouble( 2.5,2.5),
        MinEta = cms.untracked.vdouble(-2.5,-2.5),
        ParticleID1 = cms.untracked.vint32(443, -443),
        ParticleID2 = cms.untracked.vint32(443, -443),
        MinInvMass = cms.untracked.double(1.0),
        MaxInvMass = cms.untracked.double(16.0),
)

ProductionFilterSequence = cms.Sequence(generator*FourMuonFilter)