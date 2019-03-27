# c4d-custom-sanity-check
Pre submit script to set custom frame range
Only tested with Deadline 10

## Install
Copy CustomSanityChecks.py to REPO/Submission/Cinema4D/Main/CustomSanityChecks.py
It will run automatically right before the submission dialog is shown.
Use at your own risk!

## Description
When submitting jobs to Deadline its often usefull to have the first and the last frame rendered first.
This script takes the frame range from the Render Settings and reformats it like this:
firstFrame, lastFrame, midFrame and then the whole frame range.
So if frame range in Render Settings are 0-200 the resulting frame range will look like this:
`0,200,100,0-200`
Deadline will clean this up on submission so it looks like this:
`0,200,100,1-99,101,199`