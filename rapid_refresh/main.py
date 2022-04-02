import yaml

with open("inventory.yml") as f:
    inventory = yaml.safe_load(f)

app1: list[str] = list(inventory["all"]["children"]["app1"]["hosts"].keys())

# https://help.ivanti.com/ht/help/en_US/ISM/2019.1/admin/Content/Configure/API/Structure_of_the_API_URL.htm
