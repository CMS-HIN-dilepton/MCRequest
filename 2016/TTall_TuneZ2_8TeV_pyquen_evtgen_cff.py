import FWCore.ParameterSet.Config as cms

from Configuration.Generator.PythiaUEZ2Settings_cfi import *

generator = cms.EDFilter("PyquenGeneratorFilter",
      ExternalDecays = cms.PSet(
         # de-activated because only one of EvtGen and Tauola seems to work at a time
         # EvtGen = cms.untracked.PSet(
         #     decay_table = cms.FileInPath('GeneratorInterface/ExternalDecays/data/DECAY_NOLONGLIFE.DEC'),
         #     list_forced_decays = cms.vstring(),
         #     operates_on_particles = cms.vint32(0),
         #     particle_property_file = cms.FileInPath('GeneratorInterface/ExternalDecays/data/evt.pdl'),
         #     use_default_decay = cms.untracked.bool(True),
         #     user_decay_file = cms.FileInPath('GeneratorInterface/ExternalDecays/data/Validation.dec')
         # ),
         Tauola = cms.untracked.PSet(
            InputCards = cms.PSet(
               mdtau = cms.int32(0),
               pjak1 = cms.int32(0),
               pjak2 = cms.int32(0)
               ),
            UseTauolaPolarization = cms.bool(True)
            ),
         parameterSets = cms.vstring(#'EvtGen', 
            # parameterSets = cms.vstring('EvtGen', 
            'Tauola')
         ),
      comEnergy = cms.double(8160.0),
      aBeamTarget = cms.double(208.0),
      protonSide = cms.untracked.int32(2),
      qgpInitialTemperature = cms.double(1.0), ## initial temperature of QGP; allowed range [0.2,2.0]GeV;
      qgpProperTimeFormation = cms.double(0.1), ## proper time of QGP formation; allowed range [0.01,10.0]fm/c;
      hadronFreezoutTemperature = cms.double(0.14),
      doRadiativeEnLoss = cms.bool(True), ## if true, perform partonic radiative en loss
      doCollisionalEnLoss = cms.bool(False),
      qgpNumQuarkFlavor = cms.int32(0),  ## number of active quark flavors in qgp; allowed values: 0,1,2,3
      numQuarkFlavor = cms.int32(0), ## to be removed
      doIsospin = cms.bool(True),
      angularSpectrumSelector = cms.int32(0), ## angular emitted gluon spectrum :
      embeddingMode = cms.bool(False),
      backgroundLabel = cms.InputTag("generator"), ## ineffective in no mixing
      doQuench = cms.bool(False),
      bFixed = cms.double(0.0), ## fixed impact param (fm); valid only if cflag_=0
      cFlag = cms.int32(0), ## centrality flag
      bMin = cms.double(0.0), ## min impact param (fm); valid only if cflag_!=0
      bMax = cms.double(0.0), ## max impact param (fm); valid only if cflag_!=0
      pythiaPylistVerbosity = cms.untracked.int32(1),
      pythiaHepMCVerbosity = cms.untracked.bool(True),
      maxEventsToPrint = cms.untracked.int32(0),
      PythiaParameters = cms.PSet(pythiaUESettingsBlock,
         processParameters = cms.vstring('MSEL=0         ! User defined processes', 
            'MSUB(81)  = 1     ! qqbar to QQbar', 
            'MSUB(82)  = 1     ! gg to QQbar', 
            'MSTP(7)   = 6     ! flavor = top', 
            'PMAS(6,1) = 172.5  ! top quark mass', 
            'MDME(190,1) = 1 !W decay into dbar u', 
            'MDME(191,1) = 1 !W decay into dbar c', 
            'MDME(192,1) = 1 !W decay into dbar t', 
            'MDME(194,1) = 1 !W decay into sbar u', 
            'MDME(195,1) = 1 !W decay into sbar c', 
            'MDME(196,1) = 1 !W decay into sbar t', 
            'MDME(198,1) = 1 !W decay into bbar u', 
            'MDME(199,1) = 1 !W decay into bbar c', 
            'MDME(200,1) = 1 !W decay into bbar t', 
            'MDME(205,1) = 1 !W decay into bbar tp', 
            'MDME(206,1) = 1 !W decay into e+ nu_e', 
            'MDME(207,1) = 1 !W decay into mu+ nu_mu', 
            'MDME(208,1) = 1 !W decay into tau+ nu_tau'),
         parameterSets = cms.vstring('pythiaUESettings',
            'processParameters')
         ),
      pythiaUESettings = cms.vstring('MSTU(21)=1     ! Check on possible errors during program execution', 
            'MSTJ(22)=2     ! Decay those unstable particles', 
            'PARJ(71)=10 .  ! for which ctau  10 mm', 
            'MSTP(33)=0     ! no K factors in hard cross sections', 
            'MSTP(2)=1      ! which order running alphaS', 
            'MSTP(51)=10042 ! structure function chosen (external PDF CTEQ6L1)', 
            'MSTP(52)=2     ! work with LHAPDF', 
            'PARP(82)=1.832 ! pt cutoff for multiparton interactions', 
            'PARP(89)=1800. ! sqrts for which PARP82 is set', 
            'PARP(90)=0.275 ! Multiple interactions: rescaling power', 
            'MSTP(95)=6     ! CR (color reconnection parameters)', 
            'PARP(77)=1.016 ! CR', 
            'PARP(78)=0.538 ! CR', 
            'PARP(80)=0.1   ! Prob. colored parton from BBR', 
            'PARP(83)=0.356 ! Multiple interactions: matter distribution parameter', 
            'PARP(84)=0.651 ! Multiple interactions: matter distribution parameter', 
            'PARP(62)=1.025 ! ISR cutoff', 
            'MSTP(91)=1     ! Gaussian primordial kT', 
            'PARP(93)=10.0  ! primordial kT-max', 
            'MSTP(81)=21    ! multiple parton interactions 1 is Pythia default', 
            'MSTP(82)=4     ! Defines the multi-parton model')
      )

ProductionFilterSequence = cms.Sequence(generator)
