import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
	maxEventsToPrint = cms.untracked.int32(1),
	pythiaPylistVerbosity = cms.untracked.int32(1),
	filterEfficiency = cms.untracked.double(1.0),
	pythiaHepMCVerbosity = cms.untracked.bool(False),
	comEnergy = cms.double(8160.0),

	crossSection = cms.untracked.double(22.82),
	
	PythiaParameters = cms.PSet(
            pythia8CommonSettingsBlock,
            pythia8CUEP8M1SettingsBlock,
	        processParameters = cms.vstring(
                        'WeakDoubleBoson:ffbar2ZW    = on',
	    ),
            parameterSets = cms.vstring('pythia8CommonSettings',
                                        'pythia8CUEP8M1Settings',
                                        'processParameters',
                                        )
	)
)

configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('\$Revision$'),
    name = cms.untracked.string('\$Source$'),
    annotation = cms.untracked.string('WZ, 8.16 TeV, TuneCUETP8M1')
)
