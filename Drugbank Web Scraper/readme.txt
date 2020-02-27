Web Scraper + API Take-Home Challenge

Web Scraper.ipynb holds the jupyternotebook that I used.
It walks through the steps that I took while going through the challenge.

Instructions for setting up the Flask api locally

1. Open up terminal and navigate to the directory '../Drugbank Web Scraper/api
2. run the command ('python api.py') to launch the Flask api locally
3. query the api with the drug accession number. The result will return the targets of the drug, separated by commas.

Examples queries:
http://127.0.0.1:5000/drugs?accession_number=DB00619
http://127.0.0.1:5000/drugs?accession_number=DB01048
http://127.0.0.1:5000/drugs?accession_number=DB14093
