const boxesContainer = document.querySelector(".boxes-container");
// const targetLocation = document.querySelector("#answer");
let boxesTotal = 20;

let targetCore = Math.floor(Math.random() * 20);

// targetLocation.textContent = targetCore;

for (let i = 0; i < boxesTotal; i++) {
    const box = document.createElement("div");
    box.classList.add("box");
    box.textContent = "?";
    boxesContainer.appendChild(box);

    box.dataset.number = i;
    let boxId = box.dataset.number;
    
    box.addEventListener('click',() => {
        if (boxId == targetCore) {
            box.textContent = "⭐";
            box.classList.add("target-core");
        } else {
            box.textContent = "x";
            box.classList.add("selected");
        }
    });


}

