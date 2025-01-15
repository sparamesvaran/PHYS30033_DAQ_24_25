#!/usr/bin/python3

import serial
import sys

def temperature_readout(target):

        device_name='/dev/cu.usbmodem11201'
        serial_device = serial.Serial(device_name)  # open serial port

        # event counter
        n=1

        # csv file
        f_csv = open(f"temp_data_{target}_entries.csv", "w")

        while n<=target:
                line = serial_device.readline()
                text = line.decode()
                
                # extract data
                words = text.split()
                timestamp = words[3]
                temperature = words[5]

                data_string=f"{timestamp},{temperature}"

                # csv
                f_csv.write(data_string+"\n")
                print(data_string)

                n+=1

        f_csv.close()

if __name__ == '__main__':

        n_arg=len(sys.argv)

        if n_arg == 4:
                start = int(sys.argv[1])
                stop = int(sys.argv[2])
                step = int(sys.argv[3])
                actual_stop=(stop//step)*step
                print(f"I will take datasets with the number of events ranging from {start} to {actual_stop}, in steps of {step}")
                n_events_range=range(start,stop,step)
                for n in n_events_range:
                        print(f"I will read {n} events")
                        temperature_readout(n)
        elif n_arg == 2:
                n=int(sys.argv[1])
                print(f"I will read {n} events")
                temperature_readout(n)
        elif n_arg == 1:
                temperature_readout(float('inf'))
        else:
                print(f"Invalid number of arguments: {n_arg}")
