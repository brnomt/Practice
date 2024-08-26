import requests  # HTTP request
import sys  # CLI args

page = input("URL to analyze: ")

# List to save redirs.
redir = []

# 
r = requests.get(page, allow_redirects=False)

while r.status_code in [301, 302, 303, 307, 308]: #redirect code check

#301: Redirección permanente.
#302: Redirección temporal.
#303: Redirección a otra URL.
#307: Redirección temporal con el mismo método HTTP.
#308: Redirección permanente con el mismo método HTTP.

    # Print URl and status code
    print(f"Redirecting from {r.url} -> {r.headers['Location']} (Status code: {r.status_code})")

    # Save redirected URL to list
    redir.append(r.headers['Location'])

    r = requests.get(r.headers['Location'], allow_redirects=False)

# Print list
print("\nb2b redirections:")
for url in redir:
    print(url)

# Print final URL
print(f"\nFinal URL: {r.url}")
