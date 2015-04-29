python buildFeatures.py > ./train/features.svm
cat ./judge/judgement.tsv | cut -f 3 > ./train/positive.txt
paste ./train/positive.txt ./train/features.svm | sed -e 's/	/ /g' > ./train/train.svm
head -n 450 ./train/train.svm > ./train/r_train.svm
tail -n 101 ./train/train.svm > ./train/valid.svm
