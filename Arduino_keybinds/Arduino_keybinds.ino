/* 
 * You can Attach any controller to the GUI Application and Do whatever you would like with it
 * I made this code to Run an RC plane without the need to use Bluetooth controller + arduino
 * RC Remotes are Expensive As F$%& tho and they're kind of prohibited to buy in here so i had to make do
 * You can use this code for free, Distribution is prohibited.
 * www.Github.com/alyayman921
 * Aly Ayman Sarhan - June 2025
 */
 
#include "handlingClass.h"
void takeAction(double axis[6],bool button[16]);

int ledPin = 13;
double deadzone=0.2;


void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);
  Serial.println("Serial Response: Start");
}

void loop() {
  if (Serial.available() > 0) {  
    receivedChar = Serial.read();
    if (receivedChar != '\n') {
      receivedString += receivedChar;
    } 
    else
    {
      if(receivedString.startsWith("LSH")){
      processData controller1(receivedString); // received string from Serial (python)
      takeAction(controller1.axis_value,controller1.button_bool);}
      receivedString="";
    }   
    }
    //delay(1);

    
}

void takeAction(double axis[6],bool button[16]){
  /* ------------------------ Buttons---------------------------*/

    /* 
     *  BUTTONS ARE ALWAYS IN STATE 0 UNLESS YOU'RE PRESSING IT'S 1
     *  Put Button Functions Accordingly
     *  Don't Use Delays or loops unless you know what you're doing
     *  check button bool in handlingClass.h to know the number value of each button
     */
     
    // X action 
    if (button[0]==1){ // X pressed
      digitalWrite(13, 1);
      Serial.println("X Is Pressed");
    }
    // X release
    if (button[0]==0){ 
      digitalWrite(13, 0);
      
    // Circle action 
    if (button[1]==1){ // Circle pressed
      digitalWrite(13, 1);
      Serial.println("Circle Is Pressed");
    }
    // Circle release
    if (button[1]==0){ 
      digitalWrite(13, 0);
    }
    // Square action 
    if (button[2]==1){ // Square pressed
      digitalWrite(13, 1);
      Serial.println("Square Is Pressed");
    }
    // Square release
    if (button[2]==0){ 
      digitalWrite(13, 0);
    }

    // tri action 
    if (button[3]==1){ // tri pressed
      digitalWrite(13, 1);
      Serial.println("Triangle Is Pressed");
    }
    // tri release
    if (button[3]==0){ 
      digitalWrite(13, 0);
    }

/* ------------------------ AXIS---------------------------*/
    /* 
     *  Axis values are read every loop too, with their values in the array axis.value when you make an object of processData
     *  Put Button Functions Accordingly
     *  Don't Use Delays or loops unless you know what you're doing
     *  check object.axis_name to know the number value of each button, or read the handlingClass.h too
     */
    }

  if (abs(axis[0])> deadzone){
    if (axis[0]>0){
      // left stick right
      digitalWrite(13, 1);
      Serial.println("LS right");
    }else{
      //left stick to the left
      digitalWrite(13, 1);
      Serial.println("LS left");
    }
  }
  if(abs(axis[1])> deadzone){
    if (axis[1]>0){
      // left stick Up
      digitalWrite(13, 1);
      Serial.println("LS Up");
    }else{
      //left stick to the Down
      digitalWrite(13, 1);
      Serial.println("LS Down");
    }
  }

    if(abs(axis[2])> deadzone){
    if (axis[2]>0){
      digitalWrite(13, 1);
      Serial.println("RS Left");
    }else{
      //left stick to the Down
      digitalWrite(13, 1);
      Serial.println("RS Right");
    }
  }
    if(abs(axis[3])> deadzone){
    if (axis[3]>0){
      // left stick Up
      digitalWrite(13, 1);
      Serial.println("RS Up");
    }else{
      //left stick to the Down
      digitalWrite(13, 1);
      Serial.println("RS Down");
    }
  }
  
  }
