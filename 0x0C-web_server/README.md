# 0x0C. Web server

## Description
What you should learn from this project:

* What is the main role of a web server
* What is a child process
* Why web servers usually have a parent process and child processes
* What are the main HTTP requests

---

### [0. Transfer a file to your server](./0-transfer_file)
* Write a Bash script that transfers a file from our client to a server:


### [1. Install nginx web server](./1-install_nginx_web_server)
* Install nginx on your web-01 server
* Nginx should be listening on port 80
* When querying Nginx at its root / with a GET request (requesting a page) using curl, it must return a page that contains the string Holberton School
* As an answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements


### [2. Setup a domain name](./2-setup_a_domain_name)
* .TECH Domains is one of the top domain providers. They are known for the stability and quality of their DNS hosting solution. Holberton School partnered with .TECH Domains so that you can learn about DNS.


### [3. Redirection](./3-redirection)
* Readme:


### [4. Not found page 404](./4-not_found_page_404)
* Configure your Nginx server to have a custom 404 page that contains the string Ceci n'est pas une page.


### [5. Design a beautiful 404 page](./5-design_a_beautiful_404_page)
* Some of my favorites:


### [6. Install Nginx web server (w/ Puppet)](./7-puppet_install_nginx_web_server.pp)
* Time to practice configuring your server with Puppet! Just as you did before, we’d like you to install and configure an Nginx server using Puppet instead of Bash. To save time and effort, you should also include resources in your manifest to perform a 301 redirect when querying /redirect_me.

---

## Author
* **Aalaa Satti** - [alaksatti](https://github.com/alaksatti)
