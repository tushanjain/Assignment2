#!/usr/bin/python
import random
import sys
from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink 

subnet1 = '10.0.0.'
subnet2 = '11.0.0.'


def emptyNet(nHost,nSwitch):

    "Create an empty network and add nodes to it."

    net = Mininet( controller=Controller )

    info( '*** Adding controller ***\n' )
    net.addController( 'c0' )

    info( '*** Adding hosts\n' )
    odd = []
    even = []
    arr = [] 
    for i in range(nHost):
        if i%2 == 0:
            randomN = random.randint(1,50000)
            h1 = net.addHost('h' +str(i), ip = subnet1 + str(i+1) )
            s = 'h' + str(i)
            arr.append({s:randomN} )
            odd.append(h1)
        else:
            h2 = net.addHost('h' + str(i),ip = subnet2 + str(i+1) )
            randomN = random.randint(1,50000)
            s = 'h' + str(i)
            arr.append({s:randomN})
            even.append(h2)
    print 'Host name and their id are as follows : '
    print arr
    # h1 = net.addHost( 'h1', ip= ip1  )
    # h2 = net.addHost( 'h2', ip= ip2 )

    info( '*** Adding switch\n' )
    switch = []
    for i in range(nSwitch):
        s3 = net.addSwitch('s'+str(i+1))
        switch.append(s3)

#    s3 = net.addSwitch( 's3' )

    info( '*** Creating links\n' )
    for i in range(nSwitch):
        a = net.addLink( odd[i], switch[i]) 
        a.intf1.config(bw=2)
        b = net.addLink(even[i], switch[i])
        b.intf1.config(bw=1)

    for i in range(nSwitch-1):
        net.addLink(switch[i], switch[i+1])
 
    # net.addLink( h1, s3 )
    # net.addLink( h2, s3 )
    
    info( '*** Starting network\n')
    net.start()

    info( '*** Running CLI\n' )
    CLI( net )

    info( '*** Stopping network' )
    net.stop()

if __name__ == '__main__':
    nHost = sys.argv[1]
    nHost = int(nHost)
    nSwitch = sys.argv[2]
    nSwitch = int(nSwitch)
    setLogLevel( 'info' )
    emptyNet(nHost,nSwitch)
