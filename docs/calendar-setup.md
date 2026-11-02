# Google Calendar setup (account steps)

1. In Google Cloud Console, create a project named Bayesian Study Planner.
2. Enable Google Calendar API.
3. Configure Google Auth Platform branding, audience and data access for a
   personal testing app. If External/testing, add your own Google account as
   a test user. A university-managed account may require administrator access.
4. Create an OAuth client for a Desktop app, and download its JSON file.
5. Save the file locally as credentials.json in the project root.
6. Create a separate Google calendar named Study Planner Test and retain its ID.
7. During Week 11, implement installed-app OAuth using google-auth-oauthlib,
   requesting the narrowest event scope sufficient for the test calendar.
   Store the resulting token only in token.json (already ignored by Git).

Week 8 does not require authorizing or creating events. No credentials are
included in this starter, and the calendar function currently raises
NotImplementedError. Final integration should preview actions before writing,
handle conflicts and time zones, and avoid duplicate events on repeated refresh.
