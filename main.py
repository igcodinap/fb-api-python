import json
import facebook

def main():
    token = {"EAAOpVL6foG8BAFRsNLE7vy4br5tZA6N29MBptZBPjo4P0WXWYtJAU0waBOmZCslgPAFZAv0UZAhDUr9AZALu5EFS1K1AVWzmBZBMObo578lV0wyItQC8E170y6AxgC8V15oxvHJFI3yFR2T1eRsL2onwCjhYioPP8Fnq95SZB2Ijs4n6fXlnw7iO7G75SEQWuBsApmM98g7uNqaXx5hxro9IjvyEQ6s4H0jaVKMmTN5njwZDZD"}
    graph = facebook.GraphAPI(token)

    fields = ['name,email, events']

    profile = graph.get_object('me', fields = fields)

    print(json.dumps(profile, indent=4))

if __name__ =="__main__":
    main()
