#
# 
#

cat $1 | sed -e "1,6d" > ./model/modelWeight.tsv
cat ./dic/df.tsv | sort -k 1 -n > ./dic/dfIDOrder.tsv
paste ./dic/dfIDOrder.tsv ./model/modelWeight.tsv | sort -k 4 -n > ./model/wordWeight.tsv
