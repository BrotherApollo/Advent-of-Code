class Dial {
  
  constructor() {
    this.value = 50;
    this.dings = 0;
  }
  
  turn(line) {
    let dir = line.match(/[LR]/)[0]
    let value = parseInt(line.match(/\d+/)[0])    
  
    for (let i=0; i<value; i++) {
      if (dir == "L") {
        this.value = (this.value - 1) % 100;
      } else {
        this.value = (this.value + 1) % 100;
      }
      
      if (this.value == 0) {
        this.dings++;
      }
    }
  }
}