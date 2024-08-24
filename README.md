# FLIRseq
##################  1. call consensus reads  ###############

git clone https://github.com/rvolden/C3POa.git

chmod +x setup.sh

./setup.sh

python3 C3POa.py -r sample.fastq -o output -s TCR_BCR_splint.fasta -c config.txt -l 400 -d 150 -n 10 --zero

cat output/*/R2C2_Consensus.fasta > output/Consensus.fasta

##################  2. Filter the consensus reads with low confidence  ################

grep -n ">" Consensus.fasta |grep -v "_1_" > sample_n.txt

python2 extract_seq_by_id.py Consensus.fasta sample_n.txt repeat2_Consensus.fasta

##################  3.reorient consensus reads ###############

python fasta_miRNA.py --file repeat2_Consensus.fasta

##################  4. Align to the T- or B- cell receptor repertoire  ###############

conda install -c milaboratories mixcr

mixcr analyze amplicon -s hsa --starting-material rna --3-end c-primers --5-end v-primers --adapters no-adapters --contig-assembly --impute-germline-on-export Consensus_Rdir.fasta IR
