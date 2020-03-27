# 0x06. Regular expression

## Description
What you should learn from this project:
For this project, you have to build your regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.

Because the focus of this exercise is to play with regular expressions (regex), here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the //:

```
sylvain@ubuntu$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
sylvain@ubuntu$
sylvain@ubuntu$ ./example.rb 127.0.0.2
127.0.0.2
sylvain@ubuntu$ ./example.rb 127.0.0.1
127.0.0.1
sylvain@ubuntu$ ./example.rb 127.0.0.a
```

### [0. Simply matching Holberton](./0-simply_match_holberton.rb)
* The regular expression must match Holberton

### [1. Repetition Token #0](./1-repetition_token_0.rb)
![1. Repetition Token #0](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/78/repetition-token-0.png)
* Find the regular expression that will match the above cases

### [2. Repetition Token #1](./2-repetition_token_1.rb)
![2. Repetition Token #1](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/78/repetition-token-1.png)
* Find the regular expression that will match the above cases

### [3. Repetition Token #2](./3-repetition_token_2.rb)
![3. Repetition Token #2](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/78/repetition-token-2.png)
* Find the regular expression that will match the above cases

### [4. Repetition Token #3](./4-repetition_token_3.rb)
![4. Repetition Token #3](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/78/repetition-token-3.png)
* Find the regular expression that will match the above cases

### [5. Not quite HBTN yet](./5-beginning_and_end.rb)
* The regular expression must be exactly matching a string that starts with h ends with n and can have any single character in between

### [6. Call me maybe](./6-phone_number.rb)
* The regular expression must match a 10 digit phone number

### [7. OMG WHY ARE YOU SHOUTING?](./7-OMG_WHY_ARE_YOU_SHOUTING.rb)
* The regular expression must be only matching: capital letters

### [8. Textme](./100-textme.rb)
* Your script should output: [SENDER],[RECEIVER],[FLAGS]
* The sender phone number or name (including country code if present)
* The receiver phone number or name (including country code if present)
* The flags that were used

### [9. Pass LinkedIn technical interview level0](./101-passed_linkedin_regex_challenge.jpg)
* [Solve LinkedIn regex puzzle] (https://engineering.linkedin.com/puzzle)
* Provide as an answer file a screenshot containing your contact information, including your Holberton email address
---

## Author
* **Aalaa Satti** - [alaksatti](https://github.com/alaksatti)
