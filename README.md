# Kegbot on Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

This is ready to deploy repo for hosting Kegbot on Heroku.

## Requirements

* A Heroku account - free for single dyno apps like this
* An AWS account and S3 bucket - costs less than $1/month

## Quick start

For those with heroku experience and want to be able to track changes to this
repository follow the directions below. For those that don't, just press the
Deploy to Heroku button above.

1. Clone this repository
1. Create heroku app `heroku create`
1. Push to heroku `git push heroku master`
1. Add New Relic for monitoring `heroku addons:add newrelic`
1. Add MemCachier `heroku addons:add memcachier`
1. Add database `heroku addons:add heroku-postgresql:dev`
1. Add redis `heroku addons:add redistogo`
1. Add postmark `heroku addons:add postmark`
1. Set kegbot config path `heroku config:add KEGBOT_SETTINGS_DIR="/app/"`
1. Set a django secret key `heroku config:add SECRET_KEY='...'`
(you can generate one here - http://www.miniwebtool.com/django-secret-key-generator/)
1. Set your outgoing email address `heroku config:add EMAIL_FROM_ADDRESS="kegbot@example.com"`
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

**Note:** Once the site is deployed you must register your outgoing email address
with Postmark before emails will actually send. This can be done through the
Postmark configuration page, accessible from the addons section of your deployed
Heroku app.

## Upgrading

To upgrade your server installation simply pull the latest version of this repo
from github and push it to heroku. Provided no configuration changes are
necessary just run the following command.

**Note:** You can only use this upgrade path if you did not use the Deploy to
Heroku button deployment option. If you used the Heroku Button the deployed
repository will no longer track this repo.

        heroku run kegbot upgrade

## Contributing

Please report issues or send a pull request.

