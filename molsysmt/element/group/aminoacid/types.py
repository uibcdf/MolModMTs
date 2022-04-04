# This comes from MDTRAJ, we have to check if there is a place where this can also be found.

name_to_type =  {
    '00C': 'CYS',
    '01W': 'XAA',
    '02K': 'ALA',
    '02L': 'ASN',
    '03Y': 'CYS',
    '07O': 'CYS',
    '08P': 'CYS',
    '0A0': 'ASP',
    '0A1': 'TYR',
    '0A2': 'LYS',
    '0A8': 'CYS',
    '0AA': 'VAL',
    '0AB': 'VAL',
    '0AC': 'GLY',
    '0AF': 'TRP',
    '0AG': 'LEU',
    '0AH': 'SER',
    '0AK': 'ASP',
    '0BN': 'PHE',
    '0CS': 'ALA',
    '0E5': 'THR',
    '0EA': 'TYR',
    '0FL': 'ALA',
    '0NC': 'ALA',
    '0WZ': 'TYR',
    '0Y8': 'PRO',
    '143': 'CYS',
    '193': 'XAA',
    '1OP': 'TYR',
    '1PA': 'PHE',
    '1PI': 'ALA',
    '1TQ': 'TRP',
    '1TY': 'TYR',
    '1X6': 'SER',
    '200': 'PHE',
    '23F': 'PHE',
    '23S': 'XAA',
    '26B': 'THR',
    '2AD': 'XAA',
    '2AG': 'ALA',
    '2AO': 'XAA',
    '2AS': 'XAA',
    '2CO': 'CYS',
    '2DO': 'XAA',
    '2FM': 'MET',
    '2HF': 'HIS',
    '2KK': 'LYS',
    '2KP': 'LYS',
    '2LU': 'LEU',
    '2ML': 'LEU',
    '2MR': 'ARG',
    '2MT': 'PRO',
    '2OR': 'ARG',
    '2PI': 'XAA',
    '2QZ': 'THR',
    '2R3': 'TYR',
    '2SI': 'XAA',
    '2TL': 'THR',
    '2TY': 'TYR',
    '2VA': 'VAL',
    '2XA': 'CYS',
    '32S': 'XAA',
    '32T': 'XAA',
    '33X': 'ALA',
    '3AH': 'HIS',
    '3AR': 'XAA',
    '3CF': 'PHE',
    '3GA': 'ALA',
    '3MD': 'ASP',
    '3NF': 'TYR',
    '3QN': 'LYS',
    '3TY': 'XAA',
    '3XH': 'GLY',
    '4BF': 'TYR',
    '4CF': 'PHE',
    '4CY': 'MET',
    '4DP': 'TRP',
    '4FB': 'PRO',
    '4FW': 'TRP',
    '4HT': 'TRP',
    '4IN': 'TRP',
    '4MM': 'XAA',
    '4PH': 'PHE',
    '4U7': 'ALA',
    '56A': 'HIS',
    '5AB': 'ALA',
    '5CS': 'CYS',
    '5CW': 'TRP',
    '5HP': 'GLU',
    '6CL': 'LYS',
    '6CW': 'TRP',
    '6GL': 'ALA',
    '6HN': 'LYS',
    '7JA': 'ILE',
    '9NE': 'GLU',
    '9NF': 'PHE',
    '9NR': 'ARG',
    '9NV': 'VAL',
    'A5N': 'ASN',
    'A66': 'XAA',
    'AA3': 'ALA',
    'AA4': 'ALA',
    'AAR': 'ARG',
    'AB7': 'XAA',
    'ABA': 'ALA',
    'ACB': 'ASP',
    'ACL': 'ARG',
    'ADD': 'XAA',
    'AEA': 'XAA',
    'AEI': 'ASP',
    'AFA': 'ASN',
    'AGM': 'ARG',
    'AGT': 'CYS',
    'AHB': 'ASN',
    'AHH': 'XAA',
    'AHO': 'ALA',
    'AHP': 'ALA',
    'AHS': 'XAA',
    'AHT': 'XAA',
    'AIB': 'ALA',
    'AKL': 'ASP',
    'AKZ': 'ASP',
    'ALA': 'ALA',
    'ALC': 'ALA',
    'ALM': 'ALA',
    'ALN': 'ALA',
    'ALO': 'THR',
    'ALS': 'ALA',
    'ALT': 'ALA',
    'ALV': 'ALA',
    'ALY': 'LYS',
    'AN8': 'ALA',
    'APE': 'XAA',
    'APH': 'ALA',
    'API': 'LYS',
    'APK': 'LYS',
    'APM': 'XAA',
    'APP': 'XAA',
    'AR2': 'ARG',
    'AR4': 'GLU',
    'AR7': 'ARG',
    'ARG': 'ARG',
    'ARM': 'ARG',
    'ARO': 'ARG',
    'ARV': 'XAA',
    'AS2': 'ASP',
    'AS9': 'XAA',
    'ASA': 'ASP',
    'ASB': 'ASP',
    'ASH': 'ASP',
    'ASI': 'ASP',
    'ASK': 'ASP',
    'ASL': 'ASP',
    'ASM': 'XAA',
    'ASN': 'ASN',
    'ASP': 'ASP',
    'ASQ': 'ASP',
    'ASX': 'ASX',
    'AVN': 'XAA',
    'AYA': 'ALA',
    'AZK': 'LYS',
    'AZS': 'SER',
    'AZY': 'TYR',
    'B1F': 'PHE',
    'B2A': 'ALA',
    'B2F': 'PHE',
    'B2I': 'ILE',
    'B2V': 'VAL',
    'B3A': 'ALA',
    'B3D': 'ASP',
    'B3E': 'GLU',
    'B3K': 'LYS',
    'B3L': 'XAA',
    'B3M': 'XAA',
    'B3Q': 'XAA',
    'B3S': 'SER',
    'B3T': 'XAA',
    'B3U': 'HIS',
    'B3X': 'ASN',
    'B3Y': 'TYR',
    'BB6': 'CYS',
    'BB7': 'CYS',
    'BB8': 'PHE',
    'BB9': 'CYS',
    'BBC': 'CYS',
    'BCS': 'CYS',
    'BE2': 'XAA',
    'BFD': 'ASP',
    'BG1': 'SER',
    'BH2': 'ASP',
    'BHD': 'ASP',
    'BIF': 'PHE',
    'BIL': 'XAA',
    'BIU': 'ILE',
    'BJH': 'XAA',
    'BL2': 'LEU',
    'BLE': 'LEU',
    'BLY': 'LYS',
    'BMT': 'THR',
    'BNN': 'PHE',
    'BNO': 'XAA',
    'BOR': 'ARG',
    'BPE': 'CYS',
    'BSE': 'SER',
    'BTA': 'LEU',
    'BTC': 'CYS',
    'BTR': 'TRP',
    'BUC': 'CYS',
    'BUG': 'VAL',
    'C1X': 'LYS',
    'C22': 'ALA',
    'C3Y': 'CYS',
    'C4R': 'CYS',
    'C5C': 'CYS',
    'C66': 'XAA',
    'C6C': 'CYS',
    'CAF': 'CYS',
    'CAL': 'XAA',
    'CAS': 'CYS',
    'CAV': 'XAA',
    'CAY': 'CYS',
    'CCL': 'LYS',
    'CCS': 'CYS',
    'CDE': 'XAA',
    'CDV': 'XAA',
    'CEA': 'CYS',
    'CGA': 'GLU',
    'CGU': 'GLU',
    'CHF': 'XAA',
    'CHG': 'XAA',
    'CHP': 'GLY',
    'CHS': 'XAA',
    'CIR': 'ARG',
    'CLE': 'LEU',
    'CLG': 'LYS',
    'CLH': 'LYS',
    'CME': 'CYS',
    'CMH': 'CYS',
    'CML': 'CYS',
    'CMT': 'CYS',
    'CPC': 'XAA',
    'CPI': 'XAA',
    'CR5': 'GLY',
    'CS0': 'CYS',
    'CS1': 'CYS',
    'CS3': 'CYS',
    'CS4': 'CYS',
    'CSA': 'CYS',
    'CSB': 'CYS',
    'CSD': 'CYS',
    'CSE': 'CYS',
    'CSJ': 'CYS',
    'CSO': 'CYS',
    'CSP': 'CYS',
    'CSR': 'CYS',
    'CSS': 'CYS',
    'CSU': 'CYS',
    'CSW': 'CYS',
    'CSX': 'CYS',
    'CSZ': 'CYS',
    'CTE': 'TRP',
    'CTH': 'THR',
    'CUC': 'XAA',
    'CWR': 'SER',
    'CXM': 'MET',
    'CY0': 'CYS',
    'CY1': 'CYS',
    'CY3': 'CYS',
    'CY4': 'CYS',
    'CYA': 'CYS',
    'CYD': 'CYS',
    'CYF': 'CYS',
    'CYG': 'CYS',
    'CYJ': 'LYS',
    'CYM': 'CYS',
    'CYQ': 'CYS',
    'CYR': 'CYS',
    'CYS': 'CYS',
    'CZ2': 'CYS',
    'CZZ': 'CYS',
    'D11': 'THR',
    'D3P': 'GLY',
    'D4P': 'XAA',
    'DA2': 'XAA',
    'DAB': 'ALA',
    'DAH': 'PHE',
    'DAL': 'ALA',
    'DAR': 'ARG',
    'DAS': 'ASP',
    'DBB': 'THR',
    'DBS': 'SER',
    'DBU': 'THR',
    'DBY': 'TYR',
    'DBZ': 'ALA',
    'DC2': 'CYS',
    'DCL': 'XAA',
    'DCY': 'CYS',
    'DDE': 'HIS',
    'DFI': 'XAA',
    'DFO': 'XAA',
    'DGH': 'GLY',
    'DGL': 'GLU',
    'DGN': 'GLN',
    'DHA': 'SER',
    'DHI': 'HIS',
    'DHL': 'XAA',
    'DHN': 'VAL',
    'DHP': 'XAA',
    'DHV': 'VAL',
    'DI7': 'TYR',
    'DIL': 'ILE',
    'DIR': 'ARG',
    'DIV': 'VAL',
    'DLE': 'LEU',
    'DLS': 'LYS',
    'DLY': 'LYS',
    'DM0': 'LYS',
    'DMH': 'ASN',
    'DMK': 'ASP',
    'DMT': 'XAA',
    'DNE': 'LEU',
    'DNL': 'LYS',
    'DNP': 'ALA',
    'DNS': 'LYS',
    'DOA': 'XAA',
    'DOH': 'ASP',
    'DON': 'LEU',
    'DPL': 'PRO',
    'DPN': 'PHE',
    'DPP': 'ALA',
    'DPQ': 'TYR',
    'DPR': 'PRO',
    'DSE': 'SER',
    'DSG': 'ASN',
    'DSN': 'SER',
    'DSP': 'ASP',
    'DTH': 'THR',
    'DTR': 'TRP',
    'DTY': 'TYR',
    'DVA': 'VAL',
    'DYS': 'CYS',
    'ECC': 'GLN',
    'EFC': 'CYS',
    'EHP': 'PHE',
    'ESB': 'TYR',
    'ESC': 'MET',
    'EXY': 'LEU',
    'EYS': 'XAA',
    'F2F': 'PHE',
    'FAK': 'LYS',
    'FB5': 'ALA',
    'FB6': 'ALA',
    'FCL': 'PHE',
    'FGA': 'GLU',
    'FGL': 'GLY',
    'FGP': 'SER',
    'FH7': 'LYS',
    'FHL': 'LYS',
    'FHO': 'LYS',
    'FLA': 'ALA',
    'FLE': 'LEU',
    'FLT': 'TYR',
    'FME': 'MET',
    'FOE': 'CYS',
    'FP9': 'PRO',
    'FRD': 'XAA',
    'FT6': 'TRP',
    'FTR': 'TRP',
    'FTY': 'TYR',
    'FVA': 'VAL',
    'FZN': 'LYS',
    'GAU': 'GLU',
    'GCM': 'XAA',
    'GFT': 'SER',
    'GGL': 'GLU',
    'GHG': 'GLN',
    'GHP': 'GLY',
    'GL3': 'GLY',
    'GLH': 'GLN',
    'GLJ': 'GLU',
    'GLK': 'GLU',
    'GLM': 'XAA',
    'GLN': 'GLN',
    'GLQ': 'GLU',
    'GLU': 'GLU',
    'GLX': 'GLX',
    'GLY': 'GLY',
    'GLZ': 'GLY',
    'GMA': 'GLU',
    'GND': 'XAA',
    'GPL': 'LYS',
    'GSC': 'GLY',
    'GSU': 'GLU',
    'GT9': 'CYS',
    'GVL': 'SER',
    'H14': 'PHE',
    'H5M': 'PRO',
    'HAC': 'ALA',
    'HAR': 'ARG',
    'HBN': 'HIS',
    'HCS': 'XAA',
    'HFA': 'XAA',
    'HGL': 'XAA',
    'HHI': 'HIS',
    'HIA': 'HIS',
    'HIC': 'HIS',
    'HIP': 'HIS',
    'HIQ': 'HIS',
    'HIS': 'HIS',
    'HL2': 'LEU',
    'HLU': 'LEU',
    'HMR': 'ARG',
    'HPC': 'PHE',
    'HPE': 'PHE',
    'HPH': 'PHE',
    'HPQ': 'PHE',
    'HQA': 'ALA',
    'HRG': 'ARG',
    'HRP': 'TRP',
    'HS8': 'HIS',
    'HS9': 'HIS',
    'HSE': 'SER',
    'HSL': 'SER',
    'HSO': 'HIS',
    'HTI': 'CYS',
    'HTN': 'ASN',
    'HTR': 'TRP',
    'HV5': 'ALA',
    'HVA': 'VAL',
    'HY3': 'PRO',
    'HYP': 'PRO',
    'HZP': 'PRO',
    'I2M': 'ILE',
    'I58': 'LYS',
    'IAM': 'ALA',
    'IAR': 'ARG',
    'IAS': 'ASP',
    'IEL': 'LYS',
    'IGL': 'GLY',
    'IIL': 'ILE',
    'ILE': 'ILE',
    'ILG': 'GLU',
    'ILX': 'ILE',
    'IML': 'ILE',
    'IOY': 'PHE',
    'IPG': 'GLY',
    'IT1': 'LYS',
    'IYR': 'TYR',
    'IYT': 'THR',
    'IZO': 'MET',
    'JJJ': 'CYS',
    'JJK': 'CYS',
    'JJL': 'CYS',
    'K1R': 'CYS',
    'KCX': 'LYS',
    'KGC': 'LYS',
    'KNB': 'ALA',
    'KOR': 'MET',
    'KPI': 'LYS',
    'KST': 'LYS',
    'KYN': 'TRP',
    'KYQ': 'LYS',
    'L2A': 'XAA',
    'LA2': 'LYS',
    'LAA': 'ASP',
    'LAL': 'ALA',
    'LBY': 'LYS',
    'LCK': 'LYS',
    'LCX': 'LYS',
    'LCZ': 'XAA',
    'LDH': 'LYS',
    'LED': 'LEU',
    'LEF': 'LEU',
    'LEH': 'LEU',
    'LEI': 'VAL',
    'LEM': 'LEU',
    'LEN': 'LEU',
    'LET': 'LYS',
    'LEU': 'LEU',
    'LEX': 'LEU',
    'LHC': 'XAA',
    'LLP': 'LYS',
    'LLY': 'LYS',
    'LME': 'GLU',
    'LMF': 'LYS',
    'LMQ': 'GLN',
    'LP6': 'LYS',
    'LPD': 'PRO',
    'LPG': 'GLY',
    'LPL': 'XAA',
    'LPS': 'SER',
    'LSO': 'LYS',
    'LTA': 'XAA',
    'LTR': 'TRP',
    'LVG': 'GLY',
    'LVN': 'VAL',
    'LYF': 'LYS',
    'LYK': 'LYS',
    'LYM': 'LYS',
    'LYN': 'LYS',
    'LYR': 'LYS',
    'LYS': 'LYS',
    'LYX': 'LYS',
    'LYZ': 'LYS',
    'M0H': 'CYS',
    'M2L': 'LYS',
    'M2S': 'MET',
    'M30': 'GLY',
    'M3L': 'LYS',
    'MA':  'ALA',
    'MAA': 'ALA',
    'MAI': 'ARG',
    'MBQ': 'TYR',
    'MC1': 'SER',
    'MCG': 'XAA',
    'MCL': 'LYS',
    'MCS': 'CYS',
    'MD3': 'CYS',
    'MD6': 'GLY',
    'MDF': 'TYR',
    'MDH': 'XAA',
    'MEA': 'PHE',
    'MED': 'MET',
    'MEG': 'GLU',
    'MEN': 'ASN',
    'MEQ': 'GLN',
    'MET': 'MET',
    'MEU': 'GLY',
    'MF3': 'XAA',
    'MGG': 'ARG',
    'MGN': 'GLN',
    'MGY': 'GLY',
    'MHL': 'LEU',
    'MHO': 'MET',
    'MHS': 'HIS',
    'MIS': 'SER',
    'MK8': 'LEU',
    'ML3': 'LYS',
    'MLE': 'LEU',
    'MLL': 'LEU',
    'MLY': 'LYS',
    'MLZ': 'LYS',
    'MME': 'MET',
    'MMO': 'ARG',
    'MND': 'ASN',
    'MNL': 'LEU',
    'MNV': 'VAL',
    'MOD': 'XAA',
    'MP8': 'PRO',
    'MPH': 'XAA',
    'MPJ': 'XAA',
    'MPQ': 'GLY',
    'MSA': 'GLY',
    'MSE': 'MET',
    'MSL': 'MET',
    'MSO': 'MET',
    'MSP': 'XAA',
    'MT2': 'MET',
    'MTY': 'TYR',
    'MVA': 'VAL',
    'N10': 'SER',
    'N2C': 'XAA',
    'N7P': 'PRO',
    'N80': 'PRO',
    'N8P': 'PRO',
    'NA8': 'ALA',
    'NAL': 'ALA',
    'NAM': 'ALA',
    'NB8': 'ASN',
    'NBQ': 'TYR',
    'NC1': 'SER',
    'NCB': 'ALA',
    'NCY': 'XAA',
    'NDF': 'PHE',
    'NEM': 'HIS',
    'NEP': 'HIS',
    'NFA': 'PHE',
    'NHL': 'GLU',
    'NIY': 'TYR',
    'NLE': 'LEU',
    'NLN': 'LEU',
    'NLO': 'LEU',
    'NLP': 'LEU',
    'NLQ': 'GLN',
    'NMC': 'GLY',
    'NMM': 'ARG',
    'NNH': 'ARG',
    'NPH': 'CYS',
    'NPI': 'ALA',
    'NSK': 'XAA',
    'NTR': 'TYR',
    'NTY': 'TYR',
    'NVA': 'VAL',
    'NYS': 'CYS',
    'NZH': 'HIS',
    'O12': 'XAA',
    'OAR': 'ARG',
    'OAS': 'SER',
    'OBF': 'XAA',
    'OBS': 'LYS',
    'OCS': 'CYS',
    'OCY': 'CYS',
    'OHI': 'HIS',
    'OHS': 'ASP',
    'OIC': 'XAA',
    'OLE': 'XAA',
    'OLT': 'THR',
    'OLZ': 'SER',
    'OMT': 'MET',
    'ONH': 'ALA',
    'ONL': 'XAA',
    'OPR': 'ARG',
    'ORN': 'ALA',
    'ORQ': 'ARG',
    'OSE': 'SER',
    'OTB': 'XAA',
    'OTH': 'THR',
    'OXX': 'ASP',
    'P1L': 'CYS',
    'P2Y': 'PRO',
    'PAQ': 'TYR',
    'PAS': 'ASP',
    'PAT': 'TRP',
    'PAU': 'ALA',
    'PBB': 'CYS',
    'PBF': 'PHE',
    'PCA': 'GLU',
    'PCC': 'PRO',
    'PCE': 'XAA',
    'PCS': 'PHE',
    'PDL': 'XAA',
    'PEC': 'CYS',
    'PF5': 'PHE',
    'PFF': 'PHE',
    'PFX': 'XAA',
    'PG1': 'SER',
    'PG9': 'GLY',
    'PGL': 'XAA',
    'PGY': 'GLY',
    'PH6': 'PRO',
    'PHA': 'PHE',
    'PHD': 'ASP',
    'PHE': 'PHE',
    'PHI': 'PHE',
    'PHL': 'PHE',
    'PHM': 'PHE',
    'PIV': 'XAA',
    'PLE': 'LEU',
    'PM3': 'PHE',
    'POM': 'PRO',
    'PPN': 'PHE',
    'PR3': 'CYS',
    'PR9': 'PRO',
    'PRO': 'PRO',
    'PRS': 'PRO',
    'PSA': 'PHE',
    'PSH': 'HIS',
    'PTA': 'XAA',
    'PTH': 'TYR',
    'PTM': 'TYR',
    'PTR': 'TYR',
    'PVH': 'HIS',
    'PVL': 'XAA',
    'PYA': 'ALA',
    'PYL': 'PYL',
    'PYX': 'CYS',
    'QCS': 'CYS',
    'QMM': 'GLN',
    'QPA': 'CYS',
    'QPH': 'PHE',
    'R1A': 'CYS',
    'R4K': 'TRP',
    'RE0': 'TRP',
    'RE3': 'TRP',
    'RON': 'XAA',
    'RVX': 'SER',
    'RZ4': 'SER',
    'S1H': 'SER',
    'S2C': 'CYS',
    'S2D': 'ALA',
    'S2P': 'ALA',
    'SAC': 'SER',
    'SAH': 'CYS',
    'SAR': 'GLY',
    'SBL': 'SER',
    'SCH': 'CYS',
    'SCS': 'CYS',
    'SCY': 'CYS',
    'SD2': 'XAA',
    'SDP': 'SER',
    'SE7': 'ALA',
    'SEB': 'SER',
    'SEC': 'SEC',
    'SEG': 'ALA',
    'SEL': 'SER',
    'SEM': 'SER',
    'SEN': 'SER',
    'SEP': 'SER',
    'SER': 'SER',
    'SET': 'SER',
    'SGB': 'SER',
    'SHC': 'CYS',
    'SHP': 'GLY',
    'SHR': 'LYS',
    'SIB': 'CYS',
    'SLR': 'PRO',
    'SLZ': 'LYS',
    'SMC': 'CYS',
    'SME': 'MET',
    'SMF': 'PHE',
    'SNC': 'CYS',
    'SNN': 'ASN',
    'SOC': 'CYS',
    'SOY': 'SER',
    'SRZ': 'SER',
    'STY': 'TYR',
    'SUB': 'XAA',
    'SUN': 'SER',
    'SVA': 'SER',
    'SVV': 'SER',
    'SVW': 'SER',
    'SVX': 'SER',
    'SVY': 'SER',
    'SVZ': 'SER',
    'SYS': 'CYS',
    'T11': 'PHE',
    'T66': 'XAA',
    'TA4': 'XAA',
    'TAV': 'ASP',
    'TBG': 'VAL',
    'TBM': 'THR',
    'TCQ': 'TYR',
    'TCR': 'TRP',
    'TDD': 'LEU',
    'TFQ': 'PHE',
    'TH6': 'THR',
    'THC': 'THR',
    'THO': 'XAA',
    'THR': 'THR',
    'THZ': 'ARG',
    'TIH': 'ALA',
    'TMB': 'THR',
    'TMD': 'THR',
    'TNB': 'CYS',
    'TNR': 'SER',
    'TOQ': 'TRP',
    'TPH': 'XAA',
    'TPL': 'TRP',
    'TPO': 'THR',
    'TPQ': 'TYR',
    'TQI': 'TRP',
    'TQQ': 'TRP',
    'TRF': 'TRP',
    'TRG': 'LYS',
    'TRN': 'TRP',
    'TRO': 'TRP',
    'TRP': 'TRP',
    'TRQ': 'TRP',
    'TRW': 'TRP',
    'TRX': 'TRP',
    'TRY': 'TRP',
    'TST': 'XAA',
    'TTQ': 'TRP',
    'TTS': 'TYR',
    'TXY': 'TYR',
    'TY1': 'TYR',
    'TY2': 'TYR',
    'TY3': 'TYR',
    'TY5': 'TYR',
    'TYB': 'TYR',
    'TYI': 'TYR',
    'TYJ': 'TYR',
    'TYN': 'TYR',
    'TYO': 'TYR',
    'TYQ': 'TYR',
    'TYR': 'TYR',
    'TYS': 'TYR',
    'TYT': 'TYR',
    'TYW': 'TYR',
    'TYX': 'XAA',
    'TYY': 'TYR',
    'TZB': 'XAA',
    'TZO': 'XAA',
    'UMA': 'ALA',
    'UN1': 'XAA',
    'UN2': 'XAA',
    'UNK': 'XAA',
    'VAD': 'VAL',
    'VAF': 'VAL',
    'VAL': 'VAL',
    'VB1': 'LYS',
    'VDL': 'XAA',
    'VLL': 'XAA',
    'VLM': 'XAA',
    'VMS': 'XAA',
    'VOL': 'XAA',
    'WLU': 'LEU',
    'WPA': 'PHE',
    'WRP': 'TRP',
    'WVL': 'VAL',
    'X2W': 'GLU',
    'XCN': 'CYS',
    'XCP': 'XAA',
    'XDT': 'THR',
    'XPL': 'PYL',
    'XPR': 'PRO',
    'XSN': 'ASN',
    'XX1': 'LYS',
    'YCM': 'CYS',
    'YOF': 'TYR',
    'YTH': 'THR',
    'Z01': 'ALA',
    'ZAL': 'ALA',
    'ZCL': 'PHE',
    'ZFB': 'XAA',
    'ZU0': 'THR',
    'ZZJ': 'ALA'
    }

