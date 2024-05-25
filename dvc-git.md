# dvc-git

git init
dvc init
dvc add <filename>

# Save the dvc copy created to git and gitignore file having actual data file details
git add <filepath>.dvc .gitignore 
dvc remote add -d s3://bucketname
dvc push

git add .dvc/config
dvc pull


## To get old data back

git checkout HEAD^
dvc checkout
