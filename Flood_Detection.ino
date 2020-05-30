int liquidSensor= D2;
bool isItFlood=false;
void setup(){
pinMode(liquidSensor, INPUT);
Particle.variable("isFloodPresent", isItFlood);
// for mock data
Particle.function("liquid", mockFlood);
Time.zone(+10);
}
void loop(){
int floodPresence = digitalRead(liquidSensor);



if(digitalRead(liquidSensor) == LOW){
               isItFlood = true;
               
        }
        else{
                isItFlood = false;
        }


notifyUser();


//check every 2 seconds
delay(10s);// Incoming analog signal read and appointed sensor


}
void notifyUser(){
    if(isItFlood){
        Particle.publish("Flood_Detection","true", PRIVATE);
    }
}


int mockFlood(String command){
    int amount =command.toInt();
    if(amount == 1){
        isItFlood = true;
        notifyUser();
        return 1;
    }
    else{
        return -1;
    }
    
    
}