#!/usr/bin/env python3
def find_the_redheads(inp):
    output = list(filter(lambda name: inp[name] == "red",inp))
    return output

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}
print(find_the_redheads(dupont_family))