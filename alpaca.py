#!/usr/bin/env python3
#creating sets with all genes, proliferation genes and pigmentation genes 
all_set=set()
stem_set=set()
pigm_set=set()
all_genes = open('alpaca_all_genes.tsv', 'r')
stem_genes = open('alpaca_stemcellproliferation_genes.tsv', 'r')
pigm_genes = open('alpaca_pigmentation_genes.tsv', 'r')
for line in all_genes:
 all_set.add(line)
for line in stem_genes:
 stem_set.add(line)
for line in pigm_genes:
 pigm_set.add(line)
#sets with no stem genes and both stem and pigm
no_stem_genes = all_set - stem_set
print(f'All genes no stem are {no_stem_genes}')
both_stempigm = stem_set & pigm_set
print(f'In both stem and pigm we found {both_stempigm}')

