@echo off
 git init
 git add .
 git commit -am "make it better"
 rem heroku git:remote -a sanjuvarshaa
git push heroku master --force
rem done