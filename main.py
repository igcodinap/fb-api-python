import json
import facebook

def main():
    token = {"EAAOpVL6foG8BAAcZASxOCCZAE6qjHbNUPFmciLyAGCFRWhhq8XCEGFNIybiyuHatRlZAwpEcitC8EyhNjPt8h37dphwW0yj8ZC0hcZCIeRnfte8HLgUS7SjvheYINenvpdXYlsrkR8bMCYV4D7hWOMXGQwWD2NLWEAB8GiHSCuZAp8lntt3cr3Mgbr6LpBHW15jnyxPFnI8eNLsNgjABMkZAuqIqtu0T3JBSto5aherHQZDZD"}
    graph = facebook.GraphAPI(token)

    fields = ['name,email, events']

    ids = [10156853388023027, 10221292185153045]
    
    for id in ids:
        profile = graph.get_object(id, fields = fields)
        print(json.dumps(profile, indent=4))

if __name__ =="__main__":
    main()
