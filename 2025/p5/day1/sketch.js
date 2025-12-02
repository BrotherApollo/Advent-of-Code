let targetNumber = 50;
let radius = 300;
let num_numbers = 100;
let currentRotation = 0;
let targetRotation = 0;
let dataIndex = 0;
let dial;

function preload() {
  data = loadStrings("data.txt");
  // data = [50, 25, 0, 75];
}

function setup() {
  createCanvas(700, 700);
  console.log(data);
  // frameRate(1);
  
  textAlign(CENTER, CENTER);
  textSize(12);
  dial = new Dial();
  console.log(data);
}

function draw() {
  
  //setting targetNumber
  if (Math.abs(currentRotation - targetRotation) < 0.001) {
    
    dial.turn(data[dataIndex]);
    targetNumber = dial.value;
    dataIndex++;
    if (dataIndex >= data.length) {
      dataIndex = 0;
    }
  }
  
  background(220);
  translate(width / 2, height / 2);  
  
  // Drawing circle
  noFill();
  stroke(0);
  circle(0,0, radius * 2)
  circle(0,0, radius)
  fill(0);
  // Drawing dings
  text(dial.dings, 0,0);
  
  // rotating 
  targetRotation = map(targetNumber, 0, num_numbers, 0, TWO_PI);
  currentRotation = lerp(currentRotation, targetRotation, 0.5);
  rotate(-currentRotation);
  
  for (let i=0; i < num_numbers; i++) {
    
    let angle = (i / num_numbers) * TWO_PI;
    
    push();
    
    rotate(angle);
    
    translate(0, -radius+25);
    
    let displayNum = i;
    text(displayNum, 0, 0);
    
    pop();
  }
  
  
}