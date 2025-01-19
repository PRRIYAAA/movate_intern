from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

def modify_url(base_url):
    # Parse the base URL
    parsed_url = urlparse(base_url)
    query_params = parse_qs(parsed_url.query)
    
    # Modify query parameters to match the second URL format
    updated_params = {
        "pid": query_params.get("pid", [""])[0],
        "lid": query_params.get("lid", [""])[0],
        "aid": "overall",
        "certifiedBuyer": "false",
        "sortOrder": "MOST_HELPFUL"
    }
    
    # Create the updated query string
    updated_query = urlencode(updated_params)
    
    # Construct the new URL
    new_url = urlunparse((
        parsed_url.scheme,
        parsed_url.netloc,
        parsed_url.path,
        parsed_url.params,
        updated_query,
        parsed_url.fragment
    ))
    return new_url

# Base URL
base_url = "https://www.flipkart.com/flipkart-smartbuy-army-keychain-torch-screwdriver-knife-bottle-opener-key-chain/product-reviews/itm9d4dbcd2cd4b6?pid=KECFZYXGHKHBVBK8&lid=LSTKECFZYXGHKHBVBK8PCUPSM&marketplace=FLIPKART&q=keychain&store=dgv%2Ftkw%2Famn&srno=s_1_5&otracker=search&fm=organic&iid=bb785e12-a439-44b3-8b13-23371ae5b76f.KECFZYXGHKHBVBK8.SEARCH&ppt=hp&ppn=homepage&ssid=cvdh45cclc0000001737122874770&qH=857823c186f036a6"

# Convert the base URL
modified_url = modify_url(base_url)
print(modified_url)
