from subprocess import call

for x in range(1,330):
    s = str(x).zfill(3)
    mk = 'mkdir p' + s
    cp = 'cp Solution.java p' + s
    call(mk.split())
    call(cp.split())
