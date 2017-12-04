import Adafruit_ADS1x15
import time
import RPi.GPIO as GPIO

adc = Adafruit_ADS1x15.ADS1115() #creat the adc 16bits
GIAN = 1
#GPIO.setmode(GPIO,bcm)

temp_calibration =0
tem_range=10;
offset_vol =0.014
tempValue=0
current_temp= 0
temp 1,2,3 =0
reference_vol=0.5
clear_num =0
R =0

voltage =0

 res[100]={
                 318300,302903,288329,274533,261471,249100,237381,226276,215750,205768,
                 196300,187316,178788,170691,163002,155700,148766,142183,135936,130012,
                 124400,119038,113928,109059,104420,100000,95788,91775,87950,84305,
                 80830,77517,74357,71342,68466,65720,63098,60595,58202,55916,
                 53730,51645,49652,47746,45924,44180,42511,40912,39380,37910,
                 36500,35155,33866,32631,31446,30311,29222,28177,27175,26213,
                 25290,24403,23554,22738,21955,21202,20479,19783,19115,18472,
                 17260,16688,16138,15608,15098,14608,14135,13680,13242,12819,
                 12412,12020,11642,11278,10926,10587,10260,9945,9641,9347,
                 9063,8789,8525,8270,8023,7785,7555,7333,7118,6911}

def binSearch(x):
	low =0
	high =100
	while (low<=high):
		mid=(low +high)/2
		if(x<res[mid]):
			low = mid + 1
		else:
			high = mid-1
	return mid

def measureSurTemp():
	i=0
	current_temp1=0
	signal =0
	tempValue=0
	for x in xrange(1,10):
		tempValue+=value
		delay(10)
	tempValue =tempValue/10
	temp =tempValue*1.1/1023
	signal =binSearch(R)
	current_temp =signal -1+temp_calibration(res[signal-1]-R)/(res[signal-1]-res[signal])
	print(current_temp)
	return current_temp




adc.start_adc(0,gain=GIAN)
start= time.time()
while (time.time() -start)<=5.0:
	value= adc.get_last_result()
	print('Channel 0: {0}'.format(value))
	time.sleep(0.5)
	measureSurTemp()
#adc.stop_adc()

