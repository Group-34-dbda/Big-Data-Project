#sudo pip3 install kaggle

#sudo pip3 install -U kaggle-cli

testVar=$1

echo "Enter your dataset API"

#read testVar

#echo "Your Dataset Name --> $testVar"

echo 'Downloading your Dataset'

#kaggle datasets download -d arjunprasadsarkhel/2021-olympics-in-tokyo

echo $testVar

echo 'Dataset Downloaded'

ls

echo 'Saving your dataset in S3'

#aws s3 cp *.zip s3://projecdataset

#echo 'Success'

#aws s3 ls s3://projecdataset

#rm -rf *.zip
#dataFile=s3://projecdataset/campaign-contributions-19902016.zip

#echo "Downloading data from S3..."

#aws s3 cp $dataFile .

mkdir data2

mv *.zip data2/

cd data2

echo "Extracting Data..."

#tar -xvzf 2021*.zip ./data/
unzip *.zip 

ls

rm -rf *zip

#echo "Move data to HDFS..."

#hdfs dfs -mkdir data

#hdfs dfs -put * data/

#hdfs dfs -ls data/

cd ..


for var in data2/*
do
	echo "$var uploading"
	aws s3 cp $var s3://projecdataset/data2/
done
