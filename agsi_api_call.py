import requests
import pandas as pd
import time
import yaml
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

with open("config.yml", "r") as stream:
    try:
        credentials = yaml.safe_load(stream)
        api_key = (credentials['credentials']['key'])
    except yaml.YAMLError as exc:
        api_key = None
        print(exc)

request_list = [
    {
'company_name' : 'astora GmbH',
'short_name' : 'astora',
'company' : '21X000000001160J',
'country' : 'AT',
'facility' : '21W000000000078N',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'astora GmbH',
'short_name' : 'astora',
'company' : '21X000000001160J',
'country' : 'AT',
'facility' : '21W000000000078N',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'GSA LLC',
'short_name' : 'GSA',
'company' : '25X-GSALLC-----E',
'country' : 'AT',
'facility' : '25W-SPHAID-GAZ-M',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'GSA LLC',
'short_name' : 'GSA',
'company' : '25X-GSALLC-----E',
'country' : 'AT',
'facility' : '25W-SPHAID-GAZ-M',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'OMV Gas Storage GmbH',
'short_name' : 'OMV Gas Storage',
'company' : '25X-OMVGASSTORA5',
'country' : 'AT',
'facility' : '21W000000000081Y',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'OMV Gas Storage GmbH',
'short_name' : 'OMV Gas Storage',
'company' : '25X-OMVGASSTORA5',
'country' : 'AT',
'facility' : '21W000000000081Y',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'RAG Energy Storage',
'short_name' : 'RAG Energy Storage',
'company' : '23X----100225-1C',
'country' : 'AT',
'facility' : '21W000000000079L',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'RAG Energy Storage',
'short_name' : 'RAG Energy Storage',
'company' : '23X----100225-1C',
'country' : 'AT',
'facility' : '21W000000000079L',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'Uniper Energy Storage GmbH',
'short_name' : 'Uniper Energy Storage (AT)',
'company' : '21X000000001127H',
'country' : 'AT',
'facility' : '21W000000000057V',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'Uniper Energy Storage GmbH',
'short_name' : 'Uniper Energy Storage (AT)',
'company' : '21X000000001127H',
'country' : 'AT',
'facility' : '21W000000000057V',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'Fluxys Belgium S.A.',
'short_name' : 'Fluxys',
'company' : '21X-BE-A-A0A0A-Y',
'country' : 'BE',
'facility' : '21Z000000000102A',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'Fluxys Belgium S.A.',
'short_name' : 'Fluxys',
'company' : '21X-BE-A-A0A0A-Y',
'country' : 'BE',
'facility' : '21Z000000000102A',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'Bulgartransgaz EAD',
'short_name' : 'Bulgartransgaz',
'company' : '21X-BG-A-A0A0A-C',
'country' : 'BG',
'facility' : '21W000000000031C',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'Bulgartransgaz EAD',
'short_name' : 'Bulgartransgaz',
'company' : '21X-BG-A-A0A0A-C',
'country' : 'BG',
'facility' : '21W000000000031C',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'Podzemno skladište plina d.o.o.',
'short_name' : 'PSP',
'company' : '31X-PSP-OSS-HR-D',
'country' : 'HR',
'facility' : '21W000000000077P',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'Podzemno skladište plina d.o.o.',
'short_name' : 'PSP',
'company' : '31X-PSP-OSS-HR-D',
'country' : 'HR',
'facility' : '21W000000000077P',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'MND Energy Storage a.s.',
'short_name' : 'MND Energy Storage',
'company' : '27XG-MNDGS-CZ--R',
'country' : 'CZ',
'facility' : '21W000000000075T',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'MND Energy Storage a.s.',
'short_name' : 'MND Energy Storage',
'company' : '27XG-MNDGS-CZ--R',
'country' : 'CZ',
'facility' : '21W000000000075T',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'RWE Gas Storage CZ, s.r.o.',
'short_name' : 'RWE Gas Storage CZ',
'company' : '27XG-RWE-GAS-STI',
'country' : 'CZ',
'facility' : '21W000000000076R',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'RWE Gas Storage CZ, s.r.o.',
'short_name' : 'RWE Gas Storage CZ',
'company' : '27XG-RWE-GAS-STI',
'country' : 'CZ',
'facility' : '21W000000000076R',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'SPP Storage',
'short_name' : 'SPP Storage',
'company' : '27X-SPPSTORAGE-R',
'country' : 'CZ',
'facility' : '21W000000000074V',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'SPP Storage',
'short_name' : 'SPP Storage',
'company' : '27X-SPPSTORAGE-R',
'country' : 'CZ',
'facility' : '21W000000000074V',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'Gas Storage Denmark',
'short_name' : 'GSD',
'company' : '21X000000001104T',
'country' : 'DK',
'facility' : '45W000000000112V',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'Gas Storage Denmark',
'short_name' : 'GSD',
'company' : '21X000000001104T',
'country' : 'DK',
'facility' : '45W000000000112V',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'Storengy S.A.',
'short_name' : 'Storengy',
'company' : '21X000000001083B',
'country' : 'FR',
'facility' : '21W000000000073X',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'Storengy S.A.',
'short_name' : 'Storengy',
'company' : '21X000000001083B',
'country' : 'FR',
'facility' : '21W000000000073X',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'Storengy S.A.',
'short_name' : 'Storengy',
'company' : '21X000000001083B',
'country' : 'FR',
'facility' : '21W000000000072Z',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'Storengy S.A.',
'short_name' : 'Storengy',
'company' : '21X000000001083B',
'country' : 'FR',
'facility' : '21W000000000072Z',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'Storengy S.A.',
'short_name' : 'Storengy',
'company' : '21X000000001083B',
'country' : 'FR',
'facility' : '21W0000000000710',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'Storengy S.A.',
'short_name' : 'Storengy',
'company' : '21X000000001083B',
'country' : 'FR',
'facility' : '21W0000000000710',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'Storengy S.A.',
'short_name' : 'Storengy',
'company' : '21X000000001083B',
'country' : 'FR',
'facility' : '21W0000000000702',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'Storengy S.A.',
'short_name' : 'Storengy',
'company' : '21X000000001083B',
'country' : 'FR',
'facility' : '21W0000000000702',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'Storengy S.A.',
'short_name' : 'Storengy',
'company' : '21X000000001083B',
'country' : 'FR',
'facility' : '21W000000000069O',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'Storengy S.A.',
'short_name' : 'Storengy',
'company' : '21X000000001083B',
'country' : 'FR',
'facility' : '21W000000000069O',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'Storengy S.A.',
'short_name' : 'Storengy',
'company' : '21X000000001083B',
'country' : 'FR',
'facility' : '21W000000000084S',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'Storengy S.A.',
'short_name' : 'Storengy',
'company' : '21X000000001083B',
'country' : 'FR',
'facility' : '21W000000000084S',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'Storengy S.A.',
'short_name' : 'Storengy',
'company' : '21X000000001083B',
'country' : 'FR',
'facility' : '63W197197128864M',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'Storengy S.A.',
'short_name' : 'Storengy',
'company' : '21X000000001083B',
'country' : 'FR',
'facility' : '63W197197128864M',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'Teréga S.A.',
'short_name' : 'Teréga',
'company' : '21X-FR-B-A0A0A-J',
'country' : 'FR',
'facility' : '21W000000000068Q',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'Teréga S.A.',
'short_name' : 'Teréga',
'company' : '21X-FR-B-A0A0A-J',
'country' : 'FR',
'facility' : '21W000000000068Q',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'astora GmbH',
'short_name' : 'astora (Germany)',
'company' : '21X000000001160J',
'country' : 'DE',
'facility' : '21Z000000000271O',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'astora GmbH',
'short_name' : 'astora (Germany)',
'company' : '21X000000001160J',
'country' : 'DE',
'facility' : '21Z000000000271O',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'astora GmbH',
'short_name' : 'astora (Germany)',
'company' : '21X000000001160J',
'country' : 'DE',
'facility' : '21W0000000001148',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'astora GmbH',
'short_name' : 'astora (Germany)',
'company' : '21X000000001160J',
'country' : 'DE',
'facility' : '21W0000000001148',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'astora GmbH',
'short_name' : 'astora (Germany)',
'company' : '21X000000001160J',
'country' : 'DE',
'facility' : '21W0000000001261',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'astora GmbH',
'short_name' : 'astora (Germany)',
'company' : '21X000000001160J',
'country' : 'DE',
'facility' : '21W0000000001261',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'bayernugs GmbH',
'short_name' : 'bayernugs',
'company' : '37X0000000000151',
'country' : 'DE',
'facility' : '21W0000000000184',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'bayernugs GmbH',
'short_name' : 'bayernugs',
'company' : '37X0000000000151',
'country' : 'DE',
'facility' : '21W0000000000184',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'Berliner Erdgasspeicher GmbH & Co. KG',
'short_name' : 'BES',
'company' : '37X0000000000224',
'country' : 'DE',
'facility' : '21W0000000001083',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'Berliner Erdgasspeicher GmbH & Co. KG',
'short_name' : 'BES',
'company' : '37X0000000000224',
'country' : 'DE',
'facility' : '21W0000000001083',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'EDF Gas Deutschland GmbH',
'short_name' : 'EDF Gas Deutschland',
'company' : '37X000000000152S',
'country' : 'DE',
'facility' : '37W000000000003M',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'EDF Gas Deutschland GmbH',
'short_name' : 'EDF Gas Deutschland',
'company' : '37X000000000152S',
'country' : 'DE',
'facility' : '37W000000000003M',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'EnBW Etzel Speicher GmbH',
'short_name' : 'EnBW Etzel Speicher',
'company' : '11X0-0000-0667-8',
'country' : 'DE',
'facility' : '11W0-0000-0432-M',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'EnBW Etzel Speicher GmbH',
'short_name' : 'EnBW Etzel Speicher',
'company' : '11X0-0000-0667-8',
'country' : 'DE',
'facility' : '11W0-0000-0432-M',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'Eneco Gasspeicher BV',
'short_name' : 'Eneco Gasspeicher',
'company' : '21X0000000010849',
'country' : 'DE',
'facility' : '21W000000000012G',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'Eneco Gasspeicher BV',
'short_name' : 'Eneco Gasspeicher',
'company' : '21X0000000010849',
'country' : 'DE',
'facility' : '21W000000000012G',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'Equinor Storage Deutschland GmbH',
'short_name' : 'Equinor Storage Deutschland',
'company' : '21X000000001368W',
'country' : 'DE',
'facility' : '21W000000000100J',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'Equinor Storage Deutschland GmbH',
'short_name' : 'Equinor Storage Deutschland',
'company' : '21X000000001368W',
'country' : 'DE',
'facility' : '21W000000000100J',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'Erdgasspeicher Peissen GmbH',
'short_name' : 'Erdgasspeicher Peissen',
'company' : '21X000000001297T',
'country' : 'DE',
'facility' : '21W0000000000281',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'Erdgasspeicher Peissen GmbH',
'short_name' : 'Erdgasspeicher Peissen',
'company' : '21X000000001297T',
'country' : 'DE',
'facility' : '21W0000000000281',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'Etzel-Kavernenbetriebsgesellschaft GmbH & Co. KG',
'short_name' : 'EKB',
'company' : '21X000000001080H',
'country' : 'DE',
'facility' : '21Z000000000291I',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'Etzel-Kavernenbetriebsgesellschaft GmbH & Co. KG',
'short_name' : 'EKB',
'company' : '21X000000001080H',
'country' : 'DE',
'facility' : '21Z000000000291I',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'EWE Gasspeicher GmbH',
'short_name' : 'EWE Gasspeicher',
'company' : '21X0000000011756',
'country' : 'DE',
'facility' : '21W0000000001075',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'EWE Gasspeicher GmbH',
'short_name' : 'EWE Gasspeicher',
'company' : '21X0000000011756',
'country' : 'DE',
'facility' : '21W0000000001075',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'EWE Gasspeicher GmbH',
'short_name' : 'EWE Gasspeicher',
'company' : '21X0000000011756',
'country' : 'DE',
'facility' : '21W000000000048W',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'EWE Gasspeicher GmbH',
'short_name' : 'EWE Gasspeicher',
'company' : '21X0000000011756',
'country' : 'DE',
'facility' : '21W000000000048W',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'EWE Gasspeicher GmbH',
'short_name' : 'EWE Gasspeicher',
'company' : '21X0000000011756',
'country' : 'DE',
'facility' : '21W000000000104B',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'EWE Gasspeicher GmbH',
'short_name' : 'EWE Gasspeicher',
'company' : '21X0000000011756',
'country' : 'DE',
'facility' : '21W000000000104B',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'EWE Gasspeicher GmbH',
'short_name' : 'EWE Gasspeicher',
'company' : '21X0000000011756',
'country' : 'DE',
'facility' : '21W000000000103D',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'EWE Gasspeicher GmbH',
'short_name' : 'EWE Gasspeicher',
'company' : '21X0000000011756',
'country' : 'DE',
'facility' : '21W000000000103D',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'EWE Gasspeicher GmbH',
'short_name' : 'EWE Gasspeicher',
'company' : '21X0000000011756',
'country' : 'DE',
'facility' : '21W0000000001067',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'EWE Gasspeicher GmbH',
'short_name' : 'EWE Gasspeicher',
'company' : '21X0000000011756',
'country' : 'DE',
'facility' : '21W0000000001067',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'EWE Gasspeicher GmbH',
'short_name' : 'EWE Gasspeicher',
'company' : '21X0000000011756',
'country' : 'DE',
'facility' : '21W0000000000508',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'EWE Gasspeicher GmbH',
'short_name' : 'EWE Gasspeicher',
'company' : '21X0000000011756',
'country' : 'DE',
'facility' : '21W0000000000508',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'EWE Gasspeicher GmbH',
'short_name' : 'EWE Gasspeicher',
'company' : '21X0000000011756',
'country' : 'DE',
'facility' : 'PRIOR_EWE_000001',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'EWE Gasspeicher GmbH',
'short_name' : 'EWE Gasspeicher',
'company' : '21X0000000011756',
'country' : 'DE',
'facility' : 'PRIOR_EWE_000001',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'EWE Gasspeicher GmbH',
'short_name' : 'EWE Gasspeicher',
'company' : '21X0000000011756',
'country' : 'DE',
'facility' : '37W000000000002O',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'EWE Gasspeicher GmbH',
'short_name' : 'EWE Gasspeicher',
'company' : '21X0000000011756',
'country' : 'DE',
'facility' : '37W000000000002O',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'HanseWerk AG',
'short_name' : 'HanseWerk',
'company' : '21X0000000013805',
'country' : 'DE',
'facility' : '21W000000000020H',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'HanseWerk AG',
'short_name' : 'HanseWerk',
'company' : '21X0000000013805',
'country' : 'DE',
'facility' : '21W000000000020H',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'Kommunale Gasspeichergesellschaft Epe mbH & Co. KG',
'short_name' : 'KGE',
'company' : '21X000000001140P',
'country' : 'DE',
'facility' : '21W000000000097J',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'Kommunale Gasspeichergesellschaft Epe mbH & Co. KG',
'short_name' : 'KGE',
'company' : '21X000000001140P',
'country' : 'DE',
'facility' : '21W000000000097J',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'MND Energy Storage Germany GmbH',
'short_name' : 'MND Energy Storage Germany',
'company' : '37X000000000042Z',
'country' : 'DE',
'facility' : '21W000000000064Y',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'MND Energy Storage Germany GmbH',
'short_name' : 'MND Energy Storage Germany',
'company' : '37X000000000042Z',
'country' : 'DE',
'facility' : '21W000000000064Y',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'MND Energy Storage Germany GmbH',
'short_name' : 'MND Energy Storage Germany',
'company' : '37X000000000042Z',
'country' : 'DE',
'facility' : '21W0000000000621',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'MND Energy Storage Germany GmbH',
'short_name' : 'MND Energy Storage Germany',
'company' : '37X000000000042Z',
'country' : 'DE',
'facility' : '21W0000000000621',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'MND Energy Storage Germany GmbH',
'short_name' : 'MND Energy Storage Germany',
'company' : '37X000000000042Z',
'country' : 'DE',
'facility' : '37Y000000000386Q',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'MND Energy Storage Germany GmbH',
'short_name' : 'MND Energy Storage Germany',
'company' : '37X000000000042Z',
'country' : 'DE',
'facility' : '37Y000000000386Q',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'NAFTA Speicher Inzenham GmbH',
'short_name' : 'NAFTA Speicher Inzenham',
'company' : '21X0000000011748',
'country' : 'DE',
'facility' : '21W0000000000192',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'NAFTA Speicher Inzenham GmbH',
'short_name' : 'NAFTA Speicher Inzenham',
'company' : '21X0000000011748',
'country' : 'DE',
'facility' : '21W0000000000192',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'NUON Epe Gasspeicher GmbH',
'short_name' : 'NUON Epe Gasspeicher',
'company' : '37X0000000000119',
'country' : 'DE',
'facility' : '21W000000000005D',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'NUON Epe Gasspeicher GmbH',
'short_name' : 'NUON Epe Gasspeicher',
'company' : '37X0000000000119',
'country' : 'DE',
'facility' : '21W000000000005D',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'OMV Gas Storage Germany GmbH',
'short_name' : 'OMV Gas Storage Germany',
'company' : '25X-OMVGASSTORA5',
'country' : 'DE',
'facility' : '21W000000000056X',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'OMV Gas Storage Germany GmbH',
'short_name' : 'OMV Gas Storage Germany',
'company' : '25X-OMVGASSTORA5',
'country' : 'DE',
'facility' : '21W000000000056X',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'RWE Gas Storage West GmbH',
'short_name' : 'RWE Gas Storage West',
'company' : '21X000000001262B',
'country' : 'DE',
'facility' : '21W0000000000532',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'RWE Gas Storage West GmbH',
'short_name' : 'RWE Gas Storage West',
'company' : '21X000000001262B',
'country' : 'DE',
'facility' : '21W0000000000532',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'RWE Gas Storage West GmbH',
'short_name' : 'RWE Gas Storage West',
'company' : '21X000000001262B',
'country' : 'DE',
'facility' : '21W0000000000524',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'RWE Gas Storage West GmbH',
'short_name' : 'RWE Gas Storage West',
'company' : '21X000000001262B',
'country' : 'DE',
'facility' : '21W0000000000524',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'RWE Gas Storage West GmbH',
'short_name' : 'RWE Gas Storage West',
'company' : '21X000000001262B',
'country' : 'DE',
'facility' : '21W000000000004F',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'RWE Gas Storage West GmbH',
'short_name' : 'RWE Gas Storage West',
'company' : '21X000000001262B',
'country' : 'DE',
'facility' : '21W000000000004F',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'RWE Gas Storage West GmbH',
'short_name' : 'RWE Gas Storage West',
'company' : '21X000000001262B',
'country' : 'DE',
'facility' : '21W0000000000516',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'RWE Gas Storage West GmbH',
'short_name' : 'RWE Gas Storage West',
'company' : '21X000000001262B',
'country' : 'DE',
'facility' : '21W0000000000516',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'RWE Gas Storage West GmbH',
'short_name' : 'RWE Gas Storage West',
'company' : '21X000000001262B',
'country' : 'DE',
'facility' : '21W0000000000265',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'RWE Gas Storage West GmbH',
'short_name' : 'RWE Gas Storage West',
'company' : '21X000000001262B',
'country' : 'DE',
'facility' : '21W0000000000265',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'RWE Gas Storage West GmbH',
'short_name' : 'RWE Gas Storage West',
'company' : '21X000000001262B',
'country' : 'DE',
'facility' : '21W000000000003H',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'RWE Gas Storage West GmbH',
'short_name' : 'RWE Gas Storage West',
'company' : '21X000000001262B',
'country' : 'DE',
'facility' : '21W000000000003H',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'RWE Gas Storage West GmbH',
'short_name' : 'RWE Gas Storage West',
'company' : '21X000000001262B',
'country' : 'DE',
'facility' : '21W000000000121B',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'RWE Gas Storage West GmbH',
'short_name' : 'RWE Gas Storage West',
'company' : '21X000000001262B',
'country' : 'DE',
'facility' : '21W000000000121B',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'Storengy Deutschland GmbH',
'short_name' : 'Storengy Deutschland',
'company' : '21X000000001072G',
'country' : 'DE',
'facility' : '21W000000000093R',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'Storengy Deutschland GmbH',
'short_name' : 'Storengy Deutschland',
'company' : '21X000000001072G',
'country' : 'DE',
'facility' : '21W000000000093R',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'Storengy Deutschland GmbH',
'short_name' : 'Storengy Deutschland',
'company' : '21X000000001072G',
'country' : 'DE',
'facility' : '21W000000000092T',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'Storengy Deutschland GmbH',
'short_name' : 'Storengy Deutschland',
'company' : '21X000000001072G',
'country' : 'DE',
'facility' : '21W000000000092T',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'Storengy Deutschland GmbH',
'short_name' : 'Storengy Deutschland',
'company' : '21X000000001072G',
'country' : 'DE',
'facility' : '21W0000000000273',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'Storengy Deutschland GmbH',
'short_name' : 'Storengy Deutschland',
'company' : '21X000000001072G',
'country' : 'DE',
'facility' : '21W0000000000273',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'Storengy Deutschland GmbH',
'short_name' : 'Storengy Deutschland',
'company' : '21X000000001072G',
'country' : 'DE',
'facility' : '21W000000000091V',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'Storengy Deutschland GmbH',
'short_name' : 'Storengy Deutschland',
'company' : '21X000000001072G',
'country' : 'DE',
'facility' : '21W000000000091V',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'Storengy Deutschland GmbH',
'short_name' : 'Storengy Deutschland',
'company' : '21X000000001072G',
'country' : 'DE',
'facility' : '21W000000000090X',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'Storengy Deutschland GmbH',
'short_name' : 'Storengy Deutschland',
'company' : '21X000000001072G',
'country' : 'DE',
'facility' : '21W000000000090X',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'Storengy Deutschland GmbH',
'short_name' : 'Storengy Deutschland',
'company' : '21X000000001072G',
'country' : 'DE',
'facility' : '21W000000000089I',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'Storengy Deutschland GmbH',
'short_name' : 'Storengy Deutschland',
'company' : '21X000000001072G',
'country' : 'DE',
'facility' : '21W000000000089I',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'SWKiel Speicher GmbH ',
'short_name' : 'SWKiel Speicher',
'company' : '37X000000000051Y',
'country' : 'DE',
'facility' : '21W000000000058T',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'SWKiel Speicher GmbH ',
'short_name' : 'SWKiel Speicher',
'company' : '37X000000000051Y',
'country' : 'DE',
'facility' : '21W000000000058T',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'SWKiel Speicher GmbH ',
'short_name' : 'SWKiel Speicher',
'company' : '37X000000000051Y',
'country' : 'DE',
'facility' : '21W0000000001164',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'SWKiel Speicher GmbH ',
'short_name' : 'SWKiel Speicher',
'company' : '37X000000000051Y',
'country' : 'DE',
'facility' : '21W0000000001164',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'Thüringer Energie Speichergesellschaft mbH',
'short_name' : 'TEP',
'company' : '21X000000001307F',
'country' : 'DE',
'facility' : '21W000000000030E',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'Thüringer Energie Speichergesellschaft mbH',
'short_name' : 'TEP',
'company' : '21X000000001307F',
'country' : 'DE',
'facility' : '21W000000000030E',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'Trianel Gasspeicher Epe GmbH',
'short_name' : 'Trianel Gasspeicher Epe',
'company' : '21X000000001310Q',
'country' : 'DE',
'facility' : '21W000000000085Q',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'Trianel Gasspeicher Epe GmbH',
'short_name' : 'Trianel Gasspeicher Epe',
'company' : '21X000000001310Q',
'country' : 'DE',
'facility' : '21W000000000085Q',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'Uniper Energy Storage GmbH',
'short_name' : 'Uniper Energy Storage',
'company' : '21X000000001127H',
'country' : 'DE',
'facility' : '21W000000000067S',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'Uniper Energy Storage GmbH',
'short_name' : 'Uniper Energy Storage',
'company' : '21X000000001127H',
'country' : 'DE',
'facility' : '21W000000000067S',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'Uniper Energy Storage GmbH',
'short_name' : 'Uniper Energy Storage',
'company' : '21X000000001127H',
'country' : 'DE',
'facility' : '21W000000000066U',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'Uniper Energy Storage GmbH',
'short_name' : 'Uniper Energy Storage',
'company' : '21X000000001127H',
'country' : 'DE',
'facility' : '21W000000000066U',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'Uniper Energy Storage GmbH',
'short_name' : 'Uniper Energy Storage',
'company' : '21X000000001127H',
'country' : 'DE',
'facility' : '21W000000000065W',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'Uniper Energy Storage GmbH',
'short_name' : 'Uniper Energy Storage',
'company' : '21X000000001127H',
'country' : 'DE',
'facility' : '21W000000000065W',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'Uniper Energy Storage GmbH',
'short_name' : 'Uniper Energy Storage',
'company' : '21X000000001127H',
'country' : 'DE',
'facility' : '21W0000000000613',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'Uniper Energy Storage GmbH',
'short_name' : 'Uniper Energy Storage',
'company' : '21X000000001127H',
'country' : 'DE',
'facility' : '21W0000000000613',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'Uniper Energy Storage GmbH',
'short_name' : 'Uniper Energy Storage',
'company' : '21X000000001127H',
'country' : 'DE',
'facility' : '21W0000000000605',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'Uniper Energy Storage GmbH',
'short_name' : 'Uniper Energy Storage',
'company' : '21X000000001127H',
'country' : 'DE',
'facility' : '21W0000000000605',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'Uniper Energy Storage GmbH',
'short_name' : 'Uniper Energy Storage',
'company' : '21X000000001127H',
'country' : 'DE',
'facility' : '21W000000000059R',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'Uniper Energy Storage GmbH',
'short_name' : 'Uniper Energy Storage',
'company' : '21X000000001127H',
'country' : 'DE',
'facility' : '21W000000000059R',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'Uniper Energy Storage GmbH',
'short_name' : 'Uniper Energy Storage',
'company' : '21X000000001127H',
'country' : 'DE',
'facility' : '21W0000000000168',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'Uniper Energy Storage GmbH',
'short_name' : 'Uniper Energy Storage',
'company' : '21X000000001127H',
'country' : 'DE',
'facility' : '21W0000000000168',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'Uniper Energy Storage GmbH',
'short_name' : 'Uniper Energy Storage',
'company' : '21X000000001127H',
'country' : 'DE',
'facility' : '21W000000000083U',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'Uniper Energy Storage GmbH',
'short_name' : 'Uniper Energy Storage',
'company' : '21X000000001127H',
'country' : 'DE',
'facility' : '21W000000000083U',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'VNG Gasspeicher GmbH',
'short_name' : 'VNG Gasspeicher GmbH',
'company' : '21X000000001138C',
'country' : 'DE',
'facility' : '21W000000000120D',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'VNG Gasspeicher GmbH',
'short_name' : 'VNG Gasspeicher GmbH',
'company' : '21X000000001138C',
'country' : 'DE',
'facility' : '21W000000000120D',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'VNG Gasspeicher GmbH',
'short_name' : 'VNG Gasspeicher GmbH',
'company' : '21X000000001138C',
'country' : 'DE',
'facility' : '21W0000000001091',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'VNG Gasspeicher GmbH',
'short_name' : 'VNG Gasspeicher GmbH',
'company' : '21X000000001138C',
'country' : 'DE',
'facility' : '21W0000000001091',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'VNG Gasspeicher GmbH',
'short_name' : 'VNG Gasspeicher GmbH',
'company' : '21X000000001138C',
'country' : 'DE',
'facility' : '21W0000000000427',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'VNG Gasspeicher GmbH',
'short_name' : 'VNG Gasspeicher GmbH',
'company' : '21X000000001138C',
'country' : 'DE',
'facility' : '21W0000000000427',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'VNG Gasspeicher GmbH',
'short_name' : 'VNG Gasspeicher GmbH',
'company' : '21X000000001138C',
'country' : 'DE',
'facility' : '21W000000000023B',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'VNG Gasspeicher GmbH',
'short_name' : 'VNG Gasspeicher GmbH',
'company' : '21X000000001138C',
'country' : 'DE',
'facility' : '21W000000000023B',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'VNG Gasspeicher GmbH',
'short_name' : 'VNG Gasspeicher GmbH',
'company' : '21X000000001138C',
'country' : 'DE',
'facility' : '21W000000000128Y',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'VNG Gasspeicher GmbH',
'short_name' : 'VNG Gasspeicher GmbH',
'company' : '21X000000001138C',
'country' : 'DE',
'facility' : '21W000000000128Y',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'HEXUM Földgáz Zrt.',
'short_name' : 'HEXUM',
'company' : '21X0000000013643',
'country' : 'HU',
'facility' : '21W000000000086O',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'HEXUM Földgáz Zrt.',
'short_name' : 'HEXUM',
'company' : '21X0000000013643',
'country' : 'HU',
'facility' : '21W000000000086O',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'Hungarian Gas Storage',
'short_name' : 'HGS',
'company' : '21X0000000013635',
'country' : 'HU',
'facility' : '21W000000000087M',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'Hungarian Gas Storage',
'short_name' : 'HGS',
'company' : '21X0000000013635',
'country' : 'HU',
'facility' : '21W000000000087M',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'PSE Kinsale Energy Limited',
'short_name' : 'Kinsale Energy',
'company' : '47X0000000000584',
'country' : 'IE',
'facility' : '47W000000000245J',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'PSE Kinsale Energy Limited',
'short_name' : 'Kinsale Energy',
'company' : '47X0000000000584',
'country' : 'IE',
'facility' : '47W000000000245J',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'Edison Stoccaggio S.p.A.',
'short_name' : 'Edison Stoccaggio',
'company' : '21X0000000013651',
'country' : 'IT',
'facility' : '21W000000000095N',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'Edison Stoccaggio S.p.A.',
'short_name' : 'Edison Stoccaggio',
'company' : '21X0000000013651',
'country' : 'IT',
'facility' : '21W000000000095N',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'IGS S.p.A.',
'short_name' : 'IGS',
'company' : '59X4-IGSTORAGE-T',
'country' : 'IT',
'facility' : '59W-IGSTORAGE-0Q',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'IGS S.p.A.',
'short_name' : 'IGS',
'company' : '59X4-IGSTORAGE-T',
'country' : 'IT',
'facility' : '59W-IGSTORAGE-0Q',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'Stogit S.p.A.',
'short_name' : 'Stogit',
'company' : '21X000000001250I',
'country' : 'IT',
'facility' : '21Z000000000274I',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'Stogit S.p.A.',
'short_name' : 'Stogit',
'company' : '21X000000001250I',
'country' : 'IT',
'facility' : '21Z000000000274I',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'JSC Conexus Baltic Grid',
'short_name' : 'Conexus Baltic Grid',
'company' : '21X000000001379R',
'country' : 'LV',
'facility' : '21W000000000113A',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'JSC Conexus Baltic Grid',
'short_name' : 'Conexus Baltic Grid',
'company' : '21X000000001379R',
'country' : 'LV',
'facility' : '21W000000000113A',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'EnergyStock BV',
'short_name' : 'EnergyStock',
'company' : '21X000000001057C',
'country' : 'NL',
'facility' : '21W000000000006B',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'EnergyStock BV',
'short_name' : 'EnergyStock',
'company' : '21X000000001057C',
'country' : 'NL',
'facility' : '21W000000000006B',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'EWE Gasspeicher GmbH',
'short_name' : 'EWE Gasspeicher (NL)',
'company' : '21X0000000011756',
'country' : 'NL',
'facility' : '21W0000000001059',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'EWE Gasspeicher GmbH',
'short_name' : 'EWE Gasspeicher (NL)',
'company' : '21X0000000011756',
'country' : 'NL',
'facility' : '21W0000000001059',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'Nederlandse Aardolie Maatschappij B.V.',
'short_name' : 'NAM *',
'company' : '21X000000001075A',
'country' : 'NL',
'facility' : '21W000000000001L',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'Nederlandse Aardolie Maatschappij B.V.',
'short_name' : 'NAM *',
'company' : '21X000000001075A',
'country' : 'NL',
'facility' : '21W000000000001L',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'Nederlandse Aardolie Maatschappij B.V.',
'short_name' : 'NAM *',
'company' : '21X000000001075A',
'country' : 'NL',
'facility' : '21W000000000015A',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'Nederlandse Aardolie Maatschappij B.V.',
'short_name' : 'NAM *',
'company' : '21X000000001075A',
'country' : 'NL',
'facility' : '21W000000000015A',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'TAQA Gas Storage B.V.',
'short_name' : 'TAQA Gas Storage',
'company' : '21X000000001120V',
'country' : 'NL',
'facility' : '21W0000000000087',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'TAQA Gas Storage B.V.',
'short_name' : 'TAQA Gas Storage',
'company' : '21X000000001120V',
'country' : 'NL',
'facility' : '21W0000000000087',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'TAQA Piek Gas B.V.',
'short_name' : 'TAQA Piek Gas',
'company' : '21X0000000013732',
'country' : 'NL',
'facility' : '21W000000000002J',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'TAQA Piek Gas B.V.',
'short_name' : 'TAQA Piek Gas',
'company' : '21X0000000013732',
'country' : 'NL',
'facility' : '21W000000000002J',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'Gas Storage Poland sp. z o.o.',
'short_name' : 'GSP',
'company' : '53XPL000000OSMP5',
'country' : 'PL',
'facility' : '21Z000000000382F',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'Gas Storage Poland sp. z o.o.',
'short_name' : 'GSP',
'company' : '53XPL000000OSMP5',
'country' : 'PL',
'facility' : '21Z000000000382F',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'Gas Storage Poland sp. z o.o.',
'short_name' : 'GSP',
'company' : '53XPL000000OSMP5',
'country' : 'PL',
'facility' : '21Z000000000383D',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'Gas Storage Poland sp. z o.o.',
'short_name' : 'GSP',
'company' : '53XPL000000OSMP5',
'country' : 'PL',
'facility' : '21Z000000000383D',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'Gas Storage Poland sp. z o.o.',
'short_name' : 'GSP',
'company' : '53XPL000000OSMP5',
'country' : 'PL',
'facility' : '21Z000000000381H',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'Gas Storage Poland sp. z o.o.',
'short_name' : 'GSP',
'company' : '53XPL000000OSMP5',
'country' : 'PL',
'facility' : '21Z000000000381H',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'Gas Storage Poland sp. z o.o.',
'short_name' : 'GSP',
'company' : '53XPL000000OSMP5',
'country' : 'PL',
'facility' : 'PRIOR_OSM_000001',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'Gas Storage Poland sp. z o.o.',
'short_name' : 'GSP',
'company' : '53XPL000000OSMP5',
'country' : 'PL',
'facility' : 'PRIOR_OSM_000001',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'REN Armazenagem S.A.',
'short_name' : 'REN Armazenagem',
'company' : '21X0000000013627',
'country' : 'PT',
'facility' : '16ZAS01--------8',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'REN Armazenagem S.A.',
'short_name' : 'REN Armazenagem',
'company' : '21X0000000013627',
'country' : 'PT',
'facility' : '16ZAS01--------8',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'Depomures SA',
'short_name' : 'Depomures',
'company' : '21X000000001300T',
'country' : 'RO',
'facility' : '21Z000000000309P',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'Depomures SA',
'short_name' : 'Depomures',
'company' : '21X000000001300T',
'country' : 'RO',
'facility' : '21Z000000000309P',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'SNGN ROMGAZ SA FILIALA DE INMAGAZINARE GN DEPOGAZ PLOIESTI SRL \/ AGSI+',
'short_name' : 'Depogaz Ploiești',
'company' : '21X-DEPOGAZ-AGSI',
'country' : 'RO',
'facility' : '21Z0000000003103',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'SNGN ROMGAZ SA FILIALA DE INMAGAZINARE GN DEPOGAZ PLOIESTI SRL \/ AGSI+',
'short_name' : 'Depogaz Ploiești',
'company' : '21X-DEPOGAZ-AGSI',
'country' : 'RO',
'facility' : '21Z0000000003103',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'SNGN ROMGAZ SA FILIALA DE INMAGAZINARE GN DEPOGAZ PLOIESTI SRL \/ AGSI+',
'short_name' : 'Depogaz Ploiești',
'company' : '21X-DEPOGAZ-AGSI',
'country' : 'RO',
'facility' : '21Z000000000313Y',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'SNGN ROMGAZ SA FILIALA DE INMAGAZINARE GN DEPOGAZ PLOIESTI SRL \/ AGSI+',
'short_name' : 'Depogaz Ploiești',
'company' : '21X-DEPOGAZ-AGSI',
'country' : 'RO',
'facility' : '21Z000000000313Y',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'SNGN ROMGAZ SA FILIALA DE INMAGAZINARE GN DEPOGAZ PLOIESTI SRL \/ AGSI+',
'short_name' : 'Depogaz Ploiești',
'company' : '21X-DEPOGAZ-AGSI',
'country' : 'RO',
'facility' : '21Z0000000003111',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'SNGN ROMGAZ SA FILIALA DE INMAGAZINARE GN DEPOGAZ PLOIESTI SRL \/ AGSI+',
'short_name' : 'Depogaz Ploiești',
'company' : '21X-DEPOGAZ-AGSI',
'country' : 'RO',
'facility' : '21Z0000000003111',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'SNGN ROMGAZ SA FILIALA DE INMAGAZINARE GN DEPOGAZ PLOIESTI SRL \/ AGSI+',
'short_name' : 'Depogaz Ploiești',
'company' : '21X-DEPOGAZ-AGSI',
'country' : 'RO',
'facility' : '21Z000000000314W',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'SNGN ROMGAZ SA FILIALA DE INMAGAZINARE GN DEPOGAZ PLOIESTI SRL \/ AGSI+',
'short_name' : 'Depogaz Ploiești',
'company' : '21X-DEPOGAZ-AGSI',
'country' : 'RO',
'facility' : '21Z000000000314W',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'SNGN ROMGAZ SA FILIALA DE INMAGAZINARE GN DEPOGAZ PLOIESTI SRL \/ AGSI+',
'short_name' : 'Depogaz Ploiești',
'company' : '21X-DEPOGAZ-AGSI',
'country' : 'RO',
'facility' : '21Z000000000315U',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'SNGN ROMGAZ SA FILIALA DE INMAGAZINARE GN DEPOGAZ PLOIESTI SRL \/ AGSI+',
'short_name' : 'Depogaz Ploiești',
'company' : '21X-DEPOGAZ-AGSI',
'country' : 'RO',
'facility' : '21Z000000000315U',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'SNGN ROMGAZ SA FILIALA DE INMAGAZINARE GN DEPOGAZ PLOIESTI SRL \/ AGSI+',
'short_name' : 'Depogaz Ploiești',
'company' : '21X-DEPOGAZ-AGSI',
'country' : 'RO',
'facility' : '21Z000000000316S',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'SNGN ROMGAZ SA FILIALA DE INMAGAZINARE GN DEPOGAZ PLOIESTI SRL \/ AGSI+',
'short_name' : 'Depogaz Ploiești',
'company' : '21X-DEPOGAZ-AGSI',
'country' : 'RO',
'facility' : '21Z000000000316S',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'Nafta a.s.',
'short_name' : 'Nafta',
'company' : '42X-NAFTA-SK---U',
'country' : 'SK',
'facility' : '21W000000000088K',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'Nafta a.s.',
'short_name' : 'Nafta',
'company' : '42X-NAFTA-SK---U',
'country' : 'SK',
'facility' : '21W000000000088K',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'Pozagas a.s.',
'short_name' : 'Pozagas',
'company' : '42X-POZAGAS-SK-V',
'country' : 'SK',
'facility' : '21W000000000047Y',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'Pozagas a.s.',
'short_name' : 'Pozagas',
'company' : '42X-POZAGAS-SK-V',
'country' : 'SK',
'facility' : '21W000000000047Y',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'Enagas GTS S.A.U',
'short_name' : 'Enagás GTS',
'company' : '21X0000000013368',
'country' : 'ES',
'facility' : '21W000000000032A',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'Enagas GTS S.A.U',
'short_name' : 'Enagás GTS',
'company' : '21X0000000013368',
'country' : 'ES',
'facility' : '21W000000000032A',
'from': '-01-01',
'to' : '-06-30'
},
{
'company_name' : 'Swedegas AB',
'short_name' : 'Swedegas',
'company' : '21X-SE-A-A0A0A-F',
'country' : 'SE',
'facility' : '21W0000000000435',
'from': '-07-01',
'to' : '-12-31'
},
{
'company_name' : 'Swedegas AB',
'short_name' : 'Swedegas',
'company' : '21X-SE-A-A0A0A-F',
'country' : 'SE',
'facility' : '21W0000000000435',
'from': '-01-01',
'to' : '-06-30'
}
]
# request_list = [{
# 'company_name' : 'Swedegas AB',
# 'short_name' : 'Swedegas',
# 'company' : '21X-SE-A-A0A0A-F',
# 'country' : 'SE',
# 'facility' : '21W0000000000435',
# 'from': '-07-01',
# 'to' : '-12-31'
# },
# {
# 'company_name' : 'Swedegas AB',
# 'short_name' : 'Swedegas',
# 'company' : '21X-SE-A-A0A0A-F',
# 'country' : 'SE',
# 'facility' : '21W0000000000435',
# 'from': '-01-01',
# 'to' : '-06-30'
# }]



