// received String looks like this "LSH:-0.02|LSV:-0.02|RSH:+0.07|RSV:+0.01|LTT:-1.00|RTT:-1.00|circle|square|triangle|dpad_up|";
#include <Arduino.h>
char receivedChar;
String receivedString;
String tempButton;
String checkButton;

class processData{
  public:
    String axis_name[6];
    String axis_value_String[6];
    double axis_value[6];
    bool button_bool[16];
    
    String button_map[16] = {
    "x", "circle", "square", "triangle", "share", "ps", "options", "L3",
    "R3", "LB", "RB", "dpad_up", "dpad_down", "dpad_left", "dpad_right", "touchpad"};
    
    
    processData(String Input){
        // Processing axis 
        
    for (int i = 0; i < 60; i += 10) { // axis take first 60 characters

        for (int j = 0; j < 3; j++) { // axis name
            axis_name[i / 10] += Input[j + i];
        }

        for (int j = 0; j < 5; j++) { // axis value str
            axis_value_String[i / 10] += Input[j + i + 4]; 
        }

        for (int i=0;i<6;i++){
            axis_value[i]=axis_value_String[i].toDouble(); // convert to double
            
            
        }

    }

    // button processing
    String temp_button_String[16];
    for (int i=0;i<16;i++){           // no button input at the start, bool = 0 
      button_bool[i]=0;
      }

      int b_index = 0; // Indexing buttons in their respective position
      for (unsigned int x=0;x<Input.length()-60;x++){

        char c=Input[x+60];
        if (c!='\n' && c!='|'){ // strip the buttons
            tempButton+=c; 
        } 
        else
        {
          temp_button_String[b_index]=tempButton; // next button
          b_index++;
          tempButton="";
        }
      }
      
      for (int x=0;x<16;x++){
        tempButton=temp_button_String[x]; // if the button is in the button_map, it will assign 1 to it's bool
        for (int y=0;y<16;y++){
            checkButton=button_map[y];
            if (tempButton==checkButton){
              button_bool[y]=true;
            }
          }
      }
    }
};
