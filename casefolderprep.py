# Creates case folder structure

import os

case_folders = ['reports', 'documentation']
evidence_folders = ['acquisition']

case_drive = 'F:\\'
evidence_drive = 'E:\\'

case_number = input('Enter the case number: ')
case_type = input('Enter the type of crime. If blank type NA: ')
case_agent = input('Enter the last name of the requesting agent. If blank type NA: ')
case_name = case_number + '_' + case_type + '_' + case_agent + '\\'

casepath = case_drive + case_name
evidencepath = evidence_drive + case_name

try:
    os.mkdir(casepath)
    print('Created %s'%(casepath))
    os.mkdir(evidencepath)
    print('Created %s'%(evidencepath))
except:
    print('There was an error setting up your case (folder may already exist)')

evidence_number = input('Enter the evidence item number: ')
evidence_number = evidence_number + '\\'

case_itempath = casepath + evidence_number
evidence_itempath = evidencepath + evidence_number

try:
    os.mkdir(case_itempath)
    print('Created %s'%(case_itempath))
except:
    print('There was an error setting up your case (folder may already exist)')

for folder in case_folders:
    pathname = case_itempath + folder
    try:
        os.mkdir(pathname)
        print('Created %s'%(pathname))
    except:
        print('There was an error setting up your case')

try:
    os.mkdir(evidence_itempath)
    print('Created %s'%(evidence_itempath))
except:
    print('There was an error setting up your case (folder may already exist)')

for folder in evidence_folders:
    pathname = evidence_itempath + folder
    try:
        os.mkdir(pathname)
        print('Created %s'%(pathname))
    except:
        print('There was an error setting up your case')

more_evidence = input('Do you have more evidence? [Y/N]: ')

while more_evidence.lower() != 'n':
    evidence_number = input('Enter the evidence item number: ')
    evidence_number = evidence_number + '\\'

    case_itempath = casepath + evidence_number
    print(case_itempath)
    evidence_itempath = evidencepath + evidence_number
    print(evidence_itempath)

    try:
        os.mkdir(case_itempath)
        print('Created %s'%(case_itempath))
    except:
        print('There was an error setting up your case(folder may already exist)')

    for folder in case_folders:
        pathname = case_itempath + folder
        try:
            os.mkdir(pathname)
            print('Created %s'%(pathname))
        except:
            print('There was an error setting up your case(folder may already exist)')

    try:
        os.mkdir(evidence_itempath)
        print('Created %s'%(evidence_itempath))
    except:
        print('There was an error setting up your case (folder may already exist)')

    for folder in evidence_folders:
        pathname = evidence_itempath + folder
        try:
            os.mkdir(pathname)
            print('Created %s'%(pathname))
        except:
            print('There was an error setting up your case (folder may already exist)')
    
    more_evidence = input('Do you have more evidence? [Y/N]: ')
