# Auto generated configuration file
# using: 
# Revision: 1.381.2.28 
# Source: /local/reps/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: 2013/Filter2013/python/Ups2SMM_5p02TeV_TuneCUETP8M1_cfi.py --mc --eventcontent RAWSIM --datatier GEN-SIM --conditions STARTHI53_V27::All --beamspot Realistic5TeVPPbBoost --step GEN,SIM --no_exec -n 1000
import FWCore.ParameterSet.Config as cms

process = cms.Process('SIM')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('GeneratorInterface.HiGenCommon.VtxSmearedRealistic5TeVPPbBoost_cff')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.381.2.28 $'),
    annotation = cms.untracked.string('2013/Filter2013/python/Ups2SMM_5p02TeV_TuneCUETP8M1_cfi.py nevts:1000'),
    name = cms.untracked.string('PyReleaseValidation')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    fileName = cms.untracked.string('Ups2SMM_5p02TeV_TuneCUETP8M1_cfi_py_GEN_SIM.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN-SIM')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    )
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'STARTHI53_V27::All', '')

process.oniafilter = cms.EDFilter("PythiaFilter",
    MaxEta = cms.untracked.double(1000.0),
    Status = cms.untracked.int32(2),
    MinEta = cms.untracked.double(-1000.0),
    MinPt = cms.untracked.double(0.0),
    ParticleID = cms.untracked.int32(100553)
)


process.generator = cms.EDFilter("Pythia8GeneratorFilter",
    pythiaPylistVerbosity = cms.untracked.int32(0),
    filterEfficiency = cms.untracked.double(0.109),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(5023.0),
    crossSection = cms.untracked.double(1430000.0),
    maxEventsToPrint = cms.untracked.int32(0),
    PythiaParameters = cms.PSet(
        pythia8CommonSettings = cms.vstring('Main:timesAllowErrors = 10000', 
            'Check:epTolErr = 0.01', 
            'Beams:setProductionScalesFromLHEF = off', 
            'SLHA:keepSM = on', 
            'SLHA:minMassSM = 1000.', 
            'ParticleDecays:limitTau0 = on', 
            'ParticleDecays:tau0Max = 10', 
            'ParticleDecays:allowPhotonRadiation = on'),
        pythia8CUEP8M1Settings = cms.vstring('Tune:pp 14', 
            'Tune:ee 7', 
            'MultipartonInteractions:pT0Ref=2.4024', 
            'MultipartonInteractions:ecmPow=0.25208', 
            'MultipartonInteractions:expPow=1.6'),
        processParameters = cms.vstring('Bottomonium:states(3S1) = 100553', 
            'Bottomonium:O(3S1)[3S1(1)] = 4.63', 
            'Bottomonium:O(3S1)[3S1(8)] = 0.045', 
            'Bottomonium:O(3S1)[1S0(8)] = 0.06', 
            'Bottomonium:O(3S1)[3P0(8)] = 0.06', 
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
            '100553:onMode = off', 
            '100553:onIfAny = 13 -13', 
            'PhaseSpace:pTHatMin = 2.'),
        parameterSets = cms.vstring('pythia8CommonSettings', 
            'pythia8CUEP8M1Settings', 
            'processParameters')
    )
)


process.mumugenfilter = cms.EDFilter("MCParticlePairFilter",
    Status = cms.untracked.vint32(1, 1),
    BetaBoost = cms.untracked.double(-0.465),
    MaxEta = cms.untracked.vdouble(2.5, 2.5),
    MinEta = cms.untracked.vdouble(-2.5, -2.5),
    ParticleCharge = cms.untracked.int32(-1),
    MinP = cms.untracked.vdouble(2.5, 2.5),
    ParticleID1 = cms.untracked.vint32(13),
    ParticleID2 = cms.untracked.vint32(13)
)


process.ProductionFilterSequence = cms.Sequence(process.generator+process.oniafilter+process.mumugenfilter)

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.endjob_step,process.RAWSIMoutput_step)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.ProductionFilterSequence * getattr(process,path)._seq 

process.Timing = cms.Service("Timing",
  summaryOnly = cms.untracked.bool(False),
  useJobReport = cms.untracked.bool(True)
)
