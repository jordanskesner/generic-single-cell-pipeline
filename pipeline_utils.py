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

        ## fasta url
        fasta_url = urls["fasta_url"]
        gtf_url = urls["gtf_url"]

        ## redirect stdout for logging purposes
        with open(log_path, "w") as f:
            with redirect_stdout(f):

                ##
                print(f"Genome: {genome}")
                print(f"Fasta url: {fasta_url}")
                print(f"gtf url: {gtf_url}")
                
                ## construct filepaths
                ## NOTE: backslash defaults with os.path.join on windows. replace with forward slash
                fasta_path = os.path.join(genome_dir, os.path.basename(urls["fasta_url"])).replace("\\", "/")
                gtf_path = os.path.join(genome_dir, os.path.basename(urls["gtf_url"])).replace("\\", "/")
        
                # print
                print(f"Saving fasta file to: {fasta_path}")
                print(f"Saving gtf file to: {gtf_path}")
        
                ## download fasta file
                try:
                    urllib.request.urlretrieve(fasta_url, fasta_path)
                except Exception as e:
                    print(f"Failed to download {fasta_url}: {e}")

                ## download gtf file
                try:
                    urllib.request.urlretrieve(gtf_url, gtf_path)
                except Exception as e:
                    print(f"Failed to download {gtf_url}: {e}")


