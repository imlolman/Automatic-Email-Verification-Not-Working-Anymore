import AutomaticEmailVerification as aev

print("All Available Domains: ")
print(aev.getAvailableDomains())
print(aev.fetch("aRandomMail"+aev.getADomain()))