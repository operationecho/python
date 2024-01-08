import sys


def main(IPAddress):
    #Help()
    #Subnets()
    Subnets = """

                                O_o

        _______________________________________________
        Mask | TotalIP |  Formula   |  Total Usable IPs
        -----------------------------------------------
        32  =  1 IP    =   2**0     =  1 Usable IP
        31  =  2 IPs   =  (2**1)-2  =  0 Usable IPs
        30  =  4 IPs   =  (2**2)-2  =  2 Usable IPs
        29  =  8 IPs   =  (2**3)-2  =  6 Usable IPs
        28  =  16 IPs  =  (2**4)-2  =  14 Usable IPs
        27  =  32 IPs  =  (2**5)-2  =  30 Usable IPs
        26  =  64 IPs  =  (2**6)-2  =  62 Usable IPs
        25  =  128 IPs =  (2**7)-2  =  126 Usable IPs
        24  =  256 IPs =  (2**8)-2  =  254 Usable IPs

        """
    IPResults = SmartIPRange(IPAddress)
    print(IPResults)
    return IPResults


def Help():
    if len(sys.argv) == 1 or sys.argv[1].lower() == "-h":
        print("""
                                                    BOOM SHOCKA LOCKA

                            O_o  


        You done messed up. Try this next time:
            python ipsubnet_explode.py 192.168.0.15/28

        """)
        sys.exit(1)





def SmartIPRange(IPAddress):
    FullIP = IPAddress #sys.argv[1]
    # print(FullIP)
    SplitFullIP = FullIP.split("/")
    SubnetMaskNo = SplitFullIP[1]
    IntSubnetMask = int(SubnetMaskNo)
    IPAddress = SplitFullIP[0]
    PrefixSplit = IPAddress.split(".")
    Prefix = "{}.{}.{}.".format(PrefixSplit[0], PrefixSplit[1], PrefixSplit[2])

    SubnetRange = 2 ** (32 - IntSubnetMask)
    SubnetMaskEnd = 256 - SubnetRange

    IPResults = ""

    if IntSubnetMask > 23:
        LastOctet = PrefixSplit[3]

        FoundNetworkIP = "no"
        LowerNumber = 0
        UpperNumber = SubnetRange
        while FoundNetworkIP == "no":
            for i in range(LowerNumber, UpperNumber):
                # print(i)
                if int(LastOctet) == i:
                    # IPNetworkNumber = Prefix + str(LowerNumber)
                    FoundNetworkIP = "yes"
                    break
            else:
                LowerNumber += SubnetRange
                UpperNumber += SubnetRange
                if i >= 256:
                    FoundNetworkIP = "yes"

        IPResults += "IP Address = {}\n".format(IPAddress)
        IPResults += "SubnetMask = 255.255.255.{}\n".format(str(SubnetMaskEnd))
        IPResults += "Network IP = {}{}\n".format(Prefix, str(LowerNumber))
        IPResults += "Broadcast IP = {}{}\n".format(Prefix, str(UpperNumber - 1))
        IPResults += "Usable IPs = {}\n".format(SubnetRange - 2)
        ShowIPs = input("Want to see the Usable IPs in the network range? [y/n]: ")
        print("\n")
        if ShowIPs.lower() == "y":
            UsableIPs = "Usable Ips"
            #
            i = LowerNumber
            while i < UpperNumber - 2:
                i += 1
                UsableIPs += "{}\n".format(Prefix + str(i))

            IPResults += UsableIPs

    elif IntSubnetMask < 24 and IntSubnetMask > 15:
        SubnetRange = 2 ** (32 - (IntSubnetMask + 8))
        SubnetMaskEnd = 256 - SubnetRange
        LastOctet = PrefixSplit[2]

        FoundNetworkIP = "no"
        LowerNumber = 0
        UpperNumber = SubnetRange
        while FoundNetworkIP == "no":
            for i in range(LowerNumber, UpperNumber):
                # print(i)
                if int(LastOctet) == i:
                    # IPNetworkNumber = Prefix + str(LowerNumber)
                    FoundNetworkIP = "yes"
                    break
            else:
                LowerNumber += SubnetRange
                UpperNumber += SubnetRange
                if i >= 256:
                    FoundNetworkIP = "yes"

        IPResults += "IP Address = {}\n".format(IPAddress)
        IPResults += "SubnetMask = 255.255.{}.0\n".format(str(SubnetMaskEnd))
        IPResults += "Network IP = {}.{}.{}.0\n".format(PrefixSplit[0], PrefixSplit[1], str(LowerNumber))
        IPResults += "Broadcast IP = {}.{}.{}.255\n".format(PrefixSplit[0], PrefixSplit[1], str(UpperNumber - 1))
        IPResults += "Minimum IP = {}.{}.{}.1".format(PrefixSplit[0], PrefixSplit[1], str(LowerNumber))
        IPResults += "Maximum IP = {}.{}.{}.254".format(PrefixSplit[0], PrefixSplit[1], str(UpperNumber - 1))
        IPResults += "Usable IPs = {}".format(2 ** (32 - (IntSubnetMask)) - 2)



    elif IntSubnetMask < 16 and IntSubnetMask > 7:
        SubnetRange = 2 ** (32 - (IntSubnetMask + 16))
        SubnetMaskEnd = 256 - SubnetRange
        LastOctet = PrefixSplit[1]

        FoundNetworkIP = "no"
        LowerNumber = 0
        UpperNumber = SubnetRange
        while FoundNetworkIP == "no":
            for i in range(LowerNumber, UpperNumber):
                # print(i)
                if int(LastOctet) == i:
                    # IPNetworkNumber = Prefix + str(LowerNumber)
                    FoundNetworkIP = "yes"
                    break
            else:
                LowerNumber += SubnetRange
                UpperNumber += SubnetRange
                if i >= 256:
                    FoundNetworkIP = "yes"

        IPResults += "IP Address = {}".format(IPAddress)
        IPResults += "SubnetMask = 255.{}.0.0".format(str(SubnetMaskEnd))
        IPResults += "Network IP = {}.{}.0.0".format(PrefixSplit[0], PrefixSplit[1], str(LowerNumber))
        IPResults += "Broadcast IP = {}.{}.255.255".format(PrefixSplit[0], str(UpperNumber - 1))
        IPResults += "Minimum IP = {}.{}.0.1".format(PrefixSplit[0], PrefixSplit[1], str(LowerNumber))
        IPResults += "Maximum IP = {}.{}.255.254".format(PrefixSplit[0], str(UpperNumber - 1))
        IPResults += "Usable IPs = {}".format(2 ** (32 - (IntSubnetMask)) - 2)

    else:
        print("work in progress")

    return IPResults

if "__main__" == __name__:
    main(sys.argv[1])
