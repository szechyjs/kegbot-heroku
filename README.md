# Kegbot on Heroku

This is ready to deploy repo for hosting Kegbot on Heroku.

## Requirements

* A Heroku account
* An AWS account and S3 bucket

## Quick start

For those with heroku experience this should be pretty easy.

1. Clone this repository
2. Create heroku app `heroku create`
3. Push to heroku `git push heroku master`
4. Add New Relic for monitoring `heroku addons:add newrelic`
5. Add database `heroku addons:add heroku-postgresql:dev`
6. Promote the database `heroku pg:promote HEROKU_POSTGRESQL_CYAN_URL` Note: replace CYAN with the color from the previous command.
7. Set kegbot config path `heroku config:add KEGBOT_SETTINGS_DIR=/app/`
8. Initialize database
````
  heroku run kegbot syncdb --all --noinput -v 0

  heroku run kegbot migrate --all --fake --noinput -v 0
````
9. Set the following config variables for you S3 bucket.
````
  heroku config:add AWS_ACCESS_KEY_ID="XXXXXXXXXXXXXXXXXXXX"
  heroku config:add AWS_SECRET_ACCESS_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
  heroku config:add AWS_STORAGE_BUCKET_NAME="bbbbbbbb"
  heroku config:add AWS_S3_CUSTOM_DOMAIN="bbbbbbbb.s3.amazonaws.com"
  ````
9. Upload static files to S3 bucket `heroku run kegbot collectstatic`
10. Visit site `heroku open` and finish initial configuration

## Contributing

Please report issues or send a  pull request.

