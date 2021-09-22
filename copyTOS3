#! /bin/sh

#sudo pip3 install kaggle

#sudo pip3 install -U kaggle-cli

testVar=$1

echo "Enter your dataset API"

#read testVar

#echo "Your Dataset Name --> $testVar"

echo 'Downloading your Dataset'

#kaggle datasets download -d arjunprasadsarkhel/2021-olympics-in-tokyo

$testVar

echo 'Dataset Downloaded'

ls

echo 'Saving your dataset in S3'

aws s3 cp *.zip s3://bd-project/

echo 'Success'

aws s3 ls s3://bd-project/

rm -rf ./*.zip
