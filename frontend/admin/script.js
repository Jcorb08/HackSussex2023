let sharkHolderDiv = document.querySelector("#sharkHolder");
let sharks = document.querySelectorAll('.shark');
let sharkHolder = sharkHolderDiv.getBoundingClientRect();
let center = [sharkHolder.width / 2, sharkHolder.height / 2];
let angleIncrement = Math.PI * 2 / sharks.length;
let distance = 300;

for (let i = 0; i < sharks.length; i++) {
    let offset = [Math.sin(angleIncrement * i) * distance, Math.cos(angleIncrement * i) * distance];
    sharks[i].style.left = center[0] + offset[0] + 'px';
    sharks[i].style.top = center[1] - offset[1] + 'px';
}

document.querySelector("#getterButton").addEventListener("click", function() {
    //fetch server data
});

document.querySelector("#fightButton").addEventListener("click", function() {
    startFight();
});

class Shark {

    constructor(colour) {
        this.name = colour + " Shark";
        this.hp = 100;
        this.attack = 5;
        this.defense = 5;
        this.speed = 10;
        this.weapons = [];
        this.equippedWeapon = null;
        this.currentSpeed = -1;
    }

}

class Sword {
    constructor() {
        this.imgPath = "../images/Sword.png";
        this.attack = 5;
        this.defence = 4;
        this.speed = 2;
    }
}

class Axe {
    constructor() {
        this.imgPath = "../images/Axe.png";
        this.attack = 7;
        this.defence = 3;
        this.speed = 3;
    }
}

class Stick {
    constructor() {
        this.imgPath = "../images/Stick.png";
        this.attack = 3;
        this.defence = 2;
        this.speed = 7;
    }
}

class FishingRod {
    constructor() {
        this.imgPath = "../images/Fishing-Rod.png";
        this.attack = 2;
        this.defence = 6;
        this.speed = 3;
    }
}

class ThrownWeapon {
    constructor(element, startPos, endPos) {
        this.element = element;
        this.elapsedTime = 0;
        this.startPos = startPos;
        this.endPos = endPos;
    }
}

mysharks = [new Shark("Blue"), new Shark("Green"), new Shark("Orange"), new Shark("Purple"), new Shark("Red")];

mysharks.forEach(shark => {
    shark.weapons.push(new Sword());
    shark.weapons.push(new Sword());
    shark.weapons.push(new Axe());
    shark.weapons.push(new Axe());
    shark.weapons.push(new Stick());
    shark.weapons.push(new Stick());
    shark.weapons.push(new FishingRod());
    shark.weapons.push(new FishingRod());
});

async function startFight() {

    let fighting = true;

    while(fighting) {

        for (let i = 0; i < mysharks.length; i++) {

            //if weapon not equipped then equip
            if (!mysharks[i].equippedWeapon) {
                if(mysharks[i].weapons.length <= 0) {
                    fighting = false
                }
                let randomWeapon = Math.floor(Math.random()*mysharks[i].weapons.length)
                let myWeapon = mysharks[i].weapons.splice(randomWeapon, 1)[0];
                mysharks[i].equippedWeapon = myWeapon;
                mysharks[i].currentSpeed = mysharks[i].speed - mysharks[i].equippedWeapon.speed;
            }
            //reduce weapon timer
            mysharks[i].currentSpeed--;
            //if weapon timer is 0 then attack
            if (mysharks[i].currentSpeed <= 0) {
                let randomShark = undefined;
                do {
                    randomShark = Math.floor(Math.random()*mysharks.length)
                } while(randomShark == i);

                let mySharkBox = sharks[i].getBoundingClientRect();
                let randomSharkBox = sharks[randomShark].getBoundingClientRect();
                let mySharkCenter = [mySharkBox.left + mySharkBox.width / 2, mySharkBox.top + mySharkBox.height / 2];
                let randomSharkCenter = [randomSharkBox.left + randomSharkBox.width / 2, randomSharkBox.top + randomSharkBox.height / 2];
                let thrownWeapon = document.createElement("img");
                thrownWeapon.classList.add("thrownWeapon");
                thrownWeapon.src = mysharks[i].equippedWeapon.imgPath;
                thrownWeapon.style.left = mySharkCenter[0] + 'px';
                thrownWeapon.style.top = mySharkCenter[1] + 'px';
                sharkHolderDiv.appendChild(thrownWeapon);
                thrownWeapons.push(new ThrownWeapon(thrownWeapon, mySharkCenter, randomSharkCenter));
                mysharks[i].equippedWeapon = null;
                await delay(500);
            }
            //if no weapons remove from action list
            //if dead remove from game
            //if no weapons or 4 dead end fight
        }

        //fighting = false

    }

}

function delay(time) {
    return new Promise(resolve => setTimeout(resolve, time));
}

let thrownWeapons = [];

let start, previousTimeStamp;

function animate(timestamp) {

    if (start == undefined) {
        start = timestamp;
    }
    let deltaTime = ((timestamp - start) - previousTimeStamp) / 1000;
    previousTimeStamp = timestamp - start;

    thrownWeapons.forEach(weapon => {
        weapon.elapsedTime += deltaTime;
        let x = weapon.startPos[0] + (weapon.endPos[0] - weapon.startPos[0]) * (weapon.elapsedTime * 2);
        let y = weapon.startPos[1] + (weapon.endPos[1] - weapon.startPos[1]) * (weapon.elapsedTime * 2);
        weapon.element.style.left = x + 'px';
        weapon.element.style.top = y + 'px';

        if (weapon.elapsedTime > 0.5) {
            weapon.element.remove();
            thrownWeapons.splice(thrownWeapons.indexOf(weapon), 1);
        }

    });

    window.requestAnimationFrame(animate);

}

window.requestAnimationFrame(animate);
