# Automatic-Email-Verification

Building a Python module For Automatic Email Verification using Python and temp-mail.org

 ## Usage

### Simply add module to your project and

```python
import AutomaticEmailVerification as aev
```

### You can get all available domains by using 
```python
aev.getAvailableDomains() # Returns a List of Available Domains
```

### You can get a random domain by using 
```python
aev.getADomain() # Returns a string ex: @cliptik.net
```

### **Fetch an email using**
```python
aev.fetch("aRandomMail@cliptik.net") 

# Returns a String in case of Error.
# or returns an array of emails each with link, subject, sender, body.

# optionally you can specify weather you want all the content or not.

aev.fetch("aRandomMail@cliptik.net", body, subject, sender,link)
# each as 0|1 as per your requirement.
```

## An CLI Version is Comming Soon.....