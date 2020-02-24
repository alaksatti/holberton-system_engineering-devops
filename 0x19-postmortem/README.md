# Postmortem:

![meme, deploy before testing what could go wrong](https://cdn-images-1.medium.com/max/1600/1*spPhbypXBVdCYBaLai-Cxw.png) <br><br><br>

## Summary:<br>
On 02/18/2020 at 10:04 am PST a Wordpress website was down for approximately 17 minutes. During this time 100% of the website was unresponsive where all users experienced an internal server error (status code of 500). The root cause of the outage was a typographical error of a file name in which the file extension was incorrectly labeled as .phpp instead of .php . The website was running smoothly again 10:22 pm.<br><br>
## Timeline:<br>
02/18/2020 at 10:04 am PST: Website visitors reported the website to be down.<br>
02/18/2020 at 10:06 am PST: Engineers checked the website and found the 500 status code - internal server error.<br>
02/18/2020 at 10:07 am PST: All running processes were checked using ps -auxf .<br>
02/18/2020 at 10:10 am PST: A combination of strace -p {process}and tmux with curl -sI {local IP address} was used to narrow down possible sources of issues. Because Wordpress websites utilize a LAMP stack, processes involving Apache2, MySQL, and PHP were investigated as the root cause.<br>
02/18/2020 at 10:12 am PST: Apache2 and MySQL processes turned out to be functioning properly, indicating the error had to do with PHP. Error was found regarding error logs where the file var/www/html/wp-includes/class-wp-locale.php was not found. Further investigation revealed a typographical error in which the file was incorrectly named /var/www/html/wp-includes/class-wp-locale.phpp .<br>
02/18/2020 at 10:13 am PST: The issue was escalated to a team in the SRE division.<br>
02/18/2020 at 10:17 am PST: A puppet script was created to correct the typographical error.<br>
02/18/2020 at 10:18 am PST: Changes were checked by QA team before deployment to make sure issues were resolved.<br>
02/18/2020 at 10:21 am PST: Changes were deployed on all servers and website was restored and completely responsive.<br><br>
## Root Cause & Resolution:<br>
The root cause of the issue is a typographical error in which the file /var/www/html/wp-includes/class-wp-locale.phpp was required instead of the file /var/www/html/wp-includes/class-wp-locale.php . The error comes from the file extensions where .phpp was incorrectly specified instead of .php . The .phpp file did not exist causing the 500 status code error and resulting in the total outage. A puppet script was created to correct the typographical error, tested properly, and then deployed on all servers within 17 minutes of the outage. A copy of the puppet script can be found below:<br><br>
file { '/var/www/html/wp-includes/class-wp-locale.phpp':
      ensure => present,
      source => '/var/www/html/wp-includes/class-wp-locale.php',
}<br><br>
## Corrective and preventative measures:<br>
Important preventative measures that can be taken to ensure an error like this does not occur again involves testing new code before deployment. Improving the process to allow for multiple tests to be conducted before deployment minimizes the chance for errors like this one. Tasks that can be done to address the issue involve creating multiple layers of testing, testing done by multiple people, and utilizing versions of the site before deployment so that in the case an error occurs causing an outage a backup/previous version would be launched.<br><br><br>

![meme, test before you deploy](https://cdn-images-1.medium.com/max/1600/1*b-M0tsI9d29JcdoO2Zj6Rw.png)
