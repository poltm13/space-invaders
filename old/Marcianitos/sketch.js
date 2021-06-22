let spaceShip;
let start = false;
let lasers = [];
let penguins = [];
let stars;

function preload()  {
    shipImg = loadImage('../files/ship.png');
    penguinImg = loadImage('../files/spacePenguin.png');
    heartImg = loadImage('../files/heart.png');
    
}

function setup()    {
    createCanvas(600, 690);
    spaceShip = new Ship();
    stars = new Stars();
}

function draw()    {
    background(0);
    
    stars.update();
    
    spaceShip.update();
    spaceShip.render();
    
    for (let i=0; i<lasers.length; i++) {
        lasers[i].update();
        lasers[i].render();
    
        let hit = lasers[i].hits(penguins);
        if (hit)    {
            penguins.splice(hit - 1, 1);
            lasers.splice(i, 1);
        } else if (lasers[i].offScreen())   {
            lasers.splice(i, 1);
    
        }
    }
    
    for (let i=0; i<penguins.length; i++)   {
        penguins[i].update();
        penguins[i].render();
    }
    
    
    game();
}

function keyPressed() {
    switch (key)    {
        case ' ':
            lasers.push(new Laser(spaceShip.posX, spaceShip.posY - spaceShip.size/2));
            break;
        case 's':
            start = true;
            loop();
            break;
        case 'p':
            start = false;
            noLoop();
            break;
        default:
            break;
    }
}

function game() {
    if (!start) {
        noLoop();
        textSize(32);
        fill('white');
        textAlign(CENTER);
        text('PRESS S TO START', width/2, height/2);
    } else  {
        if (random(0, 100) < 1)    {
            penguins.push(new Penguin());
        }
    }
}

















