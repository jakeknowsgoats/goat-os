# Architect manifest — https://arc.codes
# Tally is a static, single-file web app. No Lambda functions, no database:
# Architect just deploys ./public to S3 + CloudFront as a static site.

@app
tally

@static
# Deploy everything in ./public. `spa true` falls back to index.html for any
# path, so deep links / refreshes always load the app.
fingerprint false
spa true

@aws
region us-east-1
