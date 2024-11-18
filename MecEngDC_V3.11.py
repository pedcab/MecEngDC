#Module import
import math
#Run again loop (continues at the end of the program)
while True:
        #Title name
        TitleName=('Mechanical Engineering Design Calculator')
        Version=('V3.11_27022024')
        Author=('P.Cabral')
        AuthorContact=('pedro_cabral@sapo.pt')
        SaveFileTitle=('Summary of results')
        CautionSentence=('Kindly remember that it is considered to be good engineering practice'+'\n'+'to always double check your calculations using independent methodologies.')
        #Splash screen
        print ('  __  __           ______             _____   _____ ')
        print (' |  \/  |         |  ____|           |  __ \ / ____| ')
        print (' | \  / | ___  ___| |__   _ __   __ _| |  | | |      ')
        print (' | |\/| |/ _ \/ __|  __| | "_ \ / _` | |  | | |  ')
        print (' | |  | |  __/ (__| |____| | | | (_| | |__| | |____ ')
        print (' |_|  |_|\___|\___|______|_| |_|\__, |_____/ \_____| ')
        print ('                                 __/ |               ')
        print ('                                |___/  ')
        print (' ')
        print (TitleName)
        print (Version)
        print (Author)
        print (AuthorContact)
        print ('***************')
        print ('Kindly remember that it is considered to be good engineering practice to always double check your calculations using' +'\n'+'independent methodologies.')
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
        print (' 00  - ABOUT')
        print (' 10  - Torque - Power - RPM')
        print (' 30  - Beams structural behaviour')
        print (' 31  - Resonance frequency of simple beams')
        print (' 40  - Balance of shafts')
        print (' 41  - Power screws (required torque)')
        print (' 42  - Servomotors')
        print (' 43  - Axles to shear (radial load)')
        print (' 44  - Driveshafts to shear (torsional load)')
        print (' 45  - Geared motors for traction systems')
        print (' 50  - Cylinders')
        print (' 60  - Hydraulic power')
        print (' 70  - Bolted connections')
        print (' 80  - Static disc brakes')
        print (' 90  - Helical springs')
        print (' 100 - Spur gears')
        print (' 110 - Pressure vessels')
        print (' 120 - Linear motion dynamics')
        print (' 130 - Rectangular flat plates')
        print (' ')
        mode = int(input(' '))
        #ABOUT
        if mode == 00:
            print('This program has been compiled with the intention of providing a quick reference tool for all those interested in' + '\n' 'machine design.'+'\n'+'\n'+
                  'I decline any responsability in design errors derived from blind use of this calculator.'+'\n'+'\n'+
                  'Kindly remember that it considered to be good engineering practice to always double check your calculations using'+'\n'+
                  'independent methodologies.'+'\n'+'\n'+
                  'Output files are saved in the executable folder'+'\n'+'\n'
                  'Version notes:'+'\n'+'\n'+
                  'V1_02112020 :' +'\n'+
                  '-First version for release' +'\n'+'\n'
                  'V2_11112020 :' + '\n'+
                  '-Added 70 - Bolted connections' +'\n'+'\n'
                  'V3_19112020 :' + '\n'
                  '-Minor corrections on units and conversions'+'\n'
                  '-Added ascii art logo' +'\n'+'\n' 
                  'V3.1_25112020 :' + '\n'+
                  '-Added 43 - Axles to shear (radial load)'+ '\n'+
                  '-Added 44 - Driveshafts to shear (torsional load)' +'\n'+'\n'
                  'V3.2_26112020 :' + '\n'+
                  '-Added 80 - Static disc brakes' +'\n'+'\n'
                  'V3.3_21122020 :' + '\n'+
                  '-Corrected save routine for 50-Cylinders' + '\n'
                  '-Added 90 - Helical springs' +'\n'+'\n'
                  'V3.4_05092021 :' + '\n'+
                  '-Added 45 - Geared motors for traction systems' +'\n' +'\n'
                  'V3.5_17092021 :' + '\n'+
                  '-Corrected reservoir volume formula in 60-Hydraulic power' +'\n'+'\n'
                  'V3.6_08102021 :' + '\n'+
                  '-Corrected efficiency in 45 - Geared motors for traction systems' +'\n'+'\n'
                  'V3.7_17052022 :' + '\n'+
                  '-Corrected formula on 90 - Helical springs' +'\n'+'\n'+
                  'V3.8_27052022 :' + '\n'+
                  '-Added 100 - Spur gears' +'\n'+'\n'
                  'V3.9_28092022 :' + '\n'+
                  '-Added 110 - Pressure vessels' +'\n'+'\n'
                  'V3.10_17052023 :' + '\n'+
                  '-Added 120 - Linear movement dynamics' +'\n'+'\n'
                  'V3.11_27022024 :' + '\n'+
                  '-Added 130 - Rectangular flat plates' +'\n'+'\n'+'\n')
        #Torque - Power - RPM calculator
        if mode == 10:
                modeselected = ('Torque - Power - RPM calculator')
                print(' ')
                print('TORQUE, POWER, RPM CALCULATOR' + '\n'+ '\n'+':::DATA INPUT ("0" if unkown):::')
                Torque=eval(input("Torque (Nm)? "))
                Power=eval(input("Power(kW)? "))
                rpm=eval(input("RPM(rpm)? "))
                print('          :::RESULTS:::')
                print('          -------------')
                if Torque == 0:
                        PowerW = Power*1000
                        Torque = float ((PowerW)/((rpm/60)*2*math.pi))
                        print("          Torque: ",Torque," Nm")
                        print("          Power: ",Power," kW")
                        print("          RPM: ",rpm)
                elif Power ==0:
                        PowerW = float (Torque*(rpm/60)*2*math.pi)
                        Power = PowerW/1000
                        print("          Torque: ",Torque," Nm")
                        print("          Power: ",Power," kW")
                        print("          RPM: ",rpm)
                elif rpm ==0:
                        PowerW = Power*1000
                        rpm = float ((((PowerW)*60)/(Torque*math.pi*2)))
                        print("          Torque: ",Torque," Nm")
                        print("          Power: ",Power," kW")
                        print("          RPM: ",rpm)
                print('          -------------')
                print (CautionSentence)
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
                        if y == 0:
                                y = float(-(P*(L**3))/(3*E*I))
                                print("          Deflection: ",y," mm")
                                print("          Point load: ",P," N")
                                print("          Length: ",L, " m")
                                print("          Elastic modulus: ", E, "Pa")
                                print("          Moment of inertia: ", I, "m^4")
                        elif P ==0:
                                P = float(-((y*3*E*I)/(L**3)))
                                print("          Deflection: ",y," m")
                                print("          Point load: ",P," N")
                                print("          Length: ",L, " m")
                                print("          Elastic modulus: ", E, "Pa")
                                print("          Moment of inertia: ", I, "m^4")
                        elif L == 0:
                                L = float(((y*3*E*I)/(P))**(1/3))
                                print("          Deflection: ",y," m")
                                print("          Point load: ",P," N")
                                print("          Length: ",L, " m")
                                print("          Elastic modulus: ", E, "Pa")
                                print("          Moment of inertia: ", I, "m^4")
                        elif E == 0:
                                E = float (-(P*(L**3))/(3*y*I))
                                print("          Deflection: ",y," m")
                                print("          Point load: ",P," N")
                                print("          Length: ",L, " m")
                                print("          Elastic modulus: ", E, "Pa")
                                print("          Moment of inertia: ", I, "m^4")
                        elif I == 0:
                                I = I = float(-(P*(L**3))/(3*E*y))
                                print("          Deflection: ",y," m")
                                print("          Point load: ",P," N")
                                print("          Length: ",L, " m")
                                print("          Elastic modulus: ", E, "Pa")
                                print("          Moment of inertia: ", I, "m^4")
                        print('          -------------')
                        print (CautionSentence)
                #Beamtype cantilever, extremity point load
                if beamtype == 101:
                        beamtypeselected = ('Simply supported, mid-span point load')
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
                        if y == 0:
                                y = float(-(P*(L**3))/(48*E*I))
                                print("          Deflection: ",y," m")
                                print("          Point load: ",P," N")
                                print("          Length: ",L, " m")
                                print("          Elastic modulus: ", E, "Pa")
                                print("          Moment of inertia: ", I, "m^4")
                        elif P ==0:
                                P = float(-((y*48*E*I)/(L**3)))
                                print("          Deflection: ",y," m")
                                print("          Point load: ",P," N")
                                print("          Length: ",L, " m")
                                print("          Elastic modulus: ", E, "Pa")
                                print("          Moment of inertia: ", I, "m^4")
                        elif L ==0:
                                L = float(((y*48*E*I)/(P))**(1/3))
                                print("          Deflection: ",y," m")
                                print("          Point load: ",P," N")
                                print("          Length: ",L, " m")
                                print("          Elastic modulus: ", E, "Pa")
                                print("          Moment of inertia: ", I, "m^4")
                        elif E ==0:
                                E = float (-(P*(L**3))/(48*y*I))
                                print("          Deflection: ",y," m")
                                print("          Point load: ",P," N")
                                print("          Length: ",L, " m")
                                print("          Elastic modulus: ", E, "Pa")
                                print("          Moment of inertia: ", I, "m^4")
                        elif I ==0:
                                I = float(-(P*(L**3))/(48*E*y))
                                print("          Deflection: ",y," m")
                                print("          Point load: ",P," N")
                                print("          Length: ",L, " m")
                                print("          Elastic modulus: ", E, "Pa")
                                print("          Moment of inertia: ", I, "m^4")
                                print('          -------------')
                                print (CautionSentence)
                #Beamtype Cantilever, full length equally distributed load             
                if beamtype == 102:
                        beamtypeselected = ('Cantilever, full length equally distributed load')
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
                        if y == 0:
                                y = float(-(q*(L**4))/(8*E*I))
                                print("          Deflection: ",y," m")
                                print("          Distributed load: ", q," N/m")
                                print("          Length: ",L, " m")
                                print("          Elastic modulus: ", E, "Pa")
                                print("          Moment of inertia: ", I, "m^4")
                        elif q ==0:
                                q = float(-((y*8*E*I)/(L**4)))
                                print("          Deflection: ",y," m")
                                print("          Distributed load: ", q," N/m")
                                print("          Length: ",L, " m")
                                print("          Elastic modulus: ", E, "Pa")
                                print("          Moment of inertia: ", I, "m^4")
                        elif L ==0:
                                L = float(((y*8*E*I)/(q))**(1/4))
                                print("          Deflection: ",y," m")
                                print("          Distributed load: ", q," N/m")
                                print("          Length: ",L, " m")
                                print("          Elastic modulus: ", E, "Pa")
                                print("          Moment of inertia: ", I, "m^4")
                        elif E ==0:
                                E = float (-(q*(L**4))/(8*y*I))
                                print("          Deflection: ",y," m")
                                print("          Distributed load: ", q," N/m")
                                print("          Length: ",L, " m")
                                print("          Elastic modulus: ", E, "Pa")
                                print("          Moment of inertia: ", I, "m^4")
                        elif I ==0:
                                I = float(-(q*(L**4))/(8*E*y))
                                print("          Deflection: ",y," m")
                                print("          Distributed load: ", q," N/m")
                                print("          Length: ",L, " m")
                                print("          Elastic modulus: ", E, "Pa")
                                print("          Moment of inertia: ", I, "m^4")
                        print('          -------------')        
                        print (CautionSentence)
        #Resonance of simple beams calculator
        elif mode == 31:
                modeselected = ('Resonance of simple beams')
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
                w1=float((n1/2*(math.pi))*math.sqrt((E*I)/(q*(L**4))))
                w2=float((n2/2*(math.pi))*math.sqrt((E*I)/(q*(L**4))))
                w3=float((n3/2*(math.pi))*math.sqrt((E*I)/(q*(L**4))))
                print ('          First mode resonance frequency (Hz): ',w1,' Hz')
                print ('          Second mode resonance frequency (Hz): ',w2,' Hz')
                print ('          Third mode resonance frequency (Hz): ',w3,' Hz')
                print('          -------------')        
                print (CautionSentence)
        #Shaft's resonance frequency calculator
        elif mode == 40:
                modeselected = ('Balance of shafts')
                print (' ')
                print ('RESONANCE FREQUENCY OF ROTATING SHAFTS CALCULATOR')
                l = float(input('Unsupported length (m): '))
                E = float(input('Elastic modulus (Pa)?: '))
                I = float(input('Moment of inertia (m^4)?: '))
                m = float(input('Mass per unit length (kg/m)?: '))
                mi = float(input('Concentrated mass (kg)?: '))
                print(' ')
                print('          :::RESULTS:::')
                print('          -------------')
                print("         ",modeselected)
                print(' ')
                if mi == 0:
                        w1Thomson=((math.pi/l)**2)*(math.sqrt((E*I)/m))
                        print ('First mode resonance frequency (Hz) (Thomson): ',w1Thomson,' Hz')
                        print ('First mode resonance frequency (Hz) (Rayleigh): ','n/d')
                        print('          -------------')
                else:
                        yi = float((((mi*9.8)*(l**3))/(3*E*I))+ ((5*(m*9.8)*l**4)/(384*E*I)))
                        w1Thomson=((math.pi/l)**2)*(math.sqrt((E*I)/m))
                        w1Rayleigh=math.sqrt((9.8*mi*yi)/(mi*(yi**2)))
                        print ('First mode resonance frequency (Hz) (Thomson): ',w1Thomson,' Hz')
                        print ('First mode resonance frequency (Hz) (Rayleigh): ',w1Rayleigh,' Hz')
                        print ('          -------------')
                print('          -------------')        
                print (CautionSentence)
        #Power screw dynamics calculator
        elif mode ==41:
                modeselected = ('Power screw required actuator torque')
                print (' ')
                print ('POWER SCREW ACTUATOR TORQUE')
                print (':::DATA INPUT:::')
                F = float(input('Applied load (N): '))
                dm = float(input('Screw thread pitch diameter (mm): '))
                z = float(input('Thread pitch (mm): '))
                u = float(input('Coefficient of friction between screw and nut: '))
                rpm = float(input('Actuator rpm: '))
                v = float(input('Required movement speed (m/min): '))
                e = float(input('Actuator efficiency: '))
                Mt =  ((F*(dm/1000))/2) * (((z/1000)+math.pi*u*(dm/1000))/(math.pi*(dm/1000)-u*(z/1000)))
                Srpm = (v*1000)/z
                i = rpm / Srpm
                P = (Mt * (Srpm/60) * (2*math.pi)) * (1/e)
                print(' ')
                print('          :::RESULTS:::')
                print('          -------------')
                print("         ",modeselected)
                print(' ')
                print('Applied load: ', F, ' N')
                print('Required movement speed: ', v,' m/min')
                print('Actuator efficiency: ',e)
                print('Screw thread pitch diameter: ', dm, ' mm')
                print('Screw thread pitch: ', z, ' mm')
                print('Coefficient of friction between screw and nut: ', u)
                print('Actuator rpm: ',rpm)
                print('Screw rpm: ',Srpm)
                print('Required reduction: 1/',i)
                print('Torque required to displace the load: ', Mt, ' Nm')
                print('Power required to displace the load: ', P/1000, 'kW')
                print('          -------------')        
                print (CautionSentence)    
        #Sermomotor's sizing calculator
        elif mode == 42:
                modeselected = ('Servos')
                print(' ')
                print('SIZING OF SERVO MOTORS FOR HORIZONTAL MOTION')
                print(':::DATA INPUT:::')
                m = float(input('Mass to be maneuvered (kg): '))
                v = float(input('Speed to achieve (m/min): '))
                t = float(input('Time available for acceleration (s): '))
                dp = float(input('Diameter of the final drive pulley, gear, sprocket, etc...(mm): '))
                i = float(input('Total available gear reduction: '))
                R = float(input('Desired load/servo inertia ratio: '))
                rpm = float(input('Nominal servo RPM: '))
                e = float(input('Overall efficiency of the chosen transmission train: '))
                S = float(input('Safety factor (applied to the load): '))
                a = (v/60)/t
                F =(m*S)*a
                Mt = F * ((dp/2)/1000) * (1/e) 
                Irm = (m*S)*(((dp/2)/1000)**2)
                Mts = Mt / i
                Ps = Mts * ((rpm/60)*(2*math.pi))
                Is = (Irm/((i**2)*R)) * (1/e)
                Is104 = Is * (10**4)
                print(' ')
                print('          :::RESULTS:::')
                print('          -------------')
                print("         ",modeselected)
                print(' ')
                print('Mass to be maneuvered: ', m, ' kg')
                print('Speed to achieve: ', v, ' m/min')
                print('Time available for acceleration: ', t, ' s')
                print('Diameter of the final drive pulley, gear, sprocket, etc...', dp, ' mm')
                print('Total available gear reduction: ',i)
                print('Desired load/servo inertia ratio: ',R)
                print('Nominal servo rpm: ', rpm)
                print('Overall efficiency of the chosen transmission train: ', e)
                print('Safety factor (applied to the load): ',S)
                print('Movement acceleration: ', a, ' m/s^2')
                print('Acceleration force: ', F, ' N')
                print('Torque at the final drive: ', Mt, ' Nm')
                print('Load rotational inertia: ',Irm, ' kgm^2')
                print('Target servo nominal torque: ',Mts, ' Nm')
                print('Target nominal servo power: ', Ps,' W')
                print('Target servo inertia: ', Is,' kgm^2')
                print('Target servo inertia: ', Is104,'*10^-4 kgm^2')
                print (CautionSentence)                    
        #Sizing of axles
        elif mode == 43:
            modeselected = ('Axles to shear under radial load')
            print(' ')
            print('SIZING OF SOLID AXLES TO SHEAR UNDER RADIAL LOAD')
            print(':::DATA INPUT:::')
            P = float(input('Radial load (N): '))
            nS = float(input('Quantity of shear sections: '))
            sigma_adm = float(input('Allowable yield strength of the material (MPa): '))
            tau_adm = (sigma_adm*(10**6)) / (math.sqrt(3))
            d_min = 2* ((math.sqrt(P/(nS*tau_adm)))*(math.sqrt(math.pi)))
            print(' ')
            print('          :::RESULTS:::')
            print('          -------------')
            print("         ",modeselected)
            print(' ')
            print('Radial load: ', P, ' N')  
            print('Quantity of shear sections: ', nS)
            print('Allowable yield strength of the material: ', sigma_adm, ' MPa')
            print('Allowable shear strength of the material: ', tau_adm*10**-6, ' MPa')
            print('Minimum diameter required: ', d_min*1000, ' mm')
            print('          -------------')        
            print (CautionSentence)
        #Sizing of driveshafts
        elif mode == 44:
            modeselected = ('Driveshafts to shear under torsional load')
            print(' ')
            print('SIZING OF SOLID DRIVESHAFTS TO SHEAR UNDER TORSIONAL LOAD')
            print(':::DATA INPUT:::')
            P = float(input('Power to transmit (kW): '))
            rpm = float(input('RPM: '))
            Mt = (P*1000) / ((rpm/60)*(2*math.pi))
            sigma_adm = float(input('Allowable yield strength of the material (MPa): '))
            tau_adm = (sigma_adm*(10**6)) / (math.sqrt(3))
            d_min = (2 * math.pow((2*Mt),(1/3))) / (math.pow((math.pi * tau_adm),(1/3)))
            print(' ')
            print('          :::RESULTS:::')
            print('          -------------')
            print("         ",modeselected)
            print(' ')
            print('Power to transmit: ',P, ' kW')
            print('RPM: ',rpm, ' kW')
            print('Torque: ', Mt, ' Nm')
            print('Allowable yield strength of the material: ', sigma_adm, ' MPa')
            print('Allowable shear strength of the material: ', tau_adm*10**-6, ' MPa')
            print('Minimum required diameter: ',d_min*1000,' mm')
            print('          -------------')        
            print (CautionSentence)
        #Sizing of geared motors for traction systems
        elif mode == 45:
                modeselected = ('Geared motors for traction systems')
                print(' ')
                print('SIZING OF GEARED MOTORS FOR TRACTION APPLICATIONS')
                print(':::DATA INPUT:::')
                F = float(input('Traction effort required (N): '))
                D = float(input('Diameter of the traction wheel, sprocket, etc... (mm): '))
                v = float(input('Required movement speed (m/min): '))
                nomRpm = float(input('Nominal motor rpm: '))
                Hz = float(input('Frequency inverter service value (Hz): '))
                Ro = float(input('Total transmission efficiency: '))
                Perim =  math.pi * (D*10**-3)
                rpm = v/Perim
                i = (nomRpm*(Hz/50))/rpm
                Mt = F * ((D*10**-3)/2)
                P = (Mt * ((rpm/60)*2*math.pi))*10**-3 * 1/Ro
                print(' ')
                print('          :::RESULTS:::')
                print('          -------------')
                print("         ",modeselected)
                print(' ')
                print('Traction effort required: ',F, ' N')
                print('Diameter of the traction wheel: ',D, ' mm')
                print('Required movement speed: ',v, 'm/min')
                print('Nominal motor rpm: ',nomRpm, 'rpm')
                print('Frequency inverter service value: ',Hz,'Hz')
                print('Traction wheel rpm: ',rpm,'rpm')
                print('Transmission system efficiency: ',Ro)
                print('Required geared motor reduction: ',i)
                print('Required geared motor torque: ',Mt, 'Nm')
                print('Required geared motor power: ',P,'kW')
                print('          -------------')        
                print (CautionSentence)           
        #Cylinder's force calculator
        elif mode == 50:
                modeselected = ('Cylinders')
                print (' ')
                print ('ACTUATOR CYLINDERS CALCULATOR')
                print (':::DATA INPUT:::')
                D = float(input('Piston diameter (mm)?: '))
                d = float(input('Rod diameter (mm)?: '))
                P = float(input('Available fluid pressure (bar)?: '))
                print(' ')
                print('          :::RESULTS:::')
                print('          -------------')
                print("         ",modeselected)
                print(' ')
                Ffwresult=(P*100000)*math.pi*((D/1000)/2)**2
                Fretresult=(P*100000)*((math.pi*((D/1000)/2)**2)-(math.pi*((d/1000)/2)**2))
                print('Forward force: ',Ffwresult, ' N')
                print('Return force: ',Fretresult, ' N')
                print('Piston diameter: ',D, ' mm')
                print('Rod diameter: ', d, ' mm')
                print('Available fluid pressure: ', P, ' bar')
                print('          -------------')        
                print (CautionSentence)    
        #Hydraulic pump power calculator
        elif mode == 60:
                modeselected = ('Hydraulic power')
                print(' ')
                print('HYDRAULIC POWER CALCULATOR')
                print(':::DATA INPUT:::')
                F = float(input('Load (N)?: '))
                n = float(input('Ammount of actuators?: '))
                P = float(input('Hydraulic pressure (bar)?: '))
                t = float(input('Stroke time (s)?: '))
                L = float(input('Stroke lenght (mm)?: '))
                rpm = float(input('Pump rpm?: '))
                e = float(input('Pump group efficiency?: '))
                print(' ')
                print('          :::RESULTS:::')
                print('          -------------')
                print("         ",modeselected)
                print(' ')
                D = 2* math.sqrt((F/n)/((P*100000)*math.pi))
                V = math.pi * ((D/2)**2) * (L/1000)
                q = (V) / (t)
                Vt = V + 3*q
                Vstroke = V/((rpm/60)*t)
                Pp = ((rpm/60) * Vstroke * (P*100000))/e
                print('Actuator diameter: ',D*1000, ' mm')
                print('Actuator volume: ',V*1000, ' l')
                print('Fluid flow: ',q*1000*60,' l/min' )
                print('Fluid reservoir volume: ',V*1000+3*(q*1000*60),' l')
                print('Pump capacity: ',Vstroke*1000000,' cm^3')
                print('Pump group power: ',Pp/1000,' kW')
                print('          -------------')        
                print (CautionSentence)   
        #Bolted connections calculator
        elif mode == 70:
                modeselected = ('Bolted connections')
                print(' ')
                print('BOLTED CONNECTIONS CALCULATOR')
                print(':::DATA INPUT:::')
                Fs = float(input('Shear load (N)?: '))
                Ft = float(input('Traction load (N)?: '))
                Bc = input('Bolt class (8.8, 10.9, 12.9)?: ')
                if Bc == '8.8':
                    Sadm = 0.9*(640*(10**6))
                elif Bc == '10.9':
                    Sadm = 0.9*(940*(10**6))
                elif Bc == '12.9':
                    Sadm = 0.9*(1100*(10**6))
                ub = float(input('Thread friction coeficient "k"?: '))
                Dp = float(input('Desired bolt resistant diameter (mm)?: '))
                u = float(input('Friction between contact faces?: '))
                print(' ')
                print('          :::RESULTS:::')
                print('          -------------')
                print("         ",modeselected)
                print(' ')
                Fns = Fs/u
                Fnt = Ft
                Fn = Fns+Fnt
                MinTotalSection = Fns / Sadm
                BoltSection = math.pi * ((Dp/2)/1000)**2
                nBolts = round(MinTotalSection / BoltSection)
                Mt = (ub * Fns *(Dp/1000)) / nBolts
                print('Required number of bolts: ',nBolts,' bolts')
                print('Required tightening torque @ 90% yield: ',Mt,' Nm')
                print('          -------------')        
                print (CautionSentence)
        #Static disc brakes calculator
        elif mode == 80:
                modeselected = ('Static disc brakes')
                print(' ')
                print('STATIC DISC BRAKES')
                print(':::DATA INPUT:::')
                Mt = float(input('Torque to counteract (Nm)?: '))
                P = float(input('Available service pressure (bar)?: '))
                u = float(input('Available friction coefficient?: '))
                d = float(input('Diameter of the braking track (mm)?: '))
                n = float(input('Ammount of actuators?: '))
                Fbrake = Mt / ((d/2)/1000)
                Fact = (Fbrake / u) / n
                dminmm = (2 * math.sqrt (Fact/(100000*P*math.pi)))*1000
                print(' ')
                print('          :::RESULTS:::')
                print('          -------------')
                print("         ",modeselected)
                print(' ')
                print('Braking torque: ',Mt,' Nm')
                print('Actuator service pressure: ',P,' bar')
                print('Ammount of actuators ',n)
                print('Friction coefficient: ',u)
                print('Diameter of the braking track: ',d,' mm')
                print('Braking force: ',Fbrake,' N')
                print('Actuation force (per actuator): ',Fact,' N')
                print('Minimum actuator effective diameter (per actuator): ',dminmm,' mm')
                print('          -------------')        
                print (CautionSentence)
        #Helical springs calculator
        elif mode == 90:
                modeselected = ('Helical springs')
                print(' ')
                print('HELICAL SPRINGS')
                print(':::DATA INPUT:::')
                d = float(input('Wire diameter (mm)?: '))
                D = float(input("Outer diameter (mm)?: "))
                n = float(input("Number of active coils?: "))
                L = float(input("Active length (mm)?:"))
                G = float(input("Shear modulus (GPa) (Spring steel typical: 80 GPa)?: "))
                sigmaAdm = float(input("Yield strength (MPa) (Spring steel typical: 450 MPa )?: "))

                tauAdm = (sigmaAdm*10**6)/(math.sqrt (3))
                pitchDiam = D - d
                C = pitchDiam / d
                kB = (4*C+2)/(4*C-3)
                pitch = (L/1000)/n
                k = (((d/1000)**4)*(G*10**9)) / (8 * ((pitchDiam/1000)**3) * n)
                Fmax =(((math.pi) *(d/1000)**3) * (tauAdm)) / (8 * kB * (pitchDiam/1000))
                Stroke = Fmax / k

                print(' ')
                print('          :::RESULTS:::')
                print('          -------------')
                print("         ",modeselected)
                print(' ')
                print('Pitch (mm): ', pitch*1000, ' mm')
                print('Spring constant: ',k/1000,' N/mm')
                print("Maximum safe force: ",Fmax, ' N')
                print("Maximum safe deflection: ", Stroke*1000, ' mm')              
                print('          -------------')        
                print (CautionSentence)
        #Spur gears calculator
        elif mode == 100:
                modeselected = ('Spur gears')
                print(' ')
                print('Spur gears')
                print(':::DATA INPUT:::')
                P = float(input("Power to transmit (kW)?: "))
                rpm = float(input("Angular speed (rpm)?: "))
                sigma = float(input("Yield strength of the material (MPa)?: "))
                h = float(input("Tooth height (mm)?: "))
                e = float(input("Tooth foot thickness (mm)?: "))
                ap = float(input("Gear pressure angle (º)?: "))
                dp = float(input("Gear pitch diameter (mm)?: "))

                Mt = (P*1000)/((rpm/60)*2*math.pi)
                Ft = (Mt/((dp/1000)/2))* math.cos((ap*math.pi)/180)
                L = ((6 * Ft * (h/1000)) / (((e/1000)**2)*(sigma*10**6)))*1000

                print(' ')
                print('          :::RESULTS:::')
                print('          -------------')
                print("         ",modeselected)
                print(' ')
                print("Power to transmit (kW): ", P, " kW")
                print("Angular speed: ",rpm," rpm")
                print("Material yield strength: ",sigma, " MPa")
                print("Tooth height: ", h, " mm")
                print("Tooth foot thickness: ", e, " mm")
                print("Gear pressure angle: ", ap, " º")
                print("Gear pitch diameter: ", dp, " mm")
                print("Applied torque: ", Mt, " Nm")
                print("Tangential force: ", Ft, " N")
                print("Required tooth base length: ", L, " mm")
                print('          -------------')        
                print (CautionSentence)
        #Pressure vessels calculator
        elif mode == 110:
                modeselected = ('Pressure vessels')
                print(' ')
                print('Pressure vessels')
                print(':::DATA INPUT:::')
                Pnom = float(input("Service pressure (bar)?: "))
                sP = float(input("Safety factor?: "))
                h = float(input("Vessel lenght (m)?: "))
                sigma = float(input("Allowable yield strenght of the material (MPa)?: "))
                V = float(input("Required vessel volume (l)?: "))

                Di = 2 * (math.sqrt ((V/1000) / ((h) * math.pi))) 
                Fsep = (Pnom * 10**5) * sP * (h) * (math.pi * Di)
                s = Fsep / (h*(sigma*(10**6)))

                print(' ')
                print('          :::RESULTS:::')
                print('          -------------')
                print("         ",modeselected)
                print(' ')
                print("Service pressure: ", Pnom, " bar")
                print("Safety factor: ",sP)
                print("Vessel length: ",h, " m")
                print("Allowable yield strenght of the material: ", sigma, " MPa")
                print("Vessel volume: ", V, " l")
                print("Required internal diameter: ", Di*1000, " mm")
                print("Seam separation force: ", Fsep/1000, " kN")
                print("Minimum required wall thickness: ", s*1000, " mm")
                print('          -------------')        
                print (CautionSentence)
        #Linear motion dynamics calculator
        elif mode == 120:
                modeselected = ('Linear motion dynamics')
                print(' ')
                print('Linear motion dynamics')
                print(':::DATA INPUT:::')
                x = float(input("Movement stroke (mm)?: "))
                t = float(input("Required time (s): "))
                a = float(input("Acceleration ramp (% of total time)?: "))
                d = float(input("Deceleration ramp (% of total time)?: "))
                ta = t * (a/100)     #acceleration time
                xa = x * (a/100)     #acceleration stroke
                td = t * (d/100)     #deceleration time
                xd = x * (d/100)     #deceleration stroke
                tc = t - (ta + td)   #constant speed time
                xc = x- (xa + xd)    #constant speed stroke
                vavg = (x/1000)/t    #average speed
                                     #x=x0+v0*t+1/2*a*t^2 and v=v0+a*t
                vp = (2*(xa/1000))/ta #peak speed
                acc = 2*((xa/1000)/(ta**2)) #acceleration
                dec = (((x/1000)-(xa/1000)-(xc/1000)-vp*td)/(td**2))*2 #deceleration             
                print(' ')
                print('          :::RESULTS:::')
                print('          -------------')
                print("         ",modeselected)
                print(' ')
                print("Stroke: ", x, "mm")
                print("Total time: ", t, "s")
                print("Time under acceleration: ", ta, "s")
                print("Time at constant speed: ", tc, "s")
                print("Time under deceleration: ", td, "s")                              
                print("Stroke under acceleration: ", xa, "mm")
                print("Stroke at constant speed: ", xc, "mm")
                print("Stroke under deceleration: ", xd, "mm")                
                print("Acceleration: ", acc, "m/s^2")
                print("Peak speed: ", vp, "m/s")
                print("Average speed: ", vavg, "m/s")
                print("Deceleration: ",dec, "m/s^2")
                print('          -------------')        
                print (CautionSentence)
                
                
                
                
                
                #Rectangular flat plates calculator
        elif mode == 130:
                modeselected = ('Rectangular flat plates (J.Carvill, empyrical)')
                print(' ')
                print(modeselected)
                print(':::DATA INPUT:::')
                
                s  = float(input("Thickness (mm)?: "))
                d  = float(input("Material density (kg/m^3)?: "))
                dl = float(input("Distributed load (N)?: "))
                ta = float(input("Short edge (m)?: "))
                tb = float(input("Long edge (m)?: "))
                EGPa  = float(input("Elastic modulus (GPa)?: "))
               
                
                t = s/1000             #Thickness m
                E = EGPa * (10**9)     #Elastic modulus Pa
                a = ta * tb            #Surface area m^2
                w = a * t * d          #Self weight kg
                pw = (w / a) * 9.8     #Self weight induced pressure Pa
                pl = dl / a            #Load induced pressure Pa
                p = pw + pl            #Total pressure Pa
                
                sigmaC = (p * (a**2)) / ((2*(t**2)) * (0.623 * ((ta/tb)**6)+1)) #Calculated stress @ middle of long edge clamped plate
                yC = (0.0284 * p * (a**4)) / ((E * (t**3)) * (1.056*((ta/tb)**5)+1))#Calculated deflection @ center clamped plate
                
                sigmaS = ((0.75 * p * (a**2)) / ((t**2) * (1.61 * ((ta/tb)**3) + 1)))#Calculated stress @ center simply supported plate
                yS = ((0.142 * p * (a**4)) / ((E * (t**3)) * (2.21 * ((ta/tb)**3) + 1)))#Calculated deflection @ center simply supported plate
                
                print(' ')
                print('          :::RESULTS:::')
                print('          -------------')
                print("         ",modeselected)
                print(' ')
                print("Load: ", dl, "N")
                print("Density: ", d, "kg/m^3")
                print("Thickness: ", t, "mm")
                print("Short edge length: ", ta, "m")
                print("Long edge length: ", tb, "m")
                print("Elastic modulus: ", E, "Pa")
                print("Surface area: ", a, "m^2")
                print("Self weight: ", w, "kg")
                print("Self weight induced pressure: ", pw, "Pa")
                print("Load weight induced pressure: ", pl, "Pa")
                print("Total pressure: ", p, "Pa")
                print("Stress: ", sigmaC*(10**-6), "MPa at CLAMPED PLATE long edge mid span")
                print("Stress: ", sigmaS*(10**-6), "MPa at SIMPLY SUPPORTED PLATE  surface center point")
                print("Deflection: ", yC*(10**3), "mm at CLAMPED PLATE surface center point")
                print("Deflection: ", yS*(10**3), "mm at SIMPLY SUPPORTED PLATE surface center point")
  
                
                
                print('          -------------')        
                print (CautionSentence)
                
                
                
                
        #SAVE RESULTS
        print (' ')
        save=input('Save (y/n)?: ')
        if save=='y':
                if mode == 10:
                        filename=input('Filename?: ')
                        f = open(filename + ".txt",'w')
                        f.write(TitleName + '\n' + Version + '\n' + Author + '\n' + AuthorContact + '\n' + '\n' + 'Filename: ' + filename + '\n' + '\n' + SaveFileTitle + '\n' + '\n' + modeselected  + '\n' + '\n')
                        f.write('Torque-------------: ' + (str(Torque)) + ' Nm' + '\n')
                        f.write('Power--------------: ' + (str(Power)) + ' kW' + '\n')
                        f.write('rpm----------------:' + (str(rpm)) + '\n'+ '\n'+ '\n')
                        f.write(CautionSentence)
                        f.close()
                elif mode == 30:
                        filename=input('Filename?: ')
                        f = open(filename + ".txt",'w')
                        f.write(TitleName + '\n' + Version + '\n' + Author + '\n' + AuthorContact + '\n' + '\n' + 'Filename: ' + filename + '\n' + '\n' + SaveFileTitle + '\n' + '\n' + modeselected  + '\n' + '\n')       
                        f.write('Beam type------------------------------: ' + (str(beamtypeselected)) + '\n' )
                        f.write('Deflection-----------------------------: ' + (str(y)) + ' m'+'\n' )
                        if modeselected == 100 or modeselected == 101:   
                                f.write('Load-----------------------------: ' + (str(P)) + ' N'+'\n' )
                        elif modeselected == 102:
                                f.write('Load-----------------------------: ' + (str(q)) + ' N/m'+'\n' )
                        f.write('Length---------------------------------: ' + (str(L)) + ' m'+'\n' )
                        f.write('Elastic modulus------------------------: ' + (str(E)) + ' Pa'+'\n' )
                        f.write('Moment of inertia----------------------: ' + (str(I)) + ' m^4' + '\n'+ '\n'+ '\n')
                        f.write(CautionSentence)
                        f.close()
                elif mode == 31:
                        filename=input('Filename?: ')
                        f = open(filename + ".txt",'w')
                        f.write(TitleName + '\n' + Version + '\n' + Author + '\n' + AuthorContact + '\n' + '\n' + 'Filename: ' + filename + '\n' + '\n' + SaveFileTitle + '\n' + '\n' + modeselected  + '\n' + '\n')
                        f.write('Distributed load------------------------------: ' + (str(q)) + ' kg/m' + '\n' )
                        f.write('Lenght----------------------------------------: ' + (str(L)) + ' m' + '\n' )
                        f.write('Elastic modulus-------------------------------: ' + (str(E)) + ' Pa' + '\n')
                        f.write('Moment of inertia-----------------------------: ' + (str(I)) + ' m^4' + '\n')
                        f.write('First mode resonance frequency----------------: ' + (str(w1)) + ' Hz' + '\n')
                        f.write('Second mode resonance frequency---------------: ' + (str(w2)) + ' Hz' + '\n')
                        f.write('Third mode resonance frequency----------------: ' + (str(w3)) + ' Hz' + '\n'+ '\n'+ '\n')
                        f.write(CautionSentence)
                        f.close()
                elif mode == 40:
                        filename=input('Filename?: ')
                        f = open(filename + ".txt",'w')
                        f.write(TitleName + '\n' + Version + '\n' + Author + '\n' + AuthorContact + '\n' + '\n' + 'Filename: ' + filename + '\n' + '\n' + SaveFileTitle + '\n' + '\n' + modeselected  + '\n' + '\n')                       
                        f.write('Unsupported lenght------------------------------: ' + (str(l)) + ' m' + '\n' )
                        f.write('Elastic modulus---------------------------------: ' + (str(E)) + ' Pa' + '\n' )
                        f.write('Moment of inertia-------------------------------: ' + (str(I)) + ' m^4' + '\n' )
                        f.write('Mass per unit lenght----------------------------: ' + (str(m)) + ' kg/m' + '\n' )
                        f.write('Concentrated mass-------------------------------: ' + (str(mi)) + ' m' + '\n' )
                        f.write('Deflection under concentrated mass--------------: ' + (str(yi)) + ' kg' + '\n' )
                        f.write('Unsupported lenght------------------------------: ' + (str(l)) + ' m' + '\n' )
                        f.write('First mode resonance frequency (Hz) (Thomson)---: ' + (str(w1Thomson)) + ' Hz' + '\n' )
                        f.write('First mode resonance frequency (Hz) (Thomson)---: ' + (str(w1Rayleigh)) + ' Hz' + '\n'+ '\n'+ '\n')
                        f.write(CautionSentence)
                        f.close()      
                elif mode == 41:
                        filename=input('Filename?: ')
                        f = open(filename + ".txt",'w')
                        f.write(TitleName + '\n' + Version + '\n' + Author + '\n' + AuthorContact + '\n' + '\n' + 'Filename: ' + filename + '\n' + '\n' + SaveFileTitle + '\n' + '\n' + modeselected  + '\n' + '\n')
                        f.write('Applied load-----------------------------------------: ' + (str(F)) + ' N' + '\n' )
                        f.write('Required movement speed------------------------------: ' + (str(v)) + ' m/min' + '\n' )
                        f.write('Actuator efficiency----------------------------------: ' + (str(e)) + '\n')
                        f.write('Screw thread pitch diameter--------------------------: ' + (str(dm)) + ' mm' + '\n' )
                        f.write('Screw thread pitch-----------------------------------: ' + (str(z)) + ' mm' + '\n' )
                        f.write('Coefficient of friction between screw and nut--------: ' + (str(u)) + '\n' )
                        f.write('Actuator rpm:----------------------------------------: ' + (str(rpm)) + '\n' )
                        f.write('Screw rpm--------------------------------------------: ' + (str(Srpm)) + '\n' )
                        f.write('Required reduction-----------------------------------:1/' + (str(i)) + '\n' )
                        f.write('Torque required to displace the load-----------------: ' + (str(Mt)) + ' Nm' + '\n' )
                        f.write('Power required to displace the load------------------: ' + (str(P/1000)) + ' kW' + '\n'+ '\n'+ '\n')
                        f.write(CautionSentence)
                        f.close()
                elif mode == 42:
                        filename=input('Filename?: ')
                        f = open(filename + ".txt",'w')
                        f.write(TitleName + '\n' + Version + '\n' + Author + '\n' + AuthorContact + '\n' + '\n' + 'Filename: ' + filename + '\n' + '\n' + SaveFileTitle + '\n' + '\n' + modeselected  + '\n' + '\n')
                        f.write('Mass to be maneuvered----------------------------------------: '+ (str(m)) + ' kg'+ '\n' )
                        f.write('Speed to achieve---------------------------------------------: '+ (str(v)) + ' m/min'+ '\n')
                        f.write('Time available for acceleration------------------------------: '+ (str(t)) + ' s'+ '\n')
                        f.write('Diameter of the final drive pulley, gear, sprocket, etc...---: '+ (str(dp)) + ' mm'+ '\n')
                        f.write('Total available gear reduction-------------------------------: '+ (str(i)) + '\n')
                        f.write('Desired load/servo inertia ratio-----------------------------: '+ (str(R)) +'\n')
                        f.write('Nominal servo rpm--------------------------------------------: '+ (str(rpm)) +'\n')
                        f.write('Overall efficiency of the chosen transmission train----------: '+ (str(e)) +'\n')
                        f.write('Safety factor (applied to the load)--------------------------: '+ (str(S)) +'\n')
                        f.write('Movement acceleration----------------------------------------: '+ (str(a)) +' m/s^2'+ '\n')
                        f.write('Acceleration force-------------------------------------------: '+ (str(F)) +' N'+ '\n')
                        f.write('Torque at the final drive------------------------------------: '+ (str(Mt)) +' Nm'+ '\n')
                        f.write('Load rotational inertia--------------------------------------: '+ (str(Irm)) +' kgm^2'+ '\n')
                        f.write('Target servo nominal torque----------------------------------: '+ (str(Mts)) +' Nm'+ '\n')
                        f.write('Target nominal servo power-----------------------------------: '+ (str(Ps)) +' W'+ '\n')
                        f.write('Target servo inertia-----------------------------------------: '+ (str(Is)) +' kgm^2'+ '\n')
                        f.write('Target servo inertia-----------------------------------------: '+ (str(Is104)) +'*10^-4 kgm^2'+ '\n'+ '\n'+ '\n')
                        f.write(CautionSentence)
                        f.close()    
                elif mode == 43:
                        filename=input('Filename?: ')
                        f = open(filename + ".txt",'w')
                        f.write(TitleName + '\n' + Version + '\n' + Author + '\n' + AuthorContact + '\n' + '\n' + 'Filename: ' + filename + '\n' + '\n' + SaveFileTitle + '\n' + '\n' + modeselected  + '\n' + '\n')
                        f.write('Radial load----------------------------------: '+ (str(P)) + ' N'+ '\n' )
                        f.write('Quantity of shear sections-------------------: '+ (str(nS)) + '\n' )
                        f.write('Allowable yield strength of the material-----: '+ (str(sigma_adm)) + ' MPa'+ '\n' )
                        f.write('Allowable shear strength of the material-----: '+ (str(tau_adm*10**-6)) + ' MPa'+ '\n' )
                        f.write('Minimum required diameter--------------------: '+ (str(d_min*1000)) + ' mm'+ '\n'+ '\n'+ '\n' )
                        f.write(CautionSentence)
                        f.close()             
                elif mode == 44:
                        filename=input('Filename?: ')
                        f = open(filename + ".txt",'w')
                        f.write(TitleName + '\n' + Version + '\n' + Author + '\n' + AuthorContact + '\n' + '\n' + 'Filename: ' + filename + '\n' + '\n' + SaveFileTitle + '\n' + '\n' + modeselected  + '\n' + '\n')
                        f.write('Power to transmit----------------------------------: '+ (str(P)) + ' kW'+ '\n' )
                        f.write('RPM-------------------: '+ (str(rpm)) + '\n' )
                        f.write('Applied torque-----: '+ (str(Mt)) + ' Nm'+ '\n' )
                        f.write('Allowable yield strength of the material-----: '+ (str(sigma_adm)) + ' MPa'+ '\n' )
                        f.write('Allowable shear strength of the material-----: '+ (str(tau_adm*10**-6)) + ' MPa'+ '\n' )
                        f.write('Minimum required diameter--------------------: '+ (str(d_min*1000)) + ' mm'+ '\n'+ '\n'+ '\n' )
                        f.write(CautionSentence)
                        f.close()
                elif mode == 45:
                        filename=input('Filename?: ')
                        f = open(filename + ".txt",'w')
                        f.write(TitleName + '\n' + Version + '\n' + Author + '\n' + AuthorContact + '\n' + '\n' + 'Filename: ' + filename + '\n' + '\n' + SaveFileTitle + '\n' + '\n' + modeselected  + '\n' + '\n')
                        f.write('Traction effort required------------: '+ (str(F)) + ' N'+ '\n' )
                        f.write('Diameter of the traction wheel------: '+ (str(D)) + '\mm'+ '\n' )
                        f.write('Required movement speed-------------: '+ (str(v)) + ' m/min'+ '\n' )
                        f.write('Nominal motor rpm-------------------: '+ (str(nomRpm)) + ' rpm'+ '\n' )
                        f.write('Traction wheel rpm------------------: '+ (str(rpm)) + ' rpm'+ '\n' )
                        f.write('Required geared motor reduction-----: '+ (str(i)) + '\n' )
                        f.write('Transmission system efficiency------: '+ (str(Ro)) + '\n' )
                        f.write('Required geared motor torque--------: '+ (str(Mt)) + ' Nm'+ '\n' )
                        f.write('Required geared motor power---------: '+ (str(P)) + ' kW'+ '\n'+ '\n'+ '\n' )           
                        f.write(CautionSentence)
                        f.close()              
                elif mode == 50:
                        filename=input('Filename?: ')
                        f = open(filename + ".txt",'w')
                        f.write(TitleName + '\n' + Version + '\n' + Author + '\n' + AuthorContact + '\n' + '\n' + 'Filename: ' + filename + '\n' + '\n' + SaveFileTitle + '\n' + '\n' + modeselected  + '\n' + '\n')
                        f.write('Piston diameter----------------: '+ (str(D)) + ' mm'+ '\n' )
                        f.write('Rod diameter-------------------: '+ (str(d)) + ' mm' + '\n' )
                        f.write('Available fluid pressure-------: '+ (str(P)) + ' bar'+ '\n' )
                        f.write('Forward force------------------: '+ (str(Ffwresult)) + ' N'+ '\n' )
                        f.write('Return force-------------------: '+ (str(Fretresult)) + ' N'+  '\n'+ '\n'+ '\n' )
                        f.write(CautionSentence)
                        f.close()
                elif mode == 60:
                        filename=input('Filename?: ')
                        f = open(filename + ".txt",'w')
                        f.write(TitleName + '\n' + Version + '\n' + Author + '\n' + AuthorContact + '\n' + '\n' + 'Filename: ' + filename + '\n' + '\n' + SaveFileTitle + '\n' + '\n' + modeselected  + '\n' + '\n')
                        f.write('Load-----------------------: ' + (str(F)) + ' N' + '\n' )
                        f.write('Ammount of actuators-------: ' + (str(n)) + '\n' )
                        f.write('Hydraulic pressure---------: ' + (str(P)) + ' bar' + '\n' )
                        f.write('Stroke time----------------: ' + (str(t)) + ' s' + '\n' )
                        f.write('Stroke lenght--------------: ' + (str(L)) + ' mm' + '\n' )
                        f.write('Pump group rpm-------------: ' + (str(rpm)) + '\n' )
                        f.write('Pump group efficiency------: ' + (str(e)) + '\n' )
                        f.write('Actuator diameter----------: ' + (str(D*1000)) + ' mm' + '\n' )
                        f.write('Actuator volume------------: ' + (str(V*1000)) + ' l' + '\n' )
                        f.write('Fluid flow-----------------: ' + (str(q*1000*60)) + ' l/min' + '\n' )
                        f.write('Fluid reservoir volume-----: ' + (str(V+3*(q*1000*60))) + ' l' + '\n' )
                        f.write('Pump capacity--------------: ' + (str(Vstroke*1000000)) + ' cm^3' + '\n' )
                        f.write('Pump group power-----------: ' + (str(Pp/1000)) + ' kW' + '\n'+ '\n'+ '\n')
                        f.write(CautionSentence)
                        f.close()
                elif mode == 70:
                        filename=input('Filename?: ')
                        f = open(filename + ".txt",'w')
                        f.write(TitleName + '\n' + Version + '\n' + Author + '\n' + AuthorContact + '\n' + '\n' + 'Filename: ' + filename + '\n' + '\n' + SaveFileTitle + '\n' + '\n' + modeselected  + '\n' + '\n')
                        f.write('Shear load--------------------------------: ' + (str(Fs)) + ' N' + '\n')
                        f.write('Traction load-----------------------------: ' + (str(Ft)) + ' N' + '\n')
                        f.write('Friction between surfaces ----------------: ' + (str(u)) + '\n')
                        f.write('Thread friction coefficient "k"-----------: ' + (str(ub)) + '\n')
                        f.write('Bolt class--------------------------------: ' + (str(Bc)) + '\n')
                        f.write('Bolt resistant diameter-------------------: ' + (str(Dp)) + ' mm' + '\n')
                        f.write('Required number of bolts------------------: ' + (str(nBolts)) + '\n')
                        f.write('Required tightening torque @ 90% yield:---: ' + (str(Mt)) + ' Nm' + '\n'+ '\n'+ '\n')
                        f.write(CautionSentence)
                        f.close()  
                elif mode == 80:
                        filename=input('Filename?: ')
                        f = open(filename + ".txt",'w')
                        f.write(TitleName + '\n' + Version + '\n' + Author + '\n' + AuthorContact + '\n' + '\n' + 'Filename: ' + filename + '\n' + '\n' + SaveFileTitle + '\n' + '\n' + modeselected  + '\n' + '\n')
                        f.write('Braking torque---------------------------------------: ' + (str(Mt)) + ' Nm' + '\n')
                        f.write('Actuator service pressure----------------------------: ' + (str(P)) + ' bar' + '\n')
                        f.write('Ammount of actuators --------------------------------: ' + (str(n)) + '\n')
                        f.write('Friction coefficient---------------------------------: ' + (str(u)) + '\n')
                        f.write('Diameter of the braking track------------------------: ' + (str(d)) +' mm' + '\n')
                        f.write('Braking force----------------------------------------: ' + (str(Fbrake)) + ' N' + '\n')
                        f.write('Actuation force (per actuator)-----------------------: ' + (str(Fact)) + ' N' + '\n')
                        f.write('Minimum actuator effective diameter (per actuator)---: ' + (str(dminmm)) + ' mm' + '\n'+ '\n'+ '\n')
                        f.write(CautionSentence)
                        f.close()
                elif mode == 90:
                        filename=input('Filename?: ')
                        f = open(filename + ".txt",'w')
                        f.write(TitleName + '\n' + Version + '\n' + Author + '\n' + AuthorContact + '\n' + '\n' + 'Filename: ' + filename + '\n' + '\n' + SaveFileTitle + '\n' + '\n' + modeselected  + '\n' + '\n')
                        f.write('Wire diameter-----------------------------: ' + (str(d)) + ' mm' + '\n')
                        f.write('Outer diameter----------------------------: ' + (str(D)) + ' mm' + '\n')
                        f.write('Active length ----------------------------: ' + (str(L))+ ' mm' + '\n')
                        f.write('Number of active coils--------------------: ' + (str(n)) + '\n')
                        f.write('Material shear modulus--------------------: ' + (str(G)) + ' GPa' + '\n')
                        f.write('Material yield strength-------------------: ' + (str(sigmaAdm)) + ' Mpa' + '\n')
                        f.write('Spring pitch------------------------------: ' + (str(pitch*1000)) + ' mm' + '\n')
                        f.write('Spring constant "k"-----------------------: ' + (str(k/1000)) + ' N/mm' + '\n')
                        f.write('Maximum safe force------------------------: ' + (str(Fmax)) + ' N' + '\n')
                        f.write('Maximum safe deflection-------------------: ' + (str(Stroke*1000)) + ' mm' + '\n'+ '\n'+ '\n')
                        f.write(CautionSentence)
                        f.close()
                elif mode == 100:
                        filename=input('Filename?: ')
                        f = open(filename + ".txt",'w')
                        f.write(TitleName + '\n' + Version + '\n' + Author + '\n' + AuthorContact + '\n' + '\n' + 'Filename: ' + filename + '\n' + '\n' + SaveFileTitle + '\n' + '\n' + modeselected  + '\n' + '\n')
                        f.write('Power to transmit-------------------------: ' + (str(P)) + ' kW' + '\n')
                        f.write('Angular speed-----------------------------: ' + (str(rpm)) + ' rpm' + '\n')
                        f.write('Material yield strenth--------------------: ' + (str(sigma))+ ' MPa' + '\n')
                        f.write('Tooth height------------------------------: ' + (str(h))+ " mm" + '\n')
                        f.write('Tooth foot thickness----------------------: ' + (str(e)) + ' mm' + '\n')
                        f.write('Gear pressure angle-----------------------: ' + (str(ap)) + ' º' + '\n')
                        f.write('Gear pitch diameter-----------------------: ' + (str(dp)) + ' mm' + '\n')
                        f.write('Applied torque----------------------------: ' + (str(Mt)) + ' Nm' + '\n')
                        f.write('Tangential force--------------------------: ' + (str(Ft)) + ' N' + '\n')
                        f.write('Required tooth base length----------------: ' + (str(L)) + ' mm' + '\n'+ '\n'+ '\n')
                        f.write(CautionSentence)
                        f.close()

                elif mode == 110:
                        filename=input('Filename?: ')
                        f = open(filename + ".txt",'w')
                        f.write(TitleName + '\n' + Version + '\n' + Author + '\n' + AuthorContact + '\n' + '\n' + 'Filename: ' + filename + '\n' + '\n' + SaveFileTitle + '\n' + '\n' + modeselected  + '\n' + '\n')
                        f.write('Service pressure-----------------: ' + (str(Pnom)) + ' bar' + '\n')
                        f.write('Safety factor--------------------: ' + (str(sP)) + '\n')
                        f.write('Vessel length--------------------: ' + (str(h))+ ' m' + '\n')
                        f.write('Material yield stregth-----------: ' + (str(sigma))+ " MPa" + '\n')
                        f.write('Vessel volume--------------------: ' + (str(V)) + ' l' + '\n')
                        f.write('Internal diameter----------------: ' + (str(Di*1000)) + ' mm' + '\n')
                        f.write('Seam separation force------------: ' + (str(Fsep/1000)) + ' kN' + '\n')
                        f.write('Minimum wall thickness-----------: ' + (str(s*1000)) + ' mm' + '\n'+ '\n'+ '\n')
                        f.write(CautionSentence)
                        f.close()
                        
                elif mode == 120:
                        filename=input('Filename?: ')
                        f = open(filename + ".txt",'w')
                        f.write(TitleName + '\n' + Version + '\n' + Author + '\n' + AuthorContact + '\n' + '\n' + 'Filename: ' + filename + '\n' + '\n' + SaveFileTitle + '\n' + '\n' + modeselected  + '\n' + '\n')
                        f.write('Movement stroke------------------: ' + (str(x)) + ' mm' + '\n')
                        f.write('Movement time--------------------: ' + (str(t)) + ' s ' + '\n')
                        f.write('Acceleration ramp----------------: ' + (str(a)) + ' % ' + '\n')
                        f.write('Deceleration ramp----------------: ' + (str(d)) + ' % ' + '\n')
                        f.write('Acceleration time----------------: ' + (str(ta)) + ' s ' + '\n')
                        f.write('Constant speed time--------------: ' + (str(tc)) + ' s ' + '\n')
                        f.write('Deceleration time----------------: ' + (str(td)) + ' s ' + '\n')
                        f.write('Acceleration stroke--------------: ' + (str(xa)) + ' mm ' + '\n')
                        f.write('Constant speed stroke------------: ' + (str(xc)) + ' mm ' + '\n')
                        f.write('Deceleration stroke--------------: ' + (str(xd)) + ' mm ' + '\n')
                        f.write('Acceleration---------------------: ' + (str(acc)) + ' m/s^2' + '\n')
                        f.write('Peak speed-----------------------: ' + (str(vp)) + ' m/s ' + '\n')
                        f.write('Deceleration---------------------: ' + (str(dec)) + ' m/s^2 ' + '\n')
                        f.write('Average speed--------------------: ' + (str(vavg)) + ' m/s ' + '\n'+ '\n'+ '\n')
                        f.write(CautionSentence)
                        f.close()
                        
                elif mode == 130:
                        filename=input('Filename?: ')
                        f = open(filename + ".txt",'w')
                        f.write(TitleName + '\n' + Version + '\n' + Author + '\n' + AuthorContact + '\n' + '\n' + 'Filename: ' + filename + '\n' + '\n' + SaveFileTitle + '\n' + '\n' + modeselected  + '\n' + '\n')
                        f.write('Load----------------------------------------: ' + (str(dl)) + ' N' + '\n')
                        f.write('Material density----------------------------: ' + (str(d)) + ' Kg/m^3' + '\n')
                        f.write('Material elastic modulus--------------------: ' + (str(EGPa)) + ' GPa' + '\n')
                        f.write('Plate thickness-----------------------------: ' + (str(t)) + ' mm' + '\n')
                        f.write('Long edge length----------------------------: ' + (str(tb)) + ' m' + '\n')
                        f.write('Short edge length---------------------------: ' + (str(ta)) + ' m' + '\n')
                        f.write('Surface area--------------------------------: ' + (str(a)) + ' m^2' + '\n')
                        f.write('Self weight---------------------------------: ' + (str(w)) + ' kg' + '\n')
                        f.write('Self weight pressure------------------------: ' + (str(pw)) + ' Pa' + '\n')
                        f.write('Load pressure-------------------------------: ' + (str(pl)) + ' Pa' + '\n')
                        f.write('Total pressure------------------------------: ' + (str(p)) + ' Pa' + '\n')
                        f.write('Stress--------------------------------------: ' + (str(sigmaC*(10**-6))) + ' MPa at CLAMPED PLATE long edge mid span' + '\n')
                        f.write('Stress--------------------------------------: ' + (str(sigmaS*(10**-6))) + ' MPa at SIMPLY SUPPORTED PLATE  surface center point' + '\n')
                        f.write('Deflection----------------------------------: ' + (str(yC*(10**3))) + ' mm at CLAMPED PLATE surface center point' + '\n')
                        f.write('Deflection----------------------------------: ' + (str(yS*(10**3))) + ' mm at SIMPLY SUPPORTED PLATE surface center point' + '\n'+ '\n'+ '\n')
                        f.write(CautionSentence)
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
