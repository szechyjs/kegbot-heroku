# Kegbot on Heroku

This is ready to deploy repo for hosting Kegbot on Heroku.

## Quick start

For those with heroku experience this should be pretty easy.

1. Clone this repository
2. Create heroku app `heroku create`
3. Push to heroku `git push heroku master`
4. Add database `heroku addons:add heroku-postgresql:dev`
5. Promote the database `heroku pg:promote HEROKU_POSTGRESQL_CYAN_URL` Note: replace CYAN with the color from the previous command.
6. Set kegbot config path `heroku config:add KEGBOT_SETTINGS_DIR=/app/`
7. Initialize database
````
  heroku run kegbot syncdb --all --noinput -v 0

  heroku run kegbot migrate --all --fake --noinput -v 0
````
8. Visit site `heroku open` and finish initial configuration

## Known Issues

* No support for media images (mugshots, session pictures, etc...)
* Poor performance due to use of django development server

## TODO

* Add S3 storage for both static and media
* Switch to gunicorn (requires S3 storage first)

## Contributing

Please report issues or send a  pull request.

