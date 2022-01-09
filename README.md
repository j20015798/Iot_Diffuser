# Iot_Diffuser

## Overview
This is an **Smart Essential Oil Diffuser** which we can chose the flavors and the amount of essential oil and power up/off the diffuser directly on your LINE with your smartphone. Why I want to do this project is because most Essential Oil Diffusers on the market need to be added essential oils with your own hands, and turn it on or off in person. For lazy man like me, if I am lying on the sofa but wanna use my diffuser, these actions would seem to be a bit troblesome, so I want to create a easier and convenient way to use this kind of machine.

## Line Bot UI

![image](https://user-images.githubusercontent.com/72622577/148680489-f0196068-06e1-40d4-84b9-7d55a86cc11a.png)

## Components
**Hardware**
* Raspberry Pi 4 *1
* Power cable *1 (for raspberry pi)
* 12V Switching Power Supply (Mean Well LRS-100-12)*1
* Computer power cable *1 (for 12V Switching Power Supply) 
* Peristaltic pump (蠕動馬達/幫浦) *3
* 4 Channel DC 5V Relay Module (4路繼電器)*1
* Water Atomization Module (超音波水霧化模組) *1
* DHT22 (溫溼度感測器)*1
* Water Sensor *1 
* MCP3008 *1
* Breadboard *1
* Dupont Line *n
* Essential oil *3
* Plastic container (to build the diffuser)
* Small carton (to elevate the pumps)

**Software**
* Python 3.7
* Line Bot




## Circuit Diagram

## Preprocessing
I'll put on some commands I've used in particular need.
Because I'm using python3 to coding, so I will use *python3* or *pip3* to enter commands.
**Before executing following steps, make sure your system is able to compile and download Python extensions with *pip*:**
>if not:
><pre><code>$ sudo apt-get update
>$ sudo apt-get install python3-pip
>$ sudo python3 -m pip install --upgrade pip setuptools wheel</pre></code>

### Using DHT22
1. Install **build-essentail** and **python-dev**
<pre><code>$ sudo apt-get update
$ sudo apt-get install build-essential python-dev</code></pre>


2.  Download and install **Adafruit_Python_DHT**
<pre><code>$ git clone https://github.com/adafruit/Adafruit_Python_DHT
$ cd  Adafruit_Python_DHT
$ sudo python3 setup.py install</code></pre>

3. Execute the monitor program
<pre><code>$ cd examples
$ sudo python3 AdafruitDHT.py 22 4 </pre></code>
22 stands for using DHT22, 4 stands for DHT22's Data line is on GPIO 4.

4. If success, you can get the humidity and temperature
<pre><code>Temp=22.0* Humidity=68.0%</pre></code>

### Using Line Bot
Install **flask** and **line-bot-sdk**
<pre><code>$ sudo pip3 install flask
$ sudo pip3 install line-bot-sdk</pre></code>

### Using Chinese 




## Build up the machine
### Set up 12V Switching Power Supply
Each of our pumps and water automization module need *12VDC* input to be activated, but our raspberry pi can't offer that much power, so we need to use power supply to *transform its 110AC input into 12VDC ouput* to supply our devices the power needed.
Because I think there may be many people(like me in the first) not knowing how to use power supply, I'll show a simple tutorial below.
![image](https://user-images.githubusercontent.com/72622577/148678545-fb4110c2-e711-4cb6-a36b-318e3ffd71ca.png)


1. To know what we need

![image](https://user-images.githubusercontent.com/72622577/148678823-a9d37588-1acd-471f-8916-1d775e6bbd7f.png)![image](https://user-images.githubusercontent.com/72622577/148678577-29f30b36-26de-40f7-9779-d7e3aa5f71f5.png)

>* L = *hot wire*, is usually **black**
>* N = *neutural wire*, is usually **white**
>* Weird gesture = *ground wire*, is usually **green**

2. Cut off the female end & Strip the outer insulation from wire

After cutting down a bit, we can see where the wires go.

 **Don't have this plug in until you have everything hooked up!**
 
![image](https://user-images.githubusercontent.com/72622577/148681351-803314eb-3c63-4b71-8fbf-179c6498c131.png)

3. Hook it up with power supply

The led lights will be on if you plug in. 

![image](https://user-images.githubusercontent.com/72622577/148680210-52835a7e-d224-4431-964b-00a641dff3fb.png)

4. Test whether it can work

![image](https://user-images.githubusercontent.com/72622577/148680425-32e9bac5-b509-49e4-a73d-785a20736ab9.png)

Success!!

### Set up the diffuser

1. Paste the automizer on the plastic without 

You should cut a circle with 1.3mm diameters one the plastic and make the automizer stick on it.

![image](https://user-images.githubusercontent.com/72622577/148680783-7a926702-0423-42a5-bb63-61bcc2e66c45.png)

2. Put a sponge in the container

Use a sponge to absorb the water our automizer needs.(I only use types to make it fixed haha.)

![image](https://user-images.githubusercontent.com/72622577/148680921-1def2e1b-2eef-4a07-8d7b-bc590900c8ce.png)

3. Combination

With the pumps elevated behind, we get a simple diffuser which can receive the essentail oils drip down!

![image](https://user-images.githubusercontent.com/72622577/148681032-403b8b95-ca19-46f5-bfa3-771dc77ab67e.png)

### Other hardware part be like

![image](https://user-images.githubusercontent.com/72622577/148681286-78c96422-0c8b-4e5d-8725-ee8f5249b6f5.png)
![image](https://user-images.githubusercontent.com/72622577/148681396-d1a7ff37-6ac3-4e7e-be37-b2366b3a7b14.png)
![image](https://user-images.githubusercontent.com/72622577/148681400-fc19bc17-9972-4649-b2bf-64214eb69c65.png)


## Build up LineBot


## Failures or difficulty I met


## References

