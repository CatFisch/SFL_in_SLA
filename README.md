# SFL_in_SLA


## License
Copyright 2021 Catharina Fischer

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.


## Annotated_excel-files
Excel files that contain argumentative essays that were automatically and manually annotated in the scope of my master theses. The original files can be accessed here: https://www.linguistik.hu-berlin.de/en/institut-en/professuren-en/korpuslinguistik/research/falko/access (see also Reznicek, Marc, Anke Lüdeling, Cedric Krummes, Franziska Schwantuschke, Maik Walter, Karin Schmidt, Hagen Hirschmann, and Torsten Andreas (2012). Das Falko-Handbuch. Korpusaufbau und Annotationen. Version 2.01)

## Converted_ANNIS_files
Contains the above mentioned excel files converted into a format readable for the search- and visualization tool ANNIS accessible here: https://korpling.german.hu-berlin.de/falko-suche/
(see Krause, Thomas and Amir Zeldes (2016). “ANNIS3: A new architecture for generic corpus query and visualization”. In: Digital Scholarship in the Humanities 2016 31.1, pp. 118–139.)

## excel2annis.pepper
Script that converts excel files into a readable ANNIS format (see also: Romary, Laurent and Florian Zipser (2010). “A model oriented approach to the mapping of annotation formats using standards”. In: Proceedings of the Workshop on Language Resource and Language Technology Standards. URL:http://hal.archives-ouvertes.fr/inria-00527799/en/).

## Misc_scripts
Is a collection of scripts to automate  minor processes like renaming columns, deleting comments or merging cells. 

## R_scripts
This folder contains all scripts I used for statistics and visualization within the scope of my thesis. 

## ComVerbTagger.py
The ComVerbTagger.py taggs 600 communication verbs (verb lemmas) received from the online reference work OWID digital version of the German “Handbuch deutscher Kommunikationsverben” accessible here: https://www.owid.de/docs/komvb/stw_idx.jsp) in the above introduced excel files by adding an additional column “repres” with the value “verbal_process” if one of the 600 verbs from the OWID list was detected in the already existing column “ZH1lemma”.

## OWID_list_of_communication_verbs.txt
List of communication verbs that are tagged by the “ComVerbTagger.py” based on the OWID digital version of the German “Handbuch deutscher Kommunikationsverben”  (see above)