def call(api_key, agis_request, year):
    count = 0
    if api_key:
        for agis_request in request_list:
            # s = requests.Session()
            print(agis_request)
            with requests.Session() as s:
                retry = Retry(connect=5, backoff_factor=0.5)
                adapter = HTTPAdapter(max_retries=retry)
                s.mount('http://', adapter)
                s.mount('https://', adapter)
                url = "https://agsi.gie.eu/api?facility=" + agis_request['facility'] + "&country=" + agis_request['country'] + "&company=" + agis_request['company'] + "&from=" +  str(year) + agis_request['from'] + "&to=" +  str(year) + agis_request['to'] + "&size=300"
                response = s.get(url, headers={'x-key': api_key})
                response.raise_for_status()  # raises exception when not a 2xx response
                if response.status_code != 204:
                    df = pd.DataFrame(response.json()["data"])
                    # print(response.json())
                    df['country'] = agis_request['country']
                    #df['id'] = agis_request[1]
                    df['short_company']  = agis_request['short_name']
                    df['company_name'] = agis_request['company_name']
                    # print(df.head)
                    # response.close()
                    if count == 0:
                        df.to_csv('agsi_' + str(year) + '_v6.csv', index=False)
                    else:
                        df.to_csv('agsi_' +  str(year) + '_v6.csv', mode='a', index=False, header=False)
                    count += 1
            time.sleep(2)
        print("year finisehd")
    else:
        print("api key not found")

years = [2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011]

for year in years:
    print('########')
    print(year)
    call(api_key, request_list, year)

print("all finished")
