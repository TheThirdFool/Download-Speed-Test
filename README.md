# Download-Speed-Test
A script to record the download and upload speed, then separately plot them.

Include this in the cronotab through using the command:

crontab -e

And then including an edited version of this code:

# =====================================================================================
# Example of job definition:
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
# |  |  |  |  |
# *  *  *  *  * user-name  command to be executed 

*/30 * * * * python /Path/To/SpeedTest.py
#*/2 * * * * echo "Doing a test"
# =====================================================================================

To visualise the data, run the second script:

python3 VisualiseSpeedTest.py

Enjoy.
