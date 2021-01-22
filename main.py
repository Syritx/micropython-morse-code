import machine
import time

LED_PIN_NB = 2
led = machine.Pin(LED_PIN_NB, machine.Pin.OUT)
led.on()

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
morse_code_equivalents = ['.-','-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '/']

def write_morse_code(data, multiplier):
    dat = list(data)
    morse_code = ''
	
    for c in dat:
	for i in range(len(letters)):
	    if c == letters[i]:
		morse_code += morse_code_equivalents[i]+' '
    
    print(morse_code)
    morse_code_dat = list(morse_code)

    wait_times = []
    for d in range(len(morse_code_dat)-1):
	if morse_code_dat[d] == '.':
	    wait_times.append(0.1*multiplier)
	
	elif morse_code_dat[d] == '-':
	    wait_times.append(0.2*multiplier)

	elif morse_code_dat[d] == ' ':
	    wait_times.append(0.3*multiplier)
	
	else:
	   wait_times.append(0.4*multiplier)

    for t in wait_times:
	if t < 0.3*multiplier:
	   time.sleep(.1*multiplier)
	   led.off()
	   time.sleep(t)
	   led.on()

	elif t == 0.3*multiplier:
	    time.sleep(0.3*multiplier)
	else:
	    time.sleep(0.4*multiplier)
