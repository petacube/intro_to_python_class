**********************************
*                                *
*  Sunday Times Data Team        *
*                                *
*  MOSSACK FONSECA:              *
*  THE PANAMA COMPANIES          *
*                                *
*  Sunday 10th April 2016        *
*                                *
**********************************

Version 1.0

By Josh Boswell (@JoshTBoswell), Tom Wills (@TomWills) & Ændrew Rininsland (@aendrew)

The Sunday Times Data Team has compiled a list of companies in Panama set up by Mossack Fonseca and their associates, as well the directors, shareholders and legal agents of those companies, as reported to the Panama companies registry.

Many of the names in this data are stooges, paid by Mossack Fonseca to conceal the identity of companies' true beneficiaries. But others - including David Cameron's late father Ian - are bona fide.

Using offshore companies is not a crime, and they do have some legitimate purposes. Just because a company or person appears in this list does not mean they have done anything wrong.

Data compiled by the Sunday Times Data Team using information from the OpenCorporates API. This data is released under the Open Database License, which can be found at:
http://www.opendatacommons.org/licenses/odbl/1.0/

Files
-----

README.txt: This file. UTF-8 encoded Unicode text with Unix line endings.

sunday_times_panama_data.csv: 103 MB CSV file. Header row + 528998 data rows. Contains one row for each position held in each Mossack Fonseca-linked company. An 'officer' may be a person or company, and their relationship to the company may be that of director, shareholder or legal agent, among others. If a person has more than one position listed, they will appear multiple times for the same company. A UTF-8 encoded Unicode CSV file with Unix line endings. 

Explanation of columns in sunday_times_panama_data.csv
------------------------------------------------------

company_url          OpenCorporates URL for the company.
company_name         Company name as stated in the Panama companies registry.
officer_position_es  Officer's position in the company, as stated in Spanish in the Panama companies registry.
officer_position_en  Officer's position in the company, translated into English by the Sunday Times Data Team.
officer_name         Officer's name, as stated in the Panama companies registry. Note that this can be the name of a person or another company. Sometimes more than one person is listed in one record.
inc_date             Incorporation date of the company.
dissolved_date       Dissolution date of the company, or 0000-00-00 if the company is current.
updated_date         Time and date given by the Panama companies registry when OpenCorporates retrieved the record.
company_type         Company type as stated in the Panama companies registry in Spanish.
mf_link              Indicator denoting officers we have linked to Mossack Fonseca. Please note that our search has not been exhaustive - there are likely many more associates of Mossack Fonseca in this data who we have not yet discovered. 0 = not linked, 1 = linked.

Methodology
-----------

We identified Mossack Fonseca directors and their associates by searching for officers of companies bearing the name 'Mossack Fonseca' registered in Panama. We then searched for other Panama companies to which these officers are connected.

We have included dissolved companies in this data. These are denoted by the presence of a date in the dissolved_date column.

Please note that the Panama companies registry does not give dates of birth for company officers. To confirm the identity of a person named in this data is likely to require further investigative work. In any case, inclusion in this data or involvement in a Mossack Fonseca company is not an indication of wrongdoing. The Sunday Times has compiled this data from a public source in the interests of transparency and accountability.

Data quality
------------

The data on companies that is available through OpenCorporates is drawn from many different government sources. In some cases the source data have errors which OpenCorporates have not yet detected and in other cases the data has been provided in very complex and impenetrable formats, which may have given rise to errors in the way it is presented here.

We have made all reasonable efforts to ensure the accuracy of this data. If you spot anything amiss, please email the Sunday Times Data Team at data@news.co.uk