# Tally

A mobile-first counter for street fundraisers — track **approaches**, **sign-ups**,
conversion rate, and full **shift** history (hours, location, CSV export). Everything
persists in `localStorage`; there is no backend.

The app itself is one self-contained file: [`public/index.html`](public/index.html)
(inline CSS + JS, no build step, no frameworks, no CDN). This folder wraps it in an
[Architect (arc.codes)](https://arc.codes) project so it deploys as a static site on
AWS (S3 + CloudFront).

## Project layout

```
tally/
├── app.arc              # Architect manifest — static-only site
├── package.json         # arc scripts + @architect/architect dev dependency
├── netlify.toml         # optional: deploy the same public/ folder on Netlify
└── public/
    └── index.html       # the entire Tally app
```

Because it is static-only, `app.arc` declares just `@app` and `@static` — no
`@http` Lambda functions and no database.

## Run it locally

```bash
cd tally
npm install
npm start          # arc sandbox → http://localhost:3333
```

`arc sandbox` serves `public/` locally, the same way it's served in production.

## Deploy with Architect

Requires AWS credentials configured in your environment (`~/.aws/credentials`
or `AWS_ACCESS_KEY_ID` / `AWS_SECRET_ACCESS_KEY`).

```bash
cd tally
npm run deploy               # staging environment
npm run deploy:production    # production environment
```

Architect provisions an S3 bucket + CloudFront distribution and uploads
`public/`. It prints the URL when it finishes.

## Deploy on Netlify (alternative)

`netlify.toml` sets the base directory to `tally` and publishes `public/`, so you
can still connect this repo to Netlify with no build command. Or drag the
`tally/public` folder onto Netlify manually.
