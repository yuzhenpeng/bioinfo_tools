import argparse
import shutil
import re
import os
import subprocess
from Bio import SeqIO
import pandas as pd
import numpy as np
from pybedtools import BedTool
from pyfaidx import Fasta

LIST = [
'AciJub',
'AcoCah',
'AilFul',
'AilMel',
'AllBul',
'AloPal',
'AmmLer',
'AnoCau',
'AntAme',
'AotNan',
'AplRuf',
'ArtJam',
'AteGeo',
'BalAcu',
'BalBon',
'BeaHun',
'BisBis',
'BosInd',
'BosMut',
'BosTau',
'BraVar',
'BubBub',
'CalDon',
'CalJac',
'CamBac',
'CamDro',
'CamFer',
'CanFam',
'CanLup',
'CapAeg',
'CapHir',
'CapPil',
'CarPer',
'CasCan',
'CatWag',
'CavApe',
'CavPor',
'CavTsc',
'CebAlb',
'CebCap',
'CerAty',
'CerCot',
'CerNeg',
'CerSim',
'ChaVel',
'CheMed',
'ChiLan',
'ChlSab',
'ChoDid',
'ChoHof',
'ChrAsi',
'ColAng',
'ConCri',
'CraTho',
'CriGam',
'CriGri',
'CroInd',
'CryFer',
'CteGun',
'CteSoc',
'CunPac',
'DasNov',
'DasPun',
'DauMad',
'DelLeu',
'DesRot',
'DicBic',
'DicSum',
'DinBra',
'DipOrd',
'DipSte',
'DolPat',
'EchTel',
'EidHel',
'ElaDav',
'EleEdw',
'EllLut',
'EllTal',
'EnhLut',
'EptFus',
'EquAsi',
'EquCab',
'EquPrz',
'EriEur',
'EryPat',
'EscRob',
'EubJap',
'EulFla',
'EulFul',
'FelCat',
'FelNig',
'FukDam',
'GalVar',
'GirTip',
'GliGli',
'GorGor',
'GraMur',
'HelPar',
'HemHyl',
'HetBru',
'HetGla',
'HipAmp',
'HipArm',
'HipGal',
'HomSap',
'HyaHya',
'HydHyd',
'HysCri',
'IctTri',
'IndInd',
'IniGeo',
'JacJac',
'KogBre',
'LasBor',
'LemCat',
'LepAme',
'LepWed',
'LipVex',
'LoxAfr',
'LycPic',
'MacFas',
'MacMul',
'MacNem',
'MacSob',
'ManJav',
'ManLeu',
'ManPen',
'MarMar',
'MegLyr',
'MelCap',
'MerUng',
'MesAur',
'MesBid',
'MicHir',
'MicMur',
'MicOch',
'MicTal',
'MinNat',
'MinSch',
'MirAng',
'MirCoq',
'MolMol',
'MonMon',
'MorBla',
'MosMos',
'MunMun',
'MurFea',
'MusAve',
'MusCar',
'MusMus',
'MusPah',
'MusPut',
'MusSpr',
'MyoBra',
'MyoCoy',
'MyoDav',
'MyoLuc',
'MyoMyo',
'MyrTri',
'NanGal',
'NasLar',
'NeoAsi',
'NeoSch',
'NocLep',
'NomLeu',
'NycCou',
'OchPri',
'OctDeg',
'OdoRos',
'OdoVir',
'OkaJoh',
'OndZib',
'OnyTor',
'OrcOrc',
'OryAfe',
'OryCun',
'OtoGar',
'OviAri',
'OviCan',
'PanHod',
'PanOnc',
'PanPan',
'PanPar',
'PanTig',
'PanTro',
'PapAnu',
'ParHer',
'PerLon',
'PerMan',
'PetTyp',
'PhoPho',
'PhyDis',
'PilTep',
'PipKuh',
'PipPip',
'PitPit',
'PlaGan',
'PonAbe',
'PonBla',
'ProCap',
'ProCoq',
'PsaObe',
'PteAle',
'PteBra',
'PtePar',
'PteVam',
'PumCon',
'PygNem',
'RanTar',
'RatNor',
'RhiBie',
'RhiFer',
'RhiPru',
'RhiRox',
'RhiSin',
'RouAeg',
'SagImp',
'SaiBol',
'SaiTat',
'ScaAqu',
'SemEnt',
'SigHis',
'SolPar',
'SorAra',
'SpeDau',
'SpiGra',
'SurSur',
'SusScr',
'TadBra',
'TamTet',
'TapInd',
'TapTer',
'ThrSwi',
'TolMat',
'TonSau',
'TraJav',
'TriMan',
'TupChi',
'TupTan',
'TurTru',
'UroGra',
'UrsMar',
'VicPac',
'VulLag',
'XerIna',
'ZalCal',
'ZapHud',
'ZipCav'
]


BASEDIR = '/lustre/scratch/daray/orf/'
os.chdir(BASEDIR + 'filtered_LINE_extracts')

for NAME in LIST:
	with open(NAME + '_filtered_LINE_test.fa', 'w+') as OUTFILE:
		SOURCEBED = BASEDIR + 'filtered_LINE_beds/' + NAME + '_filtered_LINE.bed'
		BED = BedTool(SOURCEBED)
		GENOME = BedTool(BASEDIR + 'assemblies/' + NAME + '.fa')
		FASTA = BED.sequence(fi=GENOME)
		FASTASAVE = open(FASTA.seqfn).read()
		OUTFILE.write(FASTASAVE)
