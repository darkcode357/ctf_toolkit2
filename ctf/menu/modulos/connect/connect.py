import nclib

nc = nclib.Netcat(('localhost', 90), verbose=True)
nc.echo_hex = True
nc.send(b'\x00\x0dHello, world!')
