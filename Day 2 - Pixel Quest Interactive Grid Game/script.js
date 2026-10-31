const boxesContainer = document.querySelector(".boxes-container");
const targetLocation = document.querySelector("#answer");
const targetCoreAns = document.querySelector("#targetCoreAns");
const devMode = document.querySelector("#devMode");
let boxesTotal = 20;

let targetCore = Math.floor(Math.random() * 20);

targetLocation.textContent = targetCore;

for (let i = 0; i < boxesTotal; i++) {
    const box = document.createElement("div");
    box.classList.add("box");
    box.textContent = "?";
    boxesContainer.appendChild(box);

    box.dataset.number = i;
    let boxId = box.dataset.number;
    
    const numId = document.createElement("div");
    numId.classList.add("idBox", "hidden")
    numId.textContent = boxId;
    box.appendChild(numId);

    let deveMode = false;
    
    box.addEventListener('click',() => {
        if (boxId == targetCore) {
            box.textContent = "⭐";
            box.classList.add("target-core");
            box.appendChild(numId);

        } else {
            box.textContent = "x";
            box.classList.add("selected");
            box.appendChild(numId);
        }
    });

    devMode.addEventListener('dblclick',()=>{
        if (deveMode) {
            numId.classList.add("hidden");
            targetCoreAns.classList.add("hidden");
            deveMode = false;
        } else {
            numId.classList.remove("hidden");
            targetCoreAns.classList.remove("hidden");
            deveMode = true;
        }
    });

}


