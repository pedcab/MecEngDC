#EM FALTA
#17out18 Falta criar variáveis "Result" para os modos a partir do 31 (onde aplicável)
#17out18 Não estão a imprimir no ficheiro os resultados dos cÃ¡lculos de vigas (ver "if" no código de impressão de resultados)
#22out18 Desenvolver "about"
#22out18 rever 50 (cilindros) para calcular com qualquer incógnita



#Module import
import math

#Run again loop (continues at the end of the program)
while True:

        #Splash screen
        print (' ')
        print (' ')
        print ('***************')
        print ('Mechanical Engineering Design Calculator')
        version = ('V0_22102018')
        print (version)
        print ('P.Cabral')
        print ('***************')
        print (' ')

        #Conversion factors
        #Pressure
        BarToPa=100000
        PaToBar=1/BarToPa
        #Volume
        LitreToCm3=1000
        Cm3ToLitre=1/LitreToCm3
        Cm3ToM3=1*10**-6
        M3ToCm3=1/Cm3ToM3
        #Frequency
        HzToRpm=60
        RpmToHz=1/HzToRpm
        #Power
        KwToW=1000
        WToKw=1/KwToW

        #Mode selector
        print ('SELECT MODE: ')
        print (' ')
        print ('00- ABOUT')
        print ('10- Torque - Power - RPM')
        print ('11- Torque - Diameter - Force')
        print ('20- Peripheral Velocity - Diameter - RPM')
        print ('30- Beams structural behaviour')
        print ('31- Resonance frequency of simple beams')
        print ('40- Balance of shafts')
        print ('50- Cylinders')
        print ('60- Hydraulic power')
        print (' ')
        mode = int(input(' '))

        #ABOUT


        #Torque - Power - RPM calculator
        if mode == 10:
                modeselected = ('Torque - Power - RPM calculator')
                def Torque_Power_RPM(Torque,Power,rpm):
                        if Torque == 0:
                                Torque = float ((Power*KwToW)/((rpm/60)*2*math.pi))
                                return (Torque)
                        elif Power == 0:
                                Power = float (Torque*(rpm/60)*2*math.pi)
                                return (Power*WToKw)
                        elif rpm == 0:
                                rpm = float ((((Power*KwToW)*60)/(Torque*math.pi*2)))
                                return (rpm)
                print(' ')
                print('TORQUE, POWER, RPM CALCULATOR')
                print(':::DATA INPUT ("0" if unkown):::')
                Torque=eval(input("Torque (Nm)? "))
                Power=eval(input("Power(kW)? "))
                rpm=eval(input("RPM(rpm)? "))
                print(' ')
                print('          :::RESULTS:::')
                print('          -------------')
                print("         ",modeselected)
                print(' ')
                Result=Torque_Power_RPM(Torque,Power,rpm)
                if Torque == 0:
                        TorqueResult = Result
                        PowerResult = Power
                        rpmResult = rpm
                        print("          Torque: ",TorqueResult," Nm")
                        print("          Power: ",PowerResult," kW")
                        print("          RPM: ",rpmResult)
                elif Power ==0:
                        TorqueResult = Torque
                        PowerResult = Result
                        rpmResult = rpm
                        print("          Torque: ",TorqueResult," Nm")
                        print("          Power: ",PowerResult," kW")
                        print("          RPM: ",rpmResult)
                elif rpm ==0:
                        TorqueResult = Torque
                        PowerResult = Power
                        rpmResult = Result
                        print("          Torque: ",TorqueResult," Nm")
                        print("          Power: ",PowerResult," kW")
                        print("          RPM: ",rpmResult)
                print('          -------------')

        #Torque - Diameter - Force calculator
        elif mode == 11:
                modeselected = ('Torque - Diameter - Force calculator')
                def Torque_Diameter_Force(Torque,Diameter,Force):
                        if Torque == 0:
                                Torque = float(Force*Diameter/2)
                                return (Torque)
                        elif Diameter == 0:
                                Diameter = float((Torque*2)/Force)
                                return (Diameter)
                        elif Force == 0:
                                Force = float (Torque/(Diameter/2))
                                return (Force)
                print(' ')
                print('TORQUE, DIAMETER, FORCE CALCULATOR')
                print(':::DATA INPUT ("0" if unkown):::')
                Torque=eval(input("Torque (Nm)? "))
                Diameter=eval(input("Diameter(m)? "))
                Force=eval(input("Force(N)? "))
                print(' ')
                print('          :::RESULTS:::')
                print('          -------------')
                print("         ",modeselected)
                print(' ')
                Result=Torque_Diameter_Force(Torque,Diameter,Force)
                if Torque == 0:
                        TorqueResult = Result
                        DiameterResult = Diameter
                        ForceResult = Force
                        print("          Torque: ",TorqueResult," Nm")
                        print("          Diameter: ",DiameterResult," m")
                        print("          Force: ",ForceResult," N")
                elif Diameter ==0:
                        TorqueResult = Torque
                        DiameterResult = Result
                        ForceResult = Force
                        print("          Torque: ",TorqueResult," Nm")
                        print("          Diameter: ",DiameterResult," m")
                        print("          Force: ",ForceResult," N")
                elif Force ==0:
                        TorqueResult = Torque
                        DiameterResult = Diameter
                        ForceResult = Result
                        print("          Torque: ",TorqueResult," Nm")
                        print("          Diameter: ",DiameterResult," m")
                        print("          Force: ",ForceResult," N")
                print('          -------------')

        #Peripheral velocity - Diameter - RPM calculator     
        elif mode == 20:
                modeselected = ('Peripheral velocity - Diameter - RPM calculator')
                def Velocity_Diameter_RPM(Velocity,Diameter,rpm):
                        if Velocity == 0:
                                Velocity= float(math.pi * Diameter* rpm/60)
                                return (Velocity)
                        elif Diameter == 0:
                                Diameter = float((Velocity*60)/(math.pi*rpm))
                                return (Diameter)
                        elif rpm == 0:
                                rpm = float((Velocity*60)/(math.pi*Diameter))
                                return (rpm)
                print(' ')
                print('PERIPHERAL VELOCITY, DIAMETER, RPM CALCULATOR')
                print(':::DATA INPUT ("0" if unkown):::')
                Velocity=eval(input("Peripheral velocity (m/s)? "))
                Diameter=eval(input("Diameter(m)? "))
                rpm=eval(input("RPM? "))
                print('          :::RESULTS:::')
                print('          -------------')
                print("         ",modeselected)
                print(' ')
                Result=Velocity_Diameter_RPM(Velocity,Diameter,rpm)
                if Velocity == 0:
                        VelocityResult = Result
                        DiameterResult = Diameter
                        rpmResult = rpm
                        print("          Peripheral velocity: ",VelocityResult," m/s")
                        print("          Diameter: ",DiameterResult," m")
                        print("          rpm: ",rpmResult)
                elif Diameter ==0:
                        VelocityResult = Velocity
                        DiameterResult = Result
                        rpmResult = rpm
                        print("          Peripheral velocity: ",VelocityResult," m/s")
                        print("          Diameter: ",DiameterResult," m")
                        print("          rpm: ",rpmResult)
                elif rpm ==0:
                        VelocityResult = Velocity
                        DiameterResult = Diameter
                        rpmResult = Result
                        print("          Peripheral velocity: ",VelocityResult," m/s")
                        print("          Diameter: ",DiameterResult," m")
                        print("          rpm: ",rpmResult)
                print('          -------------')


        #Structural beams (isostatic) calculator
        elif mode == 30:
                modeselected = ('Structural beams (isostatic) calculator')
                print ('STRUCTURAL BEAMS (ISOSTATIC) BEHAVIOUR CALCULATOR')
                print (' ')

                print ('Load/ Support cases: ')
                print ('100 - Cantilever, extremity point load')
                print ('101 - Simply supported, mid-span point load')
                print ('102 - Cantilever, full length equally distributed load')
                print (' ')

                beamtype = int(input('Select case: '))

                #Beamtype cantilever, extremity point load
                if beamtype == 100:
                        beamtypeselected = ('Cantilever, extremity point load')
                        def Cantilever_Extremity_Point_Load(y, P, L, E, I):
                                if y == 0:
                                        y = float(-(P*(L**3))/(3*E*I))
                                        return (y)
                                elif P == 0:
                                        P = float(-((y*3*E*I)/(L**3)))
                                        return (P)
                                elif L == 0:
                                        L = float(((y*3*E*I)/(P))**(1/3))
                                        return (L)
                                elif E == 0:
                                        E = float (-(P*(L**3))/(3*y*I))
                                        return (E)
                                elif I == 0:
                                        I = float(-(P*(L**3))/(3*E*y))
                                        return (I)

                        print(' ')
                        print('STRUCTURAL BEHAVIOUR OF BEAMS: CANTILEVER, EXTREMITY POINT LOAD CALCULATOR')
                        print(':::DATA INPUT ("0" if unkown):::')
                        y = eval(input("Deflection (m)? "))
                        P = eval(input("Point load (N)? "))
                        L = eval(input("Length (m)? "))
                        E = eval(input("Elastic modulus (Pa)? "))
                        I = eval(input("Moment of inertia (m^4)? "))
                        print(' ')
                        print('          :::RESULTS:::')
                        print('          -------------')
                        print("         ",beamtypeselected)
                        print(" ")
                        Result=Cantilever_Extremity_Point_Load(y, P, L, E, I)
                        if y == 0:
                                yResult = Result
                                PResult = P
                                LResult = L
                                EResult = E
                                IResult = I
                                print("          Deflection: ",yResult," m")
                                print("          Point load: ",PResult," N")
                                print("          Length: ",LResult, " m")
                                print("          Elastic modulus: ", EResult, "Pa")
                                print("          Moment of inertia: ", IResult, "m^4")
                        elif P ==0:
                                yResult = y
                                PResult = Result
                                LResult = L
                                EResult = E
                                IResult = I
                                print("          Deflection: ",yResult," m")
                                print("          Point load: ",PResult," N")
                                print("          Length: ",LResult, " m")
                                print("          Elastic modulus: ", EResult, "Pa")
                                print("          Moment of inertia: ", IResult, "m^4")
                        elif L ==0:
                                yResult = y
                                PResult = P
                                LResult = Result
                                EResult = E
                                IResult = I
                                print("          Deflection: ",yResult," m")
                                print("          Point load: ",PResult," N")
                                print("          Length: ",LResult, " m")
                                print("          Elastic modulus: ", EResult, "Pa")
                                print("          Moment of inertia: ", IResult, "m^4")
                        elif E ==0:
                                yResult = y
                                PResult = P
                                LResult = L
                                EResult = Result
                                IResult = I
                                print("          Deflection: ",yResult," m")
                                print("          Point load: ",PResult," N")
                                print("          Length: ",LResult, " m")
                                print("          Elastic modulus: ", EResult, "Pa")
                                print("          Moment of inertia: ", IResult, "m^4")
                        elif I ==0:
                                yResult = y
                                PResult = P
                                LResult = L
                                EResult = E
                                IResult = Result
                                print("          Deflection: ",yResult," m")
                                print("          Point load: ",PResult," N")
                                print("          Length: ",LResult, " m")
                                print("          Elastic modulus: ", EResult, "Pa")
                                print("          Moment of inertia: ", IResult, "m^4")
                        print('          -------------')

                #Beamtype cantilever, extremity point load
                if beamtype == 101:
                        beamtypeselected = ('Simply supported, mid-span point load')
                        def Simply_Supported_Mid_Span_Point_Load(y, P, L, E, I):
                                if y == 0:
                                        y = float(-(P*(L**3))/(48*E*I))
                                        return (y)
                                elif P == 0:
                                        P = float(-((y*48*E*I)/(L**3)))
                                        return (P)
                                elif L == 0:
                                        L = float(((y*48*E*I)/(P))**(1/3))
                                        return (L)
                                elif E == 0:
                                        E = float (-(P*(L**3))/(48*y*I))
                                        return (E)
                                elif I == 0:
                                        I = float(-(P*(L**3))/(48*E*y))
                                        return (I)
                        print(' ')
                        print('STRUCTURAL BEHAVIOUR OF BEAMS: SIMPLY SUPPORTED, MID-SPAN POINT LOAD CALCULATOR')
                        print(':::DATA INPUT ("0" if unkown):::')
                        y = eval(input("Deflection (m)? "))
                        P = eval(input("Point load (N)? "))
                        L = eval(input("Length (m)? "))
                        E = eval(input("Elastic modulus (Pa)? "))
                        I = eval(input("Moment of inertia (m^4)? "))
                        print(' ')
                        print('          :::RESULTS:::')
                        print('          -------------')
                        print("         ",beamtypeselected)
                        print(" ")
                        Result=Simply_Supported_Mid_Span_Point_Load(y, P, L, E, I)
                        if y == 0:
                                yResult = Result
                                PResult = P
                                LResult = L
                                EResult = E
                                IResult = I
                                print("          Deflection: ",yResult," m")
                                print("          Point load: ",PResult," N")
                                print("          Length: ",LResult, " m")
                                print("          Elastic modulus: ", EResult, "Pa")
                                print("          Moment of inertia: ", IResult, "m^4")
                        elif P ==0:
                                yResult = y
                                PResult = Result
                                LResult = L
                                EResult = E
                                IResult = I
                                print("          Deflection: ",yResult," m")
                                print("          Point load: ",PResult," N")
                                print("          Length: ",LResult, " m")
                                print("          Elastic modulus: ", EResult, "Pa")
                                print("          Moment of inertia: ", IResult, "m^4")
                        elif L ==0:
                                yResult = y
                                PResult = P
                                LResult = Result
                                EResult = E
                                IResult = I
                                print("          Deflection: ",yResult," m")
                                print("          Point load: ",PResult," N")
                                print("          Length: ",LResult, " m")
                                print("          Elastic modulus: ", EResult, "Pa")
                                print("          Moment of inertia: ", IResult, "m^4")
                        elif E ==0:
                                yResult = y
                                PResult = P
                                LResult = L
                                EResult = EResult
                                IResult = I
                                print("          Deflection: ",yResult," m")
                                print("          Point load: ",PResult," N")
                                print("          Length: ",LResult, " m")
                                print("          Elastic modulus: ", EResult, "Pa")
                                print("          Moment of inertia: ", IResult, "m^4")
                        elif I ==0:
                                yResult = y
                                PResult = P
                                LResult = L
                                EResult = E
                                IResult = IResult
                                print("          Deflection: ",yResult," m")
                                print("          Point load: ",PResult," N")
                                print("          Length: ",LResult, " m")
                                print("          Elastic modulus: ", EResult, "Pa")
                                print("          Moment of inertia: ", IResult, "m^4")
                                print('          -------------')


                #Beamtype Cantilever, full length equally distributed load             
                if beamtype == 102:
                        beamtypeselected = ('Cantilever, full length equally distributed load')
                        def Simply_Supported_Mid_Span_Point_Load(y, q, L, E, I):
                                if y == 0:
                                        y = float(-(q*(L**4))/(8*E*I))
                                        return (y)
                                elif q == 0:
                                        q = float(-((y*8*E*I)/(L**4)))
                                        return (q)
                                elif L == 0:
                                        L = float(((y*8*E*I)/(q))**(1/4))
                                        return (L)
                                elif E == 0:
                                        E = float (-(q*(L**4))/(8*y*I))
                                        return (E)
                                elif I == 0:
                                        I = float(-(q*(L**4))/(8*E*y))
                                        return (I)
                        print(' ')
                        print('STRUCTURAL BEHAVIOUR OF BEAMS: SIMPLY SUPPORTED, MID-SPAN POINT LOAD CALCULATOR')
                        print(':::DATA INPUT ("0" if unkown):::')
                        y = eval(input("Deflection (m)? "))
                        q = eval(input("Distributed load (N/m)? "))
                        L = eval(input("Length (m)? "))
                        E = eval(input("Elastic modulus (Pa)? "))
                        I = eval(input("Moment of inertia (m^4)? "))
                        print(' ')
                        print('          :::RESULTS:::')
                        print('          -------------')
                        print("         ",beamtypeselected)
                        print(" ")
                        Result=Simply_Supported_Mid_Span_Point_Load(y, q, L, E, I)
                        if y == 0:
                                yResult = Result
                                qResult = q
                                LResult = L
                                EResult = E
                                IResult = I
                                print("          Deflection: ",yResult," m")
                                print("          Distributed load: ", qResult," N/m")
                                print("          Length: ",LResult, " m")
                                print("          Elastic modulus: ", EResult, "Pa")
                                print("          Moment of inertia: ", IResult, "m^4")
                        elif q ==0:
                                yResult = y
                                qResult = Result
                                LResult = L
                                EResult = E
                                IResult = I
                                print("          Deflection: ",yResult," m")
                                print("          Distributed load: ", qResult," N/m")
                                print("          Length: ",LResult, " m")
                                print("          Elastic modulus: ", EResult, "Pa")
                                print("          Moment of inertia: ", IResult, "m^4")
                        elif L ==0:
                                yResult = y
                                qResult = q
                                LResult = Result
                                EResult = E
                                IResult = I
                                print("          Deflection: ",yResult," m")
                                print("          Distributed load: ", qResult," N/m")
                                print("          Length: ",LResult, " m")
                                print("          Elastic modulus: ", EResult, "Pa")
                                print("          Moment of inertia: ", IResult, "m^4")
                        elif E ==0:
                                yResult = y
                                qResult = q
                                LResult = L
                                EResult = Result
                                IResult = I
                                print("          Deflection: ",yResult," m")
                                print("          Distributed load: ", qResult," N/m")
                                print("          Length: ",LResult, " m")
                                print("          Elastic modulus: ", EResult, "Pa")
                                print("          Moment of inertia: ", IResult, "m^4")
                        elif I ==0:
                                yResult = y
                                qResult = q
                                LResult = L
                                EResult = E
                                IResult = Result
                                print("          Deflection: ",yResult," m")
                                print("          Distributed load: ", qResult," N/m")
                                print("          Length: ",LResult, " m")
                                print("          Elastic modulus: ", EResult, "Pa")
                                print("          Moment of inertia: ", IResult, "m^4")
                                print('          -------------')
        #Resonance of simple beams calculator
        elif mode == 31:
                modeselected = ('Resonance of simple beams')
                def Resonance_Simple_Beamsn1(E,I,L,q,n1):
                        w1=float((n1/2*(math.pi))*math.sqrt((E*I)/(q*(L**4))))
                        return w1
                def Resonance_Simple_Beamsn2(E,I,L,q,n2):
                        w2=float((n2/2*(math.pi))*math.sqrt((E*I)/(q*(L**4))))
                        return w2
                def Resonance_Simple_Beamsn3(E,I,L,q,n3):
                        w3=float((n3/2*(math.pi))*math.sqrt((E*I)/(q*(L**4))))
                        return w3
                print(' ')
                print('RESONANCE OF SIMPLE BEAMS CALCULATOR')
                E = float(input('Elastic modulus (Pa)?: '))
                I = float(input('Moment of inertia (m^4)?: '))
                L = float(input('Length (m)?: '))
                q = float(input('Distributed load (N/m)?: '))
                n1 = 9.87
                n2 = 39.5
                n3 = 88.8
                print(' ')
                print('          :::RESULTS:::')
                print('          -------------')
                print("         ",modeselected)
                print(' ')
                Resultw1=Resonance_Simple_Beamsn1(E,I,L,q,n1)
                Resultw2=Resonance_Simple_Beamsn2(E,I,L,q,n2)
                Resultw3=Resonance_Simple_Beamsn3(E,I,L,q,n3)
                print ('          First mode resonance frequency (Hz): ',Resultw1,' Hz')
                print ('          Second mode resonance frequency (Hz): ',Resultw2,' Hz')
                print ('          Third mode resonance frequency (Hz): ',Resultw3,' Hz')
                print ('          -------------')


        #Shaft's resonance frequency calculator
        elif mode == 40:
                modeselected = ('Balance of shafts')
                def Balance_Shafts_Thomson(l, E, I, m):
                        w1Thomson=((math.pi/l)**2)*(math.sqrt((E*I)/m))
                        return w1Thomson
                def Balance_Shafts_Rayleigh(l, E, I, m ,mi, yi):
                        w1Rayleigh=math.sqrt((9.8*mi*yi)/(mi*(yi**2)))
                        return w1Rayleigh
                print (' ')
                print ('RESONANCE FREQUENCY OF ROTATING SHAFTS CALCULATOR')
                print (':::DATA INPUT (zero if unknown):::')
                l = float(input('Unsupported length (m): '))
                E = float(input('Elastic modulus (Pa)?: '))
                I = float(input('Moment of inertia (m^4)?: '))
                m = float(input('Mass per unit length (kg/m)?: '))
                mi = float(input('Concentrated mass (kg)?: '))
                yi = float((((mi*9.8)*(l**3))/(3*E*I))+ ((5*(m*9.8)*l**4)/(384*E*I)))
                print(' ')
                print('          :::RESULTS:::')
                print('          -------------')
                print("         ",modeselected)
                print(' ')
                if mi == 0:
                        w1Thomson=Balance_Shafts_Thomson(l,E,I,m)
                        print ('First mode resonance frequency (Hz) (Thomson): ',w1Thomson,' Hz')
                        print ('First mode resonance frequency (Hz) (Rayleigh): ','n/d')
                        print('          -------------')
                else:
                        w1Thomson=Balance_Shafts_Thomson(l,E,I,m)
                        w1Rayleigh=Balance_Shafts_Rayleigh(l,E,I,m,mi,yi)
                        print ('First mode resonance frequency (Hz) (Thomson): ',w1Thomson,' Hz')
                        print ('First mode resonance frequency (Hz) (Rayleigh): ',w1Rayleigh,' Hz')
                        print ('          -------------')

        #Cylinder's force/ diameter calculator



        elif mode == 50:
                modeselected = ('Cylinders')
                def Cylinders(Ffw,Fret,D,d,P):
                        if Ffw == 0:
                                Ffw = P*math.pi*(D/2)**2
                                return Ffw
                        elif Fret == 0:
                                Fret = P*(math.pi*(D/2)**2)-(math.pi*(d/2)**2)
                                return  Fret
                        elif D == 0:
                                D = 2*math.sqrt(Ffw/(P*math.pi))
                                return D
                        elif d == 0:
                                d = (math.sqrt((P*math.pi*(D**2)-4*Fret)/P))/(math.sqrt(math.pi))
                                return d
                print (' ')
                print ('ACTUATOR CYLINDERS CALCULATOR')
                print (':::DATA INPUT (zero if unknown):::')
                Ffw = float(input('Forward force (N)?: '))
                Fret = float(input('Return force (N)?: '))
                D = float(input('Piston diameter (m)?: '))
                d = float(input('Rod diameter (m)?: '))
                P = float(input('Available fluid pressure (Pa)?: '))
                print(' ')
                print('          :::RESULTS:::')
                print('          -------------')
                print("         ",modeselected)
                print(' ')
                Result=Cylinders(Ffw,Fret,D,d,P)

                #Result=Torque_Power_RPM(Torque,Power,rpm)
                #if Torque == 0:
                 #       TorqueResult = Result
                  #      PowerResult = Power
                   #     rpmResult = rpm
                    #    print("          Torque: ",TorqueResult," Nm")
                     #   print("          Power: ",PowerResult," kW")
                      #  print("          RPM: ",rpmResult)


                if Ffw == 0 :
                        Ffwresult=Result
                        Fretresult=Fret
                        Dresult=D
                        dresult=d
                        Presult=P
                        print('Forward force: ',Result, ' N')
                        print('Return force: ',Fret, ' N')
                        print('Piston diameter: ',D, ' m')
                        print('Rod diameter: ', d, ' m')
                        print('Available fluid pressure: ', P, ' bar')
                        print('          -------------')
                elif Fret == 0:
                        Ffwresult=Ffw
                        Fretresult=Result
                        Dresult=D
                        dresult=d
                        Presult=P
                        print('Forward force: ',Ffw, ' N')
                        print('Return force: ',Result, ' N')
                        print('Piston diameter: ',D, ' m')
                        print('Rod diameter: ', d, ' m')
                        print('Available fluid pressure: ', P, ' bar')
                        print('          -------------')
                elif D == 0:
                        Ffwresult=Ffw
                        Fretresult=Fret
                        Dresult=Result
                        dresult=d
                        Presult=P
                        print('Forward force: ',Ffw, ' N')
                        print('Return force: ',Fret, ' N')
                        print('Piston diameter: ',Result, ' m')
                        print('Rod diameter: ', d, ' m')
                        print('Available fluid pressure: ', P, ' bar')
                        print('          -------------')
                elif d == 0:
                        Ffwresult=Ffw
                        Fretresult=Fret
                        Dresult=D
                        dresult=Result
                        Presult=P
                        print('Forward force: ',Ffw, ' N')
                        print('Return force: ',Fret, ' N')
                        print('Piston diameter: ',D, ' m')
                        print('Rod diameter: ', Result, ' m')
                        print('Available fluid pressure: ', P, ' bar')
                        print ('          -------------')
                elif P == 0:
                        Ffwresult=Ffw
                        Fretresult=Fret
                        Dresult=D
                        dresult=d
                        Presult=Result
                        print('Forward force: ',Ffw, ' N')
                        print('Return force: ',Fret, ' N')
                        print('Piston diameter: ',D, ' m')
                        print('Rod diameter: ', d, ' m')
                        print('Available fluid pressure: ', Result, ' bar')
                        print ('          -------------')

        #Hydraulic pump power calculator
        elif mode == 60:
                modeselected = ('Hydraulic power')
                def HydraulicPower(Power,rpm,Vstroke,pressure,efficiency,D,d,L,vfw,vrev,tfw,trev):
                        if Power==0:
                                Power=((rpm*RpmToHz)*(Vstroke*Cm3ToM3)*(pressure*BarToPa))/efficiency
                                return Power
                        elif rpm==0:
                                rpm=((Power*KwToW)*efficiency)/((Vstroke*Cm3ToM3)*(pressure*BarToPa))
                                return rpm
                print(' ')
                print('HYDRAULIC POWER CALCULATOR')
                print(':::DATA INPUT ("0" if unkown):::')
                Power = float(input('Power (kW)?: '))
                rpm = float(input('RPM ?: '))
                Vstroke = float(input('Displacement (cm^3/revolution)?: '))
                pressure = float(input('Hydraulic pressure (bar)?: '))
                efficiency = float(input('Combined efficiency ?: '))
                D = float(input('Cylinder diameter (mm)?: '))
                d = float(input('Rod diameter (mm)?: '))
                L = float(input('Stroke length (mm)?: '))
                vfw = float(input('Forward stroke speed (mm/min)?: '))
                vrev = float(input('Return stroke speed (mm/min)?: '))
                tfw = float(input('Forward stroke time (s)?: '))
                trev = float(input('Return stroke time (s)?: '))
                print(' ')
                print('          :::RESULTS:::')
                print('          -------------')
                print("         ",modeselected)
                print(' ')
                Result=HydraulicPower(Power,rpm,Vstroke,pressure,efficiency,D,d,L,vfw,vrev,tfw,trev)
                if Power == 0:
                        print('Power: ',Result*WToKw, ' kW')
                        print('RPM: ',rpm)
                        print('Pump displacement: ',Vstroke, ' cm^3/revolution')
                        print('Pressure: ',pressure, ' bar')
                        print('Efficiency: ',efficiency)
                        print('Cylinder diameter: ',D, ' mm')
                        print('Rod diameter: ',d, ' mm')
                        print('Stroke length: ',L,' mm')
                        print('Forward stroke speed: ',vfw, ' mm/min')
                        print('Return stroke speed: ',vrev, ' mm/min')
                        print('Forward stroke time: ',tfw, 's')
                        print('Return stroke time: ',trev, 's')
                        print('          -------------')
                elif rpm==0:
                        print('Power: ',Power, ' kW')
                        print('RPM: ',Result*HzToRpm)
                        print('Pump displacement: ',Vstroke, ' cm^3/revolution')
                        print('Pressure: ',pressure, ' bar')
                        print('Efficiency: ',efficiency)
                        print('Efficiency: ',efficiency)
                        print('Cylinder diameter: ',D, ' mm')
                        print('Rod diameter: ',d, ' mm')
                        print('Stroke length: ',L,' mm')
                        print('Forward stroke speed: ',vfw, ' mm/min')
                        print('Return stroke speed: ',vrev, ' mm/min')
                        print('Forward stroke time: ',tfw, 's')
                        print('Return stroke time: ',trev, 's')
                        print('          -------------')
        #SAVE RESULTS
        print (' ')
        save=input('Save (y/n)?: ')
        if save=='y':
                if mode==10:
                        filename=input('Filename?: ')
                        f = open(filename, 'w')
                        f.write('Mechanical Engineering Design Calculator\n')
                        f.write(version)
                        f.write(' \n')
                        f.write('Results summary\n')
                        f.write(' \n')
                        f.write('Filename: ')
                        f.write(filename)
                        f.write(' \n')
                        f.write(' \n')
                        f.write(str(modeselected))
                        f.write(' \n')
                        f.write(' \n')
                        f.write('Torque (Nm): ')
                        f.write(str (TorqueResult))
                        f.write(' \n')
                        f.write('Power (W): ')
                        f.write(str (PowerResult))
                        f.write(' \n')
                        f.write('RPM: ')
                        f.write(str (rpmResult))
                        f.close()
                elif mode==11:
                        filename=input('Filename?: ')
                        f = open(filename, 'w')
                        f.write('Mechanical Engineering Design Calculator\n')
                        f.write(version)
                        f.write(' \n')
                        f.write('Results summary\n')
                        f.write(' \n')
                        f.write('Filename: ')
                        f.write(filename)
                        f.write(' \n')
                        f.write(' \n')
                        f.write(str(modeselected))
                        f.write(' \n')
                        f.write(' \n')
                        f.write('Torque (Nm): ')
                        f.write(str (TorqueResult))
                        f.write(' \n')
                        f.write('Diameter (m): ')
                        f.write(str (DiameterResult))
                        f.write(' \n')
                        f.write('Force (N): ')
                        f.write(str (ForceResult))
                        f.close()
                elif mode==20:
                        filename=input('Filename?: ')
                        f = open(filename, 'w')
                        f.write('Mechanical Engineering Design Calculator\n')
                        f.write(version)
                        f.write(' \n')
                        f.write('Results summary\n')
                        f.write(' \n')
                        f.write('Filename: ')
                        f.write(filename)
                        f.write(' \n')
                        f.write(' \n')
                        f.write(str(modeselected))
                        f.write(' \n')
                        f.write(' \n')
                        f.write('Peripheral velocity (m/s): ')
                        f.write(str (VelocityResult))
                        f.write(' \n')
                        f.write('Diameter (m): ')
                        f.write(str (DiameterResult))
                        f.write(' \n')
                        f.write('RPM: ')
                        f.write(str (rpmResult))
                        f.close()
                elif mode==30:
                        filename=input('Filename?: ')
                        f = open(filename, 'w')
                        f.write('Mechanical Engineering Design Calculator\n')
                        f.write(version)
                        f.write(' \n')
                        f.write('Results summary\n')
                        f.write(' \n')
                        f.write('Filename: ')
                        f.write(filename)
                        f.write(' \n')
                        f.write(' \n')
                        f.write(str(modeselected))
                        f.write(' \n')
                        f.write(' \n')
                        f.write('Beam type: ')
                        f.write(str (beamtypeselected))
                        f.write(' \n')
                        f.write('Deflection (m): ')
                        f.write(str (yResult))
                        f.write(' \n')
                        if modeselected == 100 or modeselected == 101:
                                f.write('Load (N): ')
                                f.write(str (PResult))
                                f.write(' \n')
                        elif modeselected == 102:
                                f.write('Load (N/m): ')
                                f.write(str (qResult))
                                f.write(' \n')
                        f.write('Length (m): ')
                        f.write(str (LResult))
                        f.write(' \n')
                        f.write('Elastic modulus (Pa): ')
                        f.write(str (EResult))
                        f.write(' \n')
                        f.write('Moment of inertia (m^4): ')
                        f.write(str (IResult))
                        f.close()
                elif mode==31:
                        filename=input('Filename?: ')
                        f = open(filename, 'w')
                        f.write('Mechanical Engineering Design Calculator\n')
                        f.write(version)
                        f.write(' \n')
                        f.write('Results summary\n')
                        f.write(' \n')
                        f.write('Filename: ')
                        f.write(filename)
                        f.write(' \n')
                        f.write(' \n')
                        f.write(str(modeselected))
                        f.write(' \n')
                        f.write(' \n')
                        f.write('Distributed load (kg/m): ')
                        f.write(str (q))
                        f.write(' \n')
                        f.write('Length (m): ')
                        f.write(str (L))
                        f.write(' \n')
                        f.write('Elastic modulus (Pa): ')
                        f.write(str (E))
                        f.write(' \n')
                        f.write('Moment of inertia (m^4): ')
                        f.write(str (I))
                        f.write(' \n')
                        f.write('First mode resonance frequency (Hz): ')
                        f.write(str (Resultw1))
                        f.write(' \n')
                        f.write('Second mode resonance frequency (Hz): ')
                        f.write(str (Resultw2))
                        f.write(' \n')
                        f.write('Third mode resonance frequency (Hz): ')
                        f.write(str (Resultw3))
                        f.write(' \n')
                        f.close()
                elif mode==40:
                        filename=input('Filename?: ')
                        f = open(filename, 'w')
                        f.write('Mechanical Engineering Design Calculator\n')
                        f.write(version)
                        f.write(' \n')
                        f.write('Results summary\n')
                        f.write(' \n')
                        f.write('Filename: ')
                        f.write(filename)
                        f.write(' \n')
                        f.write(' \n')
                        f.write(str(modeselected))
                        f.write(' \n')
                        f.write(' \n')
                        f.write('Unsupported length (m): ')
                        f.write(str (l))
                        f.write(' \n')
                        f.write('Elastic modulus (Pa): ')
                        f.write(str (E))
                        f.write(' \n')
                        f.write('Moment of inertia (m^4): ')
                        f.write(str (I))
                        f.write(' \n')
                        f.write('Mass per unit length (kg/m): ')
                        f.write(str (m))
                        f.write(' \n')
                        f.write('Concentrated mass (kg): ')
                        f.write(str (mi))
                        f.write(' \n')
                        f.write('Deflection under concentrated mass (m): ')
                        f.write(str (yi))
                        f.write(' \n')
                        f.write('First mode resonance frequency (Hz) (Thomson): ')
                        f.write(str (w1Thomson))
                        f.write(' \n')
                        f.write('First mode resonance frequency (Hz) (Rayleigh): ')
                        f.write(str (w1Rayleigh))
                        f.write(' \n')
                        f.close()
                elif mode==50:
                        filename=input('Filename?: ')
                        f = open(filename, 'w')
                        f.write('Mechanical Engineering Design Calculator\n')
                        f.write(version)
                        f.write(' \n')
                        f.write('Results summary\n')
                        f.write(' \n')
                        f.write('Filename: ')
                        f.write(filename)
                        f.write(' \n')
                        f.write(' \n')
                        f.write(str(modeselected))
                        f.write(' \n')
                        f.write(' \n')
                        f.write('Forward force (N): ')
                        f.write(str (Ffwresult))
                        f.write(' \n')
                        f.write('Return force (N): ')
                        f.write(str (Fretresult))
                        f.write(' \n')
                        f.write('Piston diameter (m): ')
                        f.write(str (Dresult))
                        f.write(' \n')
                        f.write('Rod diameter (m): ')
                        f.write(str (dresult))
                        f.write(' \n')
                        f.write('Available fluid pressure (Pa): ')
                        f.write(str (Presult))
                        f.write(' \n')
                        f.close()
                elif mode==60:
                        filename=input('Filename?: ')
                        f = open(filename, 'w')
                        f.write('Mechanical Engineering Design Calculator\n')
                        f.write(version)
                        f.write(' \n')
                        f.write('Results summary\n')
                        f.write(' \n')
                        f.write('Filename: ')
                        f.write(filename)
                        f.write(' \n')
                        f.write(' \n')
                        f.write(str(modeselected))
                        f.write(' \n')
                        f.write(' \n')
                        f.write('Power (kW): ')
                        f.write(str (Power))
                        f.write(' \n')
                        f.write('RPM: ')
                        f.write(str (rpm))
                        f.write(' \n')
                        f.write('Pump displacement (cm^3/revolution): ')
                        f.write(str (Vstroke))
                        f.write(' \n')
                        f.write('Pressure (bar): ')
                        f.write(str (pressure))
                        f.write(' \n')
                        f.write('Efficiency: ')
                        f.write(str (efficiency))
                        f.write(' \n')
                        f.write('Cylinder diameter (mm): ')
                        f.write(str (D))
                        f.write(' \n')
                        f.write('Rod diameter (d): ')
                        f.write(str (d))
                        f.write(' \n')
                        f.write('Stroke length (mm): ')
                        f.write(str (L))
                        f.write(' \n')
                        f.write('Forward stroke speed (mm/min): ')
                        f.write(str (vfw))
                        f.write(' \n')
                        f.write('Return stroke speed (mm/min): ')
                        f.write(str (vrev))
                        f.write(' \n')
                        f.write('Forward stroke time (s): ')
                        f.write(str (tfw))
                        f.write(' \n')
                        f.write('Return stroke time (s): ')
                        f.write(str (trev))
                        f.write(' \n')
                        f.close()
        elif save=='n':
                print('Not saved!')
        print (' ')

#Run again loop control
        while True:
                answer = input('Run again? (y/n): ')
                if answer in ('y', 'n'):
                        break
                print ('Invalid input.')
        if answer == 'y':
                continue
        else:
                print ('Goodbye!')
                print (' ')
                print (' ')
                print (' ')
                break
