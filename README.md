# Kegbot on Heroku

This is ready to deploy repo for hosting Kegbot on Heroku.

## Requirements

* A Heroku account
* An AWS account and S3 bucket

## Quick start

For those with heroku experience this should be pretty easy.

1. Clone this repository
1. Create heroku app `heroku create`
1. Push to heroku `git push heroku master`
1. Add New Relic for monitoring `heroku addons:add newrelic`
1. Add MemCachier `heroku addons:add memcachier`
1. Add database `heroku addons:add heroku-postgresql:dev`
1. Promote the database `heroku pg:promote HEROKU_POSTGRESQL_CYAN_URL` Note: replace CYAN with the color from the previous command.
1. Add redis `heroku addons:add redistogo`
1. Copy the redis url from `heroku config | grep REDISTOGO`
1. Run `heroku config:add REDIS_URL=redis://...` using the url from the previous step.
1. Set kegbot config path `heroku config:add KEGBOT_SETTINGS_DIR=/app/`
1. Set a django secret key `heroku config:add SECRET_KEY=...` (you can generate one here - http://www.miniwebtool.com/django-secret-key-generator/)
1. Set the following config variables for your S3 bucket.

        heroku config:add AWS_ACCESS_KEY_ID="XXXXXXXXXXXXXXXXXXXX"
        heroku config:add AWS_SECRET_ACCESS_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        heroku config:add AWS_STORAGE_BUCKET_NAME="bbbbbbbb"
        heroku config:add AWS_S3_CUSTOM_DOMAIN="bbbbbbbb.s3.amazonaws.com"

1. Initialize database

        heroku run kegbot syncdb --all --noinput -v 0
        heroku run kegbot migrate --all --fake --noinput -v 0

1. Upload static files to S3 bucket `heroku run kegbot collectstatic`
1. Visit site `heroku open` and finish initial configuration

## Upgrading

To upgrade your server installation simply pull the latest version of this repo from github
and push it to heroku. Provided no configuration changes are necessary just run the
following command.

        heroku run kegbot upgrade

## Contributing

Please report issues or send a pull request.

