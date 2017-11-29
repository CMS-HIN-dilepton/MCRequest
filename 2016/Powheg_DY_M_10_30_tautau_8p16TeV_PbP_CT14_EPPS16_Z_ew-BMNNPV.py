import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *
from Configuration.Generator.Pythia8PowhegEmissionVetoSettings_cfi import *
from GeneratorInterface.ExternalDecays.TauolaSettings_cff import *


externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    args = cms.vstring('/afs/cern.ch/work/e/echapon/public/DY_pA_2016/DY_M_10_30_tautau_8p16TeV_Pbp_CT14_EPPS16_Z_ew-BMNNPV.tgz'),
#    args = cms.vstring("PATH/TO/TARBALL/GRIDPACK.tgz"),
    nEvents = cms.untracked.uint32(1),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)

generator = cms.EDFilter("Pythia8HadronizerFilter",
                         maxEventsToPrint = cms.untracked.int32(1),
                         pythiaPylistVerbosity = cms.untracked.int32(1),
                         filterEfficiency = cms.untracked.double(1.0),
                         pythiaHepMCVerbosity = cms.untracked.bool(False),
                         comEnergy = cms.double(8160.),
                         ExternalDecays = cms.PSet(
                            Tauola = cms.untracked.PSet(
                               TauolaPolar,
                               TauolaDefaultInputCards
                               ),
                            parameterSets = cms.vstring('Tauola')
                            ),
                         PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
        pythia8PowhegEmissionVetoSettingsBlock,
        processParameters = cms.vstring(
            'POWHEG:nFinal = 1',   ## Number of final state particles
                                   ## (BEFORE THE DECAYS) in the LHE
                                   ## other than emitted extra parton
          ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CUEP8M1Settings',
                                    'pythia8PowhegEmissionVetoSettings',
                                    'processParameters'
                                    )
        )
                         )

ProductionFilterSequence = cms.Sequence(generator)
