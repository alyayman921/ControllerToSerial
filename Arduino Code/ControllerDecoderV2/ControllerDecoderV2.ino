#include <string.h>
char receivedChar;
String receivedString;
String tempButton;
String checkButton;
float deadzone=0.2;
float fvalue[6];
int ledPin = 13;

//String input="LSH:-0.02|LSV:-0.02|RSH:+0.07|RSV:+0.01|LTT:-1.00|RTT:-1.00|circle|square|triangle|dpad_up|";

String button_map[16] = {
    "x", "circle", "square", "triangle", "share", "ps", "options", "L3",
    "R3", "LB", "RB", "dpad_up", "dpad_down", "dpad_left", "dpad_right", "touchpad"
};

struct ProcessedData {
    String axis_name[6];
    String axis_value[6];
    String button_received[16];
    
    int button_bool[16]; // Boolean array for button press detection
    
};

ProcessedData processInput(String received) {
    ProcessedData data; // Struct to hold the arrays
    int b_index = 0;
    for (int z=0;z<16;z++){
      data.button_bool[z]=0;
      }
    // Processing axis values
    for (int i = 0; i < 60; i += 10) {
        for (int j = 0; j < 3; j++) {
            data.axis_name[i / 10] += received[j + i]; // Concatenating axis name
        }
        for (int j = 0; j < 4; j++) {
            data.axis_value[i / 10] += received[j + i + 4]; // Concatenating axis value
        }
    }
  // button process
      for (int x=0;x<received.length()-60;x++){
        char c=received[x+60];
        if (c!='\n' && c!='|'){
            tempButton+=c;
        } else{
          data.button_received[b_index]=tempButton;
          b_index++;
          tempButton="";
        }
      }
      for (int x=0;x<16;x++){
        tempButton=data.button_received[x];
        for (int y=0;y<16;y++){
            checkButton=button_map[y];
            if (tempButton==checkButton){
              data.button_bool[y]=true;
            }
          }
      }
      return data;
}

void setup() {
  Serial.begin(115200);
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);
  Serial.println("Serial Response: Start");
}
//ProcessedData result = processInput(receivedString);

void processAxis(String Value[6]) {
  for (int i=0;i<6;i++){
    fvalue[i]=Value[i].toFloat();
  }
if (fvalue[4]> -0.8 && fvalue[5] > -0.8){
    // Do nothing
    Serial.println("Stop1");
  } else{
  if (abs(fvalue[0])> deadzone && fvalue[5] > 0){
    if (fvalue[0]>0){
      // left stick right
      digitalWrite(13, 1);
      Serial.println("Steer To Right, Forward");
    }else{
      //left stick to the left
      digitalWrite(13, 1);
      Serial.println("Steer To Left, Forward");
    }
  }if (abs(fvalue[0])> deadzone && fvalue[4] > 0){
    if (fvalue[0]>0){
      // left stick right
      digitalWrite(13, 1);
      Serial.println("Steer To Right, Backward");
    }else{
      //left stick to the left
      digitalWrite(13, 1);
      Serial.println("Steer To Left, Backward");
    }
  }if (fvalue[5]>0 && abs(fvalue[0])<deadzone){
Serial.println("Move Forwards")  ;  

  }if (fvalue[4]>0 && abs(fvalue[0])<deadzone){
Serial.println("Backwards")  ;  

  }
  else{
  //Serial.println("Stop2")   ; 
  }
  }
}

void loop() {
  if (Serial.available() > 0) {
    receivedChar = Serial.read();
    if (receivedChar != '\n') {
      receivedString += receivedChar;
    } 
    else{
      if(receivedString.startsWith("LSH")){
      ProcessedData result = processInput(receivedString);
      processButton(result.button_bool);
      processAxis(result.axis_value);
    }
      receivedString="";
    }   
}
}


void processButton(int button_active[16]) {
    
    if (button_active[0]==1){ // X pressed
    // X action Here
      digitalWrite(13, 1);
      Serial.println("X Is Pressed");
    }
    if (button_active[0]==0){ // X unpressed
    // Undo X action Here
      digitalWrite(13, 0);
    }
    
    }



