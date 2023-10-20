#!/usr/bin/env python3
#creating lists text files for comm comparing
stem_set=set()
stem_list=[]
tf_set=()
tf_list=[]
stem_genes = open('alpaca_stemcellproliferation_genes.tsv', 'r')
tf_genes = open('alpaca_tf.tsv', 'r')
for line in stem_genes:
 stem_list.append(line)
for line1 in tf_genes:
 tf_list.append(line1)
stem_list=sorted(stem_list)
tf_list=sorted(tf_list)
o_tf = open('sorted_tf.tsv', 'w')
o_stem = open('sorted_stem.tsv', 'w')
o_tf.write(str(tf_list))
o_stem.write(str(stem_list))

