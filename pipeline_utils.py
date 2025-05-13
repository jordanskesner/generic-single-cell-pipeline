#=== Imports ===#
import pipeline_utils
import os
import urllib.request
from datetime import datetime
import sys
from contextlib import redirect_stdout

#=== Function to download genome sequences and annotations ===#
def download_genome(genome_info, output_dir):
    ##
    print(f"Downloading {len(genome_info)} genomes")

    ##
    for genome, urls in genome_info.items():

        ##
        print(f"Currently downloading genome {genome}")
        
        ## construct parent dir
        genome_dir = os.path.join(output_dir, genome)
        print(f"Saving genome data at {genome_dir}")
        os.makedirs(genome_dir, exist_ok=True)

        ##
        log_path = os.path.join(genome_dir, "replace_download_log.txt").replace("\\", "/")
        log_path = log_path.replace("replace", genome)
        with open(log_path, "w") as f:
            pass
        print(f"Saving logfile to: {log_path}")

        ## urls
        genome_url = urls["genome_url"]
        gtf_url = urls["gtf_url"]
        cdna_url = urls["cdna_url"]
        cds_url = urls["cds_url"]
        ncrna_url = urls["ncrna_url"]
        pep_url = urls["pep_url"]

        ## redirect stdout for logging purposes
        with open(log_path, "w") as f:
            with redirect_stdout(f):

                ##
                print(f"Genome: {genome}")
                print(f"Genome url: {genome_url}")
                print(f"gtf url: {gtf_url}")
                print(f"cdna url: {cdna_url}")
                print(f"cds url: {cds_url}")
                print(f"ncrna url: {ncrna_url}")
                print(f"pep url: {pep_url}")
                
                ## timestamp
                now = datetime.now()
                timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
                print("Operation performed at:", timestamp)
                
                ## construct filepaths
                ## NOTE: backslash defaults with os.path.join on windows. replace with forward slash
                genome_path = os.path.join(genome_dir, os.path.basename(urls["genome_url"])).replace("\\", "/")
                gtf_path = os.path.join(genome_dir, os.path.basename(urls["gtf_url"])).replace("\\", "/")
                cdna_path = os.path.join(genome_dir, os.path.basename(urls["cdna_url"])).replace("\\", "/")
                cds_path = os.path.join(genome_dir, os.path.basename(urls["cds_url"])).replace("\\", "/")
                ncrna_path = os.path.join(genome_dir, os.path.basename(urls["ncrna_url"])).replace("\\", "/")
                pep_path = os.path.join(genome_dir, os.path.basename(urls["pep_url"])).replace("\\", "/")
        
                # print
                print(f"Saving genome file to: {genome_path}")
                print(f"Saving gtf file to: {gtf_path}")
                print(f"Saving cdna file to: {cdna_path}")
                print(f"Saving cds file to: {cds_path}")
                print(f"Saving ncrna file to: {ncrna_path}")
                print(f"Saving pep file to: {pep_path}")
        
                ## download genome file ##
                try:
                    # check if file exists, if not, create it
                    if not genome_path.is_file():
                        print(f"File '{genome_path}' does not exist. Downloading...")
                        urllib.request.urlretrieve(genome_url, genome_path)
                    else:
                        print(f"File '{genome_path}' already exists. Skipping")
                except Exception as e:
                    print(f"Failed to download {genome_url}: {e}")

                ## download gtf file ##
                try:
                    # check if file exists, if not, create it
                    if not gtf_path.is_file():
                        print(f"File '{gtf_path}' does not exist. Downloading...")
                        urllib.request.urlretrieve(gtf_url, gtf_path)
                    else:
                        print(f"File '{gtf_path}' already exists. Skipping")
                except Exception as e:
                    print(f"Failed to download {gtf_url}: {e}")
                    
                ## download cdna file ##
                try:
                    # check if file exists, if not, create it
                    if not cdna_path.is_file():
                        print(f"File '{cdna_path}' does not exist. Downloading...")
                        urllib.request.urlretrieve(cdna_url, cdna_path)
                    else:
                        print(f"File '{cdna_path}' already exists. Skipping")
                except Exception as e:
                    print(f"Failed to download {cdna_url}: {e}")
                    
                ## download cds file ##
                try:
                    # check if file exists, if not, create it
                    if not cds_path.is_file():
                        print(f"File '{cds_path}' does not exist. Downloading...")
                        urllib.request.urlretrieve(cds_url, cds_path)
                    else:
                        print(f"File '{cds_path}' already exists. Skipping")
                except Exception as e:
                    print(f"Failed to download {cds_path}: {e}")
                    
                ## download ncrna file ##
                try:
                    # check if file exists, if not, create it
                    if not ncrna_path.is_file():
                        print(f"File '{ncrna_path}' does not exist. Downloading...")
                        urllib.request.urlretrieve(ncrna_url, ncrna_path)
                    else:
                        print(f"File '{ncrna_path}' already exists. Skipping")
                except Exception as e:
                    print(f"Failed to download {ncrna_url}: {e}")
                    
                ## download pep file ##
                try:
                    # check if file exists, if not, create it
                    if not pep_path.is_file():
                        print(f"File '{pep_path}' does not exist. Downloading...")
                        urllib.request.urlretrieve(pep_url, pep_path)
                    else:
                        print(f"File '{pep_path}' already exists. Skipping")
                except Exception as e:
                    print(f"Failed to download {pep_url}: {e}")
                    
                    
#=== Output an XML object as a formatted tree for inspection ===#                    
def explore(obj, indent=0):
    spacing = "  " * indent
    if isinstance(obj, dict):
        for key, value in obj.items():
            print(f"{spacing}{key}: {type(value)}")
            explore(value, indent + 1)
    elif isinstance(obj, list):
        print(f"{spacing}List of length {len(obj)}")
        if len(obj) > 0:
            explore(obj[0], indent + 1)
    else:
        print(f"{spacing}{type(obj)} → {obj}")
                    
                    
                    


