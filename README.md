## Quickstart
- check compose file for changes specific to your environment, most importantly, the backend volume
- `docker-compose up rsspy`
- Navigate to http://localhost (with port number as defined in compose file for rsspy service)

### Caveat 
The frontend currently doesn't render anything if it cannot reach the backend.  If new database, you will need to wait until the coin_updater script finishes the first time.
This can take several minutes.