import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *
#TuneCUETP8M1

generator = cms.EDFilter("Pythia8GeneratorFilter",
  maxEventsToPrint = cms.untracked.int32(0),
  pythiaPylistVerbosity = cms.untracked.int32(0),
  filterEfficiency = cms.untracked.double(1),
  pythiaHepMCVerbosity = cms.untracked.bool(False),
  comEnergy = cms.double(8160.0),
  PythiaParameters = cms.PSet(
    pythia8CommonSettingsBlock,
    pythia8CUEP8M1SettingsBlock,
    processParameters = cms.vstring(
    'ParticleDecays:limitTau0 = off',
    'ParticleDecays:limitCylinder = on',
    'ParticleDecays:xyMax = 2000',
    'ParticleDecays:zMax = 4000',
    'HardQCD:all = on',
    'PhaseSpace:pTHatMin = 20',
    'PhaseSpace:pTHatMax = 9999',
    '130:mayDecay = on',
    '211:mayDecay = on',
    '321:mayDecay = on'
    ),
    parameterSets = cms.vstring('pythia8CommonSettings',
      'pythia8CUEP8M1Settings',
      'processParameters',
    )
  )
)

mugenfilter = cms.EDFilter("MCSmartSingleParticleFilter",
      MinPt = cms.untracked.vdouble(15., 15.),
      MinEta = cms.untracked.vdouble(-3.0, -3.0),
      MaxEta = cms.untracked.vdouble(3.0, 3.0),
      ParticleID = cms.untracked.vint32(13, -13),
      Status = cms.untracked.vint32(1, 1),
      MaxDecayRadius = cms.untracked.vdouble(2000., 2000.),
      MinDecayZ = cms.untracked.vdouble(-4000., -4000.),
      MaxDecayZ = cms.untracked.vdouble(4000., 4000.),
#      BetaBoost = cms.untracked.double(0.434)
)

configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('PYTHIA 8 QCD in NN (pt-hat 20 GeV) at sqrt(s) = 8.16 TeV')
)

ProductionFilterSequence = cms.Sequence(generator*mugenfilter)
