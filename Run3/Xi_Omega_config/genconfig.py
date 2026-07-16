# with command line options: CMSSW_15_0_8 --mc --eventcontent RAWSIM --datatier GEN-SIM --conditions 150X_mcRun3_2025_forOO_realistic_v7 --beamspot MatchHI --step GEN,SIM --scenario HeavyIons --geometry DB:Extended --era Run3_2025_OXY --pileup HiMixGEN --pileup_input dbs:/MinBias_OO_5p36TeV_hijing/HINOOSpring25GS-150X_mcRun3_2025_forOO_realistic_v7-v1/GEN-SIM --nThreads 8 --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 100000 

#------------------------------------
#GenXsecAnalyzer:
#------------------------------------
#Before Filter: total cross section = 5.728e+10 +- 0.000e+00 pb
#Filter efficiency (taking into account weights)= (97) / (100000) = 9.700e-04 +- 9.844e-05
#Filter efficiency (event-level)= (97) / (100000) = 9.700e-04 +- 9.844e-05    [TO BE USED IN MCM]

#After filter: final cross section = 5.556e+07 +- 5.639e+06 pb
#After filter: final fraction of events with negative weights = 0.000e+00 +- 0.000e+00
#After filter: final equivalent lumi for 1M events (1/fb) = 1.800e-05 +- 1.827e-06

# 0.004009 sec/output event, 306 kB/output event

import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *
from GeneratorInterface.EvtGenInterface.EvtGenSetting_cff import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
                         pythiaPylistVerbosity = cms.untracked.int32(0),
                         pythiaHepMCVerbosity = cms.untracked.bool(False),
                         comEnergy = cms.double(5362.0),
                         maxEventsToPrint = cms.untracked.int32(0),
                         ExternalDecays = cms.PSet(
                             EvtGen130 = cms.untracked.PSet(
                                 decay_table = cms.string('GeneratorInterface/EvtGenInterface/data/DECAY_2010.DEC'),
                                 operates_on_particles = cms.vint32(),
                                 particle_property_file = cms.FileInPath('GeneratorInterface/EvtGenInterface/data/evt.pdl'),
                                 list_forced_decays = cms.vstring('D_Omega','Myanti-D_Omega'),
                                 user_decay_embedded= cms.vstring(
                                     """                                                                                                                                                             
                                     Alias        D_Omega                 Omega-                                                                                                                     
                                     Alias        Myanti-D_Omega                 anti-Omega+                                                                                         
                                     Decay D_Omega                                                                                                                                                   
                                     1.000           Lambda0     K-     PHSP;                                                                                                                        
                                     Enddecay                                                                                                                                                        
                                     Decay Myanti-D_Omega                                                                                                                                            
                                     1.000           anti-Lambda0        K+      PHSP;                                                                                                               
                                     Enddecay                                                                                                                                                        
                                     End                                                                                                                                                             
                                     """
                                 )
                             ),
                             parameterSets = cms.vstring('EvtGen130')
                         ),
                         PythiaParameters = cms.PSet(
                             pythia8CommonSettingsBlock,
                             pythia8CP5SettingsBlock,
                             processParameters = cms.vstring(
                                 'SoftQCD:nonDiffractive = on',
                                 'PhaseSpace:pTHatMin = 0',
                             ),
                             parameterSets = cms.vstring(
                                 'pythia8CommonSettings',
                                 'pythia8CP5Settings',
                                 'processParameters',
                             )
                         )
                     )

generator.PythiaParameters.processParameters.extend(EvtGenExtraParticles)


LambdaDaufilter = cms.EDFilter("PythiaMomDauFilter",
                               ParticleID = cms.untracked.int32(3334),
                               MomMinPt = cms.untracked.double(0.0),
                               MomMinEta = cms.untracked.double(-2.4),
                               MomMaxEta = cms.untracked.double(2.4),
                               DaughterIDs = cms.untracked.vint32(3122, -321),
                               NumberDaughters = cms.untracked.int32(2),
                               NumberDescendants = cms.untracked.int32(0),
                               BetaBoost = cms.untracked.double(0.0),
                            )

Lambdarapidityfilter = cms.EDFilter("PythiaFilter",
                                ParticleID = cms.untracked.int32(3334),
                                MinPt = cms.untracked.double(0.0),
                                MaxPt = cms.untracked.double(500.),
                                MinRapidity = cms.untracked.double(-2.4),
                                MaxRapidity = cms.untracked.double(2.4),
                            )


ProductionFilterSequence = cms.Sequence(generator*LambdaDaufilter*Lambdarapidityfilter)
