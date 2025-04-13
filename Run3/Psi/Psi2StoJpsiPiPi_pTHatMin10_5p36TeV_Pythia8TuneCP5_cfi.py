import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunesRun3ECM13p6TeV.PythiaCP5Settings_cfi import *
from GeneratorInterface.EvtGenInterface.EvtGenSetting_cff import *

_generator = cms.EDFilter("Pythia8GeneratorFilter",
			 pythiaPylistVerbosity = cms.untracked.int32(0),
			 pythiaHepMCVerbosity = cms.untracked.bool(False),
			 comEnergy = cms.double(5362.0),
			 maxEventsToPrint = cms.untracked.int32(0),
			 ExternalDecays = cms.PSet(
			     EvtGen200 = cms.untracked.PSet(
				       decay_table = cms.string('GeneratorInterface/EvtGenInterface/data/DECAY_2020.DEC'),
				       particle_property_file = cms.FileInPath('GeneratorInterface/EvtGenInterface/data/evt.pdl'),
				       user_decay_file = cms.vstring('GeneratorInterface/ExternalDecays/data/incl_BtoPsi2S_Jpsipipi.dec'),
				       list_forced_decays = cms.vstring('Mypsi(2S)'),
				       operates_on_particles = cms.vint32()
			     ),
			     parameterSets = cms.vstring('EvtGen200')
			 ),
       PythiaParameters = cms.PSet(
			     pythia8CommonSettingsBlock,
			     pythia8CP5SettingsBlock,
			     processParameters = cms.vstring(
                                 'Charmonium:states(3S1) = 100443',
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
				                         'PhaseSpace:pTHatMin = 10.'
			     ),
			     parameterSets = cms.vstring(
				     'pythia8CommonSettings',
				     'pythia8CP5Settings',
				     'processParameters',
			     )
			 )
)

from GeneratorInterface.Core.ExternalGeneratorFilter import ExternalGeneratorFilter
generator = ExternalGeneratorFilter(_generator)

generator.PythiaParameters.processParameters.extend(EvtGenExtraParticles)

###########
# Filters #
###########

Psi2SJpsiDaufilter = cms.EDFilter("PythiaDauVFilter",
				  ParticleID = cms.untracked.int32(100443),
          NumberDaughters = cms.untracked.int32(3),
				  DaughterIDs = cms.untracked.vint32(443, 211, -211),

				  MomMinPt = cms.untracked.double(0.),
				  MomMinEta = cms.untracked.double(-2.4),
				  MomMaxEta = cms.untracked.double(2.4),

          MinPt = cms.untracked.vdouble(6.5, 0.5, 0.5),
          MinEta = cms.untracked.vdouble(-3.0, -3.0, -3.0),
          MaxEta = cms.untracked.vdouble(3.0, 3.0, 3.0),
)

mumugenfilter = cms.EDFilter("MCParticlePairFilter",
			     Status = cms.untracked.vint32(1, 1),
			     MinPt = cms.untracked.vdouble(1.0, 1.0),
			     MinP = cms.untracked.vdouble(0., 0.),
			     MaxEta = cms.untracked.vdouble(2.5, 2.5),
			     MinEta = cms.untracked.vdouble(-2.5, -2.5),
			     MinInvMass = cms.untracked.double(2.0),
			     MaxInvMass = cms.untracked.double(4.0),
			     ParticleCharge = cms.untracked.int32(-1),
			     ParticleID1 = cms.untracked.vint32(13),
			     ParticleID2 = cms.untracked.vint32(13)
)

ProductionFilterSequence = cms.Sequence(generator*mumugenfilter*Psi2SJpsiDaufilter)
