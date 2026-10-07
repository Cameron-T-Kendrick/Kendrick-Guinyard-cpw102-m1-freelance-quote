def n(nf):

    nf = nf.strip.title

def main():
    cl = input("Client: ")    
    wh = int(input("worked hours: "))
    hr = int(input("hourly rate:"))
    m = int(input("material cost"))

l = hr * wh
mc = m
tc = l + mc
    
    print("project costs: ")
    print(l)
    print(mc)
    print(tc)
    print(n)