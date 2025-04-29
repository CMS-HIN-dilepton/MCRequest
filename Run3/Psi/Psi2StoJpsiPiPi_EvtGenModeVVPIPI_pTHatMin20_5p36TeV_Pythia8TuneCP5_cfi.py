import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunesRun3ECM13p6TeV.PythiaCP5Settings_cfi import *
from GeneratorInterface.EvtGenInterface.EvtGenSetting_cff import *

# based on https://cernbox.cern.ch/pdf-viewer/public/Tws8dOkL2Vq4KPN/X_psit_slides_tmp.pdf

_generator = cms.EDFilter("Pythia8GeneratorFilter",
			 pythiaPylistVerbosity = cms.untracked.int32(0),
			 pythiaHepMCVerbosity = cms.untracked.bool(False),
			 comEnergy = cms.double(5362.0),
			 maxEventsToPrint = cms.untracked.int32(0),
			 ExternalDecays = cms.PSet(
			     EvtGen200 = cms.untracked.PSet(
                                 decay_table = cms.string('GeneratorInterface/EvtGenInterface/data/DECAY_2020.DEC'),
				 particle_property_file = cms.FileInPath('GeneratorInterface/EvtGenInterface/data/evt.pdl'),
                                 user_decay_embedded = cms.vstring(
                                     '''
                                     Particle J/psi 3.0969 9.26e-05
                                     Particle psi(2S) 3.6861 2.94e-04
                                     
                                     Alias      MyPsi2S  psi(2S)
                                     ChargeConj MyPsi2S  MyPsi2S
                                     Alias      MyJ/psi  J/psi
                                     ChargeConj MyJ/psi  MyJ/psi
                                     
                                     Decay MyPsi2S
                                     1.000         MyJ/psi      pi+    pi-      VVPIPI;

                                     Decay MyJ/psi
                                     1.000         mu+          mu-         PHOTOS VLL;

                                     Enddecay
                                     End
                                     '''),
				 list_forced_decays = cms.vstring('MyPsi2S'),
				  operates_on_particles = cms.vint32(100443, -100443),
                                 convertPythiaCodes = cms.untracked.bool(False)
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
				 'PhaseSpace:pTHatMin = 20.'
                                 
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

#generator.PythiaParameters.processParameters.extend(EvtGenExtraParticles)

###########
# Filters #
###########

Psi2StoJpsiPiPiFilter = cms.EDFilter("PythiaDauVFilter",
		       ParticleID = cms.untracked.int32(100443),
                       NumberDaughters = cms.untracked.int32(3),
		       DaughterIDs = cms.untracked.vint32(443, 211, -211),

		       #MomMinPt = cms.untracked.double(10.),
		       #MomMinEta = cms.untracked.double(-4.),
		       #MomMaxEta = cms.untracked.double(4.),
			MinPt = cms.untracked.vdouble(8., 0.6, 0.6),
			MinEta = cms.untracked.vdouble(-5.0, -4.0, -4.0),
			MaxEta = cms.untracked.vdouble(5.0, 4.0, 4.0),
)

JpsiMuMuFilter = cms.EDFilter("PythiaDauVFilter",
                          ParticleID = cms.untracked.int32(443),
                          MotherID = cms.untracked.int32(100443),
                          NumberDaughters = cms.untracked.int32(2),
                          DaughterIDs = cms.untracked.vint32(13, -13),
			     MinPt = cms.untracked.vdouble(0.5, 0.5),
			     MaxEta = cms.untracked.vdouble(2.5, 2.5),
			     MinEta = cms.untracked.vdouble(-2.5, -2.5),
)

ProductionFilterSequence = cms.Sequence(generator*Psi2StoJpsiPiPiFilter*JpsiMuMuFilter)
