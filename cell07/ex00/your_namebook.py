#!/usr/bin/env python3
def array_of_names(inp):
    output = []
    for first,last in inp.items():
        name = first.capitalize()+" "+last.capitalize()
        output.append(name)
    return output

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}
print(array_of_names(persons))

