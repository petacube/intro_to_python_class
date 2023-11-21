in this chapter we will explore real graph 
panama papers 
unday_times_panama_data.csv: 103 MB CSV file. Header row + 528998 data rows. Contains one row for each position held in each Mossack Fonseca-linked company. An 'officer' may be a person or company, and their relationship to the company may be that of director, shareholder or legal agent, among others. If a person has more than one position listed, they will appear multiple times for the same company. A UTF-8 encoded Unicode CSV file with Unix line endings. 

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


